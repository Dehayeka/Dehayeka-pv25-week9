import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QInputDialog, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout
)

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog demo')
        self.setGeometry(100, 100, 400, 150)

        mainLayout = QHBoxLayout()

        buttonLayout = QVBoxLayout()
        self.btnList = QPushButton('Choose from list', self)
        self.btnList.clicked.connect(self.getList)

        self.btnText = QPushButton('get name', self)
        self.btnText.clicked.connect(self.getText)

        self.btnInt = QPushButton('Enter an integer', self)
        self.btnInt.clicked.connect(self.getInt)

        buttonLayout.addWidget(self.btnList)
        buttonLayout.addWidget(self.btnText)
        buttonLayout.addWidget(self.btnInt)

        textLayout = QVBoxLayout()
        self.listLine = QLineEdit(self)
        self.textLine = QLineEdit(self)
        self.intLine = QLineEdit(self)

        textLayout.addWidget(self.listLine)
        textLayout.addWidget(self.textLine)
        textLayout.addWidget(self.intLine)

        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(textLayout)

        self.setLayout(mainLayout)

    def getList(self):
        items = ("C", "C++", "Java", "Python", "JavaScript")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of languages", items, 0, False)
        if ok and item:
            self.listLine.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.textLine.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")
        if ok:
            self.intLine.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
