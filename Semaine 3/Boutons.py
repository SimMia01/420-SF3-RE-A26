from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QPushButton

class Boutons(QFrame):

    def italique(self, etat):
        if etat:
            self.texte.setStyleSheet("font-style: italic;")
        else:
            self.texte.setStyleSheet("font-style: normal;")

    def gras(self, etat):
        if etat:
            self.texte.setStyleSheet("font-weight: bold;")
        else:
            self.texte.setStyleSheet("font-weight: normal;")

    def wordwrap(self, etat):
        self.texte.setWordWrap(etat)

    def augmenter(self):
        police = self.texte.font()
        taille = police.pointSize()
        police.setPointSize(taille + 1)
        self.texte.setFont(police)

    def diminuer(self):
        police = self.texte.font()
        taille = police.pointSize()
        if taille > 1:
            police.setPointSize(taille - 1)
            self.texte.setFont(police)

    def activer_desactiver(self, etat):
        if etat:
            self.texte.setStyleSheet("font-style: italic;")
            self.texte.setStyleSheet("font-weight: bold;")
            self.texte.setWordWrap(etat)
        else:
            self.texte.setStyleSheet("font-style: normal;")
            self.texte.setStyleSheet("font-weight: normal;")
            self.texte.setWordWrap(etat)

    @staticmethod
    def output():
        print("Click!")

    def __init__(self):
        super().__init__()

        #VBoxLayout
        disposition = QVBoxLayout()
        self.setLayout(disposition)

        #QLabel avec texte
        self.texte = QLabel("L'informatique, ça fait gagner beaucoup de temps...à condition d'en avoir beaucoup devant soi!")
        disposition.addWidget(self.texte)

        #Bouton qui met le texte en italique
        self.bouton_italique = QPushButton("Italique")
        self.bouton_italique.setCheckable(True)
        self.bouton_italique.toggled.connect(self.italique)
        self.bouton_italique.toggled.connect(self.output)
        disposition.addWidget(self.bouton_italique)

        #Bouton texte en gras
        self.bouton_gras = QPushButton("Gras")
        self.bouton_gras.setCheckable(True)
        self.bouton_gras.toggled.connect(self.gras)
        disposition.addWidget(self.bouton_gras)

        #Bouton wordwrap
        self.bouton_ww = QPushButton("Word Wrap")
        self.bouton_ww.setCheckable(True)
        self.bouton_ww.toggled.connect(self.wordwrap)
        disposition.addWidget(self.bouton_ww)

        #Bouton augmenter police
        self.bouton_aug = QPushButton("Augmenter la police")
        self.bouton_aug.clicked.connect(self.augmenter)
        disposition.addWidget(self.bouton_aug)

        #Bouton diminuer police
        self.bouton_dim = QPushButton("Diminuer la police")
        self.bouton_dim.clicked.connect(self.diminuer)
        disposition.addWidget(self.bouton_dim)

        #Bouton qui active/désactive tout
        self.bouton_activer = QPushButton("Activer/Désactiver tous les boutons")
        self.bouton_activer.setCheckable(True)
        self.bouton_activer.toggled.connect(self.activer_desactiver)
        disposition.addWidget(self.bouton_activer)



app = QApplication()
ex2 = Boutons()
ex2.show()
app.exec()