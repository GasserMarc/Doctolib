"""Le but est de nettoyer le texte"""

from MVP2.liste_variables import *


def Transformation_fichier(Adresse): #Adresse est le chemin d'accès spécifique à la machine
    try:
        RawData=open(Adresse,"r")
        Transformed_data=[]

        for line in RawData.readlines(): #Transformation du fichier brut txt en liste de lignes
            Transformed_data=Transformed_data+[line]
        return Transformed_data
    except IOError as error:
        print(error)


def suppr_space(List):
    new_list=[]
    for line in List:
        new=line.replace(" ","")
        new_list=new_list+[new]
    return (new_list)

def suppr_blank_and_end(List):
    new_list=[]
    for line in List:
        if "end" not in line:
            if line!='\n':
                new_list=new_list+[line]
    return new_list
