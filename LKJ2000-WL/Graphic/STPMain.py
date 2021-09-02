from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_STPMain
import sys
class STPMain(QMainWindow, Ui_STPMain.Ui_STPMain):

    def __init__(self,name = "STPM"):
        #构造函数
        super().__init__()
        self.initUI(name)
        self.cnt_tmp = 0
    def initUI(self, name):
        # 初始化函数
        self.m_ui=Ui_STPMain.Ui_STPMain()
        self.m_ui.setupUi(self)
        # self.setWindowTitle(name)
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.m_ui.handOver_pB.clicked.connect(self.slot_handOver_pB)
        self.m_ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        pass
    def setDirEditText(self, str_show):
        # 更新edit的文本
        self.m_ui.lineEdit.setText( str_show )

    def slot_handOver_pB(self):
        #pushButton的槽函数
        self.cnt_tmp = self.cnt_tmp + 1
        self.setDirEditText(str(self.cnt_tmp))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = STPMain()
    md.show()
    app.exec_()
    # sys.exit(app.exec_())