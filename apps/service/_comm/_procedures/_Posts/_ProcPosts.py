#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! imports
import math
from apps.service._comm._models.__CommPosts import *

class ProcPostsTemplate(object):
    
    def __init__(self, Posts, Pages=False, Limits=False):
        self.Posts = Posts
        self.Pages = Pages
        self.Limits = Limits
        self._GetPaging()

        
    #! get pictures
    def _GetHeroesPictures(self, Heroes):
        List_Heroes = []
        size = 'ssm'
        Heroes = Heroes.split(',')
        for hero in Heroes:
            info = HeroesParser(hero)
            info.Heroes_Detail()
            hinfo = info._GetHeroesDetailTemplate()
            List_Heroes.append({
                                'hero' : hero,
                                'picture' : hinfo[0]['avatar'][size],
                                'w' : hinfo[0]['psizes'][size]['w'],
                                'h' : hinfo[0]['psizes'][size]['h'],
                                })

        return List_Heroes

    def _GetPaging(self):
        self.PostsCount = float(len(self.Posts))
        self.PagesCount = int(math.ceil( self.PostsCount / float(self.Limits)))
        
        if not self.Pages > self.PagesCount:
            if self.Pages == 1:
                self.Start = self.Pages - 1
            else:
                if self.Limits == 1: 
                    self.Start = self.Pages - 1
                else:
                    self.Start = self.Pages
            self.End = self.Pages - 1 + self.Limits
            
            return [self.Start, self.End]
            
        else:
            return False
    
    #! template
    def _GetTemplate(self):
        
        PageConfig = self._GetPaging()
        if PageConfig:
            PageStart = PageConfig[0]
            PageEnd = PageConfig[1]
            self.Posts = self.Posts.order_by('-id')[PageStart: PageEnd]
        
        
        List = []
        ListDate = []
        DictData = []
        for sort in self.Posts:
            PostsByDate = CommPosts.objects.filter(date=sort['date']).order_by('-id')


            ListDate = []
            for post in PostsByDate:
                #! arrange list posts
                ListDate.append({
                                  'account' : post.accounts.username,
                                  'note' : post.note,
                                  'heroes' : post.heroes,
                                  'pic' : self._GetHeroesPictures(post.heroes),
                                  'date' : post.date.strftime('%A, %b %d'),
                                  'datetime' : post.datetime.strftime('%A, %b %d')
                                })

            #! arrange list by date
            List.append({
                          'date' : sort['date'].strftime('%A, %b %d'),
                          'data' : ListDate,
                          'count' : self.PostsCount,
                          'page' : self.Pages
                        })
        
        return List
        
class ProcPosts(ProcPostsTemplate):

    def __init__(self):
        pass
        
    #! format parameter specific hero
    def sortByDate(self):
        sortPostsDate = CommPosts.objects.values('date').annotate(count=Count('id')).order_by('-id')
        super(ProcPosts,self).__init__(sortPostsDate)         

    def sortByDatePaginated(self, Pages, Limits):
        sortPostsDate = CommPosts.objects.values('date').annotate(count=Count('id')).order_by('-id')
        super(ProcPosts,self).__init__(sortPostsDate, Pages, Limits)         
