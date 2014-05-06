import os

class HeroesStrings():
    
    def __init__(self):
        
        self.ext = '.json'

        #! OS path
        self.public = os.path.realpath('Public') 
        self.service = os.path.join(self.public, 'service')
        self.root = os.path.join(self.public, '/media/_json/_d2/_Heroes')

        
    def Strings(self, para):
        test = open(self.root + para + self.ext)
        return test
            