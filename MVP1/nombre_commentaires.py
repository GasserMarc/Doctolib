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
        if lines[0][0]=='#':
            nombre_commentaires += 1
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
