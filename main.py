import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from main_gui import CustomerApp


def main():

        app = QApplication(sys.argv)
        window = CustomerApp()
        window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()
