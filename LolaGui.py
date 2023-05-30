from threading import main_thread
from LolaUI import Ui_Lola
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import lola
import sys

class MainThread(QThread):

    StartExe = main_thread()

    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        lola.EjecutarMain

class Gui_Start(QMainWindow):
    StartExe = main_thread()
    def __init__(self):
        super().__init__()

        self.gui = Ui_Lola()
        self.gui.setupUi(self)
        self.gui.bg_2.clicked.connect(self.EmpezarTarea)
    
    def EmpezarTarea(self):
        self.gui.label = QtGui.QMovie("..//G.U.I Material//VoiceReg//Ntuks.gif")
        self.gui.bg_2.setMovie(self.gui.label)
        self.gui.label.start()

    StartExe.start()

GuiApp = QApplication(sys.argv)
lola_gui = Gui_Start()
lola_gui.show()
exit(GuiApp.exec_())