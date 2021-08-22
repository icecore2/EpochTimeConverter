import datetime
import logging
from PyQt5 import QtWidgets, uic

import sys


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('AppUi.ui', self)

        # logger_settings
        LOG_FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
        logging.basicConfig(format=LOG_FORMAT)
        logging.getLogger("MainLogger")

        # QPushButton
        self.convert_ms_button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.convert_ms_button.clicked.connect(self.convert_to_date)

        # QPushButton
        self.convert_date_button = self.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.convert_date_button.clicked.connect(self.convert_to_ms)

        # QTextEdit
        self.textEdit = self.findChild(QtWidgets.QTextEdit, "textEdit")

        # QTextEdit
        self.textEdit_2 = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")

        # QLabel
        self.labelResult = self.findChild(QtWidgets.QLabel, "labelResult")

        # QLabel
        self.labelResult_2 = self.findChild(QtWidgets.QLabel, "labelResult_2")

        # QDateTimeEdit
        self.dateTimeEdit = self.findChild(QtWidgets.QDateTimeEdit, "dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat('dd-MM-yyyy hh:mm:ss')
        self.dateTimeEdit.setDateTime(datetime.datetime.now())

        # QPushButton
        self.setNowTime = self.findChild(QtWidgets.QPushButton, "pushButton_now")
        self.setNowTime.clicked.connect(self.nowTime)

        self.show()

    def nowTime(self):
        self.dateTimeEdit.setDateTime(datetime.datetime.now())
        self.dateTimeEdit.update()

    def convert_to_date(self):
        text_plain = self.textEdit.toPlainText()
        # 1629187214377
        if self.textEdit.toPlainText() != '' and self.textEdit.toPlainText().isdigit():
            text_plain = int(text_plain)
            text = datetime.datetime.fromtimestamp(text_plain / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            self.textEdit_2.setText(str(text))
            self.textEdit_2.copy()
            print(text)
        else:
            print(f"{text_plain} is invalid as digit")

    def convert_to_ms(self):

        text = self.dateTimeEdit.dateTime()
        text = text.toMSecsSinceEpoch()
        self.textEdit_2.setText(str(text))
        self.textEdit_2.copy()

        print(str(text))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    app.exec_()
