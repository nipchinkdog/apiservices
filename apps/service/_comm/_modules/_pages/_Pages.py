from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! lib: auth
from apps.service._api_lib._auth.__Authenticate import *

class PagesAbout(View):
    _template = '_pages/about.html'
    def get(self, request, *args, **kwargs):
        initAuthenticate = Authenticate(request)
        AuthData = initAuthenticate.GetSession()
        return render_to_response(self._template, 
                                  { 'AuthData' : AuthData },
                                  context_instance=RequestContext(request))        