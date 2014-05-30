from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! serializer
from apps.service._api._comm._serializers._votes._VotesSer import *

class VotesPost(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        data = {}
        data['accounts'] = 1;
        data['posts'] = kwargs['postsid'];
        serializer = VotesSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)