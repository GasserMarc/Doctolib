

def ratio_spaces(code_candidat):
    with open(code_candidat,'r') as code:
        text = code.read()
        N = len(text)
        n = text.count(' ')
        return (n/N)* 100

def ratio_commentaires(Code_candidat): #calcule le rapport commentaire/texte
    with open (Code_candidat, 'r') as code:
        texte = code.read()
    with open (Code_candidat, 'r') as code:
        lignes = code.readlines()
    longueur_code = len(texte)
    longueur_commentaires = 0
    for i in range(len(lignes)):
        ligne = lignes[i]
        for lettre in ligne:
            if lettre == '#':
                pos = ligne.find('#')
                l_commentaire = len(ligne[pos:]) - 1 #renvoie la longueur du commentaire en ne comptant pas '#"
                longueur_commentaires += l_commentaire
    return (longueur_commentaires/ longueur_code)*100 #renvoie un pourcentage


print(ratio_commentaires("EventCandidateB.rb"))

'''with open ("EventCandidateB.rb") as code:
    texte = code.read()
    print(len(texte))'''

'''print(ratio_spaces("EventCandidatA.rb"))
print(ratio_spaces("EventCandidateB.rb"))'''
