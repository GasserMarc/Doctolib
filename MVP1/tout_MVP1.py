'''
Ce bloc de fonctions permet de renvoyer une liste avec tous les noms de fonctions utilisées dans le code par le
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
    return list_of_functions #renvoie la liste des fonctions et le nombre de fonctions


'''
Cette fonction compte le nombre de commentaires dans le code du candidat
'''
def compte_commentaires(file_name):
    """Sur un fichier Ruby, les commentaires sont repérés par des # (comme Python) et des = sont utilisés comme des
    triples guillemets."""
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
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    try:
                        if lines[i-1][j] != '#':
                            nombre_commentaires += 1
                        break
                    except IndexError:
                        nombre_commentaires+=1
                        break
            # Les commentaires entre = se terminent uniquement par un =end seul sur une ligne
            if lines[i][0:4] == '=end':
                nombre_commentaires += 1
    #print('Il y a ' + str(nombre_commentaires) + ' commentaires dans le code')
    return nombre_commentaires


'''
Cette fonction renvoie la liste des tests effectués
'''
def list_tests(tests_candidat):
    with open (tests_candidat, "r" ) as tests:
        lecture_tests = tests.readlines()
        list_of_tests = []
        for line in lecture_tests:
            words = line.split()
            if len(line) < 2: #il y a nécessairement plus de 1 mot sur une ligne définissant un test.
                pass
            elif words[0] == 'test':
                pos1 = line.find('"')
                borne = pos1+1 # on démarre la nouvelle recherche à partir de l'élément suivant '"'
                newline = line[borne:]
                pos2 = newline[pos1:].find('"')
                list_of_tests.append(line[borne:pos2])
    return list_of_tests


'''
Cette fonction renvoie le nombre de boucles imbriquées utilisées par le candidat
'''


def count_boucles(code_candidat):
    #on compte le nombre de boucles dans le code du candidat, définies par "each"
    with open (code_candidat,"r") as code :
        textealire=code.readlines() #on ouvre le code du candidat et on lit toutes les lignes en renvoyant la liste de lignes
        textealire=str(textealire) #on met sous forme d'une string pour faciliter la lecture
        nombredeboucle=textealire.count(".each")#on compte le nombre de boucle avec "count""
        #print("Le fichier contient" ,nombredeboucle, "boucle(s)")
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
        #print(compteur,"ligne(s), soit ",compteur/longueur * 100,"%")
    return compteur


'''
Cette fonction renvoie le nom des variables utilisées par le candidat
'''

def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.readlines()
        variables= []
        for line in lecture_code:
            words=line.split()
            if len (words)<2:
                pass #si il y a moins de 2 mots il ne peut pas avoir de variable
            elif words[1] == '=':
                variables.append(words[0]) #cree la liste de variables
    return (variables)


def run_script_MVP_1(code_candidat):
    '''
    Cette fonction prend le code du candidat et renvoie un dictionnaire qui renvoie toutes les caractéristiques
    évaluées par les autres fonctions du programme
    :param code_candidat:
    :return:
    '''
    resultats = {}
    if len(list_functions(code_candidat)) != 0:
        resultats['functionCount']=len(list_functions(code_candidat))
    if len(list_tests(code_candidat)) != 0:
        resultats['testCount']=len(list_tests(code_candidat))
    resultats['commentCount']=compte_commentaires(code_candidat)
    resultats['loopCount']=count_boucles(code_candidat)
    resultats['tooLongLines']=caractere_ligne(code_candidat)
    resultats['variableCount']=len(listes_de_variables(code_candidat))
    print(resultats)
    return resultats


print(run_script_MVP_1("EventCandidatA.rb"))



