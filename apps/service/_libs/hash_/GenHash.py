from apps.borrow._imports.Encryptions_init import *
def GenHash():
    salt_one = bcrypt.gensalt()
    salt_two = bcrypt.gensalt()
    hash = bcrypt.hashpw(salt_one, salt_two)
    md5_one = hashlib.md5()
    md5_one.update(hash)
    md5_hex = str(md5_one.hexdigest())
    md5_count = int(len(md5_hex)) - 1
    md5_token = []
    selections = [20,25,30]
    selection_index = random.randint(0,2)
    selection_val = selections[selection_index]
    for num in range(selection_val):
        char = random.randint(0,md5_count)
        md5_token.append(md5_hex[char])
    _token = ''.join(md5_token)
    return _token