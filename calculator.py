from PyQt5.QtWidgets import *
from gui import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_takoyaki.setVisible(False)
        self.label_ramune.setVisible(False)
        self.label_ramen.setVisible(False)
        self.input_takoyaki.setVisible(False)
        self.input_ramune.setVisible(False)
        self.input_ramen.setVisible(False)
        self.button_add_takoyaki.setVisible(False)
        self.button_add_ramune.setVisible(False)
        self.button_add_ramen.setVisible(False)
        self.button_clear.setVisible(False)
        self.button_main.setVisible(False)
        self.label_total.setVisible(False)
        self.button_clear_takoyaki.setVisible(False)
        self.button_clear_ramune.setVisible(False)
        self.button_clear_ramen.setVisible(False)

        self.button_shop

    def add(self):
        pass

    def clear(self):
        pass

    def total(self):
        pass
