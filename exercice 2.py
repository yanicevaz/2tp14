from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QTextEdit, QCheckBox, QGridLayout

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.layout = QVBoxLayout()
        self.gridlayout = QGridLayout()

        self.label = QLabel("Laissez un commentaire")
        self.text = QTextEdit()
        self.validerbutton = QPushButton("Success")
        self.annulerbutton= QPushButton("Cancel")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.gridlayout.addWidget(self.validerbutton,0,0)
        self.gridlayout.addWidget(self.annulerbutton,0,1)

        self.layout.addLayout(self.gridlayout)
        self.setLayout(self.layout)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()

