#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommPosts import *
from django.contrib.auth.models import User

class CommPostsVotes(models.Model):
    id = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(User, null=True, blank=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    class Meta:
        db_table = 'comm_votes'
