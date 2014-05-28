from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! lib: parser
from apps.service._api_lib._d2._heroes._HeroesParser import *
#! lib: posts
from apps.service._api_lib._comm._posts._ProcPosts import *


class PostsList(View):

    heroes = HeroesParser()
    #! Str
    heroes.Heroes_Class('str')
    hstr = heroes._GetHeroesListTemplate()
    #! Agi
    heroes.Heroes_Class('agi')
    hagi = heroes._GetHeroesListTemplate()
    #! Int
    heroes.Heroes_Class('int')
    hint = heroes._GetHeroesListTemplate()
    
    #! All
    heroes.Heroes_All()
    hall = heroes._GetHeroesListTemplate()
    

    #! list post
    init_Posts = ProcPosts()
    init_Posts.sortByDatePaginated(2, 2)
    sortByDatePosts = init_Posts._GetTemplate()
    
    _template = '_base/index.html'
    def get(self, request, *args, **kwargs):
        return render_to_response(self._template, 
                                  {
                                   #! posts
                                   'sorByDatePosts' : self.sortByDatePosts,
                                   #! create init
                                   'hstr' : self.hstr,
                                   'hagi' : self.hagi,
                                   'hint' : self.hint,
                                   'hall' : self.hall},
                                  context_instance=RequestContext(request))        