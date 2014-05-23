#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! imports
from apps.service._comm._models.__CommPosts import *

class ProcPostsTemplate(object):
    
    def __init__(self, Posts, Pages=False, Limits=False):
        self.Posts = Posts
        self.Pages = Pages
        self.Limits = Limits
        self.PostsCount = Posts.Count()
        self.PagesBreakDown = self.PostsCount / self.Limits
        self.PagesStart = self.Limits * self.Pages
    
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
    
    #! template
    def _GetTemplate(self):
        List = []
        ListDate = []
        DictData = []
        for sort in self.Posts[self.PagesStart:self.Limits]:
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
                          'count' : self.PostCount,
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
        

