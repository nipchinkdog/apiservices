#! imports
from apps.service._comm._models.__CommPostsVotes import *

class ProcVotes(object):

    def __init__(self):
        pass
        
    def deleteByUserId(self, postsId, accountsId):
        objVotes = CommPostsVotes.objects.filter(posts_id=postsId, accounts_id=accountsId)
        objVotes.delete()
        return True         
