''' analyse qualitative des fonctions :
détecter si le nom de la fonction revient dans le commentaire,
voir si la fonction fait plus d’une/ deux lettre(s),
ne s’appelle pas fonction, pas de majuscule '''

def List_fonctions(Code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    List_of_functions = []
    with open(Code_candidat, "r") as code:
        lines = code.readlines() #lines = liste de toutes les lignes du code.
    for i in range(len(lines)):
        mots = lines[i].split() #mots = liste de tous les mots de la line[i]
        if mots[0] == "def":
            List_of_functions.append(mots[1])
    return List_of_functions, len(List_of_functions) #renvoie le liste des fonctions et le nombre de fonctions


