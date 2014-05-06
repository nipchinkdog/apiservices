# Author : nip
from apps.borrow._imports.Pythons_init import *
def DateTimeDifferenceCss(n):
    CssClass_1 = 'brw-card-red'
    CssClass_2 = 'brw-card-green'
    if n < 0:
        return CssClass_1
    else:
        return CssClass_2
