
from MVP2.Nettoyage_texte import *

def Transformation_fichier(Adresse): #Adresse est le chemin d'accès spécifique à la machine
    try:
        RawData=open(Adresse,"r")
        Transformed_data=[]

        for line in RawData.readlines(): #Transformation du fichier brut txt en liste de lignes
            Transformed_data=Transformed_data+[line]
        return Transformed_data
    except IOError as error:
        print(error)


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

def Coeff_Dice(List,Precision): #https://fr.wikipedia.org/wiki/Indice_de_Sørensen-Dice
    Result=np.zeros((len(List),len(List)))#Création d'une matrice N*N pour enregistrer les résultats
    img=np.zeros((len(List),len(List),3),dtype ='uint8')#Même matrice, mais avec des couleurs
    Total=0
    for ligneref in range(len(List)): #Ligne a comparer
        for ligneanalysee in range(len(List)): #Ligne comparée
            A=egalitelist(List[ligneref],List[ligneanalysee])#Egalise la longueur des deux lignes
            compt=0
            for i in range(len(A[0])):
                if A[0][i]==A[1][i]:
                    compt=compt+1 #Compte les caractères en commun entre les deux lignes
            if compt/len(A[0])< Precision:
                res=float(0)
            else:
                res=float(compt/len(A[0]))
            if res>0.5+Precision:
                Total=Total+1
            Result[ligneref][ligneanalysee]=res#Affecte résultat à matrice
            img[ligneref][ligneanalysee]=[255,255-int(res*255),255-int(res*255)]#Idem
    plt.imshow(img)
    plt.show ()
    print("Il y a eu "+str(Total-len(List))+" ligne(s) avec un taux de correspondance supérieur à "+str((0.5+Precision)*100)+"%, sur un total de "+ str(len(List)*(len(List)-1)/2)+" comparaisons effectuées")

    return(Result)

def mix(chaine):
    return chaine

def Coeff_Dice_max(List,Precision): #https://fr.wikipedia.org/wiki/Indice_de_Sørensen-Dice
    Result=np.zeros((len(List),len(List)))#Création d'une matrice N*N pour enregistrer les résultats
    img=np.zeros((len(List),len(List),3),dtype ='uint8')#Même matrice, mais avec des couleurs
    Total=0
    Test=0
    for ligneref in range(len(List)): #Ligne a comparer
        for ligneanalysee in range(len(List)): #Ligne comparée
            max=0
            for i in range(len(List[ligneref])):
                List[ligneref]=List[ligneref][i:]+List[ligneref][:i]
                A=egalitelist(List[ligneref],List[ligneanalysee])#Egalise la longueur des deux lignes
                compt=0
                for i in range(len(A[0])):
                    if A[0][i]==A[1][i]:
                        compt=compt+1 #Compte les caractères en commun entre les deux lignes
                if compt/len(A[0])< Precision:
                    res=float(0)
                else:
                    res=float(compt/len(A[0]))
                if res>max:
                    max=res

            Result[ligneref][ligneanalysee]=max#Affecte résultat à matrice

            if max>0.5+Precision:
                img[ligneref][ligneanalysee]=[0,0,0]#Idem
                Total=Total+1
            else:
                img[ligneref][ligneanalysee]=[255,255-int(max*255),255-int(max*255)]#Idem
    plt.imshow(img)
    plt.show ()
    print("Il y a eu "+str(Total-len(List))+" ligne(s) avec un taux de correspondance supérieur à "+str((0.5+Precision)*100)+"%, sur un total de "+ str(len(List)*(len(List)-1)/2)+" comparaisons effectuées")
    return(Result)


A=Transformation_fichier("/Users/PaulJoly/PycharmProjects/Projet_Doctolib/MVP2/event_candidate_b.rb")
print(Coeff_Dice(A,0.1))
B=suppr_space(A)
print(Coeff_Dice(B,0.1))
C=suppr_blank_and_end(B)
print(Coeff_Dice(C,0.1))
print(Coeff_Dice_max(C,0.3))
