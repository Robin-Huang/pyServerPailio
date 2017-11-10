# pyServerPailio

## 開發環境
- Python3.5.3
- PyQt5.9.1
- Tensorflow 1.4.0

## 說明
此為 [PailioApp](https://github.com/Robin-Huang/PailioApp) 的伺服端，
同時也是 [serverPailioRecognition](https://github.com/Robin-Huang/serverPailioRecognition) 的改良版本。<br>

過去以 Qt 建立伺服器介面，並用 QProcess 呼叫 Python 執行辨識，
但須不斷重新載入辨識的 CNN 模型，較耗時(在我的筆電(用 CPU )處理一張圖約 6 sec )，
因此改將所有工作都在 Python 下運行，介面以 PyQt 處理，一張圖處裡約剩 3 sec 。<br>
