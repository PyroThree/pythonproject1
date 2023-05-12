# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_shop = QtWidgets.QPushButton(self.centralwidget)
        self.button_shop.setGeometry(QtCore.QRect(100, 130, 180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_shop.setFont(font)
        self.button_shop.setObjectName("button_shop")
        self.label_restaurant = QtWidgets.QLabel(self.centralwidget)
        self.label_restaurant.setGeometry(QtCore.QRect(30, 30, 320, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_restaurant.setFont(font)
        self.label_restaurant.setAlignment(QtCore.Qt.AlignCenter)
        self.label_restaurant.setObjectName("label_restaurant")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(100, 270, 180, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.button_add_ramen = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_ramen.setGeometry(QtCore.QRect(260, 300, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_ramen.setFont(font)
        self.button_add_ramen.setObjectName("button_add_ramen")
        self.button_add_takoyaki = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_takoyaki.setGeometry(QtCore.QRect(260, 120, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_takoyaki.setFont(font)
        self.button_add_takoyaki.setObjectName("button_add_takoyaki")
        self.button_add_ramune = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_ramune.setGeometry(QtCore.QRect(260, 210, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_add_ramune.setFont(font)
        self.button_add_ramune.setObjectName("button_add_ramune")
        self.label_takoyaki = QtWidgets.QLabel(self.centralwidget)
        self.label_takoyaki.setGeometry(QtCore.QRect(10, 125, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_takoyaki.setFont(font)
        self.label_takoyaki.setObjectName("label_takoyaki")
        self.label_ramune = QtWidgets.QLabel(self.centralwidget)
        self.label_ramune.setGeometry(QtCore.QRect(10, 215, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ramune.setFont(font)
        self.label_ramune.setObjectName("label_ramune")
        self.label_ramen = QtWidgets.QLabel(self.centralwidget)
        self.label_ramen.setGeometry(QtCore.QRect(10, 305, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ramen.setFont(font)
        self.label_ramen.setObjectName("label_ramen")
        self.label_total = QtWidgets.QLabel(self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(210, 405, 111, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(40, 370, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.input_takoyaki = QtWidgets.QLineEdit(self.centralwidget)
        self.input_takoyaki.setGeometry(QtCore.QRect(150, 135, 100, 20))
        self.input_takoyaki.setObjectName("input_takoyaki")
        self.input_ramune = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ramune.setGeometry(QtCore.QRect(150, 225, 100, 20))
        self.input_ramune.setObjectName("input_ramune")
        self.input_ramen = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ramen.setGeometry(QtCore.QRect(150, 315, 100, 20))
        self.input_ramen.setObjectName("input_ramen")
        self.button_clear_takoyaki = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_takoyaki.setGeometry(QtCore.QRect(370, 135, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_clear_takoyaki.setFont(font)
        self.button_clear_takoyaki.setObjectName("button_clear_takoyaki")
        self.button_clear_ramune = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_ramune.setGeometry(QtCore.QRect(370, 225, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_clear_ramune.setFont(font)
        self.button_clear_ramune.setObjectName("button_clear_ramune")
        self.button_clear_ramen = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear_ramen.setGeometry(QtCore.QRect(370, 315, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_clear_ramen.setFont(font)
        self.button_clear_ramen.setObjectName("button_clear_ramen")
        self.button_main = QtWidgets.QPushButton(self.centralwidget)
        self.button_main.setGeometry(QtCore.QRect(40, 420, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_main.setFont(font)
        self.button_main.setObjectName("button_main")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(330, 405, 47, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setText("")
        self.label_price.setObjectName("label_price")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gui"))
        self.button_shop.setText(_translate("MainWindow", "Shop"))
        self.label_restaurant.setText(_translate("MainWindow", "Benjis Snack Shack"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.button_add_ramen.setText(_translate("MainWindow", "Add"))
        self.button_add_takoyaki.setText(_translate("MainWindow", "Add"))
        self.button_add_ramune.setText(_translate("MainWindow", "Add"))
        self.label_takoyaki.setText(_translate("MainWindow", "Takoyaki - $7.00"))
        self.label_ramune.setText(_translate("MainWindow", "Ramune - $2.50"))
        self.label_ramen.setText(_translate("MainWindow", "Ramen - $11.50"))
        self.label_total.setText(_translate("MainWindow", "Grand Total = "))
        self.button_clear.setText(_translate("MainWindow", "Clear Cart"))
        self.button_clear_takoyaki.setText(_translate("MainWindow", "X"))
        self.button_clear_ramune.setText(_translate("MainWindow", "X"))
        self.button_clear_ramen.setText(_translate("MainWindow", "X"))
        self.button_main.setText(_translate("MainWindow", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
