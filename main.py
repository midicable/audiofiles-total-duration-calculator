from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    app.exec_()