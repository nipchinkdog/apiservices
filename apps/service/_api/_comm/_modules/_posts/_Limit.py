from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! lib posts
from apps.service._api_lib._comm._posts._ProcPosts import *

class PostsLimit(APIView):

    def get(self, request, format=None, *args, **kwargs):
        page = int(kwargs['page'])
        limit = int(kwargs['limit'])
        
        #! limit posts
        init_Posts = ProcPosts()
        init_Posts.sortByDatePaginated(page, limit)
        sortByDatePosts = init_Posts._GetTemplate()
        return Response( sortByDatePosts )
 