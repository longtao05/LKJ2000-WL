# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\work\fjl\LKJ2000-WL\LKJ2000-WL\Graphic\Login1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 256)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(109, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cho_label = QtWidgets.QLabel(self.groupBox_2)
        self.cho_label.setObjectName("cho_label")
        self.horizontalLayout_2.addWidget(self.cho_label)
        spacerItem1 = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wl_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.wl_pushButton.setObjectName("wl_pushButton")
        self.horizontalLayout.addWidget(self.wl_pushButton)
        self.stp_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.stp_pushButton.setObjectName("stp_pushButton")
        self.horizontalLayout.addWidget(self.stp_pushButton)
        self.other_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.other_pushButton.setEnabled(False)
        self.other_pushButton.setObjectName("other_pushButton")
        self.horizontalLayout.addWidget(self.other_pushButton)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cho_label.setText(_translate("Form", "请选择使用工具类型"))
        self.wl_pushButton.setText(_translate("Form", "无线换装"))
        self.stp_pushButton.setText(_translate("Form", "STP"))
        self.other_pushButton.setText(_translate("Form", "其他"))
