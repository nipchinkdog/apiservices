#! json config files
#! variable assignments
#! ex: Dire/Radiant/Str/Int/Agi
from apps.service._api_init._d2.Heroes_init import *
import os
        
#! All Heroes in api_init
Heroes = Heroes_Overall

css = ''
for hero in Heroes:
    
    size_l = 'width: 256px; height: 144px;'
    size_m = 'width: 176px; height: 99px;'
    size_s = 'width: 96px; height: 54px;'
    size_ss = 'width: 76px; height: 43px;'
    size_xs = 'width: 56px; height: 32px;'
    size_ico = 'width: 32px; height: 32px;'
    
    filelarge = '_Heroes/_Large/'
    filemedium = '_Heroes/_Medium/'
    filesmall = '_Heroes/_Small/'
    filessmall = '_Heroes/_SSmall/'
    filexsmall = '_Heroes/_XSmall/'
    fileicon = '_MiniHeroes/'
    
    filetype = '_Class_' + Heroes[hero][0]['type']
    filepics = Heroes[hero][0]['name'] + '.png'
    filecss = filetype + '/' + filepics
    filecssicon = filepics.lower()
    
    #! variations
    h1 = '.aps-' + Heroes[hero][0]['name']+ '-lg' + ' { background: url("'+ filelarge + filecss +'"); '+ size_l +' }' + '\n'
    h2 = '.aps-' + Heroes[hero][0]['name']+ '-md' + ' { background: url("'+ filemedium + filecss +'"); '+ size_m +' }' + '\n'
    h3 = '.aps-' + Heroes[hero][0]['name']+ '-sm' + ' { background: url("'+ filesmall + filecss +'"); '+ size_s +' }' + '\n'
    h3s = '.aps-' + Heroes[hero][0]['name']+ '-ssm' + ' { background: url("'+ filessmall + filecss +'"); '+ size_ss +' }' + '\n'
    h4 = '.aps-' + Heroes[hero][0]['name']+ '-xs' + ' { background: url("'+ filexsmall + filecss +'"); '+ size_xs +' }' + '\n'
    icon = '.aps-' + Heroes[hero][0]['name']+ '-ico' + ' { background: url("'+ fileicon + filecssicon +'"); '+ size_ico +' }' + '\n'
    
    css += h1 + h2 + h3 + h3s + h4 + icon

#! open and write the file
public_path = os.path.realpath('Public')  # get current directory
service_path = os.path.join(public_path, 'service')
media_path = os.path.join(service_path, 'media')
src_path = os.path.join(media_path, '_src')
app_path = os.path.join(src_path, '_d2')
file_path = os.path.join(app_path, 'heroes-css-framework.css')

file = open(file_path, 'w')
file.write(css)
file.close()
