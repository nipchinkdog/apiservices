# author: Jayson
# Avatar

def Avatar(id):
    import os
    root = '/static/borrow/media/avt/'
    pic = str(id)+'.jpg'
    module_dir = os.path.realpath('public')  # get current directory
    app = os.path.join(module_dir, 'borrow')
    type = os.path.join(app, 'media')
    directory = os.path.join(type, 'avt')
    file = os.path.join(directory, pic)
    deffault = '0.jpg'
    if os.path.exists(file):
        avt = root + pic    
    else:
        avt = root + deffault

    return avt

        
        