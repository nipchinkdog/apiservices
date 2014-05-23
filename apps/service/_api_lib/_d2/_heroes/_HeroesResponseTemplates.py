#! Pictures Lib
from apps.service._api_lib._d2._heroes._HeroesPictures import *
 
#! Response Template
class HeroesResponseTemplate(object):
    
    def __init__(self, Heroes):
        self.List = []
        self.Heroes_Data = Heroes
        

    def _GetTemplate(self, heroes_data, pictures_data, skills_data, pictures_size):
        self.List.append({
                          'hero' : heroes_data['name'],
                          'info' : heroes_data,
                          'avatar' : pictures_data,
                          'skills' : skills_data,
                          'psizes' : pictures_size,
                        })
        
        List = sorted(self.List, key=lambda k: (k['hero']))
        self.List = List
        return self.List
        
    
    def _GetHeroesDetailTemplate(self):

        #! Heroes Pictures
        Pictures_init = HeroesPictures(self.Heroes_Data['name'], 
                                       self.Heroes_Data['type'])
        self.Pictures_Data = Pictures_init.Pictures()
        self.Skills_Data = Pictures_init.Skills()
        self.Pictures_Sizes = Pictures_init.PicturesSizes()

        #! construct data
        return self._GetTemplate(self.Heroes_Data, self.Pictures_Data, self.Skills_Data, self.Pictures_Sizes)

        
    def _GetHeroesListTemplate(self):
        for hero in self.Heroes_Data:

            #! Heroes Pictures
            Pictures_init = HeroesPictures(self.Heroes_Data[hero][0]['name'], 
                                           self.Heroes_Data[hero][0]['type'])
            self.Pictures_Data = Pictures_init.Pictures()
            self.Skills_Data = Pictures_init.Skills()
            self.Pictures_Sizes = Pictures_init.PicturesSizes()
    
            #! construct data
            self._GetTemplate(self.Heroes_Data[hero][0], self.Pictures_Data, self.Skills_Data, self.Pictures_Sizes)
        
        return self.List
