# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\work\fjl\LKJ2000-WL\LKJ2000-WL\Graphic\test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1055, 585)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tag_groupBox = QtWidgets.QGroupBox(Dialog)
        self.tag_groupBox.setTitle("")
        self.tag_groupBox.setObjectName("tag_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tag_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tag_lab = QtWidgets.QLabel(self.tag_groupBox)
        self.tag_lab.setObjectName("tag_lab")
        self.horizontalLayout_2.addWidget(self.tag_lab)
        self.devName_lab = QtWidgets.QLabel(self.tag_groupBox)
        self.devName_lab.setObjectName("devName_lab")
        self.horizontalLayout_2.addWidget(self.devName_lab)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tag_groupBox)
        self.dateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7994, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.stationName_lab = QtWidgets.QLabel(self.tag_groupBox)
        self.stationName_lab.setObjectName("stationName_lab")
        self.horizontalLayout_2.addWidget(self.stationName_lab)
        self.trainNo_lab = QtWidgets.QLabel(self.tag_groupBox)
        self.trainNo_lab.setObjectName("trainNo_lab")
        self.horizontalLayout_2.addWidget(self.trainNo_lab)
        self.verticalLayout_2.addWidget(self.tag_groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.ledA_lab = QtWidgets.QLabel(self.groupBox_5)
        self.ledA_lab.setObjectName("ledA_lab")
        self.gridLayout.addWidget(self.ledA_lab, 0, 0, 1, 1)
        self.ledB_lab = QtWidgets.QLabel(self.groupBox_5)
        self.ledB_lab.setObjectName("ledB_lab")
        self.gridLayout.addWidget(self.ledB_lab, 0, 1, 1, 1)
        self.ledTmis_lab = QtWidgets.QLabel(self.groupBox_5)
        self.ledTmis_lab.setObjectName("ledTmis_lab")
        self.gridLayout.addWidget(self.ledTmis_lab, 0, 2, 1, 1)
        self.ledILock_lab = QtWidgets.QLabel(self.groupBox_5)
        self.ledILock_lab.setObjectName("ledILock_lab")
        self.gridLayout.addWidget(self.ledILock_lab, 0, 3, 1, 1)
        self.stationO_lab = QtWidgets.QLabel(self.groupBox_5)
        self.stationO_lab.setObjectName("stationO_lab")
        self.gridLayout.addWidget(self.stationO_lab, 0, 4, 1, 1)
        self.stationT_lab = QtWidgets.QLabel(self.groupBox_5)
        self.stationT_lab.setObjectName("stationT_lab")
        self.gridLayout.addWidget(self.stationT_lab, 0, 5, 1, 1)
        self.stationT_lab_2 = QtWidgets.QLabel(self.groupBox_5)
        self.stationT_lab_2.setObjectName("stationT_lab_2")
        self.gridLayout.addWidget(self.stationT_lab_2, 0, 6, 1, 1)
        self.stationF_lab = QtWidgets.QLabel(self.groupBox_5)
        self.stationF_lab.setObjectName("stationF_lab")
        self.gridLayout.addWidget(self.stationF_lab, 0, 7, 1, 1)
        self.A_lab = QtWidgets.QLabel(self.groupBox_5)
        self.A_lab.setObjectName("A_lab")
        self.gridLayout.addWidget(self.A_lab, 1, 0, 1, 1)
        self.B_lab = QtWidgets.QLabel(self.groupBox_5)
        self.B_lab.setObjectName("B_lab")
        self.gridLayout.addWidget(self.B_lab, 1, 1, 1, 1)
        self.tmis_lab = QtWidgets.QLabel(self.groupBox_5)
        self.tmis_lab.setObjectName("tmis_lab")
        self.gridLayout.addWidget(self.tmis_lab, 1, 2, 1, 1)
        self.iLock_lab = QtWidgets.QLabel(self.groupBox_5)
        self.iLock_lab.setObjectName("iLock_lab")
        self.gridLayout.addWidget(self.iLock_lab, 1, 3, 1, 1)
        self.one_lab = QtWidgets.QLabel(self.groupBox_5)
        self.one_lab.setObjectName("one_lab")
        self.gridLayout.addWidget(self.one_lab, 1, 4, 1, 1)
        self.two_lab = QtWidgets.QLabel(self.groupBox_5)
        self.two_lab.setObjectName("two_lab")
        self.gridLayout.addWidget(self.two_lab, 1, 5, 1, 1)
        self.three_lab = QtWidgets.QLabel(self.groupBox_5)
        self.three_lab.setObjectName("three_lab")
        self.gridLayout.addWidget(self.three_lab, 1, 6, 1, 1)
        self.four_lab = QtWidgets.QLabel(self.groupBox_5)
        self.four_lab.setObjectName("four_lab")
        self.gridLayout.addWidget(self.four_lab, 1, 7, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(10, 10))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.locoMon_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.locoMon_pB.setObjectName("locoMon_pB")
        self.gridLayout_2.addWidget(self.locoMon_pB, 0, 4, 1, 2)
        self.printJobOrder_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.printJobOrder_pB.setObjectName("printJobOrder_pB")
        self.gridLayout_2.addWidget(self.printJobOrder_pB, 3, 1, 2, 2)
        self.editMod_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.editMod_pB.setObjectName("editMod_pB")
        self.gridLayout_2.addWidget(self.editMod_pB, 0, 1, 1, 1)
        self.stpState_lE = QtWidgets.QLineEdit(self.groupBox_3)
        self.stpState_lE.setObjectName("stpState_lE")
        self.gridLayout_2.addWidget(self.stpState_lE, 0, 11, 1, 2)
        self.sendJobOrder_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.sendJobOrder_pB.setObjectName("sendJobOrder_pB")
        self.gridLayout_2.addWidget(self.sendJobOrder_pB, 0, 2, 1, 2)
        self.historyPlayB_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.historyPlayB_pB.setObjectName("historyPlayB_pB")
        self.gridLayout_2.addWidget(self.historyPlayB_pB, 0, 8, 1, 1)
        self.passStShunt_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.passStShunt_pB.setObjectName("passStShunt_pB")
        self.gridLayout_2.addWidget(self.passStShunt_pB, 0, 6, 1, 2)
        self.cancleLoco_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.cancleLoco_pB.setObjectName("cancleLoco_pB")
        self.gridLayout_2.addWidget(self.cancleLoco_pB, 0, 9, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 2, 1)
        self.handOver_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.handOver_pB.setObjectName("handOver_pB")
        self.gridLayout_2.addWidget(self.handOver_pB, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 4, 5, 1, 1)
        self.station_cB = QtWidgets.QComboBox(self.groupBox_3)
        self.station_cB.setObjectName("station_cB")
        self.station_cB.addItem("")
        self.station_cB.addItem("")
        self.station_cB.addItem("")
        self.station_cB.addItem("")
        self.gridLayout_2.addWidget(self.station_cB, 4, 3, 1, 1)
        self.maintain_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.maintain_pB.setObjectName("maintain_pB")
        self.gridLayout_2.addWidget(self.maintain_pB, 4, 7, 1, 1)
        self.powerMang_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.powerMang_pB.setEnabled(False)
        self.powerMang_pB.setObjectName("powerMang_pB")
        self.gridLayout_2.addWidget(self.powerMang_pB, 4, 8, 1, 1)
        self.refreshStation_pB = QtWidgets.QPushButton(self.groupBox_3)
        self.refreshStation_pB.setObjectName("refreshStation_pB")
        self.gridLayout_2.addWidget(self.refreshStation_pB, 4, 9, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.locoInfo_tW = QtWidgets.QTableWidget(self.groupBox)
        self.locoInfo_tW.setObjectName("locoInfo_tW")
        self.locoInfo_tW.setColumnCount(4)
        self.locoInfo_tW.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 10))
        self.locoInfo_tW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.locoInfo_tW.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.locoInfo_tW.setItem(0, 3, item)
        self.locoInfo_tW.horizontalHeader().setDefaultSectionSize(75)
        self.locoInfo_tW.horizontalHeader().setMinimumSectionSize(20)
        self.horizontalLayout.addWidget(self.locoInfo_tW)
        self.jobOrder_tW = QtWidgets.QTableWidget(self.groupBox)
        self.jobOrder_tW.setObjectName("jobOrder_tW")
        self.jobOrder_tW.setColumnCount(7)
        self.jobOrder_tW.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jobOrder_tW.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense5Pattern)
        item.setForeground(brush)
        self.jobOrder_tW.setItem(0, 0, item)
        self.jobOrder_tW.horizontalHeader().setVisible(True)
        self.jobOrder_tW.horizontalHeader().setCascadingSectionResizes(True)
        self.jobOrder_tW.horizontalHeader().setDefaultSectionSize(53)
        self.jobOrder_tW.horizontalHeader().setHighlightSections(True)
        self.jobOrder_tW.horizontalHeader().setMinimumSectionSize(15)
        self.jobOrder_tW.verticalHeader().setVisible(False)
        self.jobOrder_tW.verticalHeader().setHighlightSections(True)
        self.horizontalLayout.addWidget(self.jobOrder_tW)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tag_lab.setText(_translate("Dialog", "企业标识"))
        self.devName_lab.setText(_translate("Dialog", "设备名称"))
        self.stationName_lab.setText(_translate("Dialog", "站场名"))
        self.trainNo_lab.setText(_translate("Dialog", "机车号"))
        self.ledA_lab.setText(_translate("Dialog", "led_1"))
        self.ledB_lab.setText(_translate("Dialog", "led_2"))
        self.ledTmis_lab.setText(_translate("Dialog", "led_3"))
        self.ledILock_lab.setText(_translate("Dialog", "led_4"))
        self.stationO_lab.setText(_translate("Dialog", "led_5"))
        self.stationT_lab.setText(_translate("Dialog", "led_6"))
        self.stationT_lab_2.setText(_translate("Dialog", "led_7"))
        self.stationF_lab.setText(_translate("Dialog", "led_8"))
        self.A_lab.setText(_translate("Dialog", "A机"))
        self.B_lab.setText(_translate("Dialog", "B机"))
        self.tmis_lab.setText(_translate("Dialog", "TMIS"))
        self.iLock_lab.setText(_translate("Dialog", "联锁"))
        self.one_lab.setText(_translate("Dialog", "一场"))
        self.two_lab.setText(_translate("Dialog", "二场"))
        self.three_lab.setText(_translate("Dialog", "三场"))
        self.four_lab.setText(_translate("Dialog", "四场"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "站场图"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.locoMon_pB.setText(_translate("Dialog", "机车监控"))
        self.printJobOrder_pB.setText(_translate("Dialog", "打印作业单"))
        self.editMod_pB.setText(_translate("Dialog", "编辑模式"))
        self.stpState_lE.setText(_translate("Dialog", "正常"))
        self.sendJobOrder_pB.setText(_translate("Dialog", "发送作业单"))
        self.historyPlayB_pB.setText(_translate("Dialog", "历史回放"))
        self.passStShunt_pB.setText(_translate("Dialog", "越站调车"))
        self.cancleLoco_pB.setText(_translate("Dialog", "注销机车"))
        self.handOver_pB.setText(_translate("Dialog", "交班"))
        self.station_cB.setItemText(0, _translate("Dialog", "一场"))
        self.station_cB.setItemText(1, _translate("Dialog", "二场"))
        self.station_cB.setItemText(2, _translate("Dialog", "三场"))
        self.station_cB.setItemText(3, _translate("Dialog", "四场"))
        self.maintain_pB.setText(_translate("Dialog", "维护"))
        self.powerMang_pB.setText(_translate("Dialog", "权限管理"))
        self.refreshStation_pB.setText(_translate("Dialog", "刷新站场"))
        item = self.locoInfo_tW.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "调车单号"))
        item = self.locoInfo_tW.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "调车机"))
        item = self.locoInfo_tW.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "车次"))
        item = self.locoInfo_tW.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "时间范围"))
        __sortingEnabled = self.locoInfo_tW.isSortingEnabled()
        self.locoInfo_tW.setSortingEnabled(False)
        self.locoInfo_tW.setSortingEnabled(__sortingEnabled)
        item = self.jobOrder_tW.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "勾号"))
        item = self.jobOrder_tW.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "线别"))
        item = self.jobOrder_tW.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "作业方法"))
        item = self.jobOrder_tW.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "限速"))
        item = self.jobOrder_tW.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "首尾"))
        item = self.jobOrder_tW.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "本勾状态"))
        item = self.jobOrder_tW.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "附注"))
        __sortingEnabled = self.jobOrder_tW.isSortingEnabled()
        self.jobOrder_tW.setSortingEnabled(False)
        self.jobOrder_tW.setSortingEnabled(__sortingEnabled)
