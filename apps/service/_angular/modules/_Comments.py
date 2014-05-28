from apps.service._imports.Views_init import *

#! Angular : Comments
def Comments(request):
    return render(request, '_angular/_comments/list.html')
            