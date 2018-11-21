''' analyse qualitative des fonctions :
détecter si le nom de la fonction revient dans le commentaire,
voir si la fonction fait plus d’une/ deux lettre(s),
ne s’appelle pas fonction, pas de majuscule '''

def remove_special(s):
    s1 = s
    for i in range(len(s1)):
        if s1[i] == '(' or s1[i] == '\n':
            s1 = s[:i]
            break
    return s1

#print(remove_special('starts_at_cannot_be_greater_than_ends_at\n'))

def list_functions(Code_candidat):
    #renvoie une liste de toutes les fonctions du code du candidat.
    list_of_functions = []
    with open(Code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == "def":
            list_of_functions.append(remove_special(mots[i+1]))
    return list_of_functions, len(list_of_functions) #renvoie la liste des fonctions et le nombre de fonctions

