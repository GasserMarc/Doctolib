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
