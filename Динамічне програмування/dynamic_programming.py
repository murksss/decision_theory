from random import randint

from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import numpy as np
import mainui


def calc(matrix, test_matrix, row, col):
    return matrix[row][col] + max(test_matrix[row-1][col], test_matrix[row][col+1], test_matrix[row-1][col+1])


def choose_way(matrix, row, col):
    if row > 0:
        uno = matrix[row - 1][col]
    else:
        return 1
    if col < -1:
        dos = matrix[row][col + 1]
    else:
        return 0
    tres = matrix[row - 1][col + 1]
    return np.argmax([uno, dos, tres])


class MatplotlibWidget(QMainWindow):
    def __init__(self):
        super(MatplotlibWidget, self).__init__()
        self.way = None
        self.ui = mainui.Ui_Form()
        self.ui.setupUi(self)
        self.tmp = None
        self.tmp_test = None

        self.ui.pushButton_generate.clicked.connect(self.generate)
        self.ui.pushButton_show_way.clicked.connect(self.show_way)
        self.ui.pushButton_show_matrix.clicked.connect(self.show_matrix)
        self.ui.pushButton_show_calculated.clicked.connect(self.show_calculated)

        self.labels = [
            [self.ui.label_idx_0_0, self.ui.label_idx_0_1, self.ui.label_idx_0_2, self.ui.label_idx_0_3,
             self.ui.label_idx_0_4],
            [self.ui.label_idx_1_0, self.ui.label_idx_1_1, self.ui.label_idx_1_2, self.ui.label_idx_1_3,
             self.ui.label_idx_1_4],
            [self.ui.label_idx_2_0, self.ui.label_idx_2_1, self.ui.label_idx_2_2, self.ui.label_idx_2_3,
             self.ui.label_idx_2_4],
            [self.ui.label_idx_3_0, self.ui.label_idx_3_1, self.ui.label_idx_3_2, self.ui.label_idx_3_3,
             self.ui.label_idx_3_4],
            [self.ui.label_idx_4_0, self.ui.label_idx_4_1, self.ui.label_idx_4_2, self.ui.label_idx_4_3,
             self.ui.label_idx_4_4]]

    def show_matrix(self):
        try:
            for row in range(len(self.tmp)):
                for col in range(len(self.tmp)):
                    self.labels[row][col].setText(str(int(self.tmp[row][col])))
                    self.labels[row][col].setAlignment(Qt.AlignCenter)
        except:
            self.ui.label_route.setText('First you need to generate matrix')
            return 0

    def show_calculated(self):
        try:
            for row in range(len(self.tmp_test)):
                for col in range(len(self.tmp_test)):
                    self.labels[row][col].setText(str(int(self.tmp_test[row][col])))
                    self.labels[row][col].setAlignment(Qt.AlignCenter)
        except:
            self.ui.label_route.setText('First you need to generate matrix')
            return 0

    def clear_matrix(self):
        for row in range(len(self.labels)):
            for col in range(len(self.labels)):
                self.labels[row][col].setText(' ')
                self.labels[row][col].setAlignment(Qt.AlignCenter)
                self.labels[row][col].setStyleSheet('background-color: rgb(255, 255, 255);')

    def generate(self):
        self.clear_matrix()
        try:
            A = self.ui.lineEdit_from.text()
            B = self.ui.lineEdit_to.text()
            A = int(A)
            B = int(B)
            self.ui.label_route.setText('Generated!')
        except ValueError:
            self.ui.label_route.setText('Range must be int and not empty')
            return 0
        if A < B:
            self.ui.label_route.setText('Generated!')
        else:
            self.ui.label_route.setText('From value must be less than To')
            return 0
        self.tmp = np.zeros([5, 5])
        self.tmp_test = np.zeros([5, 5])

        for row in range(5):
            for col in range(5):
                self.tmp[row][col] = randint(A, B)

        len_ = len(self.tmp_test)
        self.tmp_test[0][-1] = self.tmp[0][-1]
        for row in range(1, len_):
            self.tmp_test[row][-1] = self.tmp[row][-1] + self.tmp_test[row - 1][-1]
        for col in range(1, len_):
            self.tmp_test[0][-1 - col] = self.tmp[0][-1 - col] + self.tmp_test[0][-col]
        for n in range(1, len_):
            for row in range(n, len_):
                self.tmp_test[row][-1 - n] = calc(self.tmp, self.tmp_test, row, -1 - n)
            for col in range(n, len_):
                self.tmp_test[n][-1 - col] = calc(self.tmp, self.tmp_test, n, -1 - col)
        self.show_matrix()

    def show_way(self):
        try:
            ways = ['↑', '→', '↗']
            self.way = ''
            row, col = 4, -5
            while row != 0 or col != -1:
                idx = choose_way(self.tmp_test, row, col)
                self.way += ways[idx] + ' '
                if idx == 0:
                    if row != 0:
                        row -= 1
                    else:
                        col += 1
                elif idx == 1:
                    if col != 0:
                        col += 1
                    else:
                        row -= 1
                elif idx == 2:
                    row -= 1
                    col += 1
                self.labels[row][col].setStyleSheet('background-color: rgb(255, 255, 0);')
            route = self.way.split(' ')[:-1]
            self.ui.label_route.setText(self.way)
            self.ui.label_idx_4_0.setStyleSheet('background-color: rgb(255, 255, 0);')
        except:
            self.ui.label_route.setText('First you need to generate matrix')
            return 0


app = QApplication([])

app.setStyle('Fusion')
window = MatplotlibWidget()

window.setWindowTitle('Shkepast Lab 6')
window.show()
app.exec_()
