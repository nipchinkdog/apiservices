#! get tags
from apps.service._api_lib._comm._posts._TplTags import *

#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

#! get pictures
from apps.service._api_lib._comm._posts._TplPictures import *

from apps.service._comm._models.__CommPostsVotes import *
from apps.service._comm._models.__CommComments import *
from apps.service._comm._models.__CommPostsChall import *

def CountComments(postsId):
    count = CommComments.objects.filter(posts_id=postsId)
    return len(count)

def CountVotes(postsId):
    count = CommPostsVotes.objects.filter(posts_id=postsId)
    return len(count)

def CountChall(postsId):
    count = CommPostsChall.objects.filter(posts_origin_id=postsId)
    return len(count)

def CountChallTo(postsId):
    count = CommPostsChall.objects.filter(posts_chall_id=postsId)
    return len(count)

def LimitNotes(s, l=50):
    return s if len(s)<=l else s[0:l-3] + ' ...'

def CountVotesSessionId(postsId, accountsId):
    if accountsId == 2: #! anonymous session
        return ''
    objVotes = CommPostsVotes.objects.filter(posts_id=postsId, accounts_id=accountsId).exists()
    if objVotes:
        return 'comm-voted'
    else:
        return ''

def NoteWordCount(note):
    import math
    words = ''.join(c if c.isalnum() else '' for c in note).split()
    avgWordRead = 180 #! words per minute
    wordsSuffix = ['read the note attached', ' min read'] #! suffixes
    wordsCount = len(words)
    wordsRead = ( ( wordsCount / avgWordRead ) * 60 ) / 60
    #wordsRead = math.floor(wordsRead)
    if wordsCount > 0:
        if wordsRead < 1: #! seconds read
            return str(wordsSuffix[0])
        elif wordsRead >= 1: #! minute read
            return wordsRead + str(wordsSuffix[1])
    else:
        return ''

#! get posts
def TplPosts(Posts, SessionId=False):
    List = []
    for post in Posts:
        
        #! steam data
        initSteamData = SteamData(post.accounts_id)
        steamDataResponse = initSteamData.GetData()
        
        #! arrange list posts
        List.append({
                'id' : post.id,
                'steamid' : steamDataResponse['player']['steamid'],
                'steamavatar' : steamDataResponse['player']['avatarmedium'],
                'steamurl' : steamDataResponse['player']['profileurl'],
                'accountid' : post.accounts_id,
                'account' : post.accounts.username,
                'note' : post.note,
                'notewords' : NoteWordCount(post.note),
                'notelimit' : LimitNotes(post.note),
                'heroes' : post.heroes,
                'pic' : TplPictures(post.heroes),
                'tags' : TplTags(post.tags),
                'date' : post.date.strftime('%A, %b %d'),
                'comments' : CountComments(post.id),
                'challenge' : CountChall(post.id),
                'votes' : CountVotes(post.id),
                'votessession' : CountVotesSessionId(post.id, SessionId)
        })
    return List

