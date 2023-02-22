from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from AudioFilesFilter.audioFilesFilter import getTotalAudioDuration


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 320, 150)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setWindowTitle('App')

        # Duration label
        self.duration_label = QtWidgets.QLabel('Total duration: ')
        self.duration_label.setFont(QFont('Helvetica', 12))

        # Files scanned label
        self.files_scanned_label = QtWidgets.QLabel('Files scanned successfully: ')
        self.files_scanned_label.setFont(QFont('Helvetica', 12))

        # Files faied to read label
        self.failed_to_read_label = QtWidgets.QLabel('Failed to read: ')
        self.failed_to_read_label.setFont(QFont('Helvetica', 12))

        # Creating path entry box
        self.path_entry = QtWidgets.QLineEdit()
        self.path_entry.setObjectName('name_entry')
        self.path_entry.setPlaceholderText('Path...')

        # Creating button
        self.button = QtWidgets.QPushButton('Scan')
        self.button.clicked.connect(self.showTotalDuration)

        self.layout().addWidget(self.duration_label)
        self.layout().addWidget(self.files_scanned_label)
        self.layout().addWidget(self.failed_to_read_label)
        self.layout().addWidget(self.path_entry)
        self.layout().addWidget(self.button)

    def showTotalDuration(self):
        data = getTotalAudioDuration(self.path_entry.text())

        self.duration_label.setText(f'Total duration: {data["duration"]}')
        self.files_scanned_label.setText(f'Files scanned successfully: '
                                        f'{data["filesRead"]}/{data["filesTotal"]}')
        self.failed_to_read_label.setText('Failed to read:\n' + '\n'.join(data['failedToRead']))
        self.path_entry.setText('')