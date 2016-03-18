# -*- coding: utf-8 -*-
import random
class JeuDeCartes:
    """ classe pour la mise en place d'un jeu de cartes"""
    def __init__(self):
        self.cartes=[]
        self.t1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.t2 = [0, 1, 2, 3]
        for l in self.t1:
            for v in self.t2:
                self.cartes.append((l, v))

    def nom_carte(self, tuples):
        """cette fonction revoie lenom de la carte en recevant comme argument le numéro et la couleur de la carte"""
        self.dico = {11:"Valet", 12: "Dame", 13: "Roi", 14: "As"}
        self.dica = {0 : "Pique", 1 : "Trèfle", 2 : "Carreau", 3 : "Coeur"}
        if(tuples[0] > 10):
            chiffre_carte = self.dico[tuples[0]] + " de " + self.dica[tuples[1]]
        else:
            chiffre_carte = str(tuples[0]) + " de " + self.dica[tuples[1]]
        return chiffre_carte

    def battre(self):
        """cette fonction servira de battre c'est à dire mélanger les cartes"""
        random.shuffle(self.cartes)

    def tirer(self):
    	"""fonction permettant de tirer une carte du jeu de cartes"""
    	if self.cartes:
    		crt = self.cartes[0]
    		del self.cartes[0]
    		return crt
    	else:
    		return None	



class Joueur:

	def __init__(self, jeu):
		self.jeu = jeu
		self.score = 0
		self.nom = 'personne'

	def setNom(self, nom):
		self.nom = nom



        




if __name__ == '__main__':
    A = Joueur(JeuDeCartes())
    B = Joueur(JeuDeCartes())

    A.setNom(raw_input("Entrer le nom du 1er joueur: "))
    B.setNom(raw_input("Entrer le nom du 2eme joueur: "))

    carte_init = A.jeu.cartes[:]
    A.jeu.battre()
    B.jeu.battre()
    for i in range(52):
    	ca = A.jeu.tirer()
    	cb = B.jeu.tirer()
    	#print "{} et {}".format(ca, cb)
    	print  "{} et {}".format(A.jeu.nom_carte(ca), B.jeu.nom_carte(cb))
    	indA = carte_init.index(ca)
    	indB = carte_init.index(cb)
    	if indA > indB:
    		A.score += 1
    	elif indA < indB:
    		B.score += 1
    	print "{} et {}".format(A.score, B.score)

    if A.score > B.score:
    	print "{} est vainqueur et a obtenu {}".format(A.nom, A.score)
    elif A.score < B.score:
    	print "{} est vainqueur et a obtenu {}".format(B.nom, B.score)
    else:
    	print "Match nul !!!!"


        
