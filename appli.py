classement = open('Classement_ligue _1_(sans_#1).csv','r')
place0 = 0
for place in classement:
    place0 += 1
    print("N°",place0,":",place,end="")