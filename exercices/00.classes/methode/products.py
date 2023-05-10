# 1. Créez un nouveau fichier Python et nommez-le "products.py".
# 2. Définissez la classe Product avec ses attributs cost, price, et marque dans la méthode init.

class Product:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque


# 3. Définissez la classe Meubles en tant que sous-classe de la classe 
# Product, en utilisant le mot-clé "class Meubles(Product):".
# 4. Définissez la méthode init de la classe Meubles en appelant la méthode 
# init de la classe parent avec le super().init(cost, price, marque).
# 5. Ajoutez les attributs spécifiques à la classe Meubles,
# tels que les matériaux, la color et les dimension.
# 6. Répétez les étapes 3 à 5 pour les classes Canape, Chaise et Table.

class Meubles(Product):
    def __init__(self, cost, price, marque, materials, color, dimension):
        super().__init__(cost, price, marque)
        self.materials = materials
        self.color = color
        self.dimension = dimension

    

class Canape(Product):
    def __init__(self, cost, price, marque, materials, color, dimension):
        super().__init__(cost, price, marque)
        self.materials = materials
        self.color = color
        self.dimension = dimension

class Chaise(Product):
    def __init__(self, cost, price, marque, materials, color, dimension):
        super().__init__(cost, price, marque)
        self.materials = materials
        self.color = color
        self.dimension = dimension

class Table(Product):
    def __init__(self, cost, price, marque, materials, color, dimension):
        super().__init__(cost, price, marque)
        self.materials = materials
        self.color = color
        self.dimension = dimension
