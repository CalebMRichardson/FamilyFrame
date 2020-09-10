import settings
import os

class Picture():

    def __init__(self, file_path):

        self.error = False
        self.path_to_file = file_path
        
        self.init_photo()

        if self.error == True:
            self.init_photo(settings.BROKEN_LINK)

    def init_photo(self):

        if os.path.exists(self.path_to_file) != True:
            self.error = True
        else:
            self.error = False
