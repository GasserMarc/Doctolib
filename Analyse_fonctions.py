''' analyse qualitative des fonctions :
détecter si le nom de la fonction revient dans le commentaire,
voir si la fonction fait plus d’une/ deux lettre(s),
ne s’appelle pas fonction, pas de majuscule '''



def remove_specials(s):
    s1 = s
    for i in range(len(s1)):
        if s1[i] == '(' or s1[i] == '\n':
            s1 = s[:i]
            break
    return s1

#print(remove_special('starts_at_cannot_be_greater_than_ends_at\n'))

def list_functions(Code_candidat): #renvoie une liste de toutes les fonctions du code du candidat.
    list_of_functions = []

    with open(Code_candidat, "r") as code:
        code = code.read() #code = chaine de caractères
        mots = code.split(' ') #liste de tous les mots du code
    for i in range(len(mots)):
        if mots[i] == "def":
            list_of_functions.append(remove_specials(mots[i+1]))
    return list_of_functions #renvoie la liste des fonctions

print(len(list_functions("EventCandidatA.rb")))

'''def trier(list_of_functions): #autre possT
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
    return Rlist_of_functions'''

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

'''print(list_tests("EventCandidatATest.rb"))
line = "il a dit : \'non\'"
print(line)
pos1 = line.find
print(line.find('\''))'''

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

print(List_fonctions("EventCandidatA.rb"))
