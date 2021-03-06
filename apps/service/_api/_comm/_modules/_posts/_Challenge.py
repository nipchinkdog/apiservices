from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! lib posts
from apps.service._api_lib._comm._posts._ProcPosts import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

class PostsChallenge(APIView):

    def get(self, request, format=None, *args, **kwargs):
        page = int(kwargs['page'])
        limit = int(kwargs['limit'])
        id = str(kwargs['id'])
        
        initAuthenticate = Authenticate(request)
        authData = initAuthenticate.GetSession()
        sessionId = authData['userid']
        
        #! limit posts
        init_Posts = ProcPosts()
        init_Posts.sortByChall(page, limit, id, sessionId)
        sortByChall = init_Posts._GetTemplate()
        return Response( sortByChall )
 