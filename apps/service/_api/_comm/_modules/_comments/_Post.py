from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

#! serializer
from apps.service._api._comm._serializers._comments._CommentsSer import *

class CommentsPost(APIView):

    def post(self, request, format=None, *args, **kwargs):

        #! authentication data
        initAuthenticate = Authenticate(request)
        AuthData = initAuthenticate.GetSession()

        data = JSONParser().parse(request)
        #! 2 anonymous
        data['accounts'] = AuthData['userid'];
        serializer = CommentsSer(data=data)
        if serializer.is_valid():
            serializer.save()
            serresponse = serializer.data
            serresponse['steamid'] = AuthData['steamid']
            serresponse['steamavatar'] = AuthData['avatar']
            return Response(serresponse)
        return Response(serializer.errors) 