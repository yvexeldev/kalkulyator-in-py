from pickletools import float8
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from calc import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_1.clicked.connect(self.btn_1_clicked)
        self.ui.btn_2.clicked.connect(self.btn_2_clicked)
        self.ui.btn_3.clicked.connect(self.btn_3_clicked)
        self.ui.btn_4.clicked.connect(self.btn_4_clicked)
        self.ui.btn_5.clicked.connect(self.btn_5_clicked)
        self.ui.btn_6.clicked.connect(self.btn_6_clicked)
        self.ui.btn_7.clicked.connect(self.btn_7_clicked)
        self.ui.btn_8.clicked.connect(self.btn_8_clicked)
        self.ui.btn_9.clicked.connect(self.btn_9_clicked)
        self.ui.btn_0.clicked.connect(self.btn_0_clicked)
        
        self.ui.btn_1x.clicked.connect(self.btn_1x_clicked)
        self.ui.btn_pow3.clicked.connect(self.btn_pow3_clicked)
        self.ui.btn_pow2.clicked.connect(self.btn_pow2_clicked)
        self.ui.btn_sqrt.clicked.connect(self.btn_sqrt_clicked)
        self.ui.btn_point.clicked.connect(self.btn_point_clicked)
        self.ui.btn_Mul.clicked.connect(self.btn_mult_clicked)
        self.ui.btn_bolish.clicked.connect(self.btn_bolish_clicked)
        self.ui.btn_Add.clicked.connect(self.btn_add_clicked)
        self.ui.btn_sub.clicked.connect(self.btn_sub_clicked)
        self.ui.btn_equal.clicked.connect(self.btn_equal_clicked)
        self.ui.btn_c.clicked.connect(self.btn_c_clicked)
        self.ui.btn_abc.clicked.connect(self.btn_abs_clicked)
        self.ui.btn_percent.clicked.connect(self.btn_percent_clicked)
        
    def btn_1_clicked(self):
        self.__add_num("1")
    def btn_2_clicked(self):
        self.__add_num("2")
    def btn_3_clicked(self):
        self.__add_num("3")
    def btn_4_clicked(self):
        self.__add_num("4")
    def btn_5_clicked(self):
        self.__add_num("5")
    def btn_6_clicked(self):
        self.__add_num("6")
    def btn_7_clicked(self):
        self.__add_num("7")
    def btn_8_clicked(self):
        self.__add_num("8")
    def btn_9_clicked(self):
        self.__add_num("9")
    def btn_0_clicked(self):
        self.__add_num("0")
    
    def btn_1x_clicked(self):
        self.ui.result.setText(str(1 / float(self.ui.result.text())))
    def btn_pow3_clicked(self):
        self.ui.result.setText(str(float(self.ui.result.text()) ** 3))
    def btn_pow2_clicked(self):
        self.ui.result.setText(str(float(self.ui.result.text()) ** 2))
        print(str(float(self.ui.result.text()) ** 2))
    def btn_sqrt_clicked(self):
        self.ui.result.setText(str(float(self.ui.result.text()) ** 0.5))
    def btn_point_clicked(self):
        if self.ui.result.text() == "0":
            self.ui.result.setText("0.")
        if "." not in self.ui.result.text():
            self.ui.result.setText(self.ui.result.text() + ".")
    def btn_abs_clicked(self):
        self.ui.result.setText(str(float(self.ui.result.text()) * -1))
    def btn_percent_clicked(self):
        self.ui.result.setText(str(float(self.ui.result.text()) / 100))
    def btn_add_clicked(self):
        self.__add_num("+")
    def btn_equal_clicked(self):
        self.ui.result.setText(str(eval(self.ui.result.text())))
    def btn_sub_clicked(self):
        self.__add_num("-")
    def btn_mult_clicked(self):
        self.__add_num("*")
    def btn_bolish_clicked(self):
        self.__add_num("/")
    def btn_c_clicked(self):
        self.ui.result.setText("0")


    def __add_num(self, num):
        if self.ui.result.text() == "0":
            self.ui.result.setText(num)
        else:
            self.ui.result.setText(self.ui.result.text() + num)

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()