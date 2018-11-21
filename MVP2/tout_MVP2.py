'''
Cette fonction renvoie la proportion de texte dupliqué
'''



'''
Ces fonctions indiquent la pertinence du nom des variables, si elles sont explicites ou si elles ne commencent pas par
une majuscule (convention) 
'''

def listes_de_variables(code_candidat):
    '''
    Donne la liste et le nombre des variables utilisées par le candidat
    :param code_candidat:
    :return: liste nom variables et nombre variables:
    '''
    with open (code_candidat, "r" ) as code:
        lecture_code=code.readlines()
        variables= []
        for line in lecture_code:
            words=line.split()
            if len (words)<2:
                pass #si il y a moins de 2 mots il ne peut pas avoir de variable
            elif words[1] == '=':
                variables.append(words[0]) #cree la liste de variables
    return (variables, len(variables))

print(listes_de_variables("/Users/baptiste/PycharmProjects/Doctolib/Exemples_codes/EventCandidatA.rb"))

def controle_nom_variable (code_candidat):
    '''
    On considère que le nom est explicite s'il contient plus de 2 lettres
    :param code_candidat:
    :return nb de variables mal nommées:
    '''
    variables=listes_de_variables(code_candidat)[0]
    nb_variable_mal_nommees=0 #compteur du nombre de variables mal nommées, avec des noms non explicites
    for nom_variables in variables:
        if len(nom_variables)<=1: #si les variables ont un nom non explicite, avec une lettre
            nb_variable_mal_nommees+=1
            #print (nb_variable_mal_nommees)
    return nb_variable_mal_nommees

def calcul_pourcentage_variables_mal_nommees(code_candidat):
    '''
    Pourcentage de variables mal nommées dans le code
    :param code_candidat:
    :return:
    '''
    nb_variables_mal_nommees=controle_nom_variable(code_candidat)
    variables=listes_de_variables(code_candidat)[0]
    pourcentage_mal_nommees=((nb_variables_mal_nommees*100)/len(variables))
    return pourcentage_mal_nommees

def majuscule_variable(code_candidat):
    '''
    Le nom de la variable ne commence pas par une majuscule
    :param code_candidat:
    :return:
    '''
    variables=listes_de_variables(code_candidat)
    nb_variable_majuscule=0 #compte le nombre de variables commençant par une majuscule
    for i in range (len(variables)):
        code_ascii=ord((variables[i][0]))
        if code_ascii>=65 or code_ascii<=90:
            nb_variable_majuscule=+1
    pourcentage_debut_majuscule= ((nb_variable_majuscule *100)/len(variables))
    return pourcentage_debut_majuscule


'''
Idem nom de fonctions
'''

def remove_special(s):
    '''
    Retire les ( et \n d'une chaîne de caractères ainsi que tous les caractères qui suivent
    :param s:
    :return:
    '''
    s1 = s
    for i in range(len(s1)):
        if s1[i] == '(' or s1[i] == '\n':
            s1 = s[:i]
            break
    return s1

#print(remove_special('starts_at_cannot_be_greater_than_ends_at\n'))

def list_functions(code_candidat):
    '''
    renvoie une liste de toutes les fonctions du code du candidat
    :param code_candidat:
    :return:
    '''
    list_of_functions = []
    with open(code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == "def":
            list_of_functions.append(remove_special(mots[i+1]))
    return list_of_functions, len(list_of_functions) #renvoie la liste des fonctions et le nombre de fonctions

def controle_nom_fonction(code_candidat):
    '''
    On considère que le nom est explicite s'il contient plus de 2 lettres
    :param code_candidat:
    :return nb de variables mal nommées:
    '''
    fonctions=list_functions(code_candidat)[0]
    nb_fonctions_mal_nommees=0 #compteur du nombre de variables mal nommées, avec des noms non explicites
    for nom_fonctions in fonctions:
        if len(nom_fonctions)<=1: #si les variables ont un nom non explicite, avec une lettre
            nb_fonctions_mal_nommees+=1
            #print (nb_variable_mal_nommees)
    return nb_fonctions_mal_nommees

def calcul_pourcentage_fonctions_mal_nommees(code_candidat):
    '''
    Pourcentage de fonctions mal nommées dans le code
    :param code_candidat:
    :return:
    '''
    nb_fonctions_mal_nommees=controle_nom_fonction(code_candidat)
    fonctions=list_functions(code_candidat)[0]
    pourcentage_mal_nommees=((nb_fonctions_mal_nommees*100)/len(fonctions))
    return pourcentage_mal_nommees

def majuscule_fonction(code_candidat):
    '''
    Le nom de la fonction ne commence pas par une majuscule
    :param code_candidat:
    :return:
    '''
    fonctions=list_functions(code_candidat)
    nb_fonctions_majuscule=0 #compte le nombre de variables commencant par une majuscule
    for i in range (len(fonctions)):
        code_ascii=ord((fonctions[i][0]))
        if code_ascii>=65 or code_ascii<=90:
            nb_fonctions_majuscule=+1
    pourcentage_debut_majuscule= ((nb_fonctions_majuscule *100)/len(fonctions))
    return pourcentage_debut_majuscule

