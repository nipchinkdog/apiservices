#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommPosts import *

class CommPostsChall(models.Model):
    id = models.AutoField(primary_key=True)
    posts_origin = models.ForeignKey(CommPosts, null=True, blank=True)
    posts_chall = models.ForeignKey(CommPosts, null=True, blank=True)
    class Meta:
        db_table = 'comm_posts_chall'

