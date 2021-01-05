def recommandation_creation(graphe_relations):
    dico_suggestion = {}
    for cle, valeur in graphe_relations.items():
        for cle2, valeur2 in graphe_relations.items():
            if cle != cle2 :
                for personne in valeur :
                    if personne in valeur2 :
                        try:
                            if not cle2 in dico_suggestion[cle]:
                                dico_suggestion[cle].append(cle2)
                        except:
                            dico_suggestion[cle] = [cle2]
                        try:
                            if not cle in dico_suggestion[cle2]:
                                dico_suggestion[cle2].append(cle)
                        except:
                            dico_suggestion[cle2] = [cle]
    return dico_suggestion


def recommandation(graphe_relations) :
    dict = recommandation_creation(graphe_relations)
    for cle, valeur in dict.items():
        for nom in valeur:
            if not nom in graphe_relations[cle]:
                print("Le reseau social propose a ", cle, " de devenir ami avec", nom)

def trace(graphe):
    reseau_social=nx.Graph()
    for cle in graphe.keys():
        reseau_social.add_node(cle)
        for ami in graphe[cle]:
            reseau_social.add_edge(cle,ami)
    nx.draw(reseau_social, with_labels=True)
    plt.draw()
    plt.show()
	
def exploitation(graphe):
    reseau_social=nx.Graph()
    for cle in graphe.keys():
		reseau_social.add_node(cle)
	for ami in graphe[cle]:
	    reseau_social.add_edge(cle,ami)
    print("nombre de sommets=",reseau_social.number_of_nodes())
    print("nombre de aretes=",reseau_social.number_of_edges())
    print("Diametre=",diameter(reseau_social))
    print("Rayon=",radius(reseau_social))
    print("Centre=",center(reseau_social))
