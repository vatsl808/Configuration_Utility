# dependencies:
# pip install pyqt5
# pip install pyserial
# If you don't have any hardware circuit (e.g., Arduino) to send or receive data, you can try a virtual port emulator for testing purposes.
# Virtual port emulator download link: https://eterlogic.com/downloads/SetupVSPE_64_1.4.7.634.zip


from PyQt5 import QtCore, QtGui, QtWidgets
import serial
# from serial.tools.list_ports import comports
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 541)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_portSetting = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_portSetting.setGeometry(QtCore.QRect(10, 10, 951, 131))
        self.gb_portSetting.setObjectName("gb_portSetting")
        self.cb_burdRate = QtWidgets.QComboBox(self.gb_portSetting)
        self.cb_burdRate.setGeometry(QtCore.QRect(540, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_burdRate.setFont(font)
        self.cb_burdRate.setObjectName("cb_burdRate")
        self.cb_burdRate.addItem("")
        self.cb_burdRate.addItem("")
        self.cb_burdRate.addItem("")
        self.le_parity = QtWidgets.QLineEdit(self.gb_portSetting)
        self.le_parity.setGeometry(QtCore.QRect(260, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_parity.setFont(font)
        self.le_parity.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.le_parity.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_parity.setReadOnly(True)
        self.le_parity.setObjectName("le_parity")
        self.lb_comPort = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_comPort.setGeometry(QtCore.QRect(170, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_comPort.setFont(font)
        self.lb_comPort.setObjectName("lb_comPort")
        self.cb_comPort = QtWidgets.QComboBox(self.gb_portSetting)
        self.cb_comPort.setGeometry(QtCore.QRect(260, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cb_comPort.setFont(font)
        self.cb_comPort.setObjectName("cb_comPort")
        self.label_9 = QtWidgets.QLabel(self.gb_portSetting)
        self.label_9.setGeometry(QtCore.QRect(590, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.le_stopBits = QtWidgets.QLineEdit(self.gb_portSetting)
        self.le_stopBits.setGeometry(QtCore.QRect(790, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_stopBits.setFont(font)
        self.le_stopBits.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.le_stopBits.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_stopBits.setReadOnly(True)
        self.le_stopBits.setObjectName("le_stopBits")
        self.lb_dataBits = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_dataBits.setGeometry(QtCore.QRect(710, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_dataBits.setFont(font)
        self.lb_dataBits.setObjectName("lb_dataBits")
        self.lb_flowControl = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_flowControl.setGeometry(QtCore.QRect(430, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_flowControl.setFont(font)
        self.lb_flowControl.setObjectName("lb_flowControl")
        self.le_dataBits = QtWidgets.QLineEdit(self.gb_portSetting)
        self.le_dataBits.setGeometry(QtCore.QRect(790, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_dataBits.setFont(font)
        self.le_dataBits.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.le_dataBits.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_dataBits.setReadOnly(True)
        self.le_dataBits.setObjectName("le_dataBits")
        self.btn_open = QtWidgets.QPushButton(self.gb_portSetting)
        self.btn_open.setGeometry(QtCore.QRect(10, 30, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open.setFont(font)
        self.btn_open.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_open.setStyleSheet("background-color:lightgray;")
        self.btn_open.setObjectName("btn_open")
        self.le_flowControl = QtWidgets.QLineEdit(self.gb_portSetting)
        self.le_flowControl.setGeometry(QtCore.QRect(540, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_flowControl.setFont(font)
        self.le_flowControl.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.le_flowControl.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_flowControl.setReadOnly(True)
        self.le_flowControl.setObjectName("le_flowControl")
        self.lb_stopBits = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_stopBits.setGeometry(QtCore.QRect(710, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_stopBits.setFont(font)
        self.lb_stopBits.setObjectName("lb_stopBits")
        self.lb_burdRate = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_burdRate.setGeometry(QtCore.QRect(430, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_burdRate.setFont(font)
        self.lb_burdRate.setObjectName("lb_burdRate")
        self.lb_parity = QtWidgets.QLabel(self.gb_portSetting)
        self.lb_parity.setGeometry(QtCore.QRect(170, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_parity.setFont(font)
        self.lb_parity.setObjectName("lb_parity")
        self.gb_read = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_read.setGeometry(QtCore.QRect(10, 160, 421, 341))
        self.gb_read.setObjectName("gb_read")
        self.le_R_temprature = QtWidgets.QLineEdit(self.gb_read)
        self.le_R_temprature.setGeometry(QtCore.QRect(180, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_R_temprature.setFont(font)
        self.le_R_temprature.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_R_temprature.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_R_temprature.setAlignment(QtCore.Qt.AlignCenter)
        self.le_R_temprature.setReadOnly(True)
        self.le_R_temprature.setObjectName("le_R_temprature")
        self.lb_R_temprature = QtWidgets.QLabel(self.gb_read)
        self.lb_R_temprature.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_R_temprature.setFont(font)
        self.lb_R_temprature.setObjectName("lb_R_temprature")
        self.lb_R_current = QtWidgets.QLabel(self.gb_read)
        self.lb_R_current.setGeometry(QtCore.QRect(20, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_R_current.setFont(font)
        self.lb_R_current.setObjectName("lb_R_current")
        self.lb_R_outputStatus = QtWidgets.QLabel(self.gb_read)
        self.lb_R_outputStatus.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_R_outputStatus.setFont(font)
        self.lb_R_outputStatus.setObjectName("lb_R_outputStatus")
        self.le_R_current = QtWidgets.QLineEdit(self.gb_read)
        self.le_R_current.setGeometry(QtCore.QRect(180, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_R_current.setFont(font)
        self.le_R_current.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_R_current.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_R_current.setAlignment(QtCore.Qt.AlignCenter)
        self.le_R_current.setReadOnly(True)
        self.le_R_current.setObjectName("le_R_current")
        self.le_R_outputStatus = QtWidgets.QLineEdit(self.gb_read)
        self.le_R_outputStatus.setGeometry(QtCore.QRect(180, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_R_outputStatus.setFont(font)
        self.le_R_outputStatus.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_R_outputStatus.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_R_outputStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.le_R_outputStatus.setReadOnly(True)
        self.le_R_outputStatus.setObjectName("le_R_outputStatus")
        self.gb_write = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_write.setGeometry(QtCore.QRect(540, 160, 421, 331))
        self.gb_write.setObjectName("gb_write")
        self.lb_W_minTemp = QtWidgets.QLabel(self.gb_write)
        self.lb_W_minTemp.setGeometry(QtCore.QRect(20, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_W_minTemp.setFont(font)
        self.lb_W_minTemp.setObjectName("lb_W_minTemp")
        self.le_W_minTemp = QtWidgets.QLineEdit(self.gb_write)
        self.le_W_minTemp.setGeometry(QtCore.QRect(250, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_W_minTemp.setFont(font)
        self.le_W_minTemp.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_W_minTemp.setMaxLength(32767)
        self.le_W_minTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.le_W_minTemp.setReadOnly(False)
        self.le_W_minTemp.setObjectName("le_W_minTemp")
        self.le_W_maxTemp = QtWidgets.QLineEdit(self.gb_write)
        self.le_W_maxTemp.setGeometry(QtCore.QRect(250, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_W_maxTemp.setFont(font)
        self.le_W_maxTemp.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_W_maxTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.le_W_maxTemp.setReadOnly(False)
        self.le_W_maxTemp.setObjectName("le_W_maxTemp")
        self.lb_W_maxTemp = QtWidgets.QLabel(self.gb_write)
        self.lb_W_maxTemp.setGeometry(QtCore.QRect(20, 80, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_W_maxTemp.setFont(font)
        self.lb_W_maxTemp.setObjectName("lb_W_maxTemp")
        self.lb_W_current = QtWidgets.QLabel(self.gb_write)
        self.lb_W_current.setGeometry(QtCore.QRect(20, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_W_current.setFont(font)
        self.lb_W_current.setObjectName("lb_W_current")
        self.le_W_current = QtWidgets.QLineEdit(self.gb_write)
        self.le_W_current.setGeometry(QtCore.QRect(250, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_W_current.setFont(font)
        self.le_W_current.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_W_current.setAlignment(QtCore.Qt.AlignCenter)
        self.le_W_current.setReadOnly(False)
        self.le_W_current.setObjectName("le_W_current")
        self.lb_W_status = QtWidgets.QLabel(self.gb_write)
        self.lb_W_status.setGeometry(QtCore.QRect(20, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_W_status.setFont(font)
        self.lb_W_status.setObjectName("lb_W_status")
        self.le_W_status = QtWidgets.QLineEdit(self.gb_write)
        self.le_W_status.setGeometry(QtCore.QRect(250, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_W_status.setFont(font)
        self.le_W_status.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.le_W_status.setStyleSheet("background-color:rgb(232,232,232);")
        self.le_W_status.setAlignment(QtCore.Qt.AlignCenter)
        self.le_W_status.setReadOnly(True)
        self.le_W_status.setObjectName("le_W_status")
        self.btn_save = QtWidgets.QPushButton(self.gb_write)
        self.btn_save.setGeometry(QtCore.QRect(120, 270, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("background-color:lightgray")
        self.btn_save.setObjectName("btn_save")
        self.radioButton = QtWidgets.QRadioButton(self.gb_write)
        self.radioButton.setGeometry(QtCore.QRect(20, 180, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gb_write)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 180, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionADD_STAFF = QtWidgets.QAction(MainWindow)
        self.actionADD_STAFF.setObjectName("actionADD_STAFF")
        self.actionVIEW_DETAILS = QtWidgets.QAction(MainWindow)
        self.actionVIEW_DETAILS.setObjectName("actionVIEW_DETAILS")
        self.btn_open.clicked.connect(self.connectSerial)  # click event
        self.btn_save.clicked.connect(self.transferData) # click event

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration Utility"))
        self.gb_portSetting.setTitle(_translate("MainWindow", "Port Setting"))
        # ports = comports()  # comport configuration
        # if ports:  # if ports are available then it is displayed in combobox
        #     for port in ports:
        #         self.cb_comPort.addItem(port)
        # else:  # else you have virual port then 1 to 50 comport is displayed, you need to configure manually
        for i in range(1, 51):
            self.cb_comPort.addItem(f"COM{i}")
        self.gb_portSetting.setTitle(_translate("MainWindow", "Port Setting"))
        self.cb_burdRate.setItemText(0, _translate("MainWindow", "9600"))
        self.cb_burdRate.setItemText(1, _translate("MainWindow", "38400"))
        self.cb_burdRate.setItemText(2, _translate("MainWindow", "115200"))
        self.le_parity.setText(_translate("MainWindow", "NONE"))
        self.lb_comPort.setText(_translate("MainWindow", "Com port:"))
        self.le_stopBits.setText(_translate("MainWindow", "1"))
        self.lb_dataBits.setText(_translate("MainWindow", "Data bits:"))
        self.lb_flowControl.setText(_translate("MainWindow", "Flow Control:"))
        self.le_dataBits.setText(_translate("MainWindow", "8"))
        self.btn_open.setText(_translate("MainWindow", "Open"))
        self.le_flowControl.setText(_translate("MainWindow", "NONE"))
        self.lb_stopBits.setText(_translate("MainWindow", "Stop bits:"))
        self.lb_burdRate.setText(_translate("MainWindow", "Burdrate:"))
        self.lb_parity.setText(_translate("MainWindow", "Parity:"))
        self.gb_read.setTitle(_translate("MainWindow", "Read"))
        self.le_R_temprature.setText(_translate("MainWindow", "0"))
        self.lb_R_temprature.setText(_translate("MainWindow", "Temprature (৹C):"))
        self.lb_R_current.setText(_translate("MainWindow", "Current (A):"))
        self.lb_R_outputStatus.setText(_translate("MainWindow", "Output Status:"))
        self.le_R_current.setText(_translate("MainWindow", "0"))
        self.le_R_outputStatus.setText(_translate("MainWindow", "OFF"))
        self.gb_write.setTitle(_translate("MainWindow", "Write"))
        self.lb_W_minTemp.setText(_translate("MainWindow", "Minimum Temprature (৹C):"))
        self.le_W_minTemp.setText(_translate("MainWindow", "20"))
        self.le_W_maxTemp.setText(_translate("MainWindow", "50"))
        self.lb_W_maxTemp.setText(_translate("MainWindow", "Maximum Temprature (৹C):"))
        self.lb_W_current.setText(_translate("MainWindow", "Current (A):"))
        self.le_W_current.setText(_translate("MainWindow", "0"))
        self.lb_W_status.setText(_translate("MainWindow", "Status:"))
        self.le_W_status.setText(_translate("MainWindow", "NOT SAVED"))
        self.btn_save.setText(_translate("MainWindow", "SAVE"))
        self.radioButton.setText(_translate("MainWindow", "Enable"))
        self.radioButton_2.setText(_translate("MainWindow", "Disable"))
        self.actionADD_STAFF.setText(_translate("MainWindow", "ADD STAFF"))
        self.actionVIEW_DETAILS.setText(_translate("MainWindow", "VIEW DETAILS"))

    def connectSerial(self):  # here comport connectivity happens
        global ser
        var_comPort = self.cb_comPort.currentText()
        var_burdRate = self.cb_burdRate.currentText()
    
        try:
            if self.btn_open.text() == "Open":
                ser = serial.Serial(
                port=var_comPort,
                baudrate=var_burdRate,
                stopbits=serial.STOPBITS_ONE,
                parity=serial.PARITY_NONE,
                bytesize=serial.EIGHTBITS,
                timeout=1,
                xonxoff= False,
                rtscts= False,
                dsrdtr= False,
                write_timeout=2
                )
                ser.rtscts = False
                ser.dsrdtr = False
                self.btn_open.setText("Close")
                self.worker = WorkerThread()
                self.worker.start()
                self.worker.data.connect(self.getdata)
            else:
                self.worker.is_running = False
                ser.close()
                self.btn_open.setText("Open")
        except serial.serialutil.SerialException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Warning")
            msg.setText("Access Denied")
            msg.exec_()

    def temprature_validation(self):  # validation for invalid temprature and current value
        mintemp = self.le_W_minTemp.text()
        maxtemp = self.le_W_maxTemp.text()
        current = self.le_W_current.text()
        try:
            mintemp = int(mintemp)
            maxtemp = int(maxtemp)
            current = float(current)
            success = True
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Invalid temprature or current value")
            msg.exec_()
            mintemp = 0
            maxtemp = 0
            current = 0.0
            success = False
        if mintemp > maxtemp:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Invalid temprature value")
            msg.exec_()
            success = False
        else:
            if (mintemp < -10 or mintemp > 100) or (maxtemp < -10 or maxtemp > 100):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Warning")
                msg.setText("Minimun temprature: -10\nMaximum temprature: 100")
                msg.exec_()
                success = False
        
        return (mintemp, maxtemp, current, success)



    def transferData(self):  # here data is transfer from app to ardunio
        if self.btn_open.text() == "Close":
            mintemp, maxtemp, current, success = self.temprature_validation()
            if success:
                if self.radioButton.isChecked():
                    t_data = {"Enable":1,"current":current,"minT":mintemp,"maxT":maxtemp}
                else:
                    t_data = {"Enable":0,"current":current,"minT":mintemp,"maxT":maxtemp}
                t_data = json.dumps(t_data)
                ser.write(f"{t_data}\r\n".encode()) # data is transfer from app to ardunio
        else:  # else error is generated
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Error")
            msg.setText("Port is not opened")
            msg.exec_()
    
    def getdata(self, data): # get data from background worker
        self.le_R_temprature.setText(str(data['temp']))
        self.le_R_current.setText(str(data['curr']))
        if data['status'] == 1:
            self.le_R_outputStatus.setText("ON")
        else:
           self.le_R_outputStatus.setText("OFF")
        if data['wrt'] == 1:
            self.le_W_status.setText("SAVED")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("success")
            msg.setText("Data saved")
            msg.exec_()
        else:
            self.le_W_status.setText("NOT SAVED")
        
# background worker for reading and writing values
class WorkerThread(QThread):
    data = pyqtSignal(dict)
    
    def __init__(self):
        super(WorkerThread, self).__init__()
        self.is_running = True

    def run(self):
        while self.is_running:  # while port is open
            recive = ser.readline() # read values (json string) from the ardunio
            recive= str(recive,'utf-8')
            ind = recive.rfind('{')
            recive = recive[ind:]
            #{temp:50,curr:5,status:0,wrt:0}
            #test_sr = '{"temp": 20, "curr": 2, "status": 1, "wtr": 0}'
            if recive:
                recive_dict = json.loads(recive)
                # print(recive_dict)
                self.data.emit(recive_dict)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
