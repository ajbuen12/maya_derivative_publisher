# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aldous\Desktop\createset.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(282, 111)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_setdialog_setname = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_setdialog_setname.setObjectName(_fromUtf8("label_setdialog_setname"))
        self.horizontalLayout.addWidget(self.label_setdialog_setname)
        self.le_setdialog_setname = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.le_setdialog_setname.setObjectName(_fromUtf8("le_setdialog_setname"))
        self.horizontalLayout.addWidget(self.le_setdialog_setname)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.button_setdialog_createset = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_setdialog_createset.setObjectName(_fromUtf8("button_setdialog_createset"))
        self.horizontalLayout_2.addWidget(self.button_setdialog_createset)
        self.button_setdialog_cancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.button_setdialog_cancel.setObjectName(_fromUtf8("button_setdialog_cancel"))
        self.horizontalLayout_2.addWidget(self.button_setdialog_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create Set", None))
        self.label_setdialog_setname.setText(_translate("Dialog", "Set name", None))
        self.button_setdialog_createset.setText(_translate("Dialog", "Create", None))
        self.button_setdialog_cancel.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

