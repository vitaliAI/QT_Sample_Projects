import requests
import pandas as pd
import sys
from PySide2.QtWidgets import (
    QDialog,
    QComboBox,
    QLabel,
    QDoubleSpinBox,
    QGridLayout,
    QApplication
)


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.get_data()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)

        self.fromComboBox = QComboBox()
        self.toComboBox = QComboBox()

        self.fromComboBox.addItems(rates)
        self.toComboBox.addItems(rates)

        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 1000)
        self.fromSpinBox.setValue(1.00)

        self.toLabel = QLabel('1.00')

        layout = QGridLayout()
        layout.addWidget(dateLabel, 0, 0)
        layout.addWidget(self.fromComboBox, 1, 0)
        layout.addWidget(self.toComboBox, 2, 0)
        layout.addWidget(self.fromSpinBox, 1, 1)
        layout.addWidget(self.toLabel, 2, 1)
        self.setLayout(layout)

        self.fromComboBox.currentIndexChanged.connect(self.update_ui)
        self.toComboBox.currentIndexChanged.connect(self.update_ui)
        self.fromSpinBox.valueChanged.connect(self.update_ui)

    def get_data(self):
        self.rates = {}

        df = pd.read_csv('fx.csv', index_col=0, parse_dates=True)
        date = df.index.max().date()

        self.rates.update(df.iloc[-1].to_dict())
        return f"Exchange rates date {date}"

    def update_ui(self):
        from_ = self.fromComboBox.currentText()
        to = self.toComboBox.currentText()

        results = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()

        self.toLabel.setText("%0.2f" % results)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
