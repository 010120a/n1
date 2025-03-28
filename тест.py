from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('1.Государственный язык Португалии:', 'Португальский', 'Английский', 'Испанский', 'Французкий'))
questions_list.append(Question('2.В каком году была основана Москва?', '1147', '1242', '1861', '1943'))
questions_list.append(Question('3.Кто первый приплыл в Америку?', 'Лейф Эйриксон', 'Эрнан Кортес', 'Христофор Колумб', 'Фернан Магеллан'))
questions_list.append(Question('4.Кто завоевал Мексику?', 'Эрнан Кортес', 'Лейф Эйриксон', 'Христофор Колумб', 'Фернан Магеллан'))
questions_list.append(Question('5.Какого города нет:', 'Буэнос Диас', 'Мекихо', 'Мадрид', 'Буэнос Айрес'))
questions_list.append(Question('6.Столица США:', 'Вашингтон', 'Нью Йорк', 'Лас Вегас', 'Финикс'))
questions_list.append(Question('7.Государственный язык Бразилии:', 'Португальский', 'Бразильский', 'Испанский', 'Государственного языка нет'))
questions_list.append(Question('8.Столица Чили:', 'Сантьяго', 'Мекихо', 'Мадрид', 'Москва'))
questions_list.append(Question('9.Столица Турции:', 'Анкара', 'Стамбул', 'Манавгад', 'Сиде'))
questions_list.append(Question('10*.Государственный язык США:', 'Государственного языка нет', 'Английский', 'Французкий', 'Испанский'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('В каком году была основана Москва?') # текст вопроса

RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    if window.cur_question == len(questions_list)-1:
        btn_OK.setText('завершить')
    else:
        btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.right_answers += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            window.neright_answers += 1

def next_question():
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    q = questions_list[window.cur_question] # взяли вопрос
    ask(q)
    window.total += 1
    print('всего:', (window.total))
    print('правильных:', window.right_answers)
    print('рейтинг:', (window.right_answers / window.total) * 100)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    elif btn_OK.text() == 'завершить':
        app.quit()
    else:
        next_question()

window.total = 0
window.right_answers = 0
window.neright_answers = 0
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()
window.setLayout(layout_card)
window.show()
app.exec()