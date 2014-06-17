from apps.service._imports.Views_init import *

#! Angular : About
def About(request):
    return render(request, '_angular/_pages/about.html')