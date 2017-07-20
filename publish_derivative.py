from PyQt4 import QtGui
from dialogbox import Ui_Form as Dialogbox_UI
from mainwindow import Ui_Form as Mainwindow_UI
from createset_dialog import Ui_Dialog as Createset_UI

import sys
import maya.mel as mel
import maya.cmds as cmds
import export_alembic as abc


class CreateSet(QtGui.QDialog, Createset_UI):


    def __init__(self, parent):
        super(CreateSet, self).__init__(parent)
        self.setupUi(self)
        self.button_setdialog_createset.clicked.connect(self.create_set)
        self.button_setdialog_cancel.clicked.connect(self.close)

    def create_set(self):

        setList = self.parent().withDerivativeAttr

        # check if there is no selected objects.
        if cmds.ls(sl=True) == []:
            message = ("No selected objects. "
                        "Select objects to create set.")
            QtGui.QMessageBox.about(self, "No selected objects",
                                    message)
        # check if set name line edit is blank.
        elif not self.le_setdialog_setname.text():
            message = ("No set name entered. "
                       "Please fill in set name.")
            QtGui.QMessageBox.about(self, "No set name",
                                    message)
        # check if set name written already exists.

        elif self.le_setdialog_setname.text() in setList:
            message = ("Set name already exists. "
                        "Fill in new one.")
            QtGui.QMessageBox.about(self, "Set name exists",
                                    message)
        # check if set name has space.
        elif ' ' in self.le_setdialog_setname.text():
            message = ("Set name must not consists of space. "
                        "Rather change space to ( _ )")
            QtGui.QMessageBox.about(self, "Blank space in setname",
                                    message)
        else:

        # get set name from line edit
            setname = self.le_setdialog_setname.text()
        # create set using set name
            cmds.sets(n = setname)
        # add derivative export attribute for set distinction
            cmds.addAttr(setname, ln='Derivative',
                         dataType='stringArray')
            self.close()

class DialogBox(QtGui.QDialog, Dialogbox_UI):


    def __init__(self, parent):
        super(DialogBox, self).__init__(parent)
        self.setupUi(self)
        self.button_add.setEnabled(False)
        self.button_done.clicked.connect(self.close)
        self.button_add.clicked.connect(self.on_add)
        self.cb_fbx.clicked.connect(self.enable_add)
        self.cb_obj.clicked.connect(self.enable_add)
        self.cb_alembic.clicked.connect(self.enable_add)
        self.listSets()

    def listSets(self):
        setList = self.parent().withDerivativeAttr

        for setname in setList:
            item = QtGui.QListWidgetItem()
            item.setText(setname)
            self.lw_dialog_layer.addItem(item)

    def enable_add(self):
        if (self.cb_obj.isChecked() or
                self.cb_alembic.isChecked() or
                self.cb_fbx.isChecked()):
                self.button_add.setEnabled(True)
        else:
            self.button_add.setEnabled(False)

    def on_add(self):
        setname = self.lw_dialog_layer.currentItem().text()
        if self.cb_obj.isChecked():
            self.parent().add_derivative(setname, 'obj')
        if self.cb_fbx.isChecked():
            self.parent().add_derivative(setname, 'fbx')
        if self.cb_alembic.isChecked():
            self.parent().add_derivative(setname, 'abc')


class MainWindow(QtGui.QDialog, Mainwindow_UI):


    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.button_addlayer.clicked.connect(self.show_dialog_box)
        self.button_export.clicked.connect(self.export_derivative)
        self.button_deletelayer.clicked.connect(self.delete_item)
        self.button_cancel.clicked.connect(self.close)
        self.button_createset.clicked.connect(self.show_createset_dialog)
        self.withDerivativeAttr = []
        self.update_list()

    def update_list(self):
        for setname in cmds.ls(type='objectSet'):
            if 'Derivative' in cmds.listAttr(setname):
                if setname not in self.withDerivativeAttr:
                    self.withDerivativeAttr.append(setname)

    def show_dialog_box(self):

        self.update_list()

        # Dialog Box error appears if no set exists
        if self.withDerivativeAttr == []:
            QtGui.QMessageBox.about(self, "No sets",
                                    "No sets created. Create set first.")
        else:
            d = DialogBox(self)
            d.exec_()

    def show_createset_dialog(self):

        self.update_list()
        CreateSet(self).exec_()

    def add_derivative(self, setname, typeformat):
        # Check if there is existing identical

        root = self.lw_derivative.invisibleRootItem()
        list_count = root.childCount()
        for i in range(list_count):
            item = root.child(i)
            derivative = item.text(0)  # left column
            fileoutput = item.text(1)  # right column
            if derivative == setname and fileoutput == typeformat:
                return
        item = QtGui.QTreeWidgetItem([setname, typeformat])
        self.lw_derivative.addTopLevelItem(item)

    def export_derivative(self):
        # Temporary output_directory
        output_directory = "C:/Users/aldous/Desktop/test/"
        # create list/dictionary to be exported with eq. format
        export_dictionary = {}

        root = self.lw_derivative.invisibleRootItem()
        list_count = root.childCount()
        for i in range(list_count):
            item = root.child(i)
            derivative = item.text(0)  # left column
            fileoutput = item.text(1)  # right column
            if derivative in export_dictionary:
                export_dictionary[derivative].append(fileoutput)
            else:
                export_dictionary[derivative] = [fileoutput]

        for derivative in export_dictionary:

            if 'fbx' in export_dictionary[derivative]:
                cmds.select(derivative, replace=True)  # select set
                # check if plugin is loaded, if not: load fbx plugin
                if not cmds.pluginInfo('fbxmaya', q=True, l=True):
                    try:
                        cmds.loadPlugin('fbxmaya')
                    except:
                        raise MissingPluginError('Unable to load fbxmaya.mll')
                path = "%s%s%s" % (output_directory, derivative, ".fbx")
                # export command
                mel.eval('FBXExport -f "%s" -s' % (path))

            if 'obj' in export_dictionary[derivative]:
                cmds.select(derivative, replace=True)  # select set
                path = "%s%s%s" % (output_directory, derivative, ".obj")
                # check if plugin is loaded, if not: load obj plugin
                if not cmds.pluginInfo('objExport', q=True, l=True):
                    try:
                        cmds.loadPlugin('objExport')
                    except:
                        raise MissingPluginError('Unable to load objExport.mll')
                # export
                cmds.file(path, pr=1, typ="OBJexport", es=1,
                          op="groups=0; ptgroups=0; materials=0; smoothing=0; normals=0")

            if 'abc' in export_dictionary[derivative]:
                cmds.select(derivative, replace=True)  # select set
                # check if plugin is loaded, if not: load abc plugin
                if not cmds.pluginInfo('AbcExport', q=True, l=True):
                    try:
                        cmds.loadPlugin('AbcExport')
                    except:
                        raise MissingPluginError('Unable to load AbcExport.mll')
                path = output_directory
                # export command
                abc.add_attr_id(derivative, path)

    def delete_item(self):
        root = self.lw_derivative.invisibleRootItem()
        for item in self.lw_derivative.selectedItems():
            (item.parent() or root).removeChild(item)

if __name__ == "__main__":
    # app = QtGui.QApplication(sys.argv)
    w = MainWindow(None)
    w.show()
    # sys.exit(app.exec_())

    #print sys.path
