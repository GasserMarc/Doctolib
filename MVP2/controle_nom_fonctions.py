from MVP2.liste_variables import *

def controle_nom_fonction (code_candidat):
    variables=listes_de_variables(code_candidat)
    nb_variable_mal_nommees=0 #compteur du nombre de variables mal nommées, avec des noms non explicites
    for nom_variables in variables:
        if len(nom_variables)<=1: #si les variables ont un nom non explicite, avec une lettre
            nb_variable_mal_nommees+=1
            print (nb_variable_mal_nommees)
    return nb_variable_mal_nommees

def calcul_pourcentage_mal_nommees(code_candidat):
    nb_variables_mal_nommées=controle_nom_fonction()
    variables=listes_de_variables(code_candidat)
    pourcentage_mal_nommees=((nb_variables_mal_nommées*100)/len(variables))
    return pourcentage_mal_nommees

print (controle_nom_fonction("EventCandidatA.rb"))

