from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! serializer
from apps.service._api._comm._serializers._comments._CommentsSer import *

class CommentsPost(APIView):

    def post(self, request, format=None, *args, **kwargs):
        data = JSONParser().parse(request)
        data['accounts'] = 1;
        serializer = CommentsSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 