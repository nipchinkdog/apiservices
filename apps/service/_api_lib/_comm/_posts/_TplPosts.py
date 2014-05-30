#! get tags
from apps.service._api_lib._comm._posts._TplTags import *

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
    
#! get posts
def TplPosts(Posts):
    List = []
    for post in Posts:
        #! arrange list posts
        List.append({
                'id' : post.id,
                'account' : post.accounts.username,
                'note' : post.note,
                'heroes' : post.heroes,
                'pic' : TplPictures(post.heroes),
                'tags' : TplTags(post.tags),
                'date' : post.date.strftime('%A, %b %d'),
                'comments' : CountComments(post.id),
                'votes' : CountVotes(post.id)
        })
    return List

