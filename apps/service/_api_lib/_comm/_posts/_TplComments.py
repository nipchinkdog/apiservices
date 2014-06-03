#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

#! get comments
def TplComments(Comments):
    List = []
    for comment in Comments:

        #! steam data
        initSteamData = SteamData(comment.accounts_id)
        SteamDataResponse = initSteamData.GetData()
        stmid = SteamDataResponse['steamid']
        avatar = SteamDataResponse['steamavatar']
        
        #! arrange list posts
        List.append({
                'id' : comment.id,
                'steamid' : stmid,
                'steamavatar' : avatar,
                'account' : comment.accounts.username,
                'note' : comment.note,
                'date' : comment.date.strftime('%A, %b %d')
        })
    return List
