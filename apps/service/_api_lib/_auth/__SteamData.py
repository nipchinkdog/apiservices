#! Imports
from apps.service._imports.Sessions_init import *
from apps.service._imports.Settings_init import *

class SteamData(models.Model):
    
    def __init__(self, uid):
        self.steamData  = CommSocialAuthUser.objects.get(user_id=uid)
        self.steamid = self.steamData.uid
    
    def GetData(self):
        SteamData = {}
        if self.steamid == '000':
            SteamData['steamid'] =  self.steamid 
            SteamData['steamavatar'] = ROOT_URL + '/static/service/media/_src/_d2/anony.png'
            return SteamData
        else:
            SteamData['steamid'] =  self.steamid 
            SteamData['steamavatar'] = self.GetAvatar();
            return SteamData
            
        
    
    def GetAvatar(self):
        steamid =  self.steamid
        import urllib
        import urllib2
        from social_auth.utils import setting
        try:
            import json as simplejson
        except ImportError:
            try:
                import simplejson
            except ImportError:
                from django.utils import simplejson        
        USER_INFO = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?'
        url = USER_INFO + urllib.urlencode({'key': setting('STEAM_API_KEY'),'steamids': steamid})
        try:
            player = simplejson.load(urllib2.urlopen(url))
        except (ValueError, IOError):
            pass
        else:
            if len(player['response']['players']) > 0:
                player = player['response']['players'][0]
                avatar = player.get('avatarmedium')
                return avatar
