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



def compte_lignes_non_code(code_candidat):
    """
    Cette fonction renvoie le nombre de lignes qui ne contiennent pas de code à proprement parler
    :param code_candidat:
    :return:
    """
    nombre_lignes_non_code = 0
    with open(code_candidat,'r') as code:
        lines = code.readlines()
        print(lines)
        for line in lines:
            if line == '\n':
                nombre_lignes_non_code += 1
            words = line.split()
            try:
                if words[0]=="#":
                    nombre_lignes_non_code += 1
            except IndexError:
                pass
        return nombre_lignes_non_code

