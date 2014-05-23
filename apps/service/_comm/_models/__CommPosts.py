#! Default Models
from apps.service._models.__Default import *

#! imports
from apps.service._comm._models.__CommAccounts import *

class CommPosts(models.Model):
    id = models.AutoField(primary_key=True)
    accounts = models.ForeignKey(CommAccounts, null=True, blank=True)
    heroes = models.CharField(max_length=120L, blank=True)
    note = models.CharField(max_length=120L, blank=True)
    type = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True, auto_now=True)
    datetime = models.DateTimeField(null=True, blank=True, auto_now=True)
    class Meta:
        db_table = 'comm_posts'
