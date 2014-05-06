from apps.borrow._imports.Sessions_init import *
def SetSession(request, id, name):
    if request.session.get('sess'):
        sess = SessionStore(session_key=request.session.get('sess'))
        sess['uid']= id
        sess['name']= name
        sess.save()
        request.session['uid'] = id
        request.session['name'] = name
    else:
        sess = SessionStore()
        sess['uid']= id
        sess['name']= name
        sess.save()
        request.session['uid'] = id
        request.session['name'] = name
        request.session['sess'] = sess.session_key

    return True
