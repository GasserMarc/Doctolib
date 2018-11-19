def count_fonction(Code_Candidat):
    with open (Code_Candidat, "r") as code :
       texte= code.read()
       listemots= texte.split()
       n=len(listemots)
       compteur=0
       for k in range (n):
            if listemots[k]== "def":
                compteur+= 1

    print("Le fichier contient " ,compteur, "fonctions")
    return (compteur)


print(count_fonction("EventCandidatA.rb"))


def count_boucles(Code_Candidat):
    with open (Code_Candidat,"r") as code :
        Ouverture2code = open(Code_Candidat, "r")
        textealire=Ouverture2code.readlines()
        Ouverture2code.close
        textealire=str(textealire)
        nombredeboucle=textealire.count("each")
        print("Le fichier contient" ,nombredeboucle, "fois une boucle")
        return(nombredeboucle)

print(count_boucles("EventCandidatA.rb"))


def nombre2commentaires(Code_Candidat):
     with open (Code_Candidat,"r") as code :
        Ouverture2code = open(Code_Candidat, "r")
        textealire=Ouverture2code.readlines()
        Ouverture2code.close
        textealire=str(textealire)
        nombredecomm=(textealire.count("#"))+(textealire.count("=end"))
        print("Le fichier contient" ,nombredecomm, "commentaires")
        return(nombredecomm)


print(nombre2commentaires("EventCandidatA.rb"))






