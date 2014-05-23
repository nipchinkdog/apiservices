#! Default Models
from apps.service._models.__Default import *

class CommPostsHeroes(models.Model):
    id = models.IntegerField(primary_key=True)
    heroes_origin = models.CharField(max_length=50L, blank=True)
    heroes_chall = models.CharField(max_length=50L, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comm_posts_heroes'
