from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import sys
import result_gui
import start_gui
import teach_gui
import dictionary_gui
import about_gui
import DataBase
import words_gui
from random import shuffle


class Start(QtWidgets.QMainWindow, start_gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # buttons
        self.teach_btn.clicked.connect(self.to_teach)
        self.dictionary_btn.clicked.connect(self.to_dictionary)
        self.about_btn.clicked.connect(self.to_about)
        self.exit_btn.clicked.connect(sys.exit)
        # window
        self.window_dictionary = Dictionary()
        self.window_about = About()

        self.show()

    def to_teach(self):
        self.words_study = DataBase.get_words_study()
        if not len(self.words_study):
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Добавте слова на изучения",
                                           QtWidgets.QMessageBox.Ok)

        else:
            self.window_teach = Teach(self.words_study)
            self.hide()
            self.window_teach.show()

    def to_dictionary(self):
        self.window_dictionary.show()
        self.hide()

    def to_about(self):
        self.window_about.show()
        self.hide()


class Teach(QtWidgets.QMainWindow, teach_gui.Ui_MainWindow):
    def __init__(self, words_study):
        super().__init__()
        self.setupUi(self)
        self.words_study = words_study
        shuffle(self.words_study)  # random
        self.start(self.words_study)
        # buttons
        self.finish_btn.clicked.connect(self.to_finish)
        self.next_btn.clicked.connect(self.to_next)

    def start(self, words_study):
        self.answer_list = []
        self.word_index = 0
        self.word_show.setText(words_study[self.word_index][0])
        self.progress.setText(str(self.word_index + 1) + "/" + str(len(words_study)))

    def to_next(self):
        self.answer = self.enter_answer.text()
        if self.answer.isalpha():
            self.answer_list.append(self.answer)
            self.enter_answer.clear()
            self.word_index += 1
            self.progress.setText(str(self.word_index + 1) + "/" + str(len(self.words_study)))
            # checking the end of list
            if self.word_index != len(self.words_study):
                self.word_show.setText(self.words_study[self.word_index][0])
            else:
                self.to_finish()
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введенное слово должно состоять только из букв.",
                                           QtWidgets.QMessageBox.Ok)

    def to_finish(self):
        if len(self.answer_list) != len(self.words_study):
            reply = QtWidgets.QMessageBox.question(self, 'Вернуться в главное меню',
                                                   "Вы уверенны? Текущий прогресс не сохраниться.",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.hide()
                window_start.show()
        else:
            self.hide()
            self.window_result = Result(self.answer_list, self.words_study)
            self.window_result.show()


class Result(QtWidgets.QMainWindow, result_gui.Ui_MainWindow):
    def __init__(self, answer_list, words_study):
        super().__init__()
        self.setupUi(self)
        self.words_study = words_study
        self.answer_list = list(map(str.lower, answer_list))
        self.result = [0, 0]
        self.errors_list = []
        self.back_btn.clicked.connect(self.to_start)
        self.score()
        self.plot()
        self.output_result()

    def score(self):
        for i, word in enumerate(self.words_study):
            if self.words_study[i][1] == self.answer_list[i]:
                self.result[0] += 1
            else:
                self.errors_list.append(
                    self.words_study[i][0] + " - " + self.words_study[i][1] + " (" + self.answer_list[i] + ");")
                self.result[1] += 1

    def plot(self):
        self.labels = ['Правильно', 'Ошибка']
        self.colors = ['green', 'red']
        plt.pie(self.result, colors=self.colors, autopct='%.1f%%')
        plt.legend(self.labels, loc="best")
        plt.savefig('result.png')
        plt.clf()

    def output_result(self):
        self.result_pixmap = QPixmap('result.png')
        self.result_img.setPixmap(self.result_pixmap)
        if len(self.errors_list):
            self.errors_list_txt = ''
            self.errors_list_txt += "Список ошибок [word- перевод (Ваш ответ)]: "
            for word in self.errors_list:
                self.errors_list_txt += word
            self.result_txt.setText(self.errors_list_txt)

    def to_start(self):
        self.hide()
        window_start.show()


class Dictionary(QtWidgets.QMainWindow, dictionary_gui.Ui_Dictionary):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.to_start)
        self.add_dictionary_btn.clicked.connect(self.add_dictionary)
        self.topic_list_show.itemDoubleClicked.connect(self.to_words)
        self.update()

    def update(self):
        self.topic_list_show.clear()
        self.topic = DataBase.get_topic()
        self.topic_list_show.addItems(self.topic)

    def to_words(self, item):
        self.hide()
        self.window_words = Words(item.text())
        self.window_words.show()

    def add_dictionary(self):
        if self.enter_topic.text().isalpha():
            DataBase.add_dictionary(self.enter_topic.text().capitalize())
            self.enter_topic.clear()
            self.update()
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Название должно состоять только из букв.",
                                           QtWidgets.QMessageBox.Ok)
            self.enter_topic.clear()

    def to_start(self):
        self.hide()
        window_start.show()


class Words(QtWidgets.QMainWindow, words_gui.Ui_MainWindow):
    def __init__(self, topic_name):
        super().__init__()
        self.setupUi(self)
        self.topic = topic_name
        self.topic_name_show.setText(self.topic)
        self.back_btn.clicked.connect(self.to_start)
        self.add_word_btn.clicked.connect(self.add_word)
        self.del_dictionary_btn.clicked.connect(self.del_dictionary)
        self.word_list_show.itemDoubleClicked.connect(self.del_word)
        self.updata()

    def updata(self):
        self.word_list_show.clear()
        self.topic_words = DataBase.get_words_topic(self.topic)
        self.word_list_show.addItems(self.topic_words)

    def to_start(self):
        if self.checkBox_stady.checkState():
            DataBase.study_status_true(self.topic)
        else:
            DataBase.study_status_false(self.topic)

        self.hide()
        window_start.to_dictionary()

    def add_word(self):
        if self.word_eng.text().isalpha() and self.word_rus.text().isalpha():
            DataBase.add_word(self.topic, self.word_eng.text().lower(), self.word_rus.text().lower())
            self.updata()
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка ", "Введенные слова должны состоять только из букв.",
                                           QtWidgets.QMessageBox.Ok)
        self.word_eng.clear()
        self.word_rus.clear()

    def del_word(self, item):
        question = "Вы уверенны, что хотите удалить слово " + item.text() + " ?"
        reply = QtWidgets.QMessageBox.question(self, 'Удалить слово',
                                               question,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            DataBase.del_word(item.text().split()[0].strip())
            self.updata()

    def del_dictionary(self, item):
        question = "Вы уверенны, что хотите удалить словарь ?"
        reply = QtWidgets.QMessageBox.question(self, 'Удалить словарь',
                                               question,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            DataBase.del_dictionary(self.topic)
            self.hide()
            window_start.to_dictionary()
            window_start.window_dictionary.update()


class About(QtWidgets.QMainWindow, about_gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.to_start)

    def to_start(self):
        self.hide()
        window_start.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_start = Start()
    sys.exit(app.exec_())
