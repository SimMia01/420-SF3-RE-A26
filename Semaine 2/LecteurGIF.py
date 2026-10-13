from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QMenu, QMenuBar, QToolBar
from PySide6.QtGui import QAction, QIcon, QMovie, QKeySequence

class LecteurGIF(QMainWindow):

    def jouer(self):
        self.animation.start()

    def stop(self):
        self.animation.stop()

    def __init__(self):
        super().__init__()

        #titre
        self.setWindowTitle("Lecteur de GIFs")

        #QAction jouer
        action_jouer = QAction(QIcon("jouer.png"), "Jouer", self)
        action_jouer.triggered.connect(self.jouer)

        #QAction stop
        action_stop = QAction(QIcon("stop.png"), "Stop", self)
        action_stop.triggered.connect(self.stop)

        #QAction quitter
        action_quitter = QAction("Quitter", self)
        action_quitter.setText("&Quitter")
        #Ajout d'un raccourci clavier
        action_quitter.setShortcut(QKeySequence("Ctrl+Q"))
        action_quitter.triggered.connect(self.close)

        #Ajout d'un QLabel à la fenêtre
        disposition = QVBoxLayout()
        etiquette = QLabel()
        disposition.addWidget(etiquette)
        widget_central = QWidget()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        #Initialisation du QMovie
        self.animation = QMovie("sup.gif")
        etiquette.setMovie(self.animation)
        self.animation.start()

        #Ajout d'un menu
        barre_menu = QMenuBar()
        menu = QMenu("&Contrôles")
        menu.addAction(action_jouer)
        menu.addAction(action_stop)
        #Ajout d'un séparateur entre les actions
        menu.addSeparator()
        menu.addAction(action_quitter)

        barre_menu.addMenu(menu)
        self.setMenuBar(barre_menu)

        #Ajout d'une barre d'outils avec les 2 actions
        barre_outils = QToolBar("Barre d'outils")
        barre_outils.addAction(action_jouer)
        barre_outils.addAction(action_stop)
        self.addToolBar(barre_outils)


app = QApplication()
lecteur = LecteurGIF()
lecteur.show()
app.exec()