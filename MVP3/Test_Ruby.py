mport os

#compte le nombre de fonctions dans le fichier de code du candidat
def count_fonction(Code_Candidat):
    with open (Code_Candidat, "r") as code :
       texte= code.read()
       listemots= texte.split()#permet de lister tous les mots du code
       n=len(listemots)#longueur de la liste des mots à lister
       compteur=0
       for k in range (n):#pour tous les k compris dans la liste des mots à lister
            if listemots[k]== "def":
                compteur+= 1#on rajoute +1 à chaque fois que l'on compte une fonction

    print("Le fichier contient " ,compteur, "fonction(s)")
    return (compteur)


print(count_fonction("EventCandidatA.rb"))

#on compte le nombre de boucles dans le code du candidat, définie par "each"
def count_boucles(Code_Candidat):
    with open (Code_Candidat,"r") as code :
        Ouverture2code = open(Code_Candidat, "r")
        textealire=Ouverture2code.readlines() #on ouvre le code du candidat et on lit toutes les lignes en renvoyant la liste de lignes
        textealire=str(textealire) #on met sous forme d'une string pour faciliter la lecture
        nombredeboucle=textealire.count("each")#on compte le nombre de boucle avec "count""
        print("Le fichier contient" ,nombredeboucle, "fois une boucle")
        return(nombredeboucle)

print(count_boucles("EventCandidatA.rb"))

#on compte le nombre de commentaires dans le code du candidat, définie par un # ou bien un =begin (...)=end
def nombre2commentaires(Code_Candidat):
     with open (Code_Candidat,"r") as code :
        Ouverture2code = open(Code_Candidat, "r")
        textealire=Ouverture2code.readlines()
        textealire=str(textealire)
        nombredecomm=(textealire.count("#"))+(textealire.count("=end"))
        print("Le fichier contient" ,nombredecomm, "commentaire(s)")
        return(nombredecomm)
print(nombre2commentaires("EventCandidatA.rb"))

#on compare 2 codes initialement et on regarde si les 2 codes font la même taille en bytes
def comparaison_code(Code_Candidat, Code_comparaison):#on prend le fichier du candidat et celui de comparaison
    if (os.path.getsize(Code_Candidat)) == (os.path.getsize(Code_comparaison)):#on compare les tailles des 2 fichiers
        print("Les 2 codes ont la même taille, ils sont sûrement similaires")
    else:
        print("Les 2 codes n'ont pas la même taille, continuons à analyser la fraude")

print(comparaison_code("EventCandidatA.rb","EventCandidatATest.rb"))

def conversionlistetochaine(chaine2caracteres):
    liste=chaine2caracteres.split()
    return liste

def comparaison_code(Code1,Code2,Code3):
    with open(Code1,"r") as code1:
        with open(Code2, "r") as code2:
            with open (Code3,"a") as code3:
                similarite = set(code1).intersection(code2)
                similarite.discard('\n')
                with open (Code3,"a") as code3:
                    compteur=0
                    for line in similarite :
                        if len(line)==0:
                            print("Il n'y aucune lignes identiques")
                        elif len(line)!=0:
                          print("Les lignes identiques sont : %s " %line)
                          compteur+=1
                    print("Le nombre de lignes identiques est : %s" %(len(line)))
                    return compteur


print(comparaison_code("essai1.rb","essai2.rb","essai3.rb"))










