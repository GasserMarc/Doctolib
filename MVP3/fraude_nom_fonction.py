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


print (fonction_de_meme_nom("C:\Users\Marie\PycharmProjects\Doctolib\Exemples_codes\EventCandidatA.rb"))

#on compare 2 codes initialement et on regarde si les 2 codes font la même taille en bytes
def comparaison_code(Code_Candidat, Code_comparaison):#on prend le fichier du candidat et celui de comparaison
    if (os.path.getsize(Code_Candidat)) == (os.path.getsize(Code_comparaison)):#on compare les tailles des 2 fichiers
        print("Les 2 codes ont la même taille, ils sont sûrement similaires")
    else:
        print("Les 2 codes n'ont pas la même taille, continuons à analyser la fraude")

print(comparaison_code("EventCandidatA.rb","EventCandidatATest.rb"))

#on cherche
def comparaison_code_avance(Code_Candidat, Code_comparaison, Code_Annexe):
    with open(Code_Candidat) as fichier1:
        with open(Code_comparaison) as fichier2:
            fichierannexe=open(Code_Annexe,"a")
            for line1 in fichier1:
                for line2 in fichier2:
                    if line1==line2:
                        fichierannexe.write("Les lignes identiques sont : %s " %(line1))
                    elif line1 != line2:
                        fichierannexe.write("Les lignes sont différentes")

#print(comparaison_code_avance("essai1.rb","essai2.rb","essaiannexe.txt"))


def compar2(Code1,Code2,Code3):
     with open(Code1,"r") as code1:
        with open(Code2, "r") as code2:
            with open (Code3,"a") as code3:
                similarite = set(code1).intersection(code2)
                similarite.discard('\n')
                with open (Code3,"a") as code3:
                    for line in similarite:
                        code3.write("Les lignes identiques sont : %s " %line) #uniquement si il y a des similarités les renvoie dans ce cas

print(compar2("EventCandidatA.rb","EventCandidatATest.rb","essaiannexe.txt"))


