from apps.service._imports.Settings_init import * #! variables: ROOT_URL etc
from apps.service._imports.Views_init import *

class DocHome(View):
    
    _template = '_doc/_d2/index.html'
    
    #! doc request example urls
    _api_doc_all = ROOT_URL+'/api/h/all/'
    _api_doc_findbyhero = ROOT_URL+'/api/h/findByHero/Bloodseeker/'
    _api_doc_findbyfaction = ROOT_URL+'/api/h/findByFaction/r/'
    _api_doc_findbyclass = ROOT_URL+'/api/h/findByClass/agi/'
    _api_doc_findbyany = ROOT_URL+'/api/h/findByAny/r/agi'

    def get(self, request):
        
        return render_to_response(self._template, 
                                  {
                                   #! demo
                                   'api_root_url' :  ROOT_URL,
                                   'api_doc_url_all' :  self._api_doc_all,
                                   'api_doc_url_findbyhero' :  self._api_doc_findbyhero,
                                   'api_doc_url_findbyfaction' :  self._api_doc_findbyfaction,
                                   'api_doc_url_findbyclass' :  self._api_doc_findbyclass,
                                   'api_doc_url_findbyany' :  self._api_doc_findbyany,
                                   }, 
                                  context_instance=RequestContext(request))
          