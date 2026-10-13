from PySide6.QtWidgets import (QMainWindow, QStatusBar, QApplication, QMenu, QToolBar, QPushButton,
                               QWidget, QVBoxLayout, QDialog)

from PySide6.QtGui import QAction

class App(QMainWindow):

    def afficher_message_menu1(self):
        self.barre_statut.setStatusTip("Menu 1")

    def afficher_message_menu2(self):
        self.barre_statut.setStatusTip("Menu 2")

    @staticmethod
    def bouton_appuye():
        print("Click!")

    def ouvrir_dialogue(self):
        #Création du dialogue
        self.dialogue = QDialog(self)
        self.dialogue.setWindowTitle("Mon dialogue")
        layout_dialogue = QVBoxLayout()
        #Bouton pour fermer
        bouton_fermer = QPushButton("Fermer")
        bouton_fermer.clicked.connect(self.dialogue.close)
        #Afficher le dialogue
        layout_dialogue.addWidget(bouton_fermer)
        self.dialogue.setLayout(layout_dialogue)
        self.dialogue.exec()

    def __init__(self):
        super().__init__()

        #titre
        self.setWindowTitle("Mon application")

        #Barre de statut
        self.barre_statut = QStatusBar(self)
        self.setStatusBar(self.barre_statut)

        #Menu 1
        self.menu1 = QMenu("&Menu1")
        self.action_menu1 = QAction("Item Menu1")
        self.menu1.addAction(self.action_menu1)
        self.menu1.triggered.connect(self.afficher_message_menu1)

        #Menu 2
        self.menu2 = QMenu("&Menu2")
        self.action_menu2 = QAction("Item Menu2")
        self.menu2.addAction(self.action_menu2)
        self.menu2.triggered.connect(self.afficher_message_menu2)

        #Ajout des menus à la barre de menu
        self.barre_menu = self.menuBar()
        self.barre_menu.addMenu(self.menu1)
        self.barre_menu.addMenu(self.menu2)

        #Barre d'outils
        self.barre_outils = QToolBar()
        bouton_outils = QPushButton("Bouton")
        #Print click
        bouton_outils.clicked.connect(self.bouton_appuye)
        self.barre_outils.addWidget(bouton_outils)
        self.addToolBar(self.barre_outils)

        #widget central
        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)
        #QVBoxLayout
        self.layout_principal = QVBoxLayout()
        self.widget_central.setLayout(self.layout_principal)
        #Bouton qui ouvre le dialogue
        self.bouton_dialogue = QPushButton("Ouvrir le dialogue")
        self.bouton_dialogue.clicked.connect(self.ouvrir_dialogue)
        self.layout_principal.addWidget(self.bouton_dialogue)


app = QApplication()
base_ui = App()
base_ui.show()
app.exec()