#! Imports
from apps.service._imports.Sessions_init import *
from apps.service._imports.Settings_init import *
import simplejson

class SteamData(models.Model):
    
    def __init__(self, id):
        self.uid = id
    
    def GetData(self):
        objSocialExists = CommSocialAuthUser.objects.filter(user_id=self.uid).exists()
        if objSocialExists:
            steamData  = CommSocialAuthUser.objects.get(user_id=self.uid)
            extraData = simplejson.loads(steamData.extra_data)
            extraData['userid'] = self.uid
            return extraData
        else:
            steamData  = CommSocialAuthUser.objects.get(user_id=2)
            extraData = simplejson.loads(steamData.extra_data)
            extraData['userid'] = 2
            return extraData
            

