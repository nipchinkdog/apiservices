from apps.service._imports.Views_init import *

#! Angular : Posts
def Search(request):
    return render(request, '_angular/_posts/list.html')