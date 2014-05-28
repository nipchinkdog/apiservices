from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! lib posts
from apps.service._api_lib._comm._posts._ProcComments import *

class CommentsList(APIView):

    def get(self, request, format=None, *args, **kwargs):
        id = int(kwargs['id'])
        #! list comments
        init_Comments = ProcComments()
        init_Comments.findByPostsId(id)
        data = init_Comments._GetTemplate()
        return Response( data )
 