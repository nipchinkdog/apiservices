from apps.service._imports.Views_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

class Logout(View):
    
    def get(self, request, *args, **kwargs):
            
        #! authentication data
        initAuth = Authenticate(request)
        AuthData = initAuth.DestroySession()
        HttpResponseRedirect(reverse('comm_posts_list'))
