
#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QButtonGroup, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel
from random import shuffle
app = QApplication([])
main_win = QWidget()
main_win.resize(600, 400)

class Question():
    def __init__(self, question_label, right_answer, wrong1, wrong2, wrong3):
        self.question_label = question_label
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)




    
def show_question():
    RadioGroupBox.show()
    question_label.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    winner1.setChecked(False)
    winner2.setChecked(False)
    winner3.setChecked(False)
    winner4.setChecked(False)
    RadioGroup.setExclusive(True)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def start_test():
    # question_label.setText('')
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'Следующий вопрос':
        next_question()
        


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')


def show_correct(rez):
    right.setText(rez)
    show_result()
    button.setText('Следующий вопрос')
    # RadioGroupBox.hide()
    # AnsGroupBox.show()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question_label)
    correct_answer.setText(q.right_answer)
    show_question()

main_win.setWindowTitle('Memory Card')
question_label = QLabel('Начинаем Тест')
RadioGroupBox = QGroupBox('Варианты ответов')
winner1 = QRadioButton()
winner2 = QRadioButton()
winner3 = QRadioButton()
winner4 = QRadioButton()
button = QPushButton('Погнали!')
answers = [winner1, winner2, winner3, winner4]
question_list = []
q1 = Question('Государственный язык Португалии?', 'Португальский', 'Английский', 'Испанский', 'Русский')
question_list.append(q1)
q2 = Question('Сколько цветов в флаге СССР?', '2', '3', '1', '9')
question_list.append(q2)
q3 = Question('Кто такой Путин?', 'Президент мира', 'Президент', 'Лучший человек на планете', 'Бог')
question_list.append(q3)
RadioGroup = QButtonGroup()
RadioGroup.addButton(winner1)
RadioGroup.addButton(winner2)
RadioGroup.addButton(winner3)
RadioGroup.addButton(winner4)
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutH4 = QHBoxLayout()

main_win.cur_question = -1
layoutH1.addWidget(question_label, alignment = Qt.AlignCenter)
layoutV2.addWidget(winner1, alignment = Qt.AlignCenter)
layoutV2.addWidget(winner2, alignment = Qt.AlignCenter)
layoutV3.addWidget(winner3, alignment = Qt.AlignCenter)
layoutV3.addWidget(winner4, alignment = Qt.AlignCenter)
layoutH4.addWidget(button, alignment = Qt.AlignCenter)
layoutH2.addLayout(layoutV2)
layoutH2.addLayout(layoutV3)
RadioGroupBox.setLayout(layoutH2)

# AnsGroupBox1 = QGroupBox('Начинаем Тест')
# right1 = QLabel('Правильно/Неправильно')
#обработка нажатий на переключатели
AnsGroupBox = QGroupBox('Результат теста')
right = QLabel('Правильно/Неправильно')
correct_answer = QLabel('Правильный ответ')
layoutH2 = QVBoxLayout()
layoutH2.addWidget(right)
layoutH2.addWidget(correct_answer, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(layoutH2)

main_layout = QVBoxLayout()


main_layout.addWidget(question_label, alignment = Qt.AlignCenter)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
main_layout.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)
main_layout.addWidget(button, alignment = Qt.AlignCenter)


button.clicked.connect(start_test)
AnsGroupBox.hide()
next_question()
main_win.setLayout(main_layout) 
#отображение окна приложения 
main_win.show()
app.exec_()