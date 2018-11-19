
def Transformation_fichier(Adresse): #Adresse est le chemin d'accès spécifique à la machine
    try:
        RawData=open(Adresse,"r")
        Transformed_data=[]

        for line in RawData.readlines(): #Transformation du fichier brut txt en liste de lignes
            Transformed_data=Transformed_data+[line]
        return Transformed_data
    except IOError as error:
        print(error)

print(Transformation_fichier("/Users/PaulJoly/PycharmProjects/Projet_Doctolib/RawData/test.txt"))

def egalitelist (chaine1,chaine2):
    n1=len(chaine1)
    n2=len(chaine2)
    if n1>n2:
        for k in range(n1-n2):
            chaine2=chaine2 + " "
    else:
        for k in range(n2-n1):
            chaine1=chaine1 + " "
    return ([str(chaine1),str(chaine2)])

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

def Coeff_Dice(List): #https://fr.wikipedia.org/wiki/Indice_de_Sørensen-Dice
    Result=np.zeros((len(List),len(List)))#Création d'une matrice N*N pour enregistrer les résultats
    img=np.zeros((len(List),len(List),3),dtype ='uint8')#Même matrice, mais avec des couleurs
    for ligneref in List: #Ligne a comparer
        for ligneanalysee in List: #Ligne comparée
            A=egalitelist(ligneref,ligneanalysee)#Egalise la longueur des deux lignes
            compt=0
            for i in range(len(A[0])):
                if A[0][i]==A[1][i]:
                    compt=compt+1 #Compte les caractères en commun entre les deux lignes

            Result[List.index(ligneref)][List.index(ligneanalysee)]=compt/len(A[0])#Affecte résultat à matrice
            img[List.index(ligneref)][List.index(ligneanalysee)]=[256-int(compt/len(A[0])*256),0,0]#Idem
    plt.imshow(img)
    plt.show ()
    return(Result)

print(Coeff_Dice(Transformation_fichier("/Users/PaulJoly/PycharmProjects/Projet_Doctolib/RawData/test.txt")))



