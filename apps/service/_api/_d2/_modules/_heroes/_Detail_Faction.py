from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

class HeroesDetail(APIView):

    def get_object(self, faction):
        try:
            info = HeroesParser()
            info.Heroes_Faction(faction)
            data = info._GetHeroesListTemplate()
            return data
        except:
            raise Http404

    def get(self, request, faction, format=None):
        return Response(self.get_object(faction))
          