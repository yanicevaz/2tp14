from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QTextEdit, QCheckBox
app = QApplication([])
mainWidget = QWidget()


layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
text = QTextEdit("Entrez votre texte")
check = QCheckBox("J'accepte les conditions d'utilisation.")

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(text)
layout.addWidget(check)

mainWidget.setLayout(layout)


mainWidget.show()
app.exec_()
