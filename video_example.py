import sys

from PySide2.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QApplication
)


class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton('Open')
        saveButton = QPushButton('Save')
        dirButton = QPushButton('Other')
        closeButton = QPushButton('Close...')

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):
        dir = '.'
        fileObj = QFileDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()
