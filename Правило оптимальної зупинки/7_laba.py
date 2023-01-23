from random import randint
from PyQt5.QtWidgets import *

from scipy.signal import savgol_filter

import numpy as np
import mainUi


def findLeader(arr, t=-1):
    return max(arr[:t])


def createArr(start, end, N):
    return [randint(start, end) for i in range(N)]


def solution(arr, t, stop):
    for i in range(t + 1, len(arr)):
        if arr[i] > stop:
            return arr[i]
    return 0


class MatplotlibWidget(QMainWindow):
    def __init__(self):

        super(MatplotlibWidget, self).__init__()
        self.ui = mainUi.Ui_Form()
        self.ui.setupUi(self)
        # loadUiType("mainUi.py", self)

        self.show_info()
        self.ui.horizontalScrollBar_value_M.valueChanged.connect(self.show_info)
        self.ui.horizontalScrollBar_value_N.valueChanged.connect(self.show_info)
        self.ui.pushButtonGenerate.clicked.connect(self.func_)
        self.ui.radioButton_P_by_t.toggled.connect(self.show_graph)
        self.ui.radioButton_P_by_delta.toggled.connect(self.show_graph)
        self.ui.radioButton_t_by_delta.toggled.connect(self.show_graph)
        self.ui.checkBox_1.toggled.connect(self.show_graph)
        self.ui.checkBox_2.toggled.connect(self.show_graph)
        self.ui.checkBox_3.toggled.connect(self.show_graph)
        self.ui.checkBox_4.toggled.connect(self.show_graph)
        self.ui.checkBox_5.toggled.connect(self.show_graph)
        self.ui.checkBox_6.toggled.connect(self.show_graph)

    def show_(self):
        self.ui.labelDelta0_value.setText(f'P(t): {max(data[0])} | t*: {np.argmax(data[0]) + 1}')
        self.ui.labelDelta1_value.setText(f'P(t): {max(data[1])} | t*: {np.argmax(data[1]) + 1}')
        self.ui.labelDelta2_value.setText(f'P(t): {max(data[2])} | t*: {np.argmax(data[2]) + 1}')
        self.ui.labelDelta3_value.setText(f'P(t): {max(data[3])} | t*: {np.argmax(data[3]) + 1}')
        self.ui.labelDelta4_value.setText(f'P(t): {max(data[4])} | t*: {np.argmax(data[4]) + 1}')
        self.ui.labelDelta5_value.setText(f'P(t): {max(data[5])} | t*: {np.argmax(data[5]) + 1}')

    def clear_(self):
        self.ui.labelDelta0_value.setText(f'')
        self.ui.labelDelta1_value.setText(f'')
        self.ui.labelDelta2_value.setText(f'')
        self.ui.labelDelta3_value.setText(f'')
        self.ui.labelDelta4_value.setText(f'')
        self.ui.labelDelta5_value.setText(f'')

    def func_(self):
        global data
        data = []
        self.clear_()
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.draw()
        try:
            start = self.ui.lineEdit_start.text()
            end = self.ui.lineEdit_end.text()
            start = int(start)
            end = int(end)
            self.ui.label_error.setText('')
        except ValueError:
            self.ui.label_error.setText('Start and End values must be integer')
            self.ui.labelTimer.setText('Error')
            return 0
        if start < end:
            self.ui.label_error.setText('')
        else:
            self.ui.label_error.setText('Start value must be less than End value')
            self.ui.labelTimer.setText('Error')
            return 0
        N = self.ui.horizontalScrollBar_value_N.value()
        M = self.ui.horizontalScrollBar_value_M.value()
        t = 1

        while t <= N - 1:

            win = [0, 0, 0, 0, 0, 0]
            for j in range(M):
                arr = createArr(start, end, N)
                absLeader = findLeader(arr)
                condLeader = findLeader(arr, t)
                sol = solution(arr, t, condLeader)
                if np.abs(sol - absLeader) <= 0:
                    win[0] += 1
                if np.abs(sol - absLeader) <= absLeader * 0.01:
                    win[1] += 1
                if np.abs(sol - absLeader) <= absLeader * 0.02:
                    win[2] += 1
                if np.abs(sol - absLeader) <= absLeader * 0.03:
                    win[3] += 1
                if np.abs(sol - absLeader) <= absLeader * 0.04:
                    win[4] += 1
                if np.abs(sol - absLeader) <= absLeader * 0.05:
                    win[5] += 1

            for i in range(6):
                data.append([0.0])
                data[i].append(win[i] / M)

            t += 1
            self.ui.progressBar.setValue(int(t * 100 / N))
            QApplication.processEvents()
        self.ui.labelTimer.setText('Data generated')
        self.ui.progressBar.setValue(100)
        self.show_()
        return data

    def show_graph(self):
        try:
            if self.ui.radioButton_P_by_t.isChecked():

                self.ui.MplWidget.canvas.axes.clear()
                if self.ui.checkBox_1.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[0], 33, 3), color='#FF0000')

                if self.ui.checkBox_2.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[1], 33, 3), color='#FF9900')

                if self.ui.checkBox_3.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[2], 33, 3), color='#FFFF00')

                if self.ui.checkBox_4.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[3], 33, 3), color='#00FF00')

                if self.ui.checkBox_5.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[4], 33, 3), color='#00FFFF')

                if self.ui.checkBox_6.isChecked():
                    self.ui.MplWidget.canvas.axes.plot(range(0, self.ui.horizontalScrollBar_value_N.value()),
                                                    savgol_filter(data[5], 33, 3), color='#FF99FF')

                self.ui.MplWidget.canvas.axes.set_ylim([0, 1])
                self.ui.MplWidget.canvas.axes.set_xlabel('t')
                self.ui.MplWidget.canvas.axes.set_ylabel('P(t)')
                if len(data) != 0:
                    self.ui.labelTimer.setText('Done!')
                else:
                    self.ui.label_error.setText('First you need to generate the data')
                    self.ui.labelTimer.setText('Error')
                self.ui.MplWidget.canvas.draw()

            if self.ui.radioButton_P_by_delta.isChecked():
                self.ui.MplWidget.canvas.axes.clear()
                deltas = [0, 1, 2, 3, 4, 5]
                pt = [max(data[0]), max(data[1]), max(data[2]), max(data[3]), max(data[4]), max(data[5])]
                self.ui.MplWidget.canvas.axes.plot(deltas, pt)
                self.ui.MplWidget.canvas.axes.set_xlabel('deltas')
                self.ui.MplWidget.canvas.axes.set_ylabel('P(t)')
                self.ui.MplWidget.canvas.axes.set_ylim([0, 1])
                self.ui.MplWidget.canvas.draw()
                self.ui.labelTimer.setText('Done!')

            if self.ui.radioButton_t_by_delta.isChecked():
                self.ui.MplWidget.canvas.axes.clear()
                deltas = [0, 1, 2, 3, 4, 5]
                t = [np.argmax(data[0]) + 1, np.argmax(data[1]) + 1, np.argmax(data[2]) + 1, np.argmax(data[3]) + 1,
                     np.argmax(data[4]) + 1, np.argmax(data[5]) + 1]
                self.ui.MplWidget.canvas.axes.plot(deltas, t)
                self.ui.MplWidget.canvas.axes.set_xlabel('deltas')
                self.ui.MplWidget.canvas.axes.set_ylabel('t*')
                self.ui.MplWidget.canvas.axes.set_ylim([0, self.ui.horizontalScrollBar_value_N.value()])
                self.ui.MplWidget.canvas.draw()
                self.ui.labelTimer.setText('Done!')
        except Exception:
            self.ui.label_error.setText('First you need to generate the data')
            self.ui.labelTimer.setText('Error')
            return 0

    def show_info(self):
        self.ui.label_N_value.setText(str(self.ui.horizontalScrollBar_value_N.value()))
        self.ui.label_M_value.setText(str(self.ui.horizontalScrollBar_value_M.value()))


app = QApplication([])

app.setStyle('Fusion')
window = MatplotlibWidget()

window.setWindowTitle('Shkepast Lab 7')
window.show()
app.exec_()
