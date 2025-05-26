import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QSlider,
    QCheckBox, QPushButton, QVBoxLayout, QListWidget, QMenuBar,
    QAction, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

class RentalCameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RasaRental")
        self.setGeometry(300, 150, 600, 800)
        self.setStyleSheet("background-color: #F1EDEC; color: #4A4A4A;")
        self.setupUI()

    def setupUI(self):
        self.logoLabel = QLabel()
        pixmap = QPixmap("dark.png")
        self.logoLabel.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.nameLabel = QLabel("Nama Penyewa:")
        self.nameLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.nameInput = QLineEdit()
        self.nameInput.setPlaceholderText("Masukkan nama penyewa")
        self.nameInput.setStyleSheet("""
            padding: 5px; 
            border-radius: 5px; 
            border: 1px solid #EED8C7;
            background-color: #FFFFFF;
            color: #4A4A4A;
        """)

        self.itemTypeLabel = QLabel("Jenis Sewa:")
        self.itemTypeLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.itemTypeCombo = QComboBox()
        self.itemTypeCombo.addItems(["Kamera", "Lensa", "Kamera dan Lensa"])
        self.itemTypeCombo.setStyleSheet("""
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #EED8C7;
            background-color: #FFFFFF;
            color: #4A4A4A;
        """)
        self.itemTypeCombo.currentIndexChanged.connect(self.updateItemList)

        self.cameraLabel = QLabel("Pilih Kamera:")
        self.cameraLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.cameraCombo = QComboBox()
        self.cameraCombo.addItems(["-", "Sony A7 III", "Sony A6400", "Sony A9", "Sony A7R IV", "Sony A7S III", "Sony ZV-1", "Sony FX3", "Sony RX100 VII"])
        self.cameraCombo.setStyleSheet("""
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #EED8C7;
            background-color: #FFFFFF;
            color: #4A4A4A;
        """)

        self.lensLabel = QLabel("Pilih Lensa:")
        self.lensLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.lensCombo = QComboBox()
        self.lensCombo.addItems(["-", "Sony 24-70mm f/2.8", "Sony 50mm f/1.8", "Sony 70-200mm f/2.8", "Sony 16-35mm f/2.8", "Sony 85mm f/1.4", "Sony 100-400mm f/4.5-5.6"])
        self.lensCombo.setStyleSheet("""
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #EED8C7;
            background-color: #FFFFFF;
            color: #4A4A4A;
        """)

        self.daysLabel = QLabel("Lama Sewa (hari):")
        self.daysLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.daysSlider = QSlider(Qt.Horizontal)
        self.daysSlider.setMinimum(1)
        self.daysSlider.setMaximum(30)
        self.daysSlider.setValue(1)
        self.daysSlider.setTickInterval(1)
        self.daysSlider.setTickPosition(QSlider.TicksBelow)
        self.daysSlider.valueChanged.connect(self.updateDaysLabel)

        self.daysValueLabel = QLabel("1 hari")

        self.batteryLabel = QLabel("Jumlah Baterai Kamera:")
        self.batteryLabel.setFont(QFont('Arial', 12, QFont.Bold))
        self.batterySlider = QSlider(Qt.Horizontal)
        self.batterySlider.setMinimum(1)
        self.batterySlider.setMaximum(5)
        self.batterySlider.setValue(1)
        self.batterySlider.setTickInterval(1)
        self.batterySlider.setTickPosition(QSlider.TicksBelow)
        self.batterySlider.valueChanged.connect(self.updateBatteryLabel)

        self.batteryValueLabel = QLabel("1 Baterai")

        self.rentButton = QPushButton("Sewa Sekarang")
        self.rentButton.setStyleSheet("""
            background-color: #F36259;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        """)
        self.rentButton.clicked.connect(self.processRental)

        self.rentalList = QListWidget()
        self.rentalList.setStyleSheet("""
            background-color: #FFFFFF;
            border-radius: 5px;
            padding: 5px;
            color: #4A4A4A;
        """)

        self.footerLabel = QLabel("NIM: F1D022105 | Nama: Adhyatmika Eka Saputra")
        self.footerLabel.setAlignment(Qt.AlignCenter)
        self.footerLabel.setStyleSheet("font-size: 10pt; color: #4A4A4A;")

        layout = QVBoxLayout()
        formLayout = QVBoxLayout()

        layout.addWidget(self.logoLabel)
        formLayout.addWidget(self.nameLabel)
        formLayout.addWidget(self.nameInput)
        formLayout.addWidget(self.itemTypeLabel)
        formLayout.addWidget(self.itemTypeCombo)
        formLayout.addWidget(self.cameraLabel)
        formLayout.addWidget(self.cameraCombo)
        formLayout.addWidget(self.lensLabel)
        formLayout.addWidget(self.lensCombo)
        formLayout.addWidget(self.daysLabel)
        formLayout.addWidget(self.daysSlider)
        formLayout.addWidget(self.daysValueLabel)
        formLayout.addWidget(self.batteryLabel)
        formLayout.addWidget(self.batterySlider)
        formLayout.addWidget(self.batteryValueLabel)
        formLayout.addWidget(self.rentButton)

        layout.addLayout(formLayout)
        layout.addWidget(self.rentalList)
        layout.addWidget(self.footerLabel)

        self.setLayout(layout)

        self.menuBar = QMenuBar(self)
        fileMenu = self.menuBar.addMenu("")

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(self.showAboutDialog)
        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.closeApp)

        fileMenu.addAction(aboutAction)
        fileMenu.addAction(exitAction)

        layout.setMenuBar(self.menuBar)

    def updateItemList(self):
        itemType = self.itemTypeCombo.currentText()
        if itemType == "Kamera":
            self.cameraCombo.setEnabled(True)
            self.lensCombo.setEnabled(False)
        elif itemType == "Lensa":
            self.cameraCombo.setEnabled(False)
            self.lensCombo.setEnabled(True)
        else:
            self.cameraCombo.setEnabled(True)
            self.lensCombo.setEnabled(True)

    def updateDaysLabel(self):
        days = self.daysSlider.value()
        self.daysValueLabel.setText(f"{days} hari")

    def updateBatteryLabel(self):
        numBatteries = self.batterySlider.value()
        self.batteryValueLabel.setText(f"{numBatteries} Baterai")

    def processRental(self):
        name = self.nameInput.text()
        itemType = self.itemTypeCombo.currentText()
        camera = self.cameraCombo.currentText()
        lens = self.lensCombo.currentText()
        days = self.daysSlider.value()
        numBatteries = self.batterySlider.value()

        if name == "":
            QMessageBox.warning(self, "Peringatan", "Nama penyewa harus diisi!")
            return

        camera_prices = {
            "Sony A7 III": 200000,
            "Sony A6400": 150000,
            "Sony A9": 250000,
            "Sony A7R IV": 300000,
            "Sony A7S III": 280000,
            "Sony ZV-1": 150000,
            "Sony FX3": 350000,
            "Sony RX100 VII": 180000
        }

        lens_prices = {
            "Sony 24-70mm f/2.8": 80000,
            "Sony 50mm f/1.8": 50000,
            "Sony 70-200mm f/2.8": 90000,
            "Sony 16-35mm f/2.8": 100000,
            "Sony 85mm f/1.4": 120000,
            "Sony 100-400mm f/4.5-5.6": 150000
        }

        total_price = 0
        rental_info = f"{name} - {days} hari"

        if camera != "-":
            total_price += camera_prices.get(camera, 0) * days
            rental_info += f" | Kamera: {camera}"

        if lens != "-":
            total_price += lens_prices.get(lens, 0) * days
            rental_info += f" | Lensa: {lens}"

        if numBatteries > 1:
            total_price += (numBatteries - 1) * 10000
            rental_info += f" | Baterai: {numBatteries} (Tambahan Rp{(numBatteries - 1) * 10000:,})"
        else:
            rental_info += f" | Baterai: {numBatteries} (Gratis)"

        rental_info += f" | Total: Rp{total_price:,}"
        self.rentalList.addItem(rental_info)

        self.nameInput.clear()
        self.cameraCombo.setCurrentIndex(0)
        self.lensCombo.setCurrentIndex(0)
        self.daysSlider.setValue(1)
        self.batterySlider.setValue(1)

        self.updateDaysLabel()

    def showAboutDialog(self):
        QMessageBox.information(self, "Tentang Aplikasi", "Aplikasi Rental Kamera & Lensa")

    def closeApp(self):
        confirm = QMessageBox.question(self, "Keluar", "Yakin mau keluar?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RentalCameraApp()
    window.show()
    sys.exit(app.exec_())
