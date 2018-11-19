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
                    print (words [i-1]) #print le nom de la variable avant le =
                    variables.append(words[i-1])
    return variables

def nombre_de_variable (code_candidat):
    variable=listes_de_variables(code_candidat)
    return (len(variable))

print (listes_de_variables("EventCandidatA.rb"))

