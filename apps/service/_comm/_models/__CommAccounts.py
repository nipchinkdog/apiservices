#! Default Models
from apps.service._models.__Default import *

class CommAccounts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20L, blank=True)
    password = models.CharField(max_length=20L, blank=True)
    email = models.CharField(max_length=20L, blank=True)
    class Meta:
        db_table = 'comm_accounts'
