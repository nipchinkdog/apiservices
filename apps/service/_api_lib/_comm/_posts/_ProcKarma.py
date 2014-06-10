#! imports
from apps.service._comm._models.__CommPosts import *
from apps.service._comm._models.__CommPostsVotes import *

class ProcKarma(object):

    def __init__(self, accountsId):
        self.accountsId = accountsId
        
    def GetKarma(self):
        objPosts = CommPosts.objects.filter(accounts_id=self.accountsId).values_list('id', flat=True)
        objVotesDraw = CommPostsVotes.objects.filter(posts_id__in=objPosts)
        objVotesCast = CommPostsVotes.objects.filter(accounts_id=self.accountsId)
        return len(objVotesDraw) - len(objVotesCast)         
