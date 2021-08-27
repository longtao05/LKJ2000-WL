from PyQt5.QtWidgets import QApplication, QFrame, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_Login
import sys
import STPMain
class Login(QFrame):
    def __init__(self,parent=None,name = "调试工具"):
        #构造函数
        super().__init__(parent)
        self.initUI(name)
    def initUI(self, name):
        # 初始化函数
        self.m_ui=Ui_Login.Ui_Form()
        self.m_ui1 = None
        self.m_ui.setupUi(self)
        self.setWindowTitle(name)
        self.initConnect()

    def initConnect(self):
        # 初始化信号与槽
        self.m_ui.wl_pushButton.clicked.connect(self.WL_slot)
        self.m_ui.stp_pushButton.clicked.connect(self.STP_slot)


    def WL_slot(self):
        #pushButton的槽函数
        print("wl")
        self.m_ui1=STPMain.STPMain()
        self.m_ui1.setupUi(self.m_ui1)
        self.m_ui1.show()

    def STP_slot(self):
        #pushButton的槽函数
        print("stp")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = Login()
    md.show()
    app.exec_()
    #sys.exit(app.exec_())