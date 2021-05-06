# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QDialog, QTableWidgetItem

# importamos la libreria zeep para implementar el servicio SOAP
from zeep import Client
# importamos base64
import base64
import geocoder


class Ui_MainWindow(QDialog):
    #url = "http://localhost:7000/ws/SOAPService?wsdl"
    url = "https://astrocaribbean.tech/ws/SOAPService?wsdl"
    # definimos nuestro cliente con la URL
    client = Client(url)

    def __init__(self):
        super().__init__()
        self.imagePath = None
        self.form = {

        }
        self.user = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1426, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(450, 220, 361, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 1421, 31))
        self.header.setStyleSheet("background-color: rgb(255, 249, 238)")
        self.header.setText("")
        self.header.setObjectName("header")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 1421, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 460, 1421, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.txtSector = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSector.setGeometry(QtCore.QRect(450, 270, 361, 22))
        self.txtSector.setObjectName("txtSector")
        self.cbxNivelAcademico = QtWidgets.QComboBox(self.centralwidget)
        self.cbxNivelAcademico.setGeometry(QtCore.QRect(450, 320, 361, 31))
        self.cbxNivelAcademico.setObjectName("cbxNivelAcademico")
        self.cbxNivelAcademico.addItem("")
        self.cbxNivelAcademico.addItem("")
        self.cbxNivelAcademico.addItem("")
        self.cbxNivelAcademico.addItem("")
        self.cbxNivelAcademico.addItem("")
        self.cbxNivelAcademico.addItem("")
        self.btnEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnviar.setGeometry(QtCore.QRect(450, 380, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEnviar.setFont(font)
        self.btnEnviar.setObjectName("btnEnviar")
        self.btnEnviar.clicked.connect(self.saveForm)
        self.tbForms = QtWidgets.QTableWidget(self.centralwidget)
        self.tbForms.setGeometry(QtCore.QRect(300, 550, 795, 271))
        self.tbForms.setColumnCount(5)
        self.tbForms.setObjectName("tbForms")
        self.tbForms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbForms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbForms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbForms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbForms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbForms.setHorizontalHeaderItem(4, item)
        self.tbForms.horizontalHeader().setCascadingSectionResizes(False)
        self.tbForms.horizontalHeader().setDefaultSectionSize(154)
        self.tbForms.horizontalHeader().setMinimumSectionSize(49)
        self.tbForms.horizontalHeader().setSortIndicatorShown(False)
        self.tbForms.horizontalHeader().setStretchLastSection(False)
        # self.tbForms.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 500, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtFoto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFoto.setEnabled(False)
        self.txtFoto.setGeometry(QtCore.QRect(450, 160, 271, 22))
        self.txtFoto.setObjectName("txtFoto")
        self.btnFoto = QtWidgets.QPushButton(self.centralwidget)
        self.btnFoto.setGeometry(QtCore.QRect(730, 160, 93, 28))
        self.btnFoto.setObjectName("btnFoto")
        self.btnFoto.clicked.connect(self.selectFile)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(1310, 0, 93, 28))
        self.btnSalir.setObjectName("btnSalir")
        self.btnSalir.clicked.connect(self.exit)
        self.lbuser = QtWidgets.QLabel(self.centralwidget)
        self.lbuser.setGeometry(QtCore.QRect(1020, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbuser.setFont(font)
        self.lbuser.setText(self.user.username)
        self.lbuser.setObjectName("lbuser")
        self.lbFoto = QtWidgets.QLabel(self.centralwidget)
        self.lbFoto.setGeometry(QtCore.QRect(140, 200, 251, 181))
        self.lbFoto.setText("")
        self.lbFoto.setObjectName("lbFoto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setTable()
        self.getLocation()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Formularios"))
        self.txtNombre.setPlaceholderText(_translate("MainWindow", "Nombre completo"))
        self.label.setText(_translate("MainWindow", "Formulario de registro"))
        self.txtSector.setPlaceholderText(_translate("MainWindow", "Sector"))
        self.cbxNivelAcademico.setCurrentText(_translate("MainWindow", "Nivel Academico"))
        self.cbxNivelAcademico.setItemText(0, _translate("MainWindow", "Nivel Academico"))
        self.cbxNivelAcademico.setItemText(1, _translate("MainWindow", "Basico"))
        self.cbxNivelAcademico.setItemText(2, _translate("MainWindow", "Medio"))
        self.cbxNivelAcademico.setItemText(3, _translate("MainWindow", "Grado"))
        self.cbxNivelAcademico.setItemText(4, _translate("MainWindow", "Maestria"))
        self.cbxNivelAcademico.setItemText(5, _translate("MainWindow", "Doctorado"))
        self.btnEnviar.setText(_translate("MainWindow", "Enviar"))
        item = self.tbForms.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Foto"))
        item = self.tbForms.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tbForms.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sector"))
        item = self.tbForms.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nivel Academico"))
        item = self.tbForms.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Formularios en registrados"))
        self.label_3.setText(_translate("MainWindow", "Subir foto"))
        self.btnFoto.setText(_translate("MainWindow", "Seleccionar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))

    def selectFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image files (*.jpg *.png *.gif *jpeg)')
        self.imagePath = fileName[0]
        pixMap = QPixmap(self.imagePath)
        pixmap5 = pixMap.scaled(200, 200)
        self.lbFoto.setPixmap(QPixmap(pixmap5))
        self.txtFoto.setText(self.imagePath)

    def translateimage(self, b64_data):
        b64 = b64_data.replace("data:image/jpeg;base64,/9j/", "")
        b64 = b64_data.replace("data:image/jpeg;base64,", "")
        b64_data2 = b64.replace(" ", "+")
        imageLabel = QtWidgets.QLabel(self.centralwidget)
        imageLabel.setText("")
        imageLabel.setScaledContents(True)

        imgdata = base64.b64decode(b64_data2)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
            pixmap = QPixmap('some_image.jpg')
            pixmap5 = pixmap.scaled(200, 200)
            imageLabel.setPixmap(pixmap5)
        return imageLabel

    def setTable(self):
        self.tbForms.clearContents()
        self.tbForms.setRowCount(0)
        ind = 0
        forms = self.client.service.findAll()

        for aux in range(0, len(forms)):

            rowPosition = self.tbForms.rowCount()
            self.tbForms.insertRow(rowPosition)
            # Foto
            if forms[ind].photo.fotoBase64 == None or forms[ind].photo.fotoBase64 == 'No':
                self.tbForms.setItem(rowPosition, 0, QTableWidgetItem("No tiene foto"))
            else:
                item = self.translateimage(forms[ind].photo.fotoBase64)
                self.tbForms.setCellWidget(rowPosition, 0, item)
                # QTableWidgetItem(self.translateimage(forms[ind].photo.fotoBase64))
            # Nombre
            self.tbForms.setItem(rowPosition, 1, QTableWidgetItem(forms[ind].name))
            # Sector
            self.tbForms.setItem(rowPosition, 2, QTableWidgetItem(forms[ind].sector))
            # Nivel
            self.tbForms.setItem(rowPosition, 3, QTableWidgetItem(forms[ind].academicLevel))
            # Usuario
            self.tbForms.setItem(rowPosition, 4, QTableWidgetItem(forms[ind].user.username))
            ind += 1
        lat, lon = self.getLocation()
        print(lat, lon)

    def saveForm(self):
        if self.txtNombre.text() != "" and self.txtSector.text() != "" and self.cbxNivelAcademico.currentText() != "Nivel Academico":
            if self.imagePath is None:
                photo = {
                    'fotoBase64': 'No'
                }
            else:
                photo = {
                    'fotoBase64': self.encodeBase64(self.imagePath)
                }

            lat, lon = self.getLocation()
            Location = {
                'longitude': lon,
                'latitude': lat
            }
            print(Location)
            form = {
                'id': '',
                'name': self.txtNombre.text(),
                'sector': self.txtSector.text(),
                'academicLevel': self.cbxNivelAcademico.currentText(),
                'photo': photo,
                'user': self.user,
                'location': Location
            }
            self.client.service.create(form)
            self.clear()
            self.setTable()

        else:
            error = QtWidgets.QErrorMessage()
            error.setWindowModality(QtCore.Qt.WindowModal)
            error.showMessage("Asegurese de que llene todas las informaciones correspondientes")
            error.setWindowTitle("Error")
            error.exec_()

    def encodeBase64(self, image_path):

        image = open(image_path, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)  # encodestring also works aswell as decodestring
        imagen = "data:image/jpeg;base64,"
        imagen += image_64_encode.decode("utf-8")
        print(image_64_encode.decode("utf-8"))
        return imagen

    def getLocation(self):
        myloc = geocoder.ip('me')
        return myloc.lng, myloc.lat

    def exit(self):
        QDialog.close()

    def clear(self):
        self.txtFoto.clear()
        self.txtSector.clear()
        self.txtNombre.clear()
        self.cbxNivelAcademico.setCurrentIndex(0)
        self.lbFoto.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
