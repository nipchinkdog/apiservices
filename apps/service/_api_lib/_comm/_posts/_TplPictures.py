#! parser
from apps.service._api_lib._d2._heroes._HeroesParser import *

#! get pictures
def TplPictures(Heroes):
    List = []
    size = 'ssm'
    Heroes = Heroes.split(',')
    for hero in Heroes:
        info = HeroesParser(hero)
        info.Heroes_Detail()
        hinfo = info._GetHeroesDetailTemplate()
        List.append({
                        'hero' : hero,
                        'css' : 'aps-'+str(hero)+'-ssm',
                        'picture' : hinfo[0]['avatar'][size],
                        'w' : hinfo[0]['psizes'][size]['w'],
                        'h' : hinfo[0]['psizes'][size]['h'],
        })
    return List
