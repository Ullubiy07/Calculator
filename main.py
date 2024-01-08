from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy, QApplication, QMenu, QSystemTrayIcon, QAction
from PyQt5.QtGui import QIcon


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 601)

        MainWindow.setFixedSize(386, 601)

        MainWindow.setStyleSheet("background-color: rgb(26, 32, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(10, 100, 371, 81))
        font = QtGui.QFont()
        font.setFamily("HONOR Sans Display GBK")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(26, 32, 52);")
        self.label_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.label_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(286, 525, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n")
        self.button_equal.setObjectName("button_equal")
        self.button_equal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button_comma = QtWidgets.QPushButton(self.centralwidget)
        self.button_comma.setGeometry(QtCore.QRect(194, 525, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_comma.setFont(font)
        self.button_comma.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_comma.setObjectName("button_comma")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(102, 525, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_0.setObjectName("button_0")
        self.button_plus_and_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus_and_minus.setGeometry(QtCore.QRect(10, 525, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_plus_and_minus.setFont(font)
        self.button_plus_and_minus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_plus_and_minus.setObjectName("button_plus_and_minus")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(10, 457, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_1.setObjectName("button_1")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(10, 389, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_4.setObjectName("button_4")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(10, 321, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_7.setObjectName("button_7")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(102, 457, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(194, 457, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_3.setObjectName("button_3")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(286, 457, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_plus.setFont(font)
        self.button_plus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_plus.setObjectName("button_plus")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(102, 389, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(194, 389, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_6.setObjectName("button_6")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(286, 389, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_minus.setFont(font)
        self.button_minus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_minus.setObjectName("button_minus")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(102, 321, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(194, 321, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 16)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 206, 206);\n")
        self.button_9.setObjectName("button_9")
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.button_multiply.setGeometry(QtCore.QRect(286, 321, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_multiply.setFont(font)
        self.button_multiply.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_multiply.setObjectName("button_multiply")
        self.button_ = QtWidgets.QPushButton(self.centralwidget)
        self.button_.setGeometry(QtCore.QRect(286, 253, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_.setFont(font)
        self.button_.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_.setObjectName("button_")
        self.button_c = QtWidgets.QPushButton(self.centralwidget)
        self.button_c.setGeometry(QtCore.QRect(194, 253, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_c.setFont(font)
        self.button_c.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_c.setObjectName("button_c")
        self.button_ce = QtWidgets.QPushButton(self.centralwidget)
        self.button_ce.setGeometry(QtCore.QRect(102, 253, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_ce.setFont(font)
        self.button_ce.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_ce.setObjectName("button_ce")
        self.button_ostatok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ostatok.setGeometry(QtCore.QRect(10, 253, 90, 65))
        font = QtGui.QFont("MS Shell DIq 2", 10)
        font.setBold(True)
        font.setWeight(75)
        self.button_ostatok.setFont(font)
        self.button_ostatok.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 255);\n")
        self.button_ostatok.setObjectName("button_ostatok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()
        layout = QGridLayout()
        self.setLayout(layout)
        # layout.addWidget
        MainWindow.setWindowIcon(QIcon("calc_logo_1.png"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.label_result.move(0, 100)
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_comma.setText(_translate("MainWindow", "."))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_plus_and_minus.setText(_translate("MainWindow", "+/-"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_multiply.setText(_translate("MainWindow", "×"))
        self.button_.setText(_translate("MainWindow", "÷"))
        self.button_c.setText(_translate("MainWindow", "C"))
        self.button_ce.setText(_translate("MainWindow", "⌫"))
        self.button_ostatok.setText(_translate("MainWindow", "%"))

    def add_function(self):
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_minus.clicked.connect(lambda: self.write_number(self.button_minus.text()))
        self.button_plus.clicked.connect(lambda: self.write_number(self.button_plus.text()))
        self.button_plus_and_minus.clicked.connect(self.change_sign)
        self.button_.clicked.connect(lambda: self.write_number(self.button_.text()))
        self.button_c.clicked.connect(self.button_delete)
        self.button_ce.clicked.connect(lambda: self.write_number(self.button_ce.text(), True))
        self.button_multiply.clicked.connect(lambda: self.write_number(self.button_multiply.text()))
        self.button_comma.clicked.connect(lambda: self.write_number(self.button_comma.text()))
        self.button_ostatok.clicked.connect(lambda: self.write_number(self.button_ostatok.text()))

        self.button_equal.clicked.connect(self.results)
        self.massive = list()
        self.count = 0



    def write_number(self, number, args=False):
        flag = False
        signs = '+-÷×%.'
        self.signs1 = '+-÷×%'
        if args:
            if len(self.label_result.text()) == 1:
                flag = True
                self.label_result.setText('0')
            else:
                self.label_result.setText(self.label_result.text()[:len(self.label_result.text()) - 1])
        if self.label_result.text() == "0" and not flag and number not in signs:
            self.label_result.setText(number)
        else:
            if not args:
                if number in signs and self.label_result.text()[len(self.label_result.text()) - 1] in signs:
                    self.label_result.setText(self.label_result.text()[:len(self.label_result.text()) - 1] + number)
                else:
                    k = self.label_result.text()
                    last_sign = k[-1]
                    if self.label_result.text()[len(k) - 1] not in self.signs1:
                        self.label_result.setText(self.label_result.text() + number)
                    else:
                        self.count += 1
                        if '×' in k:
                            k1 = k.replace('×', '*')
                            self.label_result.setText(k1)
                        if '÷' in k:
                            k1 = k.replace('÷', '/')
                            self.label_result.setText(k1)
                        self.massive.append(self.label_result.text())
                        self.label_result.setText(number)


    def button_delete(self):
        self.label_result.setText("0")
        self.massive = list()

    def change_sign(self):
        if self.label_result.text()[0] == '-':
            self.label_result.setText(self.label_result.text()[1:])
        else:
            self.label_result.setText('-' + self.label_result.text())


    def results(self):
        try:
            self.massive.append(self.label_result.text())
            res = eval(''.join(self.massive))
        except:
            res = "0"
        if len(str(res)) > 12:
            res = str(res)[0:12]
        if len(str(res)) == 3 and str(res).split('.')[-1] == '0':
            res = int(res)
        self.label_result.setText(str(res))
        self.massive = list()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
