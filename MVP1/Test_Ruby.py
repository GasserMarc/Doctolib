#compte le nombre de fonctions dans le fichier de code du candidat
def count_fonction(Code_Candidat):
    with open (Code_Candidat, "r") as code :
       texte= code.read()
       listemots= texte.split()#permet de lister tous les mots du code
       n=len(listemots)#longueur de la liste des mots à lister
       compteur=0
       for k in range (n):#pour tous les k compris dans la liste des mots à lister
            if listemots[k]== "def":
                compteur+= 1#on rajoute +1 à chaque fois que l'on comte une fonction

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







