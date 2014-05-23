from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! procedures
from apps.service._comm._procedures._Posts._ProcPosts import *


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
    
    
    #! list posts
    init_Posts = ProcPosts()
    init_Posts.sortByDate()
    sorByDatePosts = init_Posts._GetTemplate()
    
    
    _template = '_comm/list-posts.html'
    def get(self, request, *args, **kwargs):
        return render_to_response(self._template, 
                                  {
                                   #! posts
                                   'sorByDatePosts' : self.sorByDatePosts,
                                   #! create init
                                   'hstr' : self.hstr,
                                   'hagi' : self.hagi,
                                   'hint' : self.hint,
                                   'hall' : self.hall},
                                  context_instance=RequestContext(request))        