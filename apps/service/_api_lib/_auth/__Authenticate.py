#! Imports
from apps.service._imports.Sessions_init import *
from apps.service._imports.Settings_init import *

#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

class Authenticate(models.Model):
    
    def __init__(self, request):
        self.request = request
    
    def DestroySession(self):
        logout(self.request)          

    def GetSession(self):
        sessionKey = self.request.session.session_key
        if sessionKey:
            return sessionKey
        else:
            return False
    
    def GetSessionData(self):
        SessionData = {}
        if self.GetSession():
            sessionKey = self.GetSession()
            objSession = Session.objects.get(session_key=sessionKey)
            uid = objSession.get_decoded().get('_auth_user_id')
            objUser = User.objects.get(pk=uid)
           
            #! steam data
            initSteamData = SteamData(objUser.id)
            SteamDataResponse = initSteamData.GetData()

            SessionData['steamid'] = SteamDataResponse['steamid']
            SessionData['avatar'] = SteamDataResponse['steamavatar']
            SessionData['userid'] = objUser.id
            SessionData['username'] = objUser.username
            return SessionData
        else:
            SessionData['steamid'] = 0
            SessionData['avatar'] = ROOT_URL + '/static/service/media/_src/_d2/anony.png'
            SessionData['userid'] = 2
            SessionData['username'] = 'Anonymous'
            return SessionData
        
        
