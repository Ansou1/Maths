# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewerUI.ui'
#
# Created: Fri Jun  6 11:53:27 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 10, 171, 27))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(612, 10, 171, 27))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(610, 60, 171, 27))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(612, 150, 171, 27))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(612, 240, 171, 27))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.graphic = QtGui.QCheckBox(self.centralwidget)
        self.graphic.setGeometry(QtCore.QRect(640, 420, 83, 20))
        self.graphic.setObjectName(_fromUtf8("graphic"))
        self.langue = QtGui.QComboBox(self.centralwidget)
        self.langue.setGeometry(QtCore.QRect(610, 370, 171, 25))
        self.langue.setObjectName(_fromUtf8("langue"))
        self.langue.addItem(_fromUtf8(""))
        self.langue.addItem(_fromUtf8(""))
        self.langue.addItem(_fromUtf8(""))
        self.langue.addItem(_fromUtf8(""))
        self.langue.addItem(_fromUtf8(""))
        self.buttonOK = QtGui.QPushButton(self.centralwidget)
        self.buttonOK.setGeometry(QtCore.QRect(600, 490, 85, 27))
        self.buttonOK.setObjectName(_fromUtf8("buttonOK"))
        self.buttonCancel = QtGui.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(700, 490, 85, 27))
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(612, 330, 171, 27))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pourcentage = QtGui.QDoubleSpinBox(self.centralwidget)
        self.pourcentage.setGeometry(QtCore.QRect(610, 280, 171, 27))
        self.pourcentage.setDecimals(3)
        self.pourcentage.setMaximum(100.0)
        self.pourcentage.setSingleStep(0.001)
        self.pourcentage.setObjectName(_fromUtf8("pourcentage"))
        self.population = QtGui.QSpinBox(self.centralwidget)
        self.population.setGeometry(QtCore.QRect(610, 100, 171, 27))
        self.population.setMaximum(2000000000)
        self.population.setObjectName(_fromUtf8("population"))
        self.echantillon = QtGui.QSpinBox(self.centralwidget)
        self.echantillon.setGeometry(QtCore.QRect(610, 190, 171, 27))
        self.echantillon.setMaximum(2000000000)
        self.echantillon.setObjectName(_fromUtf8("echantillon"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 0, 20, 551))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 781, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(600, 130, 191, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(600, 220, 191, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(600, 310, 191, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(610, 440, 171, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.AffichageResultat = QtGui.QPlainTextEdit(self.centralwidget)
        self.AffichageResultat.setGeometry(QtCore.QRect(10, 60, 571, 491))
        self.AffichageResultat.setReadOnly(True)
        self.AffichageResultat.setObjectName(_fromUtf8("AffichageResultat"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuQuit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "209sondage", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "      Affichage des résultats", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setText(QtGui.QApplication.translate("MainWindow", "                  Donnees", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setText(QtGui.QApplication.translate("MainWindow", "        Taille de la population", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_4.setText(QtGui.QApplication.translate("MainWindow", "Taille de l\'échantillon", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_5.setText(QtGui.QApplication.translate("MainWindow", "Pourcentage", None, QtGui.QApplication.UnicodeUTF8))
        self.graphic.setText(QtGui.QApplication.translate("MainWindow", "Graphic", None, QtGui.QApplication.UnicodeUTF8))
        self.langue.setItemText(0, QtGui.QApplication.translate("MainWindow", "French", None, QtGui.QApplication.UnicodeUTF8))
        self.langue.setItemText(1, QtGui.QApplication.translate("MainWindow", "German", None, QtGui.QApplication.UnicodeUTF8))
        self.langue.setItemText(2, QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.langue.setItemText(3, QtGui.QApplication.translate("MainWindow", "Spanish", None, QtGui.QApplication.UnicodeUTF8))
        self.langue.setItemText(4, QtGui.QApplication.translate("MainWindow", "Italian", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOK.setText(QtGui.QApplication.translate("MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_6.setText(QtGui.QApplication.translate("MainWindow", "Langage", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setTitle(QtGui.QApplication.translate("MainWindow", "quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

