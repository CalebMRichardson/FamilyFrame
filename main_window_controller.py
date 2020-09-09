from controller_base import ControllerBase
from main_window import MainWindow
from picture import Picture

class MainWindowController(ControllerBase):

    def __init__(self, app):
        super().__init__(app)

        self.init_controller()

    def init_controller(self):
        self._view = MainWindow()
        self._view.next_button.clicked.connect(self.next_button_pressed)
        self._view.update_picture(Picture('photo1.jpg'))

    def next_button_pressed(self):
       self._view.update_picture(Picture('photo2.jpg'))
        
    def run(self):
        self._view.show()
        return self._app.exec_()
