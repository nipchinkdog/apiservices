#! get tags
from apps.service._api_lib._comm._posts._TplTags import *

#! get pictures
from apps.service._api_lib._comm._posts._TplPictures import *

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
                'datetime' : post.datetime.strftime('%A, %b %d')
        })
    return List

