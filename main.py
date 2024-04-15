import sys
from PyQt6 import QtWidgets,uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        uic.loadUi("svet.ui",self)
        self.btn1.clicked.connect(self.first_light)
        self.btn2.clicked.connect(self.second_light)
        self.btn3.clicked.connect(self.third_light)
        self.f = 0
        self.s = 0
        self.t = 0

    def first_light(self):
        if self.f == 1:
            self.btn1.setStyleSheet(
                """
                QPushButton#btn1 {
                    background-color: green;
                }
                """
            )
        if self.f == 2:
            self.btn1.setStyleSheet(
                """
                QPushButton#btn1 {
                    background-color: gray;
                }
                """
            )
        if self.f == 2:
            self.f = 0
        self.f += 1
    def second_light(self):
        if self.s == 1:
            self.btn2.setStyleSheet(
                """
                QPushButton#btn2 {
                    background-color: yellow;
                }
                """
            )
        if self.s == 2:
            self.btn2.setStyleSheet(
                """
                QPushButton#btn2 {
                    background-color: gray;
                }
                """
            )
        if self.s == 2:
            self.s = 0
        self.s += 1
    def third_light(self):
        if self.t == 1:
            self.btn3.setStyleSheet(
                """
                QPushButton#btn3 {
                    background-color: red;
                }
                """
            )
        if self.t == 2:
            self.btn3.setStyleSheet(
                """
                QPushButton#btn3 {
                    background-color: gray;
                }
                """
            )
        if self.t == 2:
            self.t = 0
        self.t += 1


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()