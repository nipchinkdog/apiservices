from apps.service._imports.Settings_init import *

class HeroesPictures():
    
    def __init__(self, Hero=False, HeroClass=False):
        
        
        self.List = {}
        self.ext = '.png'
        self.Hero = Hero
        self.HeroClass = HeroClass
        

        #! OS path
        
        self.root = ROOT_URL + '/static/service/media/_src/_d2/_Heroes'

        
        #! Sizes
        self.large = '/_Large'
        self.medium = '/_Medium'
        self.small = '/_Small'
        self.xsmall = '/_XSmall'

        #! Classes
        self.Class = '/_Class_' + HeroClass + '/'

    
    
      

    def Pictures(self):
        self.HeroLarge = self.root + self.large + self.Class + self.Hero + self.ext
        self.HeroMedium = self.root + self.medium + self.Class + self.Hero + self.ext
        self.HeroSmall = self.root + self.small + self.Class + self.Hero + self.ext
        self.HeroXSmall = self.root + self.xsmall + self.Class + self.Hero + self.ext
        self.List = {'lg' : self.HeroLarge, 'md' : self.HeroMedium, 'sm' : self.HeroSmall, 'xs' : self.HeroXSmall}
        return self.List        