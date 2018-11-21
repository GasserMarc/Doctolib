"""def listes_de_variables(code_candidat):
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
    return (variables)

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
    return (variables)"""


"""def nombre_de_variable (code_candidat):
    variable=listes_de_variables(code_candidat)
    return (len(variable))"""


"""def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.readlines()
        fichier=" "
        for i  in range (len(lecture_code)):
            fichier+=str (lecture_code[i])
        variables= []
        for i in range (len(lecture_code)):
            if lecture_code[i] == '=':
                if i==0:
                    break
                elif i==1:
                    variables.append(lecture_code[i-1])
                else:
                    if lecture_code[i-2][-1] == "\n":
                        variables.append(lecture_code[i-1]) #cree la liste de variables
    return (variables)


print (listes_de_variables("EventCandidatA.rb"))"""


"""with open ("EventCandidatA.rb", "r" ) as code:
        lecture_code=code.readlines()
        fichier=" "
        for i  in range (len(lecture_code)):
            fichier+=(lecture_code[i])
        print (fichier)"""


def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.readlines()
        print (lecture_code)
        variables= []
        for line in lecture_code:
            print (line)
            words=line.split()
            if len (words)<2:
                pass #si il y a moins de 2 mots il ne peut pas avoir de variable
            elif words[1] == '=':
                variables.append(words[0]) #cree la liste de variables
    return (variables)

print (listes_de_variables("EventCandidatA.rb"))
