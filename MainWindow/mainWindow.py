from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from audioFilesFilter import getTotalDurationFormatted

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 320, 150)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle('App')

        # Duration label
        greet_label = QtWidgets.QLabel('Total duration: ')
        greet_label.setFont(QFont('Helvetica', 14))

        # Creating name entry box
        name_entry = QtWidgets.QLineEdit()
        name_entry.setObjectName('name_entry')
        name_entry.setPlaceholderText('Path...')

        # Creating button
        button = QtWidgets.QPushButton('Scan', clicked = lambda: greet())

        self.layout().addWidget(greet_label)
        self.layout().addWidget(name_entry)
        self.layout().addWidget(button)

        def greet():
            greet_label.setText(f'Total duration: {getTotalDurationFormatted(name_entry.text())}')
            name_entry.setText('')