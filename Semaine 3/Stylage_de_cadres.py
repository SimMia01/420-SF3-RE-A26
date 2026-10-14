from PySide6.QtWidgets import QApplication, QFrame, QMenu, QLabel, QVBoxLayout
from PySide6.QtGui import QFont, QPixmap

class Stylage(QFrame):

    def __init__(self):
        super().__init__()

        #Titre
        self.setWindowTitle("Stylage de cadres")

        #Barre de menu à ajouter, car QFrame au lieu de QMainWindow
        disposition =QVBoxLayout()
        self.setLayout(disposition)

        #QMenu avec 2 QAction
        self.menu = QMenu("Menu")
        action_quitter = self.menu.addAction("Quitter")
        action_quitter.triggered.connect(self.close)
        action_renomer = self.menu.addAction("Renommer")
        action_renomer.triggered.connect(lambda : self.setWindowTitle("Titre modifié"))

        #QLabel avec texte riche (en HTML)
        texte_riche = QLabel()
        texte_riche.setText(
            "<h1><b>Titre</b></h1>"
            "<h2 style='color:blue;'>Sous-titre</h2>"
            "<p><i>Autre paragraphe</i></p>"
            "<p>Peux ajouter des liens: <a href='https://www.w3schools.com/Html/default.asp'>Tutoriel HTML </a></p>"
        )
        disposition.addWidget(texte_riche)

        #QLabel avec texte riche (appliqué pour tout le texte)
        texte_riche2 = QLabel()
        texte_riche2.setText("Texte riche")
        police = QFont()
        police.setBold(True)
        police.setItalic(True)
        police.setPointSize(30) #Taille de l'écriture
        texte_riche2.setFont(police)
        disposition.addWidget(texte_riche2)

        #QLabel avec image
        etiquette_image = QLabel()
        image = QPixmap("./ex1.png")
        etiquette_image.setPixmap(image)
        etiquette_image.setFrameShadow(QFrame.Shadow.Raised) #Raised, plain ou sunken
        disposition.addWidget(etiquette_image)


app = QApplication()
ex1 = Stylage()
ex1.show()
app.exec()