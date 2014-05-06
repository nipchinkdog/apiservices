from apps.borrow._imports.Encryptions_init import *
def GetHash( word, db_word, db_salt):
    #! database hash

    db_hash = bcrypt.hashpw(db_word, db_salt)
    
    #! active hashing
    now_hash = bcrypt.hashpw(word, bcrypt.gensalt())
    if now_hash == db_hash:
        return True
    else:
        return False        