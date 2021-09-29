

from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import QApplication, QDialog, QFrame, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_Login
import sys
import STPMain
class Login(QMainWindow):
    def __init__(self,parent=None,name = "调试工具"):
        #构造函数
        super().__init__(parent)
        self.initUI(name)
    def initUI(self, name):
        # 初始化函数
        self.m_ui=Ui_Login.Ui_Login()
        self.m_ui.setupUi(self)
        self.setWindowTitle(name)
        self.initConnect()
        #STP主窗口
        #self.m_uiSTPMain = STPMain.STPMain()

    def initConnect(self):
        # 初始化信号与槽
        self.m_ui.wl_pushButton.clicked.connect(self.WL_slot)
        self.m_ui.stp_pushButton.clicked.connect(self.STP_slot)

    @abstractmethod
    def WL_slot(self):
        #pushButton的槽函数
        print("wl1")

        
    @abstractmethod
    def STP_slot(self):
        #pushButton的槽函数
        print("stp1")

        #self.m_uiSTPMain.show()
        # tmp = STPMain.STPMain(self)
        # tmp.exec_()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        
        return super().closeEvent(a0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = Login()
    md.show()
    app.exec_()
    #sys.exit(app.exec_())