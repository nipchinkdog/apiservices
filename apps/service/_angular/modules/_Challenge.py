from apps.service._imports.Views_init import *

#! Angular : Challenge
def Challenge(request):
    return render(request, '_angular/_challenge/list.html')