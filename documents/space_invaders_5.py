import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application
import time 
# lancement des modules inclus dans pygame
pygame.init() 
"""
https://pixabay.com/fr/music/
bruitage = pygame.mixer.Sound("audio/bruitage.mp3")
bruitage.play()
"""
# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load('background.png')
fond2 = pygame.image.load('fond2.png') #Utiliser quand le joueur a 5 points de score
fond3 = pygame.image.load('fond3.png') #Utiliser quand le joueur a 10 ou 15points point de score 

# creation du joueur
player = space.Joueur()
# creation de la balle
police = pygame.font.SysFont("arial", 15) # créatin d'une police
victoire = pygame.font.SysFont("arial",90)
police_niveau = pygame.font.SysFont("arial", 15)
#police_pdv = pygame.font.SysFont("arial",15)
victoire_x = -100
texte_victoire = victoire.render("VICTOIRE !!!",True,"yellow")
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
joueur_niveau = space.Ennemi()
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond2,(0,0))
    
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

    if player.score == 5:
        joueur_niveau.mes_niveaux()
        for indice in range(space.Ennemi.NbEnnemis*2):
            vaisseau = space.Ennemi()
            listeEnnemis.append(vaisseau)
            
    if player.score == 10:
        for indice in range(space.Ennemi.NbEnnemis*3):
            vaisseau = space.Ennemi()
            listeEnnemis.append(vaisseau)
            
    if player.score == 15:
        for indice in range(space.Ennemi.NbEnnemis*4):
            vaisseau = space.Ennemi()
            listeEnnemis.append(vaisseau)
        
        
            
        
    if 5 <= player.score < 10:
        screen.blit(fond,(0,0))

    if player.score >= 10:
        screen.blit(fond3, (0,0))
    
    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
    
    texte = police.render(f"Score = {player.score} points",True,"red") # information de la police 
    texte_niveaux = police_niveau.render(f"Niveau = Level {joueur_niveau.niveau}",True,"red")
    #texte_pdv = police_pdv.render(f"Points de vie = {?} pdv ",True,"red")
    screen.blit(texte,(700,10))
    screen.blit(texte_niveaux,(700,35))
    #screen.blit(texte_pdv,(685,50))
    
   
        
    if player.score >= 20:
        
        if victoire_x!=270:
            time.sleep(1)
            victoire_x+=135
            screen.blit(texte_victoire, (victoire_x,249))
            
        if victoire_x >=750:
            victoire_x=-100
        
        
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
     
    pygame.display.update() # pour ajouter tout changement à l'écran
