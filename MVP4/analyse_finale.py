from MVP1.tout_MVP1 import *
from MVP2.tout_MVP2 import *
from Exemples_codes import *
import numpy as np
import matplotlib as plt

def analyse_code_candidat (code_candidat):
    analyse ={}
    if len(list_functions(code_candidat)) != 0:
        analyse['functionCount']=len(list_functions(code_candidat))
    if len(list_tests(code_candidat)) != 0:
        analyse['testCount']=len(list_tests(code_candidat))
    analyse['commentCount']=compte_commentaires(code_candidat)
    analyse['loopCount']=count_boucles(code_candidat)
    analyse['tooLongLines']=caractere_ligne(code_candidat)
    analyse['variableCount']=len(listes_de_variables(code_candidat))
    analyse["liste_de_variables"]=listes_de_variables(code_candidat)
    analyse["pourcentage_variables_mal_nommées"]=calcul_pourcentage_variables_mal_nommees(code_candidat)
    #MVP2["pourcentage_variables_majuscules"]=majuscule_variable(code_candidat)
    analyse["pourcentage_fonctions_mal_nommées"]=calcul_pourcentage_fonctions_mal_nommees(code_candidat)
    #MVP2["pourcentage_functions_majuscules"]=majuscule_fonction(adresse)
    transformed=transformation_fichier(code_candidat)
    clean=suppr_blank_and_end(suppr_space(transformed))#on enleve les espaces les lignes vides et les lignes end
    analyse["Duplication_sur_texte_non_nettoyé"]=coeff_dice(transformed,0.1)
    analyse["Duplication__sur_texte_nettoyé"]=coeff_dice(clean,0.3)
    return(analyse)

print(analyse_code_candidat("C:/Users/Victoire/PycharmProjects/Doctolib/Exemples_codes/EventCandidatA.rb"))
