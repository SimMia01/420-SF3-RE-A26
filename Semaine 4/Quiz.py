from PySide6.QtWidgets import (QRadioButton, QCheckBox, QComboBox, QLineEdit,
                               QProgressBar, QMessageBox, QPushButton, QFrame, QApplication,
                               QVBoxLayout, QLabel, QHBoxLayout, QButtonGroup)

class Quiz(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        #Pour la barre de progression (si question rep: True)
        self.questions_repondues = [False, False, False, False, False]

        #Question 1 (QRadioButton)
        q1 = QLabel("Capitale du Canada")
        dispo_q1 = QVBoxLayout()
        dispo_q1.addWidget(q1)
        dispo_repq1 = QHBoxLayout()
        self.bouton_radio1 = QRadioButton("Toronto")
        self.bouton_radio2 = QRadioButton("Ottawa")
        self.bouton_radio3 = QRadioButton("Vancouver")
        self.groupe1 = QButtonGroup()
        self.groupe1.addButton(self.bouton_radio1)
        self.groupe1.addButton(self.bouton_radio2)
        self.groupe1.addButton(self.bouton_radio3)
        self.groupe1.buttonClicked.connect(self.q1_repondue)
        dispo_repq1.addWidget(self.bouton_radio1)
        dispo_repq1.addWidget(self.bouton_radio2)
        dispo_repq1.addWidget(self.bouton_radio3)
        dispo_q1.addLayout(dispo_repq1)
        disposition.addLayout(dispo_q1)

        #Qestion 2 (QCheckBox)
        q2 = QLabel("Sélectionnez le(s) chiffre(s) paire(s)")
        dispo_q2 = QVBoxLayout()
        dispo_q2.addWidget(q2)
        dispo_repq2 = QHBoxLayout()
        self.check_1 = QCheckBox("9846531")
        self.check_2 = QCheckBox("417586")
        self.check_3 = QCheckBox("98675412")
        self.groupe2 = QButtonGroup()
        self.groupe2.addButton(self.check_1)
        self.groupe2.addButton(self.check_2)
        self.groupe2.addButton(self.check_3)
        self.groupe2.buttonClicked.connect(self.q2_repondue)
        self.groupe2.setExclusive(False)
        dispo_repq2.addWidget(self.check_1)
        dispo_repq2.addWidget(self.check_2)
        dispo_repq2.addWidget(self.check_3)
        dispo_q2.addLayout(dispo_repq2)
        disposition.addLayout(dispo_q2)

        #Question 3 (QComboBox)
        q3 = QLabel("À quelle famille appartient le chat?")
        dispo_q3 = QVBoxLayout()
        dispo_q3.addWidget(q3)
        self.combobox = QComboBox()
        self.combobox.addItem("Canins")
        self.combobox.addItem("Félins")
        self.combobox.addItem("Bovins")
        self.combobox.currentIndexChanged.connect(self.q3_repondue)
        dispo_q3.addWidget(self.combobox)
        disposition.addLayout(dispo_q3)

        #Question 4 (QLineEdit)
        q4 = QLabel("Que donne 16 * 34")
        dispo_q4 = QVBoxLayout()
        dispo_q4.addWidget(q4)
        self.line_edit = QLineEdit("")
        dispo_q4.addWidget(self.line_edit)
        self.line_edit.editingFinished.connect(self.q4_repondue)
        disposition.addLayout(dispo_q4)

        #QProgressBar
        self.barre_progres = QProgressBar()
        disposition.addWidget(self.barre_progres)
        self.barre_progres.setMaximum(4)
        self.barre_progres.setValue(0)

        #Valider les réponses
        valider = QPushButton("Valider les réponses")
        disposition.addWidget(valider)
        valider.clicked.connect(self.valider_rep)

    def q1_repondue(self):
        if not self.questions_repondues[0]:
            self.questions_repondues[0] = True
            self.barre_progres.setValue(self.barre_progres.value()+1)

    def q2_repondue(self):
        if not self.questions_repondues[1]:
            self.questions_repondues[1] = True
            self.barre_progres.setValue(self.barre_progres.value() + 1)

    def q3_repondue(self):
        if not self.questions_repondues[2]:
            self.questions_repondues[2] = True
            self.barre_progres.setValue(self.barre_progres.value()+1)

    def q4_repondue(self):
        if not self.questions_repondues[4]:
            self.questions_repondues[4] = True
            self.barre_progres.setValue(self.barre_progres.value() + 1)

    def valider_rep(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Résultats")
        resultats = "Résultats:\n"
        if self.bouton_radio2.isChecked():
            resultats += "\nQuestion 1: Correct\n"
        else:
            resultats += "\nQuestion 1: Incorrect\n"
        if self.check_2.isChecked() and self.check_3.isChecked():
            resultats += "\nQuestion 2: Correct\n"
        else:
            resultats += "\nQuestion 2: Incorrect\n"
        if self.combobox.currentText() == "Félins":
            resultats += "\nQuestion 3: Correct\n"
        else:
            resultats += "\nQuestion 3: Incorrect\n"
        if self.line_edit.text() == str(16 * 34):
            resultats += "\nQuestion 4: Correct\n"
        else:
            resultats += "\nQuestion 4: Incorrect\n"
        dialog.setText(resultats)
        dialog.exec()

app = QApplication()
quiz = Quiz()
quiz.show()
app.exec()
