# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from MVP4.analyse_finale import *

# On définit la DataFrame dans pandas pour associer les valeurs

df = pd.DataFrame.from_dict(dico_graphe(["../Exemples_codes/EventCandidatA.rb",
                                         "../Exemples_codes/EventCandidateB.rb",
                                         "../Exemples_codes/EventCandidateC.rb"]))
"""
df=pd.DataFrame({'group': ['A','B','C','D'],
'var1': [38, 1.5, 30, 4],
'var2': [29, 10, 9, 34],
'var3': [8, 39, 23, 24],
'var4': [7, 31, 33, 14],
'var5': [28, 15, 32, 14]
})
"""

code_candidats = ["../Exemples_codes/EventCandidatA.rb",
                                         "../Exemples_codes/EventCandidateB.rb",
                                         "../Exemples_codes/EventCandidateC.rb"]


for code in code_candidats:
    if comparaison_code(code)>0.25:
        print("ATTENTION : RISQUE DE FRAUDE")
        print("Le fichier "+code+" présente un taux de similarité de " + str(comparaison_code(code)) +
              " avec les codes de la base de données.")

dico = dico_graphe(code_candidats)


df = pd.DataFrame.from_dict(dico)

# On définit le nombre de variables
categories=list(df)[1:]
N = len(categories)

# On code la cercle extérieur du graphe
values=df.loc[0].drop('candidats').values.flatten().tolist()
values += values[:1]
values

# on définit l'angle entre les différentes variables
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# on initialise le graphique
ax = plt.subplot(111, polar=True)

# On définit l'axe des x
plt.xticks(angles[:-1], categories, color='grey', size=6)

# L'axe des y
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4], ["1","2","3","4"], color="grey", size=7)
plt.ylim(0,4)


for i in range(len(dico['candidats'])):
    moy_candidat = moyenne_coefficients(code_candidats[i])
    values=df.loc[i].drop('candidats').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=dico['candidats'][i]+' : Note = '+str(moy_candidat)[:4])
    ax.fill(angles, values, alpha=0.1)

# On ajoute les légendes
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Evaluation des candidats")

# On affiche le graphe
plt.show()
