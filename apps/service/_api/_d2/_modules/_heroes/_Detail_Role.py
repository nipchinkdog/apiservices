from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

class HeroesDetail(APIView):

    def get_object(self, hero):
        try:
            info = HeroesParser(hero)
            info.Heroes_Detail()
            data = info._GetHeroesDetailTemplate()
            return data
        except:
            raise Http404

    def get(self, request, hero, format=None):
        return Response(self.get_object(hero))
          