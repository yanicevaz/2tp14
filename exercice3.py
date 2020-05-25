from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("Charging...")

        icone = QIcon("C:\Desktop\drapeau-fr.png")
        layout = QGridLayout()
        label = QLabel("Hello World")
        progressBar = QProgressBar()
        lineEdit = QLineEdit()
        button = QPushButton("Click me !")

        layout.addWidget(label)
        layout.addWidget(progressBar)
        layout.addWidget(lineEdit)
        layout.addWidget(button)

        progressBar.setValue(50)
        self.setWindowIcon(icone)
        label.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

if __name__ == "__main__":
   app = QApplication([])
   window = Window()
   window.show()
   app.exec_()
