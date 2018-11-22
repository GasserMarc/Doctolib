# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
# On définit la DataFrame dans pandas pour associer les valeurs
df = pd.DataFrame({
'candidat': ['A','B','C'],
'nb_fonctions': [1, 3, 3],
'variables': [4, 2, 4],
'longueur_lignes': [2, 3, 2],
'ratio_text_fonctions': [3, 3, 3],
'boucles': [4, 1, 2],
'nombre': [3,2,3]
})
 
# On définit le nombre de variables
categories=list(df)[1:]
N = len(categories)
 
# On code la cercle extérieur du graphe
values=df.loc[0].drop('candidat').values.flatten().tolist()
values += values[:1]
values
 
# on définit l'angle entre les différentes variables
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# on initialise le graphique
ax = plt.subplot(111, polar=True)
 
# On définit l'axe des x
plt.xticks(angles[:-1], categories, color='grey', size=8)
 
# L'axe des y
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4], ["1","2","3","4"], color="grey", size=7)
plt.ylim(0,4)



# Candidat 1 en bleu
values=df.loc[0].drop('candidat').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Candidat A")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Candidat 2 en rouge
values=df.loc[1].drop('candidat').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Candidat B")
ax.fill(angles, values, 'r', alpha=0.1)

# Candidat 3 en vert
values=df.loc[2].drop('candidat').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Candidat C")
ax.fill(angles, values, 'g', alpha=0.1)

# On ajoute les légendes
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# On affiche le graphe
plt.show()
