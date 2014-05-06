from apps.service._imports.Views_init import *

#! Heroes : Classes
root_url = '_d2/_heroes/'

Heroes_Dire_Agi = simplejson.loads( render_to_string(root_url+'Heroes_Dire_Agi.json'))
Heroes_Dire_Int = simplejson.loads( render_to_string(root_url+'Heroes_Dire_Int.json'))
Heroes_Dire_Str = simplejson.loads( render_to_string(root_url+'Heroes_Dire_Str.json'))
Heroes_Radiant_Agi = simplejson.loads( render_to_string(root_url+'Heroes_Radiant_Agi.json'))
Heroes_Radiant_Int = simplejson.loads( render_to_string(root_url+'Heroes_Radiant_Int.json'))
Heroes_Radiant_Str = simplejson.loads( render_to_string(root_url+'Heroes_Radiant_Str.json'))

#! Heroes : Dire
Heroes_Dire_All = dict( Heroes_Dire_Agi.items() + Heroes_Dire_Int.items() + Heroes_Dire_Str.items() )
#! Heroes : Radiant
Heroes_Radiant_All = dict( Heroes_Radiant_Agi.items() + Heroes_Radiant_Int.items() + Heroes_Radiant_Str.items() )
#! Heroes : Agi
Heroes_Agi_All = dict( Heroes_Dire_Agi.items() + Heroes_Radiant_Agi.items() )
#! Heroes : Agi
Heroes_Int_All = dict( Heroes_Dire_Int.items() + Heroes_Radiant_Int.items() )
#! Heroes : Agi
Heroes_Str_All = dict( Heroes_Dire_Str.items() + Heroes_Radiant_Str.items() )
#! Heroes : All
Heroes_Overall = dict( Heroes_Dire_All.items() + Heroes_Radiant_All.items() )

