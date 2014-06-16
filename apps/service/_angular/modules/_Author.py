from apps.service._imports.Views_init import *

#! Angular : Author
def Author(request):
    return render(request, '_angular/_author/list.html')