#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommAccounts import *
from apps.service._comm._models.__CommPosts import *

class CommPostsVotes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    accounts = models.ForeignKey(CommAccounts, null=True, blank=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    class Meta:
        db_table = 'comm_votes'
