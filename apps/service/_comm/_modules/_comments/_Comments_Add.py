from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! imports
from apps.service._comm._models.__CommComments import *

class CommentsAdd(View):
    
    def post(self, request, *args, **kwargs):
        
            Comments_Notes = request.POST.get('notes')
            Comments_PostId = request.POST.get('post')
            
            #! init
            init_ModelComments = CommComments(accounts_id = 1,
                                  posts_id = Comments_PostId,
                                  note = Comments_Notes)

            #! save
            init_ModelComments.save()
            return HttpResponse(request['postid'])
