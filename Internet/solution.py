# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:33:11 2020

@author: José
"""

# importing the ExerciseFunction class
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


########## step 1
# You need to define the 'correct' function
# i.e. one that would be accepted as valid for the problem

def est_superieur(debit1, debit2):
    if debit1 > debit2:
        return True
    else:
        return False
    
def duree(quantite, debit):
    temps = quantite/debit    
    return f"Il faut {temps} secondes"

########## step 2
# You need to provide datasets
# This is expected to be a list of Args instances
# each one describes all the arguments to be passed
# to the function
# in this particular case we define 2 input sets, so
# the correction will have 2 meaningful rows
#
inputs_sup = [
    Args(12, 15),
    Args(15, 12),
    Args(0, 7),
    Args(7, 0),
]

inputs_duree = [
    Args(10, 1),
    Args(10, 2),
    Args(10, 7),
    Args(100, 10),
]

########## step 3
# finally we create the exercise object
# NOTE: this is the only name that should be imported from this module
#
exo_debit = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    est_superieur,
    # the inputs
    inputs_sup,
    result_renderer=PPrintRenderer(width=20),
)

exo_duree = ExerciseFunction(
    # first argument is the 'correct' function
    # it is recommended to use the same name as in the notebook, as the
    # python function name is used in HTML rendering 
    duree,
    # the inputs
    inputs_duree,
    result_renderer=PPrintRenderer(width=20),
)

def exo_calcul(jours, duree, debit):
    """test de la partie 1"""
    assert jours == 23, "le nombre de jours n'est pas correct : il faut 10 jours pour le chargement, 10 pour le déchargement et 3 pour le transit. Ca fait combien au total ?"        
    assert duree == 1987200, "le nombre de secondes n'est pas bon.\n Indice : dans 1 journée, il y a 24 * 3600 secondes. Reprenez la cellule permettant de calculer la durée"
    assert round(debit, 3) == 5.032, "le débit n'est pas bon.\n Indice : Le débit se calcule en divisant la quantité de donnée (quel est le nom de la variable ?) par un temps (quel est le nom de la donnée ?)"
    
    print("Bravo !\n Tous les tests ont réussi.\n Tu as super bien travaillé pour l'instant !")
    
def exo_adsl_fibre(debit_ADSL, debit_fibre):
    """test de la partie 2"""
    assert debit_ADSL == 1.875e-3, "le débit ADSL n'est pas bon.\n Indice : un débit de 8 Mbits/s correspond à 1 Go/s"
    assert debit_fibre != 1.25e-3, "le débit ADSL n'est pas bon.\n Indice : un débit de 8 Gbits/s correspond à 1 Go/s"
    
    print("Bravo !\n Tous les tests ont réussi.\n Tu as une nouvelle fois bien travaillé ! \n Attention, ça devient plus difficile ;)")
    