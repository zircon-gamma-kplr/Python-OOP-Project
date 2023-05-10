from methode.products import *

# Pour la classe Chaise :

canape1 = Canape(
        cost = 1000,
        price = 2000,
        marque = "OKLM",
        materials = "Cuir",
        color = "Blanc",
        dimension = '200x100x80')
        # nom = "Canape")

canape2 = Canape(
        cost = 800,
        price = 1600,
        marque = "SIESTA",
        materials = "Tissu",
        color = "Bleu",
        dimension = '150x90x70')
        # nom = "Canape")

# Pour la classe Chaise : /workspaces/Python-OOP-Project/exercices/00.classes/main_class.py

chaise1 = Chaise(
        cost = 50,
        price = 100,
        marque = "PEPOUSE",
        materials = "Plastique",
        color = "Rouge",
        dimension = '50x50x70')
        # nom = "Chaise")

chaise2 = Chaise(
        cost = 75,
        price = 150,
        marque = "PEPOUSE",
        materials = "Métal",
        color = "Gris",
        dimension = '60x60x80')
        # nom = "Chaise")

# Pour la classe Table :

table2 = Table(
        cost = 250,
        price = 500,
        marque = "TEX",
        materials = "Bois",
        color = "Chêne",
        dimension = '150x80x75')
        

table1 = Table(
        cost = 350,
        price = 700,
        marque = "TEX",
        materials = "Verre",
        color = "Transparent",
        dimension = '120x60x75')
        

print(table1.cost)
print(chaise1.cost)

print(canape1.materials)