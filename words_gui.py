# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'words.ui'
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
                                 "color: rgb(255, 255, 255)\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.topic_name_show = QtWidgets.QLabel(self.centralwidget)
        self.topic_name_show.setObjectName("topic_name")
        self.horizontalLayout_2.addWidget(self.topic_name_show)
        self.checkBox_stady = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_stady.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox_stady)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.word_rus = QtWidgets.QLineEdit(self.centralwidget)
        self.word_rus.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.word_rus, 1, 1, 1, 1)
        self.eng = QtWidgets.QLabel(self.centralwidget)
        self.eng.setObjectName("eng")
        self.gridLayout.addWidget(self.eng, 0, 0, 1, 1)
        self.word_eng = QtWidgets.QLineEdit(self.centralwidget)
        self.word_eng.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.word_eng, 1, 0, 1, 1)
        self.add_word_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_word_btn.setStyleSheet("background-color: rgb(34, 57, 57);")
        self.add_word_btn.setObjectName("add_word")
        self.gridLayout.addWidget(self.add_word_btn, 1, 2, 1, 1)
        self.rus = QtWidgets.QLabel(self.centralwidget)
        self.rus.setObjectName("rus")
        self.gridLayout.addWidget(self.rus, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.word_list_show = QtWidgets.QListWidget(self.centralwidget)
        self.word_list_show.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.word_list_show.setObjectName("word_list")
        self.verticalLayout.addWidget(self.word_list_show)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setStyleSheet("background-color: rgb(34, 57, 57);")
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout.addWidget(self.back_btn)
        self.del_dictionary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_dictionary_btn.setStyleSheet("background-color: rgb(34, 57, 57);")
        self.del_dictionary_btn.setObjectName("del_dictionary")
        self.horizontalLayout.addWidget(self.del_dictionary_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topic_name_show.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Название словаря</span></p></body></html>"))
        self.checkBox_stady.setText(_translate("MainWindow", "Изучать"))
        self.eng.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Word</p></body></html>"))
        self.add_word_btn.setText(_translate("MainWindow", "Добавить"))
        self.rus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Перевод</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><span style=\" font-size:10pt;\">*Для удаления слова кликните по нему дважды.</span></html>"))
        self.back_btn.setText(_translate("MainWindow", "Назад"))
        self.del_dictionary_btn.setText(_translate("MainWindow", "Удалить словарь"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())