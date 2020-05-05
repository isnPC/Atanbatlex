tableau = []
with open('Classement_ligue _1_(avant_COVID-19).csv','r') as fic:
        for ligne in fic:
            tableau.append(ligne.strip().split(";"))

ParisSG = tableau[1]
Marseille = tableau[2]
Rennes = tableau[3]
Lille = tableau[4]
Reims = tableau[5]
Nice = tableau[6]
Lyon = tableau[7]
Montpellier = tableau[8]
Monaco = tableau[9]
Angers = tableau[10]
Strasbourg = tableau[11]
Bordeaux = tableau[12]
Nantes = tableau[13]
Brest = tableau[14]
Metz = tableau[15]
Dijon = tableau[16]
ASSE = tableau[17]
Nimes = tableau[18]
Amiens = tableau[19]
Toulouse = tableau[20]


def calcul_resultat(equipe1,equipe2):
    if int(equipe1[2])/int(equipe1[1]) - int(equipe2[2])/int(equipe2[1]) > 0.2 :
        return equipe1[0]
    elif 0.2> equipe1[2]/equipe1[1] - equipe2[2]/equipe2[1] > -0.2 :
        return "Match nul"
    else :
        return equipe2[0]





































