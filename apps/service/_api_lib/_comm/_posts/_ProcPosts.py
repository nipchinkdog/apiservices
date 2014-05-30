#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! libs/helpers
from apps.service._api_lib._comm._posts._TplPosts import *

#! imports
import math
from apps.service._comm._models.__CommPosts import *

class ProcPostsTemplate(object):
    
    def __init__(self, Posts, Pages=False, Limits=False):
        self.Posts = Posts
        self.Pages = Pages
        self.Limits = Limits
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
                PostsByDate = CommPosts.objects.filter(date=sort['date']).order_by('-id')
                #! arrange list by date
                List.append({
                          'date' : sort['date'].strftime('%A, %b %d'),
                          'posts' : TplPosts(PostsByDate) #! tpl helper
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

    def sortByDatePaginated(self, Pages, Limits):
        sortPostsDate = CommPosts.objects.values('date').annotate(count=Count('id')).order_by('-id')
        super(ProcPosts,self).__init__(sortPostsDate, Pages, Limits)         