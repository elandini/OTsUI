# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIs\OTsUI_configUI_dialog.ui'
#
# Created: Thu Dec 17 17:14:28 2015
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_configDial(object):
    def setupUi(self, configDial):
        configDial.setObjectName(_fromUtf8("configDial"))
        configDial.resize(400, 581)
        self.verticalLayout = QtGui.QVBoxLayout(configDial)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.CONN_Box = QtGui.QGroupBox(configDial)
        self.CONN_Box.setObjectName(_fromUtf8("CONN_Box"))
        self.formLayout_3 = QtGui.QFormLayout(self.CONN_Box)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.ipaddr_Label = QtGui.QLabel(self.CONN_Box)
        self.ipaddr_Label.setObjectName(_fromUtf8("ipaddr_Label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.ipaddr_Label)
        self.ipaddr_Line = QtGui.QLineEdit(self.CONN_Box)
        self.ipaddr_Line.setObjectName(_fromUtf8("ipaddr_Line"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.ipaddr_Line)
        self.subport_Label = QtGui.QLabel(self.CONN_Box)
        self.subport_Label.setObjectName(_fromUtf8("subport_Label"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.subport_Label)
        self.subport_Line = QtGui.QLineEdit(self.CONN_Box)
        self.subport_Line.setObjectName(_fromUtf8("subport_Line"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.subport_Line)
        self.pubport_Label = QtGui.QLabel(self.CONN_Box)
        self.pubport_Label.setObjectName(_fromUtf8("pubport_Label"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.pubport_Label)
        self.pubport_Line = QtGui.QLineEdit(self.CONN_Box)
        self.pubport_Line.setObjectName(_fromUtf8("pubport_Line"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.pubport_Line)
        self.verticalLayout.addWidget(self.CONN_Box)
        self.AXIS_Box = QtGui.QGroupBox(configDial)
        self.AXIS_Box.setObjectName(_fromUtf8("AXIS_Box"))
        self.formLayout_2 = QtGui.QFormLayout(self.AXIS_Box)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.axisCmbBox = QtGui.QComboBox(self.AXIS_Box)
        self.axisCmbBox.setObjectName(_fromUtf8("axisCmbBox"))
        self.axisCmbBox.addItem(_fromUtf8(""))
        self.axisCmbBox.addItem(_fromUtf8(""))
        self.axisCmbBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.axisCmbBox)
        self.devname_Label = QtGui.QLabel(self.AXIS_Box)
        self.devname_Label.setObjectName(_fromUtf8("devname_Label"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.devname_Label)
        self.devname_Line = QtGui.QLineEdit(self.AXIS_Box)
        self.devname_Line.setObjectName(_fromUtf8("devname_Line"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.devname_Line)
        self.vgalvmax_Label = QtGui.QLabel(self.AXIS_Box)
        self.vgalvmax_Label.setObjectName(_fromUtf8("vgalvmax_Label"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.vgalvmax_Label)
        self.vgalvmax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.vgalvmax_NumDbl.setMinimum(-10.0)
        self.vgalvmax_NumDbl.setMaximum(10.0)
        self.vgalvmax_NumDbl.setObjectName(_fromUtf8("vgalvmax_NumDbl"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.vgalvmax_NumDbl)
        self.vgalvmin_Label = QtGui.QLabel(self.AXIS_Box)
        self.vgalvmin_Label.setObjectName(_fromUtf8("vgalvmin_Label"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.vgalvmin_Label)
        self.vgalvmin_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.vgalvmin_NumDbl.setMinimum(-10.0)
        self.vgalvmin_NumDbl.setMaximum(10.0)
        self.vgalvmin_NumDbl.setObjectName(_fromUtf8("vgalvmin_NumDbl"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.vgalvmin_NumDbl)
        self.nmgalvmax_Label = QtGui.QLabel(self.AXIS_Box)
        self.nmgalvmax_Label.setObjectName(_fromUtf8("nmgalvmax_Label"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.nmgalvmax_Label)
        self.nmgalvmax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.nmgalvmax_NumDbl.setMinimum(-10000.0)
        self.nmgalvmax_NumDbl.setMaximum(10000.0)
        self.nmgalvmax_NumDbl.setObjectName(_fromUtf8("nmgalvmax_NumDbl"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.nmgalvmax_NumDbl)
        self.nmgalvmin_Label = QtGui.QLabel(self.AXIS_Box)
        self.nmgalvmin_Label.setObjectName(_fromUtf8("nmgalvmin_Label"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.nmgalvmin_Label)
        self.nmgalvmin_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.nmgalvmin_NumDbl.setMinimum(-10000.0)
        self.nmgalvmin_NumDbl.setMaximum(10000.0)
        self.nmgalvmin_NumDbl.setObjectName(_fromUtf8("nmgalvmin_NumDbl"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.nmgalvmin_NumDbl)
        self.qpdmax_Label = QtGui.QLabel(self.AXIS_Box)
        self.qpdmax_Label.setObjectName(_fromUtf8("qpdmax_Label"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.qpdmax_Label)
        self.qpdmax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.qpdmax_NumDbl.setMinimum(-10.0)
        self.qpdmax_NumDbl.setMaximum(10.0)
        self.qpdmax_NumDbl.setObjectName(_fromUtf8("qpdmax_NumDbl"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.qpdmax_NumDbl)
        self.qpdmin_Label = QtGui.QLabel(self.AXIS_Box)
        self.qpdmin_Label.setObjectName(_fromUtf8("qpdmin_Label"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.qpdmin_Label)
        self.qpdmin_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.qpdmin_NumDbl.setMinimum(-10.0)
        self.qpdmin_NumDbl.setMaximum(10.0)
        self.qpdmin_NumDbl.setObjectName(_fromUtf8("qpdmin_NumDbl"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.qpdmin_NumDbl)
        self.pmax_Label = QtGui.QLabel(self.AXIS_Box)
        self.pmax_Label.setObjectName(_fromUtf8("pmax_Label"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.pmax_Label)
        self.pmax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.pmax_NumDbl.setMinimum(0.0)
        self.pmax_NumDbl.setMaximum(1000.0)
        self.pmax_NumDbl.setObjectName(_fromUtf8("pmax_NumDbl"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.pmax_NumDbl)
        self.imax_Label = QtGui.QLabel(self.AXIS_Box)
        self.imax_Label.setObjectName(_fromUtf8("imax_Label"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.imax_Label)
        self.imax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.imax_NumDbl.setMinimum(0.0)
        self.imax_NumDbl.setMaximum(1000.0)
        self.imax_NumDbl.setObjectName(_fromUtf8("imax_NumDbl"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.imax_NumDbl)
        self.speedmax_Label = QtGui.QLabel(self.AXIS_Box)
        self.speedmax_Label.setObjectName(_fromUtf8("speedmax_Label"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.LabelRole, self.speedmax_Label)
        self.speedmax_NumDbl = QtGui.QDoubleSpinBox(self.AXIS_Box)
        self.speedmax_NumDbl.setMinimum(0.0)
        self.speedmax_NumDbl.setMaximum(1000.0)
        self.speedmax_NumDbl.setObjectName(_fromUtf8("speedmax_NumDbl"))
        self.formLayout_2.setWidget(11, QtGui.QFormLayout.FieldRole, self.speedmax_NumDbl)
        self.verticalLayout.addWidget(self.AXIS_Box)
        self.OTHER_Box = QtGui.QGroupBox(configDial)
        self.OTHER_Box.setObjectName(_fromUtf8("OTHER_Box"))
        self.formLayout_4 = QtGui.QFormLayout(self.OTHER_Box)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.stimmaxfreq_NumDbl = QtGui.QDoubleSpinBox(self.OTHER_Box)
        self.stimmaxfreq_NumDbl.setMinimum(0.0)
        self.stimmaxfreq_NumDbl.setMaximum(1000.0)
        self.stimmaxfreq_NumDbl.setObjectName(_fromUtf8("stimmaxfreq_NumDbl"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.stimmaxfreq_NumDbl)
        self.stimmaxfreq_Label = QtGui.QLabel(self.OTHER_Box)
        self.stimmaxfreq_Label.setObjectName(_fromUtf8("stimmaxfreq_Label"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.stimmaxfreq_Label)
        self.verticalLayout.addWidget(self.OTHER_Box)
        self.buttonBox = QtGui.QDialogButtonBox(configDial)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(configDial)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), configDial.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), configDial.reject)
        QtCore.QMetaObject.connectSlotsByName(configDial)

    def retranslateUi(self, configDial):
        configDial.setWindowTitle(_translate("configDial", "OTsUI configuration", None))
        self.CONN_Box.setTitle(_translate("configDial", "Connection", None))
        self.ipaddr_Label.setText(_translate("configDial", "Forwarder IP address", None))
        self.subport_Label.setText(_translate("configDial", "SUB Port", None))
        self.pubport_Label.setText(_translate("configDial", "PUB Port", None))
        self.AXIS_Box.setTitle(_translate("configDial", "Axis parameters", None))
        self.axisCmbBox.setItemText(0, _translate("configDial", "X", None))
        self.axisCmbBox.setItemText(1, _translate("configDial", "Y", None))
        self.axisCmbBox.setItemText(2, _translate("configDial", "Z", None))
        self.devname_Label.setText(_translate("configDial", "Device name", None))
        self.vgalvmax_Label.setText(_translate("configDial", "Galvo Maximum [V]", None))
        self.vgalvmin_Label.setText(_translate("configDial", "Galvo Minimum [V]", None))
        self.nmgalvmax_Label.setText(_translate("configDial", "Galvo Maximum [nm]", None))
        self.nmgalvmin_Label.setText(_translate("configDial", "Galvo Minimum [nm]", None))
        self.qpdmax_Label.setText(_translate("configDial", "QPD Maximum [V]", None))
        self.qpdmin_Label.setText(_translate("configDial", "QPD Minimum [V]", None))
        self.pmax_Label.setText(_translate("configDial", "P gain Maximum", None))
        self.imax_Label.setText(_translate("configDial", "I gain Maximum", None))
        self.speedmax_Label.setText(_translate("configDial", "Speed Maximum [nm/s]", None))
        self.OTHER_Box.setTitle(_translate("configDial", "Other parameters", None))
        self.stimmaxfreq_Label.setText(_translate("configDial", "Stimuli max frequency [Hz]", None))

