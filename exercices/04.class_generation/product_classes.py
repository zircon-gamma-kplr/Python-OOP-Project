class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__

class Biens Consommation(Product):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Articles Menagers(Biens Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles Menagers):
	def __init__(self, materials, color, dimensions, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materials = materials
		self.color = color
		self.dimensions = dimensions

class Canape(Meubles):
	def __init__(self, materials, color, dimensions, cost, price, marque):
		super().__init__(materials, color, dimensions, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materials, color, dimensions, cost, price, marque):
		super().__init__(materials, color, dimensions, cost, price, marque)

class Table(Meubles):
	def __init__(self, materials, color, dimensions, cost, price, marque):
		super().__init__(materials, color, dimensions, cost, price, marque)

class Appareils Electromenagers(Articles Menagers):
	def __init__(self, capacite, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacite = capacite

class Refrigerateur(Appareils Electromenagers):
	def __init__(self, efficacite, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.efficacite = efficacite

class Lave-vaisselle(Appareils Electromenagers):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Lave-linge(Appareils Electromenagers):
	def __init__(self, programme, capacite, cost, price, marque):
		super().__init__(capacite, cost, price, marque)
		self.programme = programme

class Ustensiles Cuisine(Articles Menagers):
	def __init__(self, materialsx, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materialsx = materialsx

class Casserole(Ustensiles Cuisine):
	def __init__(self, diametre, materialsx, cost, price, marque):
		super().__init__(materialsx, cost, price, marque)
		self.diametre = diametre

class Batterie Cuisine(Ustensiles Cuisine):
	def __init__(self, nombre_pieces, materialsx, cost, price, marque):
		super().__init__(materialsx, cost, price, marque)
		self.nombre_pieces = nombre_pieces

class Habillement(Biens Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vetements(Habillement):
	def __init__(self, taille, color, matiere, cost, price, marque):
		super().__init__(cost, price, marque)
		self.taille = taille
		self.color = color
		self.matiere = matiere

class Haut(Vetements):
	def __init__(self, taille, color, matiere, cost, price, marque):
		super().__init__(taille, color, matiere, cost, price, marque)

class Pantalon(Vetements):
	def __init__(self, taille, color, matiere, cost, price, marque):
		super().__init__(taille, color, matiere, cost, price, marque)

class Robe(Vetements):
	def __init__(self, taille, color, matiere, cost, price, marque):
		super().__init__(taille, color, matiere, cost, price, marque)

class Casquette(Habillement):
	def __init__(self, color, cost, price, marque):
		super().__init__(cost, price, marque)
		self.color = color

class Chaussures(Habillement):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure

