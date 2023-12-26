import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # Set up your GUI components here
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_click)
        self.button.move(100, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('My PyQt5 App')


    def on_click(self):
        print('Button clicked!')


# Create the application object
app = QApplication(sys.argv)

# Create and show the main window
mainWindow = MainWindow()
mainWindow.show()

# Start the application's event loop
sys.exit(app.exec_())