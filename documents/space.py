import pygame  # necessaire pour charger les images et les sons
import space

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self,position,image,sens,score) :
        self.position = position
        self.image = image
        self.sens = sens
        self.score = score
    def deplacer(self):
        
    def marquer(self):
        pass
       
    
class Balle() :
    def __init__(self,tireur,depart,hauteur,image,etat) :
        self.tireur = tireur
        self.depart = depart
        self.hauteur = hauteur
        self.image = image
        self.etat = etat
    
    def bouger(self):
        pass
    
    def toucher(self,Ennemi):
        pass
class Ennemi():
    def __init(self,depart,hauteur,tipe,image,vitesse):
        self.depart = depart
        self.hauteur = hauteur
        self.tipe = tipe
        self.image = image
        self.vitesse = vitesse
        
    def avancer(self):
        
        pass
    def disparaitre(self):
        pass
    




