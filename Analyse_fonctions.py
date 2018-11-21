''' analyse qualitative des fonctions :
détecter si le nom de la fonction revient dans le commentaire,
voir si la fonction fait plus d’une/ deux lettre(s),
ne s’appelle pas fonction, pas de majuscule '''

"""def List_fonctions(Code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    List_of_functions = []
    with open(Code_candidat, "r") as code:
        lines = code.readlines() #lines = liste de toutes les lignes du code.
    for i in range(len(lines)):
        mots = lines[i].split() #mots = liste de tous les mots de la line[i]
        if mots[0] == "def":
            List_of_functions.append(mots[1])
    return List_of_functions, len(List_of_functions) #renvoie le liste des fonctions et le nombre de fonctions

print(List_fonctions("EventCandidatA.rb"))"""

def count_fonctions(Code_Candidat):
    with open (Code_Candidat,"r") as code :
        Ouverture2code = open(Code_Candidat, "r")
        textealire=Ouverture2code.readlines() #on ouvre le code du candidat et on lit toutes les lignes en renvoyant la liste de lignes
        textealire=str(textealire) #on met sous forme d'une string pour faciliter la lecture
        nombredeboucle=textealire.count("def")#on compte le nombre de boucle avec "count""
        print("Le fichier contient" ,nombredeboucle, "fonctions")
        return(nombredeboucle)

print(count_fonctions("EventCandidatA.rb"))

def List_fonctions(Code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    List_of_functions = []
    with open(Code_candidat, "r") as code:
        lines = code.readlines() #lines = liste de toutes les lignes du code.
    for i in range(len(lines)):
        mots = lines[i].split() #mots = liste de tous les mots de la line[i]
        print(mots)
    for fonctions in range(len(lines)):
        print(fonctions.text)




print(List_fonctions("EventCandidatA.rb"))
