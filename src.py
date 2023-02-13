from PyQt5 import QtWidgets, uic
import sys
from ui import TTTUI
import sys
class mainScreenUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainScreenUi, self).__init__()
        uic.loadUi('mainscreen.ui', self)
        self.PlayBtn.clicked.connect(self.openLevelPage)
        self.QuitBtn.clicked.connect(lambda x: self.close())

        self.show()

    def openLevelPage(self):
        self.close()
        #app = QtWidgets.QApplication(sys.argv)
        ui = levelUi()
        
        #app.exec_()
        #ui.setupUi(SecondScreen_MW )
        #SecondScreen_MW.show()
        # (Optional) Hide first screen
       # self.hide()
        
class levelUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(levelUi, self).__init__()
        uic.loadUi('level.ui', self)
        self.easyBtn.clicked.connect(lambda x: self.openGame(2))
        self.diffBtn.clicked.connect(lambda x: self.openGame(4))
        self.insaneBtn.clicked.connect(lambda x: self.openGame(6))
        self.QuitBtn.clicked.connect(lambda x: self.close())
        self.show()
        
    def openGame(self,val):
        self.hide()
        TTTUI(val)
        self.close()
        
app = QtWidgets.QApplication(sys.argv)
window = mainScreenUi()
app.exec_()