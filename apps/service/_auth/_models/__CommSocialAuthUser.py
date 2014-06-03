#! Default Models
from apps.service._models.__Default import *

from apps.service._auth._models.__CommAuthUser import *

class CommSocialAuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(CommAuthUser)
    provider = models.CharField(max_length=32L)
    uid = models.CharField(max_length=255L)
    extra_data = models.TextField()
    class Meta:
        db_table = 'social_auth_usersocialauth'