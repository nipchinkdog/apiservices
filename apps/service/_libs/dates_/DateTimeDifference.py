#! Author : nip
from apps.borrow._imports.Pythons_init import *
def DateTimeDifference(dbdate, span):
    if span < 1 or not span:
        return 'Open'
    else:

        datesum = dbdate + datetime.timedelta(days=span)
        datesum = datesum.replace(tzinfo=None)
        datediff = datesum - datetime.datetime.utcnow()
        #s = datedatediff.seconds
    
        return datediff.days
