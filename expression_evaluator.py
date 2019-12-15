import sys

from PySide2.QtWidgets import (
    QDialog,
    QApplication,
    QTextBrowser,
    QLineEdit,
    QVBoxLayout)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.resultsList = QTextBrowser()
        self.resultsInput = QLineEdit('Enter an expression and press return key')

        layout = QVBoxLayout()
        layout.addWidget(self.resultsList)
        layout.addWidget(self.resultsInput)
        self.setLayout(layout)

        self.resultsInput.selectAll()
        self.resultsInput.setFocus()

        self.resultsInput.returnPressed.connect(self.compute)

    def compute(self):
        try:
            text = self.resultsInput.text()
            self.resultsList.append(f"{text} = <b>{eval(text)}</b>")
        except:
            self.resultsList.append("<font color=red><b>Expression Invalid</b></font>")



app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
