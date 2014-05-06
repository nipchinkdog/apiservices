#! json config files
#! variable assignments
#! ex: Dire/Radiant/Str/Int/Agi
from apps.service._api_init._d2.Heroes_init import *

#! Parameters 
#! variable assigments
#! ex: Radiant__Para = 'r', Dire__Para = 'd'
from apps.service._api_init._d2.Parameters_init import *

#! Response Template
from apps.service._api_lib._d2._heroes._HeroesResponseTemplates import *
        
class HeroesParser(HeroesResponseTemplate):
        
    def __init__(self, hero=False):
        self.hero = hero

    #! format parameter specific hero
    def f_para_hero(self, parameter):
        parameter = parameter.lower()
        return parameter.title()          
    
    #! format parameter others
    def f_para_other(self, parameter):
        return parameter.lower()          

    #! Single
    def Heroes_Detail(self):
        hero = self.f_para_hero(self.hero)
        Heroes = Heroes_Overall[hero][0]
        super(HeroesParser,self).__init__(Heroes)

    #! All
    def Heroes_All(self):
        Heroes = Heroes_Overall
        super(HeroesParser,self).__init__(Heroes)
        

    #! Faction : Radiant/Dire
    #! faction = r, d
    def Heroes_Faction(self, faction=False ):
        
        #! prepare format
        faction = self.f_para_other(faction)
        
        if faction == Radiant__Para:
            Heroes = Heroes_Radiant_All
        elif faction == Dire__Para:
            Heroes = Heroes_Dire_All
        else:
            #! if none specified get all instead
            return self.Heroes_All()
            
        super(HeroesParser,self).__init__(Heroes)
    
    #! Class : Str/Agi/Int
    #! class = str, agi, int
    def Heroes_Class(self, clss=False ):
        
        #! prepare format
        clss = self.f_para_other(clss)
        
        if clss == Agi__Para:
            Heroes = Heroes_Agi_All
        elif clss == Int__Para:
            Heroes = Heroes_Int_All
        elif clss == Str__Para:
            Heroes = Heroes_Str_All
        else:
            #! if none specified get all instead
            return self.Heroes_All()
            
        super(HeroesParser,self).__init__(Heroes)
    
    #! Faction : Radiant/Dire : Str/Agi/Int
    #! faction = r, d
    #! clss = str, agi, int
    def Heroes_Faction_And_Class(self, faction=False, clss=False ):
        
        #! prepare format
        faction = self.f_para_other(faction)
        clss = self.f_para_other(clss)
        
        #! r
        if faction == Radiant__Para and clss == Agi__Para:
            Heroes = Heroes_Radiant_Agi
        elif faction == Radiant__Para and faction == Int__Para:
            Heroes = Heroes_Radiant_Int
        elif faction == Radiant__Para and faction == Str__Para:
            Heroes = Heroes_Radiant_Agi
        
        #! d
        elif faction == Dire__Para and clss == Agi__Para:
            Heroes = Heroes_Dire_Agi
        elif faction == Dire__Para and faction == Int__Para:
            Heroes = Heroes_Dire_Int
        elif faction == Dire__Para and faction == Str__Para:
            Heroes = Heroes_Dire_Str
        
        #! faction not specified
        elif not faction: 
            return self.Heroes_Class(faction)
        #! class not specified
        elif not clss:
            return self.Heroes_Faction(faction)
        else:
            return self.Heroes_Faction(faction)
            
        super(HeroesParser,self).__init__(Heroes)


