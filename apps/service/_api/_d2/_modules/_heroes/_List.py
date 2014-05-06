from apps.service._imports.Views_init import *
from apps.service._imports.Rest_init import *

#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

class HeroesList(APIView):

    def get(self, request, format=None):
        info = HeroesParser()
        info.Heroes_All()
        data = info._GetHeroesListTemplate()
        return Response( data )
 