from PyQt5.QtWidgets import (QLabel)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import settings
import os

class Picture(QPixmap):

    def __init__(self, _file_name):
        super().__init__()

        self.error = False
        self.path_to_file = ''
        
        self.init_photo(_file_name)

        if self.error == True:
            self.init_photo(settings.BROKEN_LINK)
            print('Picture Error: Broken Link')

    def init_photo(self, file_name):
        
        self.path_to_file = os.path.join(settings.PHOTO_DIR, file_name)

        if os.path.exists(self.path_to_file) != True:
            self.error = True
            return
        
        pixmap = QPixmap(self.path_to_file)
        fixed_pixmap = pixmap.scaled(settings.WIDTH, settings.HEIGHT, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.swap(fixed_pixmap)
        
