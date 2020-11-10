from PyQt5.QtWidgets import (QWidget, QApplication, QDesktopWidget,
                             QLabel, QVBoxLayout, QSizePolicy, QPushButton, QGraphicsOpacityEffect)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import os, settings

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.picture_label = None
        self.next_button = None
        self.picture_pixmap = None

        self.init_main_window()

    # init the main window of FamilyFrame and set layout
    def init_main_window(self):

        vLayout = QVBoxLayout()

        self.picture_label = QLabel()
        self.picture_label.setAlignment(QtCore.Qt.AlignCenter)
        vLayout.addWidget(self.picture_label, QtCore.Qt.AlignCenter)

        self.next_button = QPushButton('Next ->')
        vLayout.addWidget(self.next_button, QtCore.Qt.AlignCenter)

        self.picture_pixmap = QPixmap()
        
        self.setLayout(vLayout)
        self.setGeometry(0, 0, settings.WIDTH, settings.HEIGHT)
        self.setWindowTitle('Family Frame')
        self.center()
        self.setStyleSheet('background-color: black;')
        self.show()

    # center window to center of screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # update the picture_label's pixmap to the new picture
    def update_picture(self, picture):
        self.fade_out_label()
        self.swap_picture_pixmap(picture)
        self.picture_label.setPixmap(self.picture_pixmap)
        self.fade_in_label()

    def swap_picture_pixmap(self, picture):
        pixmap = QPixmap(picture.path_to_file)
        fixed_pixmap = pixmap.scaled(settings.WIDTH, settings.HEIGHT, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        self.picture_pixmap.swap(fixed_pixmap)

    def fade_out_label(self):
        self.picture_label.effect = QGraphicsOpacityEffect()
        self.picture_label.setGraphicsEffect(self.picture_label.effect)

        self.picture_label.animation = QtCore.QPropertyAnimation(self.picture_label.effect, b"opacity")
        self.picture_label.animation.setDuration(500)
        self.picture_label.animation.setStartValue(1)
        self.picture_label.animation.setEndValue(0)
        self.picture_label.animation.start()

    def fade_in_label(self):
        self.picture_label.effect = QGraphicsOpacityEffect()
        self.picture_label.setGraphicsEffect(self.picture_label.effect)

        self.picture_label.animation = QtCore.QPropertyAnimation(self.picture_label.effect, b"opacity")
        self.picture_label.animation.setDuration(500)
        self.picture_label.animation.setStartValue(0)
        self.picture_label.animation.setEndValue(1)
        self.picture_label.animation.start()

    def set_picture(self, picture):
        self.swap_picture_pixmap(picture)
        self.picture_label.setPixmap(self.picture_pixmap)
        self.fade_in_label()

        
def main():
    
    import sys
    from main_window_controller import MainWindowController

    app = QApplication(sys.argv)
    main_window = MainWindowController(app)
    sys.exit(main_window.run())


if __name__== '__main__':
    main()

