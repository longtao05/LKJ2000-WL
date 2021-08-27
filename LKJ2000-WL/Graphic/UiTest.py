from Ui_STPMain import Ui_MainWindow
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import Ui_STPMain
class UiTest(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(UiTest,self).__init__()
        self.ui=Ui_MainWindow()
        self.setupUi(self)
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.slot2)

    def slot1(self):
        print('交班')
        #self.dateTimeEdit = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime(),self.centralwidget)

    def slot2(self):
        print('XXXXX')

    def DataTimeChangedslot(self):
        #pass
        print('xxx')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    my_pyqt_from =UiTest()
    my_pyqt_from.show()

    sys.exit(app.exec_())
