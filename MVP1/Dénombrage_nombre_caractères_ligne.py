

def caractere_ligne (code_candidat):
    """"Cette fonction permet de dénombrer le nombre de caractère par ligne"""
    with open(code_candidat,"r") as code :
        liste_ligne= code.readlines() # liste de ligne
        longueur=len(liste_ligne)
        compteur=0
        for k in range(longueur):
                if len(liste_ligne[k])>= 79:
                    compteur += 1
        print(compteur,"ligne(s), soit ",compteur/longueur * 100,"%")
    return


