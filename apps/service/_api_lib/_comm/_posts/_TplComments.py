#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

#! get comments
def TplComments(Comments):
    List = []
    for comment in Comments:

        #! steam data
        initSteamData = SteamData(comment.accounts_id)
        steamDataResponse = initSteamData.GetData()
        
        
        #! arrange list posts
        List.append({
                'id' : comment.id,
                'steamid' : steamDataResponse['player']['steamid'],
                'steamavatar' : steamDataResponse['player']['avatarmedium'],
                'steamurl' : steamDataResponse['player']['profileurl'],
                'account' : comment.accounts.username,
                'note' : comment.note,
                'date' : comment.date.strftime('%A, %b %d')
        })
    return List
