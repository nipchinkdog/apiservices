from apps.service._imports.Rest_init import *

#! models
from apps.service._comm._models.__CommPostsVotes import *

class VotesSer(serializers.ModelSerializer):
    class Meta:
        model = CommPostsVotes