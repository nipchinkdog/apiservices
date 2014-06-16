#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! libs/helpers
from apps.service._api_lib._comm._posts._TplPosts import *

#! imports
import math
from apps.service._comm._models.__CommPosts import *
from apps.service._comm._models.__CommPostsChall import *

class ProcPostsTemplate(object):
    
    def __init__(self, Posts, PostsByDate, Pages=False, Limits=False, SessionId=False, Searching=False, PostsChallenge=False):
        self.Posts = Posts
        self.PostsByDate = PostsByDate
        self.Pages = Pages
        self.Limits = Limits
        self.SessionId = SessionId
        self.Searching = Searching
        self.PostsChallenge = PostsChallenge
        self._GetPaging()

    def _GetPaging(self):
        self.PostsCount = float(len(self.Posts))
        self.PagesCount = int(math.ceil( self.PostsCount / float(self.Limits)))
        
        if not self.Pages > self.PagesCount:
            self.Start = (self.Pages * self.Limits) - self.Limits
            self.End = self.Pages * self.Limits
            return [self.Start, self.End]
        else:
            return False
        
    #! template
    def _GetTemplate(self):
        List = []
        ListDate = []
        DictData = []
        PageConfig = self._GetPaging()
        if PageConfig:
            PageStart = PageConfig[0]
            PageEnd = PageConfig[1]
            self.Posts = self.Posts.order_by('-id')[PageStart: PageEnd]

            for sort in self.Posts:
                
                PostsByDate = self.PostsByDate.filter(date=sort['date']).order_by('-id')
                #! arrange list by date
                List.append({
                          'date' : sort['date'].strftime('%A, %b %d'),
                          'posts' : TplPosts(PostsByDate, self.SessionId) #! tpl helper
                })
           
            return List
        else:
            return []
        
class ProcPosts(ProcPostsTemplate):

    def __init__(self):
        pass
        
    def sortByDate(self):
        sortPostsDate = CommPosts.objects.values('date').annotate(count=Count('id')).order_by('-id')
        super(ProcPosts,self).__init__(sortPostsDate)         

    def sortByDatePaginated(self, Pages, Limits, SessionId=False, Searching=False):
        sortPostsDate = CommPosts.objects.values('date').annotate(count=Count('id')).order_by('-id')
        PostsByDate = CommPosts.objects.all();
        super(ProcPosts,self).__init__(sortPostsDate, PostsByDate, Pages, Limits, SessionId, False, False)     

    def sortBySearch(self, Pages, Limits, Searching, SessionId=False):
        sortPostsDate = CommPosts.objects.values('date').filter(tags__icontains=Searching).annotate(count=Count('id')).order_by('-id')
        PostsByDate = CommPosts.objects.filter(tags__icontains=Searching)
        super(ProcPosts,self).__init__(sortPostsDate, PostsByDate, Pages, Limits, SessionId, Searching, False)         
            
    def sortByChall(self, Pages, Limits, PostId, SessionId=False):
        PostsChallenge = CommPostsChall.objects.filter(posts_origin_id=PostId).values_list('posts_chall_id', flat=True)
        sortPostsDate = CommPosts.objects.values('date').filter(pk__in=PostsChallenge).annotate(count=Count('id')).order_by('-id')
        PostsByDate = CommPosts.objects.filter(pk__in=PostsChallenge)
        super(ProcPosts,self).__init__(sortPostsDate, PostsByDate, Pages, Limits, SessionId, False, PostsChallenge)         

    def sortById(self, Pages, Limits, PostId, SessionId=False):
        sortPostsDate = CommPosts.objects.values('date').filter(pk=PostId).annotate(count=Count('id')).order_by('-id')
        PostsByDate = CommPosts.objects.filter(pk=PostId)
        super(ProcPosts,self).__init__(sortPostsDate, PostsByDate, Pages, Limits, SessionId, False, False)         

    def sortByAuthor(self, Pages, Limits, AuthorId, SessionId=False):
        sortPostsDate = CommPosts.objects.values('date').filter(accounts_id=AuthorId).annotate(count=Count('id')).order_by('-id')
        PostsByDate = CommPosts.objects.filter(accounts_id=AuthorId)
        super(ProcPosts,self).__init__(sortPostsDate, PostsByDate, Pages, Limits, SessionId, False, False)         
