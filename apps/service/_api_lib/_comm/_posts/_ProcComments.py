#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! libs/helpers
from apps.service._api_lib._comm._posts._TplPosts import *
from apps.service._api_lib._comm._posts._TplComments import *

#! imports
import math
from apps.service._comm._models.__CommPosts import *
from apps.service._comm._models.__CommComments import *

class ProcCommentsTemplate(object):
    
    def __init__(self, Posts, Comments):
        self.Posts = Posts
        self.Comments = Comments

    #! template
    def _GetTemplate(self):
        List = []
        List.append({
                  'posts' : TplPosts(self.Posts), #! tpl helper
                  'comments' : TplComments(self.Comments) #! tpl helper
        })
        return List
        
class ProcComments(ProcCommentsTemplate):

    def __init__(self):
        pass
        
    def findByPostsId(self, id):
        Posts = CommPosts.objects.filter(pk=id)
        Comments = CommComments.objects.filter(posts_id=id)
        super(ProcComments,self).__init__(Posts, Comments)         
