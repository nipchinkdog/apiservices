from apps.borrow._imports.Sessions_init import *
def SetSessionReserve(request, id, name):
    sess = SessionStore(session_key=request.session['sess'])
    sess['r_uid']= id
    sess['r_name']= name
    sess.save()
    request.session['r_uid'] = id
    request.session['r_name'] = name
    return True
