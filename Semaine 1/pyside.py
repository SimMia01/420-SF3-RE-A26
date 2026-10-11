import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QVBoxLayout, QWidget
from random import choice


class FenetrePrincipale(QMainWindow):
    label_equations = [
        "a^2 + b^2 = c^2",
        "ln(xy) = ln(x) + ln(y)",
        "i^2 = 1",
        "E = mc^2"
    ]
    def handle_button_ok(self):
        #output vers la console
        print("Click")
        #Changer le texte du label
        self.label.setText(choice(self.label_equations))

    def __init__(self):
        super().__init__()

        #Création du label
        self.label = QLabel()
        self.label.setText("Cliquez pour une équation")

        #Boutton fermer
        bouton_fermer = QPushButton("Fermer")
        #Fermer l'app si bouton cliqué
        bouton_fermer.pressed.connect(self.close)
        self.setCentralWidget(bouton_fermer)

        #Boutton changer
        self.bouton_changer = QPushButton("Changer")
        self.bouton_changer.pressed.connect(self.handle_button_ok)

        #QVBoxLayout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.bouton_changer)
        main_container = QWidget()
        main_container.setLayout(main_layout)
        self.setCentralWidget(main_container)

        self.show()

#Création de l'app
app = QApplication(sys.argv)
#Création de la fenetre
w = FenetrePrincipale()
#Execution
app.exec()