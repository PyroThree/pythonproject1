from calculator import *


def main():
    application = QApplication([])
    window = Calculator()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()