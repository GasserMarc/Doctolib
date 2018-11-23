

def caractere_ligne (code_candidat):
    """"Cette fonction permet de compter le nombre de lignes de plus de 79 caractères """
    with open(code_candidat,"r") as code :
        liste_ligne= code.readlines()
        longueur=len(liste_ligne)
        compteur=0
        for k in range(longueur):
                if len(liste_ligne[k])>= 79:
                    compteur += 1
        print(compteur,"ligne(s), soit ",compteur/longueur * 100,"%")
        #renvoie un rapport nombre de lignes longues sur nombre total de lignes
    return


