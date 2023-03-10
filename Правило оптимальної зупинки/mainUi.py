# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 9, 1171, 586))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.MplWidget = MplWidget(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout_5.addWidget(self.MplWidget)
        spacerItem1 = QtWidgets.QSpacerItem(818, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelDelta0_value = QtWidgets.QLabel(self.layoutWidget2)
        self.labelDelta0_value.setText("")
        self.labelDelta0_value.setObjectName("labelDelta0_value")
        self.verticalLayout_3.addWidget(self.labelDelta0_value)
        self.labelDelta1_value = QtWidgets.QLabel(self.layoutWidget2)
        # self.labelDelta1_value.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.labelDelta1_value.setObjectName("labelDelta1_value")
        self.verticalLayout_3.addWidget(self.labelDelta1_value)
        self.labelDelta2_value = QtWidgets.QLabel(self.layoutWidget2)
        self.labelDelta2_value.setText("")
        self.labelDelta2_value.setObjectName("labelDelta2_value")
        self.verticalLayout_3.addWidget(self.labelDelta2_value)
        self.labelDelta3_value = QtWidgets.QLabel(self.layoutWidget2)
        self.labelDelta3_value.setText("")
        self.labelDelta3_value.setObjectName("labelDelta3_value")
        self.verticalLayout_3.addWidget(self.labelDelta3_value)
        self.labelDelta4_value = QtWidgets.QLabel(self.layoutWidget2)
        self.labelDelta4_value.setText("")
        self.labelDelta4_value.setObjectName("labelDelta4_value")
        self.verticalLayout_3.addWidget(self.labelDelta4_value)
        self.labelDelta5_value = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDelta5_value.sizePolicy().hasHeightForWidth())
        self.labelDelta5_value.setSizePolicy(sizePolicy)
        self.labelDelta5_value.setText("")
        self.labelDelta5_value.setObjectName("labelDelta5_value")
        self.verticalLayout_3.addWidget(self.labelDelta5_value)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_2.setStyleSheet("background-color: rgb(255, 153, 0);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_3.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);")
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_5.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy)
        self.checkBox_6.setStyleSheet("\n"
"background-color: rgb(255, 153, 255);")
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_start = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_start.setObjectName("lineEdit_start")
        self.horizontalLayout_5.addWidget(self.lineEdit_start)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_end = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_end.setObjectName("lineEdit_end")
        self.horizontalLayout_5.addWidget(self.lineEdit_end)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.label_error = QtWidgets.QLabel(self.layoutWidget2)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.verticalLayout_4.addWidget(self.label_error)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalScrollBar_value_N = QtWidgets.QScrollBar(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_value_N.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_value_N.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_value_N.setMinimum(100)
        self.horizontalScrollBar_value_N.setMaximum(1000)
        self.horizontalScrollBar_value_N.setSingleStep(100)
        self.horizontalScrollBar_value_N.setPageStep(100)
        self.horizontalScrollBar_value_N.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_value_N.setObjectName("horizontalScrollBar_value_N")
        self.verticalLayout_4.addWidget(self.horizontalScrollBar_value_N)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_N_value = QtWidgets.QLabel(self.layoutWidget2)
        self.label_N_value.setText("")
        self.label_N_value.setObjectName("label_N_value")
        self.horizontalLayout_3.addWidget(self.label_N_value)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalScrollBar_value_M = QtWidgets.QScrollBar(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_value_M.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_value_M.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_value_M.setMinimum(100)
        self.horizontalScrollBar_value_M.setMaximum(1000)
        self.horizontalScrollBar_value_M.setSingleStep(100)
        self.horizontalScrollBar_value_M.setPageStep(100)
        self.horizontalScrollBar_value_M.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_value_M.setObjectName("horizontalScrollBar_value_M")
        self.verticalLayout_4.addWidget(self.horizontalScrollBar_value_M)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_M_value = QtWidgets.QLabel(self.layoutWidget2)
        self.label_M_value.setText("")
        self.label_M_value.setObjectName("label_M_value")
        self.horizontalLayout_4.addWidget(self.label_M_value)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.labelTimer = QtWidgets.QLabel(self.layoutWidget2)
        self.labelTimer.setText("")
        self.labelTimer.setObjectName("labelTimer")
        self.verticalLayout_4.addWidget(self.labelTimer)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.pushButtonGenerate = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.verticalLayout_4.addWidget(self.pushButtonGenerate)
        self.radioButton_P_by_t = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_P_by_t.setObjectName("radioButton_P_by_t")
        self.verticalLayout_4.addWidget(self.radioButton_P_by_t)
        self.radioButton_P_by_delta = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_P_by_delta.setObjectName("radioButton_P_by_delta")
        self.verticalLayout_4.addWidget(self.radioButton_P_by_delta)
        self.radioButton_t_by_delta = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_t_by_delta.setObjectName("radioButton_t_by_delta")
        self.verticalLayout_4.addWidget(self.radioButton_t_by_delta)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.verticalLayout_6.addWidget(self.splitter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelDelta1_value.setText(_translate("Form", "             "))
        self.checkBox_1.setText(_translate("Form", "Delta 0"))
        self.checkBox_2.setText(_translate("Form", "Delta 1"))
        self.checkBox_3.setText(_translate("Form", "Delta 2"))
        self.checkBox_4.setText(_translate("Form", "Delta 3"))
        self.checkBox_5.setText(_translate("Form", "Delta 4"))
        self.checkBox_6.setText(_translate("Form", "Delta 5"))
        self.label_2.setText(_translate("Form", "Start:"))
        self.lineEdit_start.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "End:"))
        self.lineEdit_end.setText(_translate("Form", "1000"))
        self.label.setText(_translate("Form", "N:"))
        self.label_3.setText(_translate("Form", "M:"))
        self.pushButtonGenerate.setText(_translate("Form", "GENERATE"))
        self.radioButton_P_by_t.setText(_translate("Form", "P(t) | t"))
        self.radioButton_P_by_delta.setText(_translate("Form", "P(t) | delta"))
        self.radioButton_t_by_delta.setText(_translate("Form", "t* | delta"))
from mplwidget import MplWidget
