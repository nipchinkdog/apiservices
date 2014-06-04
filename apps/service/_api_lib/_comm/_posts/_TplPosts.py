#! get tags
from apps.service._api_lib._comm._posts._TplTags import *

#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

#! get pictures
from apps.service._api_lib._comm._posts._TplPictures import *

from apps.service._comm._models.__CommPostsVotes import *
from apps.service._comm._models.__CommComments import *

def CountComments(id):
    count = CommComments.objects.filter(posts_id=id)
    return len(count)

def CountVotes(id):
    count = CommPostsVotes.objects.filter(posts_id=id)
    return len(count)

def LimitNotes(s, l=270):
    return s if len(s)<=l else s[0:l-3] + ' ...'
    
#! get posts
def TplPosts(Posts):
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
                'account' : post.accounts.username,
                'note' : post.note,
                'notelimit' : LimitNotes(post.note),
                'heroes' : post.heroes,
                'pic' : TplPictures(post.heroes),
                'tags' : TplTags(post.tags),
                'date' : post.date.strftime('%A, %b %d'),
                'comments' : CountComments(post.id),
                'votes' : CountVotes(post.id)
        })
    return List

