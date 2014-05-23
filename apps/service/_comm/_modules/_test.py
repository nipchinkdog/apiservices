from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

#! imports
def testview(request):
    #return HttpResponse('test')
    return render_to_response('_ng/list.html', 
                           {},
                           context_instance=RequestContext(request))
            