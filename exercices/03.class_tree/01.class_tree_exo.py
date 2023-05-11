# Import des modules nécessaires
import json
from unidecode import unidecode
import re
import os

# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
# la fonction json_dict_from_file() reste inchangée.

local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
json_str = json.dumps(json_data)
json_data = (unidecode(json_str))
json_dict = json.loads(json_data)
print(json.dumps(json_dict, indent=4))

# Fonction pour créer un arbre à partir d'un dictionnaire Python

from treelib import Tree

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)




my_tree = Tree() #  création d'un nouvel arbre
my_tree.create_node(tag="Racine", identifier="racine") # création noeud racine
create_tree_from_dict(my_tree, "racine", json_dict) # structure de l'arbre
my_tree.show() # Affiche l'arbre

