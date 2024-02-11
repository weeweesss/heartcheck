# напиши здесь код from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QLineEdit, QApplication, QWidget, QVBoxLayout, QPushButton, QLabel)

from instr.py import *  #загружаем переменные из файла instr.py

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show()  # показываем окно
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

        self.name_text = QLabel(txt_name)
        self.l_line.addWidget(self.name_text)

        self.hintname_text = QLabel(txt_hintname)
        self.l_line.addWidget(self.hintname_text)

        self.age_text = QLabel(txt_age)
        self.l_line.addWidget(self.age_text)

        self.hintnage_text = QLabel(txt_hintage)
        self.l_line.addWidget(self.hintnage_text)

        self.test1_text = QLabel(txt_test1)
        self.l_line.addWidget(self.test1_text)

        self.hinttest1_text = QLabel(txt_hinttest1)
        self.l_line.addWidget(self.hinttest1_text)

        self.test2_text = QLabel(txt_test2)
        self.l_line.addWidget(self.test2_text)

        self.hinttest2_text = QLabel(txt_hinttest2)
        self.l_line.addWidget(self.hinttest2_text)

        self.test3_text = QLabel(txt_test3)
        self.l_line.addWidget(self.test3_text)

        self.hinttest3_text = QLabel(txt_hinttest3)
        self.l_line.addWidget(self.hinttest3_text)
        
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
app = QApplication([])
mw = MainWin()
app.exec()для второго экрана приложения
