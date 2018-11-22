from MVP1.tout_MVP1 import *
from MVP2.tout_MVP2 import *

from MVP3.fraude_nom_fonction import  *
import pandas as pd

from Exemples_codes import *
import numpy as np
import matplotlib as plt

def analyse_code_candidat (code_candidat):
    analyse ={}
    analyse['taille_moyenne_fonction']=taille_moyenne_fonctions(code_candidat)
    if len(list_tests(code_candidat)) != 0:
        analyse['testCount']=len(list_tests(code_candidat))
    analyse['%tooLongLines']=pourcentage_toolonglines(code_candidat)
    analyse["pourcentage_variables_mal_nommées"]=calcul_pourcentage_variables_mal_nommees(code_candidat)
    analyse["pourcentage_variables_majuscules"]=majuscule_variable(code_candidat)
    analyse["pourcentage_fonctions_mal_nommées"]=calcul_pourcentage_fonctions_mal_nommees(code_candidat)
    #analyse["pourcentage_functions_majuscules"]=majuscule_fonction(code_candidat)
    transformed=transformation_fichier(code_candidat)
    clean=suppr_blank_and_end(suppr_space(transformed))#on enleve les espaces les lignes vides et les lignes end
    analyse["Duplication_sur_texte_non_nettoyé"]=coeff_dice(transformed,0.1)
    analyse["Duplication_sur_texte_nettoyé"]=coeff_dice(clean,0.3)
    analyse["densite_de_commentaires"]=ratio_commentaires(code_candidat)
    analyse["densite_d_espace"]=ratio_spaces(code_candidat)

<<<<<<< HEAD
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

    if analyse['%tooLongLines']>=0.2:
        notes_candidat['%tooLongLines'] = 1
    elif 0.12<=analyse['%tooLongLines']<0.2:
        notes_candidat['%tooLongLines'] = 2
    elif 0.05<=analyse['%tooLongLines']<0.12:
        notes_candidat['%tooLongLines'] = 3
    else:
        notes_candidat['%tooLongLines'] = 4

    if 0<=analyse["Duplication_sur_texte"]<0.5:
        notes_candidat["Duplication_sur_texte"] = 4
    elif 0.5<=analyse["Duplication_sur_texte"]<1:
        notes_candidat["Duplication_sur_texte"] = 3
    elif 1<=analyse["Duplication_sur_texte"]<1.5:
        notes_candidat["Duplication_sur_texte"] = 2
    else:
        notes_candidat["Duplication_sur_texte"] = 1

    if analyse["densite_de_commentaires"] in [0,5] or analyse["densite_de_commentaires"]>40:
        notes_candidat["densite_de_commentaires"] = 1
    elif analyse["densite_de_commentaires"] in [5,10] or analyse["densite_de_commentaires"] in [30,40]:
        notes_candidat["densite_de_commentaires"] = 2
    elif analyse["densite_de_commentaires"] in [10,15] or analyse["densite_de_commentaires"] in [25,30]:
        notes_candidat["densite_de_commentaires"] = 3
    else:
        notes_candidat["densite_de_commentaires"] = 4

    if analyse["pourcentage_variables_mal_nommées"]<=5:
        notes_candidat["pourcentage_variables_mal_nommées"] = 4
    elif analyse["pourcentage_variables_mal_nommées"]<=10:
        notes_candidat["pourcentage_variables_mal_nommées"] = 3
    elif analyse["pourcentage_variables_mal_nommées"]<=20:
        notes_candidat["pourcentage_variables_mal_nommées"] = 2
    else:
        notes_candidat["pourcentage_variables_mal_nommées"] = 1



