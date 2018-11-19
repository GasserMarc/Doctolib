def listes_de_variables(code_candidat):
    with open (code_candidat, "r" ) as code:
        lecture_code=code.read()
        words=lecture_code.split(" ")
        for word in words:
            if word == '=':
                i= words.index('=') #donne l'indice du =
                print (words [i-1]) #print le nom de la variable avant le =
    return
