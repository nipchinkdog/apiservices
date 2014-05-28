#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommAccounts import *
from apps.service._comm._models.__CommPosts import *

class CommComments(models.Model):
    id = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(CommAccounts, null=True, blank=True)
    posts = models.ForeignKey(CommPosts, null=True, blank=True)
    note = models.CharField(max_length=120L, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comm_comments'
