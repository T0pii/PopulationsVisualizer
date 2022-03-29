import csv
import random
import numpy as np
from random import choices
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

matrice=[]
f = open("data/b1.csv")
csv_f = csv.reader(f)
lineCount=0

for row in csv_f:
    if lineCount == 0:
        nbSimul=int(row[0])
    if lineCount == 1:
        nbEtapes=int(row[0])
    if lineCount==2:
        etatInitial=int(row[0])-1
    if lineCount >= 3:
        matrice.append(row)
        print(matrice)
    lineCount+=1
f.close



ordre=len(matrice)

#Multiplicateur (si etat initial défini cest x1 sinon c'est x ordre)
#exemple pour fourmis aucun etat initial du coup on fait x3 (car trois simulations de 50)
if (etatInitial+1)==0:
    coeffMult=ordre;
else:
    coeffMult=1;

ligneMatrice = []
for i in range(ordre):
    ligneMatrice.append(i)

evolution=[]
for i in range(1,nbEtapes+1):
    evolution.append(i)

#nbOccurences[nbEtape][ordre] init à 0
nbOccurences=[[0 for x in range(ordre)] for y in range((nbEtapes+1)*coeffMult)] 

for i in range (0,coeffMult):
    for simul in range (0,nbSimul):
        etat=i
        #nbOccurences[0][etat]+=1
        for etape in range (1,nbEtapes+1):
            etatDepl=choices(ligneMatrice,map(float,matrice[etat]))
            etat=etatDepl[0]
            nbOccurences[etape][etat]+=1
            
couleur=["b","g","r","c","m","y","k","#ff61b1","#ffff31","#9a2d58"]

occurenceEtat=[]
for nbOrdre in range (0,ordre):
    for etape in range (1,nbEtapes+1):
        occurenceEtat.append(((nbOccurences[etape][nbOrdre]*100/(nbSimul*coeffMult))))
    plt.plot(evolution,occurenceEtat, color=couleur[nbOrdre], linewidth = 1, marker='o', markerfacecolor='blue', markersize=2,label='Etat %d' %(nbOrdre+1))
    occurenceEtat=[]

plt.ylim(0,100)
plt.xlim(1,nbEtapes)

plt.ylabel('Population a un etat donne (%)')
plt.xlabel('Etape')
plt.title('Evolution de la population en fonction du temps')
plt.legend()
plt.show()