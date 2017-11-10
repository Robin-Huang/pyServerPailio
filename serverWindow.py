# TcpServer
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore    import QObject, QFile, QDateTime, QDataStream, QDir, Qt, QIODevice, QByteArray
from PyQt5.QtGui     import QImage, QPixmap
from PyQt5.QtNetwork import QTcpServer, QTcpSocket, QHostAddress

from ui_serverWindow import Ui_serverWindow
from pailio_recognition import PailioRecog

class serverWindow(QMainWindow):
    def __init__(self, parent = None):
        super(serverWindow, self).__init__(parent)
        self.ui      = Ui_serverWindow()

        # Server & Client
        self.client  = QTcpSocket(self)
        self.server  = QTcpServer(self)

        # Recieve File
        self.curTime       = QDateTime()
        self.file          = QFile()
        self.image         = QImage()
        self.bytesReceived = 0
        self.fileSize      = 0
        self.filePath      = ''
        self.savePath      = ''

        self.ui.setupUi(self)
        self.dirSetting()

        # Pailio Recognition
        self.ui.stateBrowser.append('準備辨識系統模型...')
        self.recogPailio = PailioRecog()
        self.recogPailio.load_model()
        self.ui.stateBrowser.append('模型準備完成...\n')


        # Connect Signal & Slot
        self.ui.startBtn.clicked.connect(self.startServer)
        self.ui.stopBtn.clicked.connect(self.stopServer)
        self.server.newConnection.connect(self.acceptConnection, Qt.QueuedConnection)

    def dirSetting(self):
        dir = QDir()
        self.savePath = dir.currentPath() + '/recieve/'
        self.ui.savePath.setText(self.savePath)

    def startServer(self):
        self.server.listen(QHostAddress.Any, 37)
        self.ui.stateBrowser.append('伺服器啟動...')
        self.ui.startBtn.setEnabled(False)
        self.ui.stopBtn.setEnabled(True)

    def stopServer(self):
        self.server.close()
        self.ui.stateBrowser.append('伺服器關閉...')
        self.ui.startBtn.setEnabled(True)
        self.ui.stopBtn.setEnabled(False)

    def acceptConnection(self):
        self.curTime = QDateTime.currentDateTime()
        self.filePath = self.savePath + self.curTime.toString('yyyy-MM-dd_hh-mm-ss') + '.jpg'
        self.file = QFile(self.filePath)

        # Check File
        if self.file.open(QIODevice.WriteOnly) == 0:
            self.ui.stateBrowser.append('無法開啟檔案: ' + self.filePath)
            return

        self.bytesReceived = 0
        self.fileSize      = 0
        self.client = self.server.nextPendingConnection()

        # Connect Signal & Slot
        self.client.readyRead.connect(self.updateProgress)
        self.client.error.connect(self.displayError)

    def updateProgress(self):
        stream = QDataStream(self.client)

        # bytesAvailable > sizeof(qint64) = 8
        if self.client.bytesAvailable() > 8 and self.fileSize == 0:
            self.fileSize = int(stream.readInt64()) # stream >> self.fileSize
            self.bytesReceived += 8
            self.ui.stateBrowser.append('檔案大小: ' + str(self.fileSize / 1024) + 'KB')
            self.ui.recvProsBar.setMaximum(self.fileSize)
        else:
            self.bytesReceived += int(self.client.bytesAvailable())
            self.ui.recvProsBar.setValue(self.bytesReceived)
            self.file.write(self.client.readAll())

            # Finish Receive
            if self.fileSize == self.bytesReceived:
                self.file.close()
                self.ui.stateBrowser.append('檔案已儲存: ' + self.file.fileName())

                self.displayImage()
                self.sendProsResult()

    def displayImage(self):
        if self.image.load(self.filePath) == 0:
            self.ui.imageDisplay.setText('無法顯示圖片')
        else:
            self.ui.imageDisplay.setPixmap(QPixmap.fromImage(self.image.scaled(300,300)))

    def sendProsResult(self):
        self.ui.stateBrowser.append('開始辨識...')
        self.recogPailio.start_recognition(self.filePath)
        self.ui.stateBrowser.append('辨識完成...')

        self.prosResult = str(self.recogPailio.recogClass) + ' (相似度' + str(self.recogPailio.top_score * 100) + '%)'
        self.ui.stateBrowser.append('辨識結果: ' + self.prosResult)

        # Send result
        byteArray  = QByteArray()
        byteArray.append(bytes(self.prosResult, encoding = 'UTF-8'))
        # sendStream = QDataStream(byteArray, QIODevice.WriteOnly)
        # sendStream.writeString(bytes(self.prosResult, encoding = 'UTF-8'))
        self.client.write(byteArray)
        self.ui.stateBrowser.append('送出辨識結果...')


    def displayError(self, socketError):
        if socketError == QTcpSocket.RemoteHostClosedError:
            self.ui.stateBrowser.append('連結中斷...')
            self.ui.stateBrowser.append('-------------------------\n')
        else:
            self.ui.stateBrowser.append('Network error: ' + self.client.errorString())
            self.ui.stateBrowser.append('-------------------------\n')
        self.file = 0