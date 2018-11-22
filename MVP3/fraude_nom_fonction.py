from MVP2.Analyse_fonctions import *
import os


def fonction_de_meme_nom(code_candidat):
    '''cette fonction regarde pour chaque fonction du code écrit
    par le candidat s'il correspond une fonction de même nom
    dans les fichiers de comparaison'''

    #on va récuperer la liste de fonctions du candidat
    list_functions_candidat = list_functions(code_candidat)
    #on va créer une liste qui va contenir les informations (nom de la fonction et son nombre d'itérations)
    liste_bilan=[]
    #on va créer une liste contenant le nom des codes contenues dans la base de donnée
    liste_fichier = os.listdir("../Exemples_codes/")
    for nom_Fonction in list_functions_candidat:
        compteur=0
        #pour chaque fonction du candidat on va ouvrir les anciens codes et verifier le nom
        for fichier in liste_fichier:
            list_functions_comparaison= list_functions(str("../Exemples_codes/" + fichier))

            if nom_Fonction in list_functions_comparaison:
                compteur += 1 #on ajoute 1 si on trouve la fonction dans la base de donnée
        liste_bilan.append(nom_Fonction+ " apparait " + str(compteur)+ " fois dans la base de données")
    return liste_bilan

def comparaison_code(code_candidat):

    #crée une liste contenant le nom des codes stockés
    liste_fichier=os.listdir("../Exemples_codes/")
    lignes_identiques=0
    with open(code_candidat,"r") as candidat:
        #on va créer une liste contenant les lignes du code
        liste_ligne=candidat.readlines()
        occurence=liste_ligne.count("end")
        print(liste_ligne)
        print(occurence)
        for k in range (occurence):
            liste_ligne.remove("end")#on va pas prendre en compte les end
        for ligne in liste_ligne:
            #Pour chaque ligne du code candidat on va le tester avec les lignes des autres codes de la base de donnée
            # for fichier in liste_fichier:
                with open("C:\Marc\Coding_weeks\Doctolib\MVP1\EventCandidatA.rb", "r") as code_comparaison:
                    #pour chaque code, on crée une liste contenant ses lignes et on va tester si les lignes sont identiques
                    liste_ligne_comparaison=code_comparaison.readlines()
                    if ligne in liste_ligne_comparaison:
                        lignes_identiques += 1
                        break
    return(lignes_identiques/len(liste_ligne)) #si renvoie

print(comparaison_code("C:\Marc\Coding_weeks\Doctolib\MVP1\EventCandidatA.rb"))

