# напиши здесь код третьего экрана приложенияfrom PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel)

from instr.py import *  #загружаем переменные из файла instr.py

class FinalWin(QWidget):
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
        self.layout = QVBoxLayout()
        self.index_text = QLabel(txt_index)
        self.workheart_text = QLabel(txt_workheart)
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.workheart_text)
        self.setLayout(self.layout)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
app = QApplication([])
mw = MainWin()
app.exec()
