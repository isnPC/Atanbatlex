classement = open('Classement_ligue _1_(avant_COVID-19).csv','r')

equipe = classement.readlines()
len(equipe)

tableau = [equipe[1],equipe[2],equipe[3],equipe[4],equipe[5],equipe[6],equipe[7],equipe[8],equipe[9],equipe[10],equipe[11],equipe[12],equipe[13],equipe[14],equipe[15],equipe[16],equipe[17],equipe[18],equipe[19],equipe[20]]
"""Chaque ligne corresponds dans l'ordre à: Équipes;Matchs joués;Matchs Gagnés;Matchs perdus;Matchs nuls;Buts mis;Buts encaissés;Différence de buts;Points;5 derniers matchs(Gagnés);5 derniers matchs(Perdus);5derniers matchs(Nuls) """

ParisSG = [tableau[0]]
Marseille = [tableau[1]]
Rennes = [tableau[2]]
Lille = [tableau[3]]
Reims = [tableau[4]]
Nice = [tableau[5]]
Lyon = [tableau[6]]
Montpellier = [tableau[7]]
Monaco = [tableau[8]]
Angers = [tableau[9]]
Strasbourg = [tableau[10]]
Bordeaux = [tableau[11]]
Nantes = [tableau[12]]
Brest = [tableau[13]]
Metz = [tableau[14]]
Dijon = [tableau[15]]
ASSE = [tableau[16]]
Nimes = [tableau[17]]
Amiens = [tableau[18]]
Toulouse = [tableau[19]]

print(ParisSG)





