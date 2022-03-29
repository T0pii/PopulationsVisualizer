import csv
from random import choices
import matplotlib.pyplot as plt

matrice=[]
f = open("data/c4.csv")
csv_f = csv.reader(f)
lineCount=0


for row in csv_f:
    if lineCount == 0:
        nbSimul=int(row[0])
    if lineCount == 1:
        nbEtapes=int(row[0])
    if lineCount==2:
        etatInitial=int(row[0])
    if lineCount >= 3:
        matrice.append(row)
    lineCount+=1
f.close

ordre=len(matrice)

ligneMatrice = []
compteurEtat = []
for i in range(ordre):
    ligneMatrice.append(i)
    compteurEtat.append(0)
etapec=0
for simul in range (nbSimul):
    etat=etatInitial
    for etape in range (nbEtapes):
        etatDepl=choices(ligneMatrice,map(float,matrice[etat]))
        etat=etatDepl[0]
        listproba=etatDepl[0]
        compteurEtat[etat]+=1
        
        
        etapec+=1
        print("\nEtape :",etapec)
        print("-------------------")
        for i in range(0,ordre):
            print("Etat",i,":",round(compteurEtat[i]/(etapec),2)*100,"%","(",compteurEtat[i],"/",etapec,")")
        
print("\nNb simulation :",nbSimul)
print("Nb étapes :",nbEtapes)
print("Matrice d'ordre",ordre)
for i in range (ordre):
    print(matrice[i])
    
print("\nProbabilite d'arriver a chaque etat")

listproba=[]
listlabel=[]
sommeproba = 0
left = []
for i in range (0,ordre):
        print("Etat",i,":",round(compteurEtat[i]/(nbSimul*nbEtapes),2)*100,"(",compteurEtat[i],"/",nbSimul*nbEtapes,")")
        sommeproba = sommeproba + compteurEtat[i]/(nbSimul*nbEtapes)
        listlabel.append(i+1)
        left.append((compteurEtat[i]/(nbSimul*nbEtapes)*100))





plt.bar(listlabel,left,align='center')

plt.xlabel('Etat')
plt.ylabel('Probabilite(%)')

plt.title('Histogramme des probabilites de passer par chaque état')

plt.show()

print("Somme des proba :",sommeproba)