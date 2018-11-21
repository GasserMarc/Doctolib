'''
Cette fonction renvoie la proportion de texte dupliqué
'''



'''
Ces fonctions indiquent la pertinence du nom des variables, si elles sont explicites ou si elles ne commencent pas par
une majuscule (convention) 
'''

def listes_de_variables(code_candidat):
    '''
    Donne la liste et le nombre des variables utilisées par le candidat
    :param code_candidat:
    :return: liste nom variables et nombre variables:
    '''
    with open (code_candidat, "r" ) as code:
        lecture_code=code.readlines()
        variables= []
        for line in lecture_code:
            words=line.split()
            if len (words)<2:
                pass #si il y a moins de 2 mots il ne peut pas avoir de variable
            elif words[1] == '=':
                variables.append(words[0]) #cree la liste de variables
    return (variables, len(variables))

print(listes_de_variables("/Users/baptiste/PycharmProjects/Doctolib/Exemples_codes/EventCandidatA.rb"))

def controle_nom_variable (code_candidat):
    '''
    On considère que le nom est explicite s'il contient plus de 2 lettres
    :param code_candidat:
    :return nb de variables mal nommées:
    '''
    variables=listes_de_variables(code_candidat)[0]
    nb_variable_mal_nommees=0 #compteur du nombre de variables mal nommées, avec des noms non explicites
    for nom_variables in variables:
        if len(nom_variables)<=1: #si les variables ont un nom non explicite, avec une lettre
            nb_variable_mal_nommees+=1
            #print (nb_variable_mal_nommees)
    return nb_variable_mal_nommees

def calcul_pourcentage_variables_mal_nommees(code_candidat):
    '''
    Pourcentage de variables mal nommées dans le code
    :param code_candidat:
    :return:
    '''
    nb_variables_mal_nommees=controle_nom_variable(code_candidat)
    variables=listes_de_variables(code_candidat)[0]
    pourcentage_mal_nommees=((nb_variables_mal_nommees*100)/len(variables))
    return pourcentage_mal_nommees

def majuscule_variable(code_candidat):
    '''
    Le nom de la variable ne commence pas par une majuscule
    :param code_candidat:
    :return:
    '''
    variables=listes_de_variables(code_candidat)
    nb_variable_majuscule=0 #compte le nombre de variables commençant par une majuscule
    for i in range (len(variables)):
            code_ascii=ord((variables[i][0]))
            if code_ascii>=65 or code_ascii<=90:
                nb_variable_majuscule=+1
        code_ascii=ord((variables[i][0]))
        if code_ascii>=65 or code_ascii<=90:
            nb_variable_majuscule=+1
    pourcentage_debut_majuscule= ((nb_variable_majuscule *100)/len(variables))
    return pourcentage_debut_majuscule


'''
Idem nom de fonctions
'''

def remove_special(s):
    '''
    Retire les ( et \n d'une chaîne de caractères ainsi que tous les caractères qui suivent
    :param s:
    :return:
    '''
    s1 = s
    for i in range(len(s1)):
        if s1[i] == '(' or s1[i] == '\n':
            s1 = s[:i]
            break
    return s1

#print(remove_special('starts_at_cannot_be_greater_than_ends_at\n'))

def list_functions(code_candidat):
    '''
    renvoie une liste de toutes les fonctions du code du candidat
    :param code_candidat:
    :return:
    '''
    list_of_functions = []
    with open(code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == "def":
            list_of_functions.append(remove_special(mots[i+1]))
    return list_of_functions, len(list_of_functions) #renvoie la liste des fonctions et le nombre de fonctions

def controle_nom_fonction(code_candidat):
    '''
    On considère que le nom est explicite s'il contient plus de 2 lettres
    :param code_candidat:
    :return nb de variables mal nommées:
    '''
    fonctions=list_functions(code_candidat)[0]
    nb_fonctions_mal_nommees=0 #compteur du nombre de variables mal nommées, avec des noms non explicites
    for nom_fonctions in fonctions:
        if len(nom_fonctions)<=1: #si les variables ont un nom non explicite, avec une lettre
            nb_fonctions_mal_nommees+=1
            #print (nb_variable_mal_nommees)
    return nb_fonctions_mal_nommees

def calcul_pourcentage_fonctions_mal_nommees(code_candidat):
    '''
    Pourcentage de fonctions mal nommées dans le code
    :param code_candidat:
    :return:
    '''
    nb_fonctions_mal_nommees=controle_nom_fonction(code_candidat)
    fonctions=list_functions(code_candidat)[0]
    pourcentage_mal_nommees=((nb_fonctions_mal_nommees*100)/len(fonctions))
    return pourcentage_mal_nommees

def majuscule_fonction(code_candidat):
    '''
    Le nom de la fonction ne commence pas par une majuscule
    :param code_candidat:
    :return:
    '''
    fonctions=list_functions(code_candidat)
    nb_fonctions_majuscule=0 #compte le nombre de variables commencant par une majuscule
    for i in range (len(fonctions)):
            code_ascii=ord((fonctions[i][0]))
            if code_ascii>=65 or code_ascii<=90:
                nb_fonctions_majuscule=+1
        code_ascii=ord((fonctions[i][0]))
        if code_ascii>=65 or code_ascii<=90:
            nb_fonctions_majuscule=+1
    pourcentage_debut_majuscule= ((nb_fonctions_majuscule *100)/len(fonctions))
    return pourcentage_debut_majuscule

def Transformation_fichier(Adresse): #Adresse est le chemin d'accès spécifique à la machine
    """
    Transforme le fichier brut en liste de lignes
    :param Adresse:
    :return:
    """

    try:
        RawData=open(Adresse,"r")
        Transformed_data=[]
        for line in RawData.readlines(): #Transformation du fichier brut txt en liste de lignes
            Transformed_data=Transformed_data+[line]
        return Transformed_data
    except IOError as error:
        print(error)


def suppr_space(List):
    """
    Supprime les espaces du document
    :param List:
    :return:
    """
    new_list=[]
    for line in List:
        new=line.replace(" ","")
        new_list=new_list+[new]
    return (new_list)

def suppr_blank_and_end(List):
    """
    Supprime les end et les lignes vierges
    :param List:
    :return:
    """
    new_list=[]
    for line in List:
        if "end" not in line:
            if line!='\n':
                new_list=new_list+[line]
    return new_list

def egalitelist (chaine1,chaine2):
    """
    Egalise deux chaines de caractères
    :param chaine1:
    :param chaine2:
    :return:
    """
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
    #img=np.zeros((len(List),len(List),3),dtype ='uint8')#Même matrice, mais avec des couleurs
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
            #img[ligneref][ligneanalysee]=[255,255-int(res*255),255-int(res*255)]#Idem
    #plt.imshow(img)
    #print(Result)
    return(float(Total-len(List))/float(len(List)*(len(List)-1)/2))


def mix(chaine):
    return chaine

def Coeff_Dice_max(List,Precision): #https://fr.wikipedia.org/wiki/Indice_de_Sørensen-Dice
    Result=np.zeros((len(List),len(List)))#Création d'une matrice N*N pour enregistrer les résultats
    #img=np.zeros((len(List),len(List),3),dtype ='uint8')#Même matrice, mais avec des couleurs
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
                #img[ligneref][ligneanalysee]=[0,0,0]#Idem
                Total=Total+1
            #else:
                #img[ligneref][ligneanalysee]=[255,255-int(max*255),255-int(max*255)]#Idem
    #plt.imshow(img)
    return(float(Total-len(List))/float(len(List)*(len(List)-1)/2))


def run_script_MVP2 (Adresse):
    MVP2={}
    MVP2["liste_de_variables"]=listes_de_variables(Adresse)
    MVP2["pourcentage_variables_mal_nommées"]=calcul_pourcentage_variables_mal_nommees(Adresse)
    #MVP2["pourcentage_variables_majuscules"]=majuscule_variable(Adresse)
    MVP2["liste_des_fonctions"]=list_functions(Adresse)
    MVP2["pourcentage_fonctions_mal_nommées"]=calcul_pourcentage_fonctions_mal_nommees(Adresse)
    #MVP2["pourcentage_functions_majuscules"]=majuscule_fonction(Adresse)
    transformed=Transformation_fichier(Adresse)
    A=Coeff_Dice(transformed,0.1)
    clean=suppr_blank_and_end(suppr_space(transformed))
    C=Coeff_Dice_max(clean,0.3)
    MVP2["Duplication_ntrie"]=A
    MVP2["Duplication_trie"]=C

    return(MVP2)

A=(run_script_MVP2("/Users/PaulJoly/PycharmProjects/Projet_Doctolib/MVP2/EventCandidatA.rb"))
print(A)
