from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! imports
from apps.service._comm._models.__CommPosts import *

class PostsAdd(View):
    
    def post(self, request, *args, **kwargs):
        
        if request.POST:

            #! init
            Posts_Heroes = request.POST.getlist('heroes')
            List_Heroes = ','.join(Posts_Heroes)
            Posts_Lanes = request.POST.getlist('lanes')
            List_Lanes = ','.join(Posts_Lanes)
            
            Tags = List_Heroes + ',' + List_Lanes
            
            Posts_Notes = request.POST.get('notes')
            
            #! init
            init_ModelPosts = CommPosts(accounts_id = 1,
                                  type = 1,
                                  tags = Tags,
                                  heroes = List_Heroes, 
                                  note = Posts_Notes)
            
            #! save
            init_ModelPosts.save()
            
            return HttpResponseRedirect(reverse('comm_posts_list'))
                
            return render_to_response(self._template, 
                                      {},
                                      context_instance=RequestContext(request))
        