from STPMain import Ui_MainWindow
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
class UiTest(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(UiTest,self).__init__()
        self.setupUi(self)

    def slot1(self):
        print('交班')
        #self.dateTimeEdit = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime(),self.centralwidget)


    def DataTimeChangedslot(self):
        pass
        #print('xxx')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    my_pyqt_from =UiTest()
    my_pyqt_from.show()

    sys.exit(app.exec_())
