#! Imports
from apps.service._imports.Sessions_init import *
from apps.service._imports.Settings_init import *

#! lib: auth
from apps.service._api_lib._auth.__SteamData import *

class Authenticate(models.Model):
    
    def __init__(self, request):
        self.request = request
    
    def DestroySession(self):
        return logout(self.request)         

    def GetSession(self):
        sessionKey = self.request.session.session_key
        objSessionExists = Session.objects.filter(session_key=sessionKey).exists()
        if objSessionExists:
            objSession = Session.objects.get(session_key=sessionKey)
            userId = objSession.get_decoded().get('_auth_user_id')
            initSteamData = SteamData(userId)
            return initSteamData.GetData()
        else:
            initSteamData = SteamData(2)
            return initSteamData.GetData()
            
            
