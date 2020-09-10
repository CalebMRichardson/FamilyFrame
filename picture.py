import settings
import os

class Picture():

    def __init__(self, file_path):
        super().__init__()

        self.error = False
        self.path_to_file = file_path
        
        self.init_photo()

        if self.error == True:
            self.init_photo(settings.BROKEN_LINK)
            print('Picture Error: Broken Link')

    def init_photo(self):

        if os.path.exists(self.path_to_file) != True:
            self.error = True
            return        
