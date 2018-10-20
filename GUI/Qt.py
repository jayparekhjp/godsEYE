import sys
from PyQt4 import QtGui,QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1500,1300)
        #self.showFullScreen()
        self.setWindowTitle("GODSEYE")
        self.setWindowIcon(QtGui.QIcon('icon1.png'))
        self.home()

    def home(self):
        w=QtGui.QWidget()
        title=QtGui.QLabel(w)
        title.setText("Welcome")
        w.setGeometry(100,100,200,50)
        title.move(50,20)
        btn=QtGui.QPushButton("Quit",self)
        btn.clicked.connect(self.close_application)
        btn.resize(100,50)
        btn.move(630,600)
        self.show()

    def close_application(self):
        print("GODSEYE Closed!")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
