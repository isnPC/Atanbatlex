classement = open('Classement_ligue _1_(avant_COVID-19).csv','r')
equipe = classement.readlines()
len(equipe)
tableau = [equipe[1],equipe[2],equipe[3],equipe[4],equipe[5],equipe[6],equipe[7],equipe[8],equipe[9],equipe[10],equipe[11],equipe[12],equipe[13],equipe[14],equipe[15],equipe[16],equipe[17],equipe[18],equipe[19],equipe[20]]
print(tableau[5])