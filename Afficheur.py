from tkinter import *

# Créer une premiere fenetre
window = Tk()

#Personnalisation de la fenetre
window.title("Pronostique Atanbatlex")
window.geometry("1080x720")
window.minsize(720, 480)
window.iconbitmap("Icon.ico")


# ajouter du texte
label_title = Label(window, text="Bienvenue sur notre application de pronostique sur la ligue 1", font=("Bauhaus 93", 35))
label_title.pack(expand=YES)


def Ouvrirligue1():
    # Création de la fenetre Pronostique

    ligue1 = Tk()

    # Personnalisation de la fenetre Pronostique

    ligue1.title("Pronostique")
    ligue1.geometry("1080x720")
    ligue1.minsize(720, 480)

    # Ajout du texte Equipe 1

    label_title = Label(ligue1, text="Equipe 1", font=("Bauhaus 93", 14))
    label_title.pack(side=LEFT)

    # Ajout du texte Equipe 2

    label_title = Label(ligue1, text="Equipe 2", font=("Bauhaus 93", 14))
    label_title.pack(side=RIGHT)

    # Ajout du texte Contre

    label_title = Label(ligue1, text="Contre", font=("Bauhaus 93", 14))
    label_title.pack(expand=YES)


# Barre menu
MenuBar = Menu(window)

# Menu principaux
menuPronostique = Menu(MenuBar)
menuContact = Menu(MenuBar)
menuApropos = Menu(MenuBar)
menuAvis = Menu(MenuBar)

#Ajout des menus à la barre
MenuBar.add_cascade(label="Pronostique", menu=menuPronostique)
MenuBar.add_cascade(label="Contact", menu=menuContact)
MenuBar.add_cascade(label="A-propos", menu=menuApropos)
MenuBar.add_cascade(label="Avis", menu=menuAvis)

# Ajout de commande aux menus
menuPronostique.add_command(label="Ligue 1", command=Ouvrirligue1)

# Afficher la fênetre
window.config(menu=MenuBar)
window.mainloop()

