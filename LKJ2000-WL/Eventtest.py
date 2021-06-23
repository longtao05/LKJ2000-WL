import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
#from test import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
class MyPyQT_Form(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super(MyPyQT_Form, self).__init__()
    self.setupUi(self)
  # 实现pushButton_click()函数，textEdit是我们放上去的文本框的id
  def pushButton_click(self):
    #self.showText.setText("你点击了按钮")
    dir_path = QFileDialog.getExistingDirectory(self, "choose directory", r"C:\Users\Administrator\Desktop")
    self.showText.setText(dir_path)
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  my_pyqt_form = MyPyQT_Form()
  my_pyqt_form.show()
  sys.exit(app.exec_())
