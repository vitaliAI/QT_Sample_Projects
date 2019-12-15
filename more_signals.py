import sys

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QSpinBox, QDialog, QDial, QVBoxLayout, QApplication


class ZeroSpinBox(QSpinBox):
    zeros = 0
    atZero = Signal(int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)

    def check_zero(self, value):
        if value == 0:
            self.zeros += 1
            self.atZero.emit(self.zeros)



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.print_value)

    def print_value(self, zeros):
        print(f"The SpinBox has been at zero {zeros} times")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
