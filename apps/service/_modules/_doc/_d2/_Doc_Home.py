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

        #! requests
        api_result = requests.get(self._api_doc_findbyhero)
        #! request response variables
        api_response_url = self._api_doc_findbyhero
        api_response_status = api_result.status_code
        api_response_text = json.loads(api_result.text)
        api_response_json = api_result.json()        
       
        return render_to_response(self._template, 
                                  {#! demo
                                   'api_doc_url_all' :  self._api_doc_all,
                                   'api_doc_url_findbyhero' :  self._api_doc_findbyhero,
                                   'api_doc_url_findbyfaction' :  self._api_doc_findbyfaction,
                                   'api_doc_url_findbyclass' :  self._api_doc_findbyclass,
                                   'api_doc_url_findbyany' :  self._api_doc_findbyany,
                                   
                                   'api_root_url' :  ROOT_URL,
                                   'api_response_url' :  api_response_url,
                                   'api_response_status' :  api_response_status,
                                   'api_response_json' :  api_response_json,
                                   'api_response_result' :  api_response_text }, 
                                  context_instance=RequestContext(request))
          