def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.read()
        words=lecture_code.split(" ")
        for i in range (len(words)):
            if words[i] == '=':
                print (i)
                if i==0:
                    break
                else:
                    print (words [i-1]) #print le nom de la variable avant le =
    return

print (listes_de_variables("EventCandidatA.rb"))

