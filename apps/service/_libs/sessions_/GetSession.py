from apps.borrow._imports.Sessions_init import *
def GetSession(request, val):
    sessKey = request.session.get('sess')
    if sessKey:
        mySession = Session.objects.get(session_key=sessKey)
        if mySession:
            return mySession.get_decoded().get(val)    
        else:
            return False 
    else:
        return False
