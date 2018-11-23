from MVP1.tout_MVP1 import *
from MVP2.tout_MVP2 import *

from MVP3.fraude_nom_fonction import  *
import pandas as pd


def analyse_code_candidat (code_candidat):
    analyse ={}
    analyse['taille_moyenne_fonction']=taille_moyenne_fonctions(code_candidat)
    analyse['test_count']=len(list_tests(code_candidat[:-3]+'Test.rb'))
    analyse['assert_count']=asserts_par_test(code_candidat[:-3]+'.rb')
    analyse['tooLongLines']=pourcentage_toolonglines(code_candidat)
    analyse["pourcentage_variables_mal_nommees"]=calcul_pourcentage_variables_mal_nommees(code_candidat)
    analyse["pourcentage_fonctions_mal_nommees"]=calcul_pourcentage_fonctions_mal_nommees(code_candidat)
    #analyse["pourcentage_functions_majuscules"]=majuscule_fonction(code_candidat)
    transformed=transformation_fichier(code_candidat)
    clean=suppr_blank_and_end(suppr_space(transformed))#on enleve les espaces les lignes vides et les lignes end
    analyse["duplication_sur_texte_nettoye"]=coeff_dice(clean,0.3)
    analyse["densite_de_commentaires"]=ratio_commentaires(code_candidat)
    analyse["densite_d_espace"]=ratio_spaces(code_candidat)
    analyse["textesuspect"]=comparaison_code(code_candidat)
    resultats=pd.DataFrame.from_dict(analyse, orient='index')
    #print(resultats)
    return analyse #resultats


#print(analyse_code_candidat("../Exemples_codes/EventCandidatA.rb"))

def note_code_candidat(code_candidat):
    analyse = analyse_code_candidat(code_candidat)
    notes_candidat = {}
    if analyse['taille_moyenne_fonction']>=20:
        notes_candidat['taille_moyenne_fonction'] = 1
    elif 15<=analyse['taille_moyenne_fonction']<20:
        notes_candidat['taille_moyenne_fonction'] = 2
    elif 10<=analyse['taille_moyenne_fonction']<15:
        notes_candidat['taille_moyenne_fonction'] = 3
    else:
        notes_candidat['taille_moyenne_fonction'] = 4

    if analyse['tooLongLines']>=0.5:
        notes_candidat['tooLongLines'] = 1
    elif 0.25<=analyse['tooLongLines']<0.5:
        notes_candidat['tooLongLines'] = 2
    elif 0.1<=analyse['tooLongLines']<0.25:
        notes_candidat['tooLongLines'] = 3
    else:
        notes_candidat['tooLongLines'] = 4

    if 0<=analyse["duplication_sur_texte_nettoye"]<0.5:
        notes_candidat["duplication_sur_texte"] = 4
    elif 0.5<=analyse["duplication_sur_texte_nettoye"]<1:
        notes_candidat["duplication_sur_texte"] = 3
    elif 1<=analyse["duplication_sur_texte_nettoye"]<1.5:
        notes_candidat["duplication_sur_texte"] = 2
    else:
        notes_candidat["duplication_sur_texte"] = 1

    if analyse["densite_de_commentaires"] in [0,5] or analyse["densite_de_commentaires"]>40:
        notes_candidat["densite_de_commentaires"] = 1
    elif analyse["densite_de_commentaires"] in [5,10] or analyse["densite_de_commentaires"] in [30,40]:
        notes_candidat["densite_de_commentaires"] = 2
    elif analyse["densite_de_commentaires"] in [10,15] or analyse["densite_de_commentaires"] in [25,30]:
        notes_candidat["densite_de_commentaires"] = 3
    else:
        notes_candidat["densite_de_commentaires"] = 4

    if analyse["pourcentage_variables_mal_nommees"]<=5:
        notes_candidat["pourcentage_variables_mal_nommees"] = 4
    elif analyse["pourcentage_variables_mal_nommees"]<=10:
        notes_candidat["pourcentage_variables_mal_nommees"] = 3
    elif analyse["pourcentage_variables_mal_nommees"]<=20:
        notes_candidat["pourcentage_variables_mal_nommees"] = 2
    else:
        notes_candidat["pourcentage_variables_mal_nommees"] = 1

    if analyse["assert_count"]==1:
        notes_candidat["assert_count"] = 1
    elif analyse["assert_count"]<=1.5:
        notes_candidat["assert_count"] = 2
    elif analyse["assert_count"]<=2:
        notes_candidat["assert_count"] = 3
    else:
        notes_candidat["assert_count"] = 4

    return notes_candidat


#print(note_code_candidat("../Exemples_codes/EventCandidateC.rb"))

nom_caracteristiques = ["taille_moyenne_fonction", "tooLongLines", "duplication_sur_texte",
                            "densite_de_commentaires","pourcentage_variables_mal_nommees", "assert_count"]

def dico_graphe(liste_candidats):
    dico_candidats={"candidats":["Candidat " + chr(65+i) for i in range(len(liste_candidats))]}
    notes_caracteristiques = [[] for x in range(len(nom_caracteristiques))]
    for i in range(len(nom_caracteristiques)):
        for candidat in liste_candidats:
            notes_candidats = note_code_candidat(candidat)
            notes_caracteristiques[i].append(notes_candidats[nom_caracteristiques[i]])
        dico_candidats[nom_caracteristiques[i]]=notes_caracteristiques[i]
    return dico_candidats

#print(dico_graphe(["../Exemples_codes/EventCandidatA.rb", "../Exemples_codes/EventCandidateB.rb",
#                   "../Exemples_codes/EventCandidateC.rb"]))

def moyenne_candidat(code_candidat):
    note_globale=0
    notes = note_code_candidat(code_candidat)
    for car in nom_caracteristiques:
        note_globale += notes[car]
    return note_globale/len(nom_caracteristiques)


def moyenne_coefficients(code_candidat):
    note_globale = 0
    notes = note_code_candidat(code_candidat)
    coefficients = {}
    coefficients["taille_moyenne_fonction"]=2.5
    coefficients["tooLongLines"]=1
    coefficients["duplication_sur_texte"]=2
    coefficients["densite_de_commentaires"]=1/notes["densite_de_commentaires"]
    coefficients["pourcentage_variables_mal_nommees"]=1
    coefficients["assert_count"]=1
    somme_coeff = 0
    for car in nom_caracteristiques:
        note_globale += notes[car] * coefficients[car]
        somme_coeff += coefficients[car]
    return note_globale/somme_coeff

#print(moyenne_coefficients("../Exemples_codes/EventCandidatA.rb"))
#print(moyenne_coefficients("../Exemples_codes/EventCandidateB.rb"))
#print(moyenne_coefficients("../Exemples_codes/EventCandidateC.rb"))
