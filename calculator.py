from PyQt5.QtWidgets import *
from gui import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Calculator(QMainWindow, Ui_MainWindow):
    total = 0.00
    takoyaki = 0.00
    ramune = 0.00
    ramen = 0.00

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
        self.label_price.setVisible(False)

        self.button_shop.clicked.connect(lambda: self.shop())
        self.button_exit.clicked.connect(lambda: self.close())
        self.button_main.clicked.connect(lambda: self.menu())
        self.button_clear.clicked.connect(lambda:self.clear_cart())
        self.button_add_takoyaki.clicked.connect(lambda: self.add_takoyaki())
        self.button_add_ramune.clicked.connect(lambda: self.add_ramune())
        self.button_add_ramen.clicked.connect(lambda: self.add_ramen())
        self.button_clear_takoyaki.clicked.connect(lambda: self.clear_takoyaki())
        self.button_clear_ramune.clicked.connect(lambda: self.clear_ramune())
        self.button_clear_ramen.clicked.connect(lambda: self.clear_ramen())

    def shop(self):
        """
        Method that sets Shop buttons to be visible and usable
        """
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
        self.label_price.setVisible(True)

    def menu(self):
        """
        Method that hides all Shop buttons and makes Menu buttons visible and usable
        """
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
        self.label_price.setVisible(False)

        self.button_shop.setVisible(True)
        self.button_exit.setVisible(True)

    def add_takoyaki(self):
        """
        Method for pulling input for takoyaki and multiplying by cost and adding to total
        """
        try:
            takoyaki = float(self.input_takoyaki.text())
        except ValueError:
            self.input_takoyaki.clear()
            return
        if takoyaki <= 0:
            self.input_takoyaki.clear()
            return
        else:
            Calculator.total += takoyaki * 7.00
            self.label_price.setText(f'${Calculator.total:.2f}')
            self.input_takoyaki.clear()

    def add_ramune(self):
        """
        Method for pulling input for ramune and multiplying by cost and adding to total
        """
        try:
            ramune = float(self.input_ramune.text())
        except ValueError:
            self.input_ramune.clear()
            return
        if ramune <= 0:
            self.input_ramune.clear()
            return
        else:
            Calculator.total += ramune * 2.50
            self.label_price.setText(f'${Calculator.total:.2f}')
            self.input_ramune.clear()

    def add_ramen(self):
        """
        Method for pulling input for ramen and multiplying by cost and adding to total
        """
        try:
            ramen = float(self.input_ramen.text())
        except ValueError:
            self.input_ramen.clear()
            return
        if ramen <= 0:
            self.input_ramen.clear()
            return
        else:
            Calculator.total += ramen * 11.50
            self.label_price.setText(f'${Calculator.total:.2f}')
            self.input_ramen.clear()

    def clear_takoyaki(self):
        """
        Method to clear input for takoyaki
        """
        self.input_takoyaki.clear()

    def clear_ramune(self):
        """
        Method to clear input for ramune
        """
        self.input_ramune.clear()

    def clear_ramen(self):
        """
        Method to clear input for ramen
        """
        self.input_ramen.clear()

    def clear_cart(self):
        """
        Method to set total back to 0 and clear text of total from GUI
        """
        Calculator.total = 0.00
        self.label_price.setText('')

