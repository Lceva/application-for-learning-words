# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setStyleSheet("font: 25 14pt \"Verdana Pro Light\";\n"
                                 "background-color: rgb(47, 79, 79);\n"
                                 "color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.verticalLayout.addWidget(self.label)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setStyleSheet("background-color: rgb(34, 57, 57);")
        self.back_btn.setObjectName("back")
        self.verticalLayout.addWidget(self.back_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html>"
                                                    "<body>"
                                                    "<h1 align=\"center\">О ПРОГРАММЕ</h1>"
                                                    "<p>Программа предназначена для изучения иностранных слов.</p>"
                                                    "<p>Для начала необходимо выбрать словарь для изучения <br>"
                                                    "(Словарь -> Отметить галочкой желаемую коллекцию слов).</p>"
                                                    "<p>Далее В режиме тренировки вы увидите на экране слово английском языке.</p>"
                                                    "<p> Введите предположительный перевод данного слова в специальные поля для ввода.</p>"
                                                    "<p>В конце Вы увидите результат.</p>"
                                                    "<p>Также можно добавлять и удалять собственные слова для изучения в режиме словаря.</p>"
                                                    "<p>В режиме статискики можно посмотреть результаты всех пройденных тренировок.</p>"
                                                    "</body>"
                                                    "</html>"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
