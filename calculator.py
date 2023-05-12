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

        self.button_shop.clicked.connect(lambda: self.shop())
        self.button_exit.clicked.connect(lambda: self.close())
        self.button_main.clicked.connect(lambda: self.menu())

    def shop(self):
        self.button_shop.setVisible(False)
        self.button_exit.setVisible(False)

        self.label_takoyaki.setVisible(True)
        self.label_ramune.setVisible(True)
        self.label_ramen.setVisible(True)
        self.input_takoyaki.setVisible(True)
        self.input_ramune.setVisible(True)
        self.input_ramen.setVisible(True)
        self.button_add_takoyaki.setVisible(True)
        self.button_add_ramune.setVisible(True)
        self.button_add_ramen.setVisible(True)
        self.button_clear.setVisible(True)
        self.button_main.setVisible(True)
        self.label_total.setVisible(True)
        self.button_clear_takoyaki.setVisible(True)
        self.button_clear_ramune.setVisible(True)
        self.button_clear_ramen.setVisible(True)

    def menu(self):
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

        self.button_shop.setVisible(True)
        self.button_exit.setVisible(True)

    def total(self):
        pass
