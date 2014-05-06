from apps.borrow._imports.Encryptions_init import *
def SetHash(word):
    return bcrypt.hashpw(word, bcrypt.gensalt())
