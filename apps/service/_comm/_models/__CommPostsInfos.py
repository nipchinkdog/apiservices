#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommPosts import *

class CommPostsInfos(models.Model):
    id = models.IntegerField(primary_key=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    heroes = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'comm_posts_infos'

