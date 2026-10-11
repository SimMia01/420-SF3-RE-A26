from tkinter import Tk, Button, Label
from random import choice

class Window(Tk):

    #Fermer la fenetre quand on clique sur le bouton
    def handle_button_press(self):
        self.destroy()

    #Ajouter les citations à la liste
    def read_citations(self):
        with open('citations.txt', 'r', encoding="utf-8") as reader:
            for ligne in reader:
                self.citations.append(ligne)

    #Ajouter les \n à chaque 3 mots et avant l'auteur
    def format(self, citation):
        split = citation.split()
        resultat = ""
        i = 1
        for mot in split:
            #Avant l'auteur
            if mot.startwith("-"):
                resultat += "\n" + mot
            else:
                resultat += mot
                #\n tout les 3 mots:
                if i % 3 == 0:
                    resultat += "\n"
            resultat += " "
            i += 1
        return resultat

    def __init__(self):
        super().__init__()
        self.citations = []
        self.read_citations()

        #Titre
        self.title("Sagesse")
        #Label (texte)
        #1.   self.label = Label(text="Ils ne sont grands que parce que nous sommes à genoux\n -La Boétie")
        x = choice(self.citations) #Éviter les bugs
        self.label = Label(text=self.format(x))
        self.label.pack()
        #Boutton pour fermer
        self.button = Button(text="Fermer", command=self.handle_button_press)
        self.button.pack()

#Création de la fenetre
window = Window()
#Boucle principale
window.mainloop()