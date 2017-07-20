# -*- coding: utf-8 -*-
import sys
# Form implementation generated from reading ui file 'C:\Users\aldous\Desktop\scripting-exercise\Maya Layer Manager\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(425, 349)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_createset = QtGui.QPushButton(Form)
        self.button_createset.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_createset.setObjectName(_fromUtf8("button_createset"))
        self.horizontalLayout.addWidget(self.button_createset)
        self.button_addlayer = QtGui.QPushButton(Form)
        self.button_addlayer.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_addlayer.setObjectName(_fromUtf8("button_addlayer"))
        self.horizontalLayout.addWidget(self.button_addlayer)
        self.button_deletelayer = QtGui.QPushButton(Form)
        self.button_deletelayer.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_deletelayer.setObjectName(_fromUtf8("button_deletelayer"))
        self.horizontalLayout.addWidget(self.button_deletelayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lw_derivative = QtGui.QTreeWidget(Form)
        self.lw_derivative.setObjectName(_fromUtf8("lw_derivative"))
        self.lw_derivative.setColumnCount(2)
        self.verticalLayout.addWidget(self.lw_derivative)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.button_export = QtGui.QPushButton(Form)
        self.button_export.setObjectName(_fromUtf8("button_export"))
        self.horizontalLayout_3.addWidget(self.button_export)
        self.button_cancel = QtGui.QPushButton(Form)
        self.button_cancel.setObjectName(_fromUtf8("button_cancel"))
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Export Derivative", None))
        self.button_createset.setText(_translate("Form", "Create Set", None))
        self.button_addlayer.setText(_translate("Form", "+", None))
        self.button_deletelayer.setText(_translate("Form", "-", None))
        self.button_export.setText(_translate("Form", "Export", None))
        self.button_cancel.setText(_translate("Form", "Cancel", None))
        self.lw_derivative.setColumnWidth(0, 195)
        self.lw_derivative.resizeColumnToContents(1)
        self.lw_derivative.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.lw_derivative.headerItem().setText(0, _translate("Form", "Derivative", None))
        self.lw_derivative.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.lw_derivative.headerItem().setText(1, _translate("Form", "File Output", None))

