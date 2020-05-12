from tkinter import *
from tkinter import ttk

#Rechercher les valeures sélectionnées

def recherche(equipe):
   for ligne in range(20):
        if tableau[ligne][0] == equipe:
            return tableau[ligne]

#Calculer les différentes probabilitées

def calcul_resultat():
    equipe1 = select1.get()
    info1 = recherche(equipe1)
    equipe2 = select2.get()
    info2 = recherche(equipe2)
    if int(info1[2])/int(info1[1]) - int(info2[2])/int(info2[1]) > 0.2 :
        return (equipe1,int(info1[2])/int(info1[1]),int(info2[2])/int(info2[1]))
    elif 0.2> int(info1[2]/info1[1]) - int(info2[2]/info2[1]) > -0.2 :
        return "Match nul"
    else :
        return (equipe2,int(info1[2]/info1[1]),int(info2[2]/info2[1]))


# Création de la fenetre Pronostique

def Ouvrirligue1():
    ligue1 = Tk()

    # Personnalisation de la fenetre Pronostique

    ligue1.title("Pronostique")
    ligue1.geometry("1080x720")
    ligue1.config(background='blue')
    ligue1.minsize(720, 480)

    # Ajout du texte Equipe 1

    label_title = Label(ligue1, text="Equipe 1", font=("Bauhaus 93", 14))
    label_title.grid(row=2, column=1)

    # Ajout du texte Equipe 2

    label_title = Label(ligue1, text="Equipe 2", font=("Bauhaus 93", 14))
    label_title.grid(row=2, column=4)

    # Ajout du texte Contre

    label_title = Label(ligue1, text="Contre", font=("Bauhaus 93", 14))
    label_title.grid(row=1, column=3)

    #Ajout liste deroulante

    labelChoix = Label(ligue1, text="Veuillez choisir")
    labelChoix.grid(row=3, column=1)

    #Création de la liste des équipes

    listequipes = ["ParisSG", "Marseille", "Rennes", "Lille", "Reims", "Nice", "Lyon", "Montpellier", "Monaco", "Angers", "Strasbourg", "Bordeaux", "Nantes", "Brest", "Metz", "Dijon", "ASSE", "Nimes", "Amiens", "Toulouse"]

    #Création de l'objet

    global select1
    select1 = StringVar(ligue1)
    ListeCombo = ttk.Combobox(ligue1, values=listequipes, textvariable = select1)
    ListeCombo.grid(row=3, column=1)

    #Création de l'objet 2

    global select2
    select2 = StringVar(ligue1)
    ListeCombo2 = ttk.Combobox(ligue1, values=listequipes, textvariable = select2)
    ListeCombo2.grid(row=3, column=4)

    #Création du boutton valider

    bouttonvalider = Button(ligue1, text="Valider", command = calcul_resultat)
    bouttonvalider.grid(row=4,column=3)

    #Retour à l'utilisateur
    label_retour = Label(ligue1,)


# Création de la fenetre Contact

def OuvrirContact():

    Contact = Tk()

    # Personnalisation de la fenetre Contact

    Contact.title("Contact")
    Contact.geometry("1080x720")
    Contact.config(background='white')
    Contact.minsize(720, 480)

    #Ajout du texte

    label_title = Label(Contact, text="Voici comment nous contacter à l'aide de notre adresse mail: Atanbatlex@pronostic.pro", font=("Bauhaus 93", 35))
    label_title.pack(expand=YES)


# Création de la fenetre Apropos

def OuvrirApropos():

    Apropos = Tk()

    # Personnalisation de la fenetre Apropos

    Apropos.title("A-propos")
    Apropos.geometry("1080x720")
    Apropos.config(background='white')
    Apropos.minsize(720, 480)

# Création de la fenetre Avis

def OuvrirAvis():

    Avis = Tk()

    # Personnalisation de la fenetre Avis

    Avis.title("Avis")
    Avis.geometry("1080x720")
    Avis.config(background='white')
    Avis.minsize(720, 480)

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

#Ajout design

photo = PhotoImage(file="ligue1.png")

canvas = Canvas(window,width=1080, height=720)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(expand=YES)

#Récupérer les données du classement

tableau = []
with open('Classement_ligue _1_(avant_COVID-19).csv','r') as fic:
        for ligne in fic:
            tableau.append(ligne.strip().split(";"))

ParisSG= tableau[1]
Marseille= tableau[2]
Rennes= tableau[3]
Lille= tableau[4]
Reims= tableau[5]
Nice= tableau[6]
Lyon= tableau[7]
Montpellier= tableau[8]
Monaco= tableau[9]
Angers= tableau[10]
Strasbourg= tableau[11]
Bordeaux= tableau[12]
Nantes= tableau[13]
Brest= tableau[14]
Metz= tableau[15]
Dijon= tableau[16]
ASSE= tableau[17]
Nimes= tableau[18]
Amiens= tableau[19]
Toulouse= tableau[20]

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

# Ajout de commandes aux menus

menuPronostique.add_command(label="Ligue 1", command=Ouvrirligue1)
menuContact.add_command(label="Contact", command=OuvrirContact)
menuApropos.add_command(label="A propos", command=OuvrirApropos)
menuAvis.add_command(label="Avis", command=OuvrirAvis)


# Afficher la fênetre

window.config(menu=MenuBar)
window.mainloop()

