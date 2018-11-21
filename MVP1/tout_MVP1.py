'''
Ce bloc de fonctions permet de renvoyer une liste avec tous les noms de fonctions utilisés dans le code par le
candidat
'''

# Cette fonction retire les ( et \n et tous les caractères suivants dans une chaine de caractères
 def remove_special(s):
    s1 = s
    for i in range(len(s1)):
        if s1[i] == '(' or s1[i] == '\n':
            s1 = s[:i]
            break
    return s1

#print(remove_special('starts_at_cannot_be_greater_than_ends_at\n'))


def list_functions(code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    list_of_functions = []
    with open(code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == "def":
            list_of_functions.append(remove_special(mots[i+1]))
    return list_of_functions, len(list_of_functions) #renvoie la liste des fonctions et le nombre de fonctions


'''
Cette fonction compte le nombre de commentaires dans le code du candidat
'''
def compte_commentaires(file_name):
    #Sur un fichier Ruby, les commentaires sont repérés par des # (comme Python) et des = sont utilisés comme des
    #triples guillemets.
    nombre_commentaires = 0
    with open(file_name,'r') as code:
        lines = code.readlines()
        # On considère les lignes adjacentes commençant par de # comme étant un seul bloc de commentaire
        # Il y a plusieurs commentaires si il y a un espace entre les lignes avec des #

        # Les commentaires en bout de ligne ne répondent pas à la convention précédente
        nb_lines = len(lines)
        for i in range(nb_lines):
            # cette boucle repère les blocs de commentaires
            # seul le premier # du bloc permet d'ajouter un commentaire
            if i>0:
                if lines[i][0]=='#':
                    if lines[i-1][0] != '#':
                        nombre_commentaires += 1
            else:
                for x in lines[i]:
                    if x == '#':
                        nombre_commentaires += 1
                        break
            # Les commentaires entre = se terminent uniquement par un =end seul sur une ligne
            if lines[i][0:4] == '=end':
                nombre_commentaires += 1
    print('Il y a ' + str(nombre_commentaires) + ' commentaires dans le code')

#print(compte_commentaires("fichier_test"))


'''
Cette fonction renvoie le nombre de tests
'''


'''
Cette fonction renvoie le nombre de boucles imbriquées utilisées par le candidat
'''


def count_boucles(code_candidat):
    #on compte le nombre de boucles dans le code du candidat, définie par "each"
    with open (code_candidat,"r") as code :
        ouverture2code = open(code_candidat, "r")
        textealire=ouverture2code.readlines() #on ouvre le code du candidat et on lit toutes les lignes en renvoyant la liste de lignes
        textealire=str(textealire) #on met sous forme d'une string pour faciliter la lecture
        nombredeboucle=textealire.count("each")#on compte le nombre de boucle avec "count""
        print("Le fichier contient" ,nombredeboucle, "fois une boucle")
        return(nombredeboucle)


'''
Cette fonction retourne le nombre de caractères par ligne : il est conseillé de ne pas en mettre plus de 79 pour
que le code soit lisible
'''
def caractere_ligne (code_candidat):
    """"Cette fonction permet de dénombrer le nombre de caractère par ligne"""
    with open(code_candidat,"r") as code :
        liste_ligne= code.readlines() # liste de ligne
        longueur=len(liste_ligne)
        compteur=0
        for k in range(longueur):
                if len(liste_ligne[k])>= 79:
                    compteur += 1
        print(compteur,"ligne(s), soit ",compteur/longueur * 100,"%")
    return


'''
Cette fonction renvoie le nom des variables utilisées par le candidat et leur nombre
'''

def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.read()
        words=lecture_code.split(" ")
        variables= []
        for i in range (len(words)):
            if words[i] == '=':
                if i==0:
                    break
                else:
                    variables.append(words[i-1]) #cree la liste de variables
    return (variables, len(variables))


def run_script_MVP_1(code_candidat):
    resultats = {}
    resultats[functionCount]=list_functions(code_candidat)
