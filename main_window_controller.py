from controller_base import ControllerBase
from main_window import MainWindow
from picture import Picture
import os
import settings

class MainWindowController(ControllerBase):

    def __init__(self, app):
        super().__init__(app)

        self.pictures = []
        self.index = 0
    
        self.init_controller()

    def init_controller(self):
        self._view = MainWindow()
        self._view.setMouseTracking(True)
        self.load()
        self._view.next_button.clicked.connect(self.next_button_pressed)
        if len(self.pictures) > 0:
            self._view.set_picture(self.pictures[self.index])

    def next_button_pressed(self):
        self.move_to_previous_picture()

    def move_to_next_picture(self):
        if (self.index) == len(self.pictures) -1:
            self.index = 0
        else:
            self.index+=1
        self._view.update_picture(self.pictures[self.index])

    def move_to_previous_picture(self):
        if (self.index) == 0:
            self.index = len(self.pictures)-1
        else:
            self.index-=1
        self._view.update_picture(self.pictures[self.index])
        
    def mouseMoveEvent(self, event):
        print('Mouse coords: {} : {}'.format(event.x(), event.y()))

    def run(self):
        self._view.show()
        return self._app.exec_()

    # load photos from photos directory
    def load(self):

        for file in os.listdir(settings.PHOTO_DIR):
            p = Picture(os.path.join(settings.PHOTO_DIR, file))
            self.pictures.append(p)
        
