from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

#! imports
from apps.service._comm._models.__CommPosts import *
from apps.service._comm._models.__CommPostsChall import *

class PostsAdd(View):
    
    def checkLane(self, list):
        list = len(list)
        if list == 1:
            return 'Offlane'
        elif list == 2:
            return 'Duallane'
        elif list == 3:
            return 'Trilane'
        else:
            return 'Combo'
    
    def genId(self):
        multiplier = 99999
        resultId = multiplier + CommPosts.objects.count()
        return resultId 
    
    def post(self, request, *args, **kwargs):
        
        if request.POST:

            #! init
            Posts_Id = request.POST.get('postid')
            Posts_Notes = request.POST.get('notes')
            Posts_Heroes = request.POST.getlist('heroes')
            
            List_Lanes = self.checkLane(Posts_Heroes)
            List_Heroes = ','.join(Posts_Heroes)
            List_Tags = List_Heroes + ',' + List_Lanes

            #! authentication data
            initAuthenticate = Authenticate(request)
            AuthData = initAuthenticate.GetSession()
            
            id = self.genId()
            init_ModelPosts = CommPosts(id = id, 
                                        accounts_id = AuthData['userid'],
                                        type = 1,
                                        tags = List_Tags,
                                        heroes = List_Heroes, 
                                        note = Posts_Notes)
            init_ModelPosts.save()
            
            if Posts_Id:
                init_ModelPostsChall = CommPostsChall(posts_origin_id = Posts_Id, 
                                                      posts_chall_id = id)
                init_ModelPostsChall.save()
            
            return HttpResponseRedirect(reverse('comm_posts_list'))
        