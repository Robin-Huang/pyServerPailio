import sys
import serverWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    server = serverWindow.serverWindow()
    server.show()

    sys.exit(app.exec())