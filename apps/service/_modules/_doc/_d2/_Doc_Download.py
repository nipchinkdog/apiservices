from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

class DocDownload(View):
    _template = '_doc/_d2/index-doc-css-download.html'
    def get(self, request):
        return render_to_response(self._template, 
                                  {},
                                  context_instance=RequestContext(request))