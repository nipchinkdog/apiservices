from apps.service._imports.Views_init import *
from apps.service._imports.Sessions_init import *

#! imports
def Logout(request):
    #return HttpResponse('test')
    return render_to_response('_ng/list.html', 
                           {},
                           context_instance=RequestContext(request))
            