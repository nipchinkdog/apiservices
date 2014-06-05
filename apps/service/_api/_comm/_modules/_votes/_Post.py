from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! models
from apps.service._comm._models.__CommPostsVotes import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *
#! lib: comm
from apps.service._api_lib._comm._posts._ProcVotes import *

#! serializer
from apps.service._api._comm._serializers._votes._VotesSer import *

class VotesPost(APIView):
    
    def get_Auth(self, request):
        #! authentication data
        initAuthenticate = Authenticate(request)
        authData = initAuthenticate.GetSession()
        return authData
        
    def get(self, request, format=None, *args, **kwargs):
        #! call Auth
        authData = self.get_Auth(request)
        
        #! assign to data
        data = {}
        data['accounts'] = authData['userid']
        data['posts'] = kwargs['postsid']
        serializer = VotesSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors)

    def delete(self, request, format=None, *args, **kwargs):
        #! call auth
        authData = self.get_Auth(request)
        accountsId = authData['userid']
        postId = kwargs['postsid']
        #! call procedure
        initProcVotes = ProcVotes()
        initProcVotes.deleteByUserId(postId, accountsId)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    