from MVP2.Analyse_fonctions import *
import os


def fonction_de_meme_nom(Code_candidat, base_de_donnees):

    '''cette fonction regarde pour chaque fonction du code écrit
    par le candidat s'il correspond une fonction de même nom
    dans les fichiers de comparaison'''

    #on va récuperer la liste de fonctions du candidat et la longueur de cette liste
    list_functions_candidat, nombre_fonctions_candidat = list_functions(Code_candidat)
    #on va créer une liste qui va contenir les informations (nom de la fonction et son nombre d'itérations)
    liste_bilan=[]
    #on va créer une liste contenant le nom des codes contenues dans la base de donnée
    liste_fichier = os.listdir(base_de_donnees)
    for k in range (nombre_fonctions_candidat):
        compteur=0
        #pour chaque fonction du candidat on va ouvrir les anciens codes et verifier le nom
        for fichier in liste_fichier:
            
            with open(str(os.path.abspath(fichier)),"r") as fichier_comparaison:
                # on va récupèrer une liste de toutes les fonctions du fichier ouvert
                list_functions_comparaison,nombre_fonctions_comparaison = list_functions(fichier_comparaison)
                #Et on va tester si il existe une fonction avec le même nom
                if list_functions_candidat[k] in list_functions_comparaison:
                    compteur += 1 #on ajoute 1 si on trouve la fonction dans la base de donnée
        liste_bilan.append([list_functions_candidat[k]+ "apparait" + str(compteur)+ "fois dans la base de données"])
    return liste_bilan

print(fonction_de_meme_nom("C:\Marc\Coding_weeks\Doctolib\EventCandidatA.rb","C:\Marc\Coding_weeks\Doctolib\MVP3\BaseDeDonnees")



