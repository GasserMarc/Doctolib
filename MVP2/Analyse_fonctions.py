''' analyse qualitative des fonctions :
détecter si le nom de la fonction revient dans le commentaire,
voir si la fonction fait plus d’une/ deux lettre(s),
ne s’appelle pas fonction, pas de majuscule '''



def list_functions(Code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    list_of_functions = []
    with open(Code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == len(mots):
            pass
        elif mots[i] == "def":
            list_of_functions.append(mots[i+1])
    return list_of_functions #renvoie la liste des fonctions et le nombre de fonctions



def trier(list_of_functions): #ne fonctionne pas
    Rlist_of_functions = []
    for function in list_of_functions:
        Rfunction = ''
        for i in list(function):
            if i not in ["\n","("]:
                Rfunction += i
            else:
                break
        # autre fonction possible : Rfunction = Rfunction.replace("\n",'')
        Rlist_of_functions += [Rfunction]
    return Rlist_of_functions

def remove_special(s):
    s1 = ''
    for i in range(len(s)):
        if s[i] in ('\n', '('):
            s1 = s[:i]
            break
    return s1

print(remove_special(list_functions('EventCandidatA.rb'))) #ne fonctionne pas pour trier les caractères speciaux"
'''print(list("nomfonction"))'''





