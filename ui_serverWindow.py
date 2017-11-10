# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_serverWindow(object):
    def setupUi(self, serverWindow):
        serverWindow.setObjectName("serverWindow")
        serverWindow.resize(775, 481)
        serverWindow.setStyleSheet("background-color:rgb(153, 153, 153);")
        self.centralWidget = QtWidgets.QWidget(serverWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 461, 391))
        self.frame.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_recgResult = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_recgResult.setFont(font)
        self.label_recgResult.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_recgResult.setObjectName("label_recgResult")
        self.horizontalLayout_3.addWidget(self.label_recgResult)
        self.recgResult = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recgResult.sizePolicy().hasHeightForWidth())
        self.recgResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recgResult.setFont(font)
        self.recgResult.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.recgResult.setAlignment(QtCore.Qt.AlignCenter)
        self.recgResult.setObjectName("recgResult")
        self.horizontalLayout_3.addWidget(self.recgResult)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_recvState = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_recvState.setFont(font)
        self.label_recvState.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_recvState.setObjectName("label_recvState")
        self.horizontalLayout_2.addWidget(self.label_recvState)
        self.recvProsBar = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recvProsBar.sizePolicy().hasHeightForWidth())
        self.recvProsBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recvProsBar.setFont(font)
        self.recvProsBar.setStyleSheet("QProgressBar{\n"
"border : 2px solid grey;\n"
"border-radius  : 5px;\n"
"width: 10px;\n"
"margin : 1px;\n"
"background-color :rgb(185, 255, 247);\n"
"color : rgb(0, 0, 0);\n"
"}\n"
"QProgressBar:chunk{\n"
"background-color :rgb(115, 202, 255);\n"
"width: 15px;\n"
"margin: 1px;\n"
"}")
        self.recvProsBar.setProperty("value", 0)
        self.recvProsBar.setAlignment(QtCore.Qt.AlignCenter)
        self.recvProsBar.setObjectName("recvProsBar")
        self.horizontalLayout_2.addWidget(self.recvProsBar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.imageDisplay = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageDisplay.sizePolicy().hasHeightForWidth())
        self.imageDisplay.setSizePolicy(sizePolicy)
        self.imageDisplay.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.imageDisplay.setText("")
        self.imageDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDisplay.setObjectName("imageDisplay")
        self.gridLayout.addWidget(self.imageDisplay, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_savePath = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_savePath.setFont(font)
        self.label_savePath.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_savePath.setObjectName("label_savePath")
        self.horizontalLayout_8.addWidget(self.label_savePath)
        self.savePath = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePath.sizePolicy().hasHeightForWidth())
        self.savePath.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.savePath.setFont(font)
        self.savePath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.savePath.setText("")
        self.savePath.setAlignment(QtCore.Qt.AlignCenter)
        self.savePath.setObjectName("savePath")
        self.horizontalLayout_8.addWidget(self.savePath)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(480, 20, 281, 391))
        self.frame_2.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stateBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.stateBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stateBrowser.setObjectName("stateBrowser")
        self.gridLayout_4.addWidget(self.stateBrowser, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet("QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"background-color: rgb(141, 241, 226);\n"
"border:2px;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(109, 186, 175);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(49, 84, 79);\n"
"}")
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.stopBtn.setFont(font)
        self.stopBtn.setStyleSheet("QPushButton{\n"
"color:rgb(0, 0, 0);\n"
"background-color:rgb(255, 165, 255);\n"
"border:2px;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(184, 119, 184);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(126, 81, 126);\n"
"background-color: rgb(49, 84, 79);\n"
"}")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_ip = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_ip.setFont(font)
        self.label_ip.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_9.addWidget(self.label_ip)
        self.ip = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ip.sizePolicy().hasHeightForWidth())
        self.ip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ip.setFont(font)
        self.ip.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.ip.setText("")
        self.ip.setAlignment(QtCore.Qt.AlignCenter)
        self.ip.setObjectName("ip")
        self.horizontalLayout_9.addWidget(self.ip)
        self.gridLayout_4.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.frame_2.raise_()
        self.frame.raise_()
        serverWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(serverWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 775, 20))
        self.menuBar.setObjectName("menuBar")
        serverWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(serverWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        serverWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(serverWindow)
        self.statusBar.setObjectName("statusBar")
        serverWindow.setStatusBar(self.statusBar)

        self.retranslateUi(serverWindow)
        QtCore.QMetaObject.connectSlotsByName(serverWindow)

    def retranslateUi(self, serverWindow):
        _translate = QtCore.QCoreApplication.translate
        serverWindow.setWindowTitle(_translate("serverWindow", "serverWindow"))
        self.label_recgResult.setText(_translate("serverWindow", "判別結果 : "))
        self.recgResult.setText(_translate("serverWindow", "判斷結果(相似度%)"))
        self.label_recvState.setText(_translate("serverWindow", "接收狀態 : "))
        self.label_savePath.setText(_translate("serverWindow", "存檔路徑 : "))
        self.startBtn.setText(_translate("serverWindow", "Start"))
        self.stopBtn.setText(_translate("serverWindow", "Stop"))
        self.label_ip.setText(_translate("serverWindow", "IP : "))

