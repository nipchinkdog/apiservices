#! Pictures Lib
from apps.service._api_lib._d2._heroes._HeroesPictures import *
 
#! Response Template
class HeroesResponseTemplate(object):
    
    def __init__(self, Heroes):
        self.List = []
        self.Heroes_Data = Heroes
        

    def _GetTemplate(self, heroes_data, pictures_data):
        self.List.append({
                          'hero' : heroes_data['name'],
                          'info' : heroes_data,
                          'avatar' : pictures_data,
                        })
        
        List = sorted(self.List, key=lambda k: (k['hero']))
        self.List = List
        return self.List
        
    
    def _GetHeroesDetailTemplate(self):

        #! Heroes Pictures
        Pictures_init = HeroesPictures(self.Heroes_Data['name'], 
                                       self.Heroes_Data['type'])
        self.Pictures_Data = Pictures_init.Pictures()

        #! construct data
        return self._GetTemplate(self.Heroes_Data, self.Pictures_Data)

        
    def _GetHeroesListTemplate(self):
        for hero in self.Heroes_Data:

            #! Heroes Pictures
            Pictures_init = HeroesPictures(self.Heroes_Data[hero][0]['name'], 
                                           self.Heroes_Data[hero][0]['type'])
            self.Pictures_Data = Pictures_init.Pictures()
    
            #! construct data
            self._GetTemplate(self.Heroes_Data[hero][0], self.Pictures_Data)
        
        return self.List
