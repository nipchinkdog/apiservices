#! json config files
#! variable assignments
#! ex: Dire/Radiant/Str/Int/Agi
from apps.service._api_init._d2.Heroes_init import *

from apps.service._imports.Settings_init import *

class HeroesPictures():
    
    def __init__(self, Hero=False, HeroClass=False):
        
        
        self.List = {}
        self.ext = '.png'
        self.Hero = Hero
        self.HeroClass = HeroClass
        

        #! OS path
        
        self.root = ROOT_URL + '/static/service/media/_src/_d2/_Heroes'
        self.ico = ROOT_URL + '/static/service/media/_src/_d2/_MiniHeroes/'
        self.skill = ROOT_URL + '/static/service/media/_src/_d2/_Skills'

        
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
        self.HeroIcon = self.ico + self.Hero.lower() + self.ext
        self.List = {
                    'lg' : self.HeroLarge, 
                    'md' : self.HeroMedium, 
                    'sm' : self.HeroSmall, 
                    'xs' : self.HeroXSmall, 
                    'ico' : self.HeroIcon
                    }
        return self.List   
    
    def Skills(self):
        Skills = []
        Icons = []
        for skills in Heroes_Skills[self.Hero]:
            for index in range(0, len(skills)):
                index = str(index+1)
                skill = skills['sk' + index ]
                sk = 'skill_' + index
                
                #! pre format filename
                self.HeroSkillFile = self.Hero + '_' + skill[0]['name']
                self.HeroSkillFile = self.HeroSkillFile.replace (' ', '_')
                self.HeroSkillFile = self.HeroSkillFile.title()
                
                self.SkillLarge = self.skill + self.large + '/' + self.HeroSkillFile + self.ext
                self.SkillMedium = self.skill + self.medium + '/' + self.HeroSkillFile + self.ext
                self.SkillSmall = self.skill + self.small + '/' + self.HeroSkillFile + self.ext
                self.SkillXSmall = self.skill + self.xsmall + '/' + self.HeroSkillFile + self.ext
                
                Icons = {
                          'lg' : self.SkillLarge,
                          'md' : self.SkillMedium,
                          'sm' : self.SkillSmall,
                          'xs' : self.SkillXSmall,
                        }
                Skills.append({
                               sk : skill[0]['name'],
                               'desc' : skill[0]['desc'],
                               'icons' : Icons
                                })
        return Skills
                
    
    
    
    