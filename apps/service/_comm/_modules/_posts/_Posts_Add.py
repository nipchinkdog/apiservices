from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

#! imports
from apps.service._comm._models.__CommPosts import *
from apps.service._comm._models.__CommPostsChall import *

class PostsAdd(View):
    
    def post(self, request, *args, **kwargs):
        
        if request.POST:

            #! init
            PickPosts_Id = request.POST['postid']
            Posts_Heroes = request.POST.getlist('heroes')
            List_Heroes = ','.join(Posts_Heroes)
            Posts_Lanes = request.POST.getlist('lanes')
            List_Lanes = ','.join(Posts_Lanes)
            
            Tags = List_Heroes + ',' + List_Lanes
            
            Posts_Notes = request.POST.get('notes')

            #! authentication data
            initAuthenticate = Authenticate(request)
            AuthData = initAuthenticate.GetSession()
            
            #! init
            #! 2 anonymous'
            
            multiplier = 99999
            counter = CommPosts.objects.count()
            CounterPosts_Id = multiplier + counter
            
            init_ModelPosts = CommPosts(id=CounterPosts_Id, accounts_id = AuthData['userid'],
                                  type = 1,
                                  tags = Tags,
                                  heroes = List_Heroes, 
                                  note = Posts_Notes)
            
            #! save
            init_ModelPosts.save()
            
            if PickPosts_Id:
                init_ModelPostsChall = CommPostsChall(posts_origin_id = PickPosts_Id, posts_chall_id = CounterPosts_Id)
                init_ModelPostsChall.save()
                
            
            return HttpResponseRedirect(reverse('comm_posts_list'))
        