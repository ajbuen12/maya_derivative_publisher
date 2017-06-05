# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\aldous\Desktop\scripting-exercise\publish_alembic\ui\dialogbox.ui'
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
        Form.resize(291, 364)
        Form.setMinimumSize(QtCore.QSize(284, 364))
        Form.setMaximumSize(QtCore.QSize(16777215, 11111111))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lw_dialog_layer = QtGui.QListWidget(Form)
        self.lw_dialog_layer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lw_dialog_layer.setModelColumn(0)
        self.lw_dialog_layer.setObjectName(_fromUtf8("lw_dialog_layer"))
        self.verticalLayout.addWidget(self.lw_dialog_layer)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cb_fbx = QtGui.QCheckBox(Form)
        self.cb_fbx.setObjectName(_fromUtf8("cb_fbx"))
        self.horizontalLayout.addWidget(self.cb_fbx)
        self.cb_obj = QtGui.QCheckBox(Form)
        self.cb_obj.setObjectName(_fromUtf8("cb_obj"))
        self.horizontalLayout.addWidget(self.cb_obj)
        self.cb_alembic = QtGui.QCheckBox(Form)
        self.cb_alembic.setObjectName(_fromUtf8("cb_alembic"))
        self.horizontalLayout.addWidget(self.cb_alembic)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_add = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setMaximumSize(QtCore.QSize(87, 50))
        self.button_add.setSizeIncrement(QtCore.QSize(0, 0))
        self.button_add.setObjectName(_fromUtf8("button_add"))
        self.horizontalLayout_2.addWidget(self.button_add)
        self.button_done = QtGui.QPushButton(Form)
        self.button_done.setObjectName(_fromUtf8("button_done"))
        self.horizontalLayout_2.addWidget(self.button_done)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.lw_dialog_layer.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lw_dialog_layer.setSortingEnabled(False)
        self.label.setText(_translate("Form", "Format", None))
        self.cb_fbx.setText(_translate("Form", "fbx", None))
        self.cb_obj.setText(_translate("Form", "obj", None))
        self.cb_alembic.setText(_translate("Form", "alembic", None))
        self.button_add.setText(_translate("Form", "Add", None))
        self.button_done.setText(_translate("Form", "Done", None))

