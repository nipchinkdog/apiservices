from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

#! serializer
from apps.service._api._comm._serializers._votes._VotesSer import *

class VotesPost(APIView):

    def get(self, request, format=None, *args, **kwargs):

        #! authentication data
        initAuth = Authenticate(request)
        AuthData = initAuth.GetSessionData()

        data = {}
        #! 2 anonymous
        data['accounts'] = AuthData['userid'];
        data['posts'] = kwargs['postsid'];
        serializer = VotesSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)