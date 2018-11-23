# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from MVP4.analyse_finale import *

# On définit la DataFrame dans pandas pour associer les valeurs
dico = dico_graphe(["../Exemples_codes/EventCandidatA.rb",
                                         "../Exemples_codes/EventCandidateB.rb",
                                         "../Exemples_codes/EventCandidateC.rb"])

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
    values=df.loc[i].drop('candidats').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=dico['candidats'][i])
    ax.fill(angles, values, alpha=0.1)

# On ajoute les légendes
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Notes candidats")

# On affiche le graphe
plt.show()
