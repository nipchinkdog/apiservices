from apps.service._imports.Rest_init import *

#! models
from apps.service._comm._models.__CommComments import *

class CommentsSer(serializers.ModelSerializer):
    class Meta:
        model = CommComments