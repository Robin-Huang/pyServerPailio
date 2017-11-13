# pyServerPailio

## 開發環境
- Python 3.5.3
- PyQt 5.9.1
- Tensorflow 1.4.0

## 說明
此為 [PailioApp](https://github.com/Robin-Huang/PailioApp) 的伺服端，
同時也是 [serverPailioRecognition](https://github.com/Robin-Huang/serverPailioRecognition) 的改良版本。<br>

過去以 Qt 建立伺服器介面，並用 QProcess 呼叫 Python 執行辨識，
但須不斷重新載入辨識的 CNN 模型，較耗時(在我的筆電(用 CPU )處理一張圖約 6 sec )，
因此改將所有工作都在 Python 下運行，介面以 PyQt 處理，一張圖處裡約剩 3 sec 。<br>

- ui_serverWindow.ui<br>
在 [serverPailioRecognition](https://github.com/Robin-Huang/serverPailioRecognition) 設計的 UI 介面。<br>

- ui_serverWindow.py<br>
利用 PyQT5 中的 PyUIC 將 [ui_serverWindow.ui](https://github.com/Robin-Huang/pyServerPailio/blob/master/ui_serverWindow.py) 轉為 .py 檔，便可藉由 PyQT5 在 Python 下執行 Qt 的 UI 介面。<br>

- serverWindow.py<br>
接收 [PailioApp](https://github.com/Robin-Huang/PailioApp) 的圖檔，將圖檔傳入 [pailio_recognition.py](https://github.com/Robin-Huang/pyServerPailio/blob/master/pailio_recognition.py) 進行辨識並回傳辨識結果。同時控制 [ui_serverWindow.py](https://github.com/Robin-Huang/pyServerPailio/blob/master/ui_serverWindow.py) 各項元件的作用。<br>

- pailio_recognition.py<br>
辨識接收到的圖檔。<br>

## 問題紀錄
#### Q1. 如何接收客戶端( TcpSocket )檔案，又如何知道檔案已接收完成?
A. 在客戶端會傳送一組 QByteArray 資訊，前 8 bytes 紀錄該檔案的位元大小，因此接收到資料後，先讀取該檔案大小，便可知道之後要讀取多少大小的資料。實際做法參考 [serverWindow.py](https://github.com/Robin-Huang/pyServerPailio/blob/master/serverWindow.py) 中的 updateProgress 。<br>
