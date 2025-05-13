import pygame
import random

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de Blocs")

blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (200, 0, 0)
vert = (0, 200, 0)
bleu = (0, 0, 200)

horloge = pygame.time.Clock()
score = 0

class Bloc:
    def __init__(self):
        self.x = random.randint(0, largeur - 50)
        self.y = -50
        self.vitesse = random.randint(5, 15)
        self.largeur = 50
        self.hauteur = 50

    def deplacer(self):
        self.y += self.vitesse

    def afficher(self):
        pygame.draw.rect(fenetre, rouge, (self.x, self.y, self.largeur, self.hauteur))

joueur_x = largeur // 2
joueur_y = hauteur - 60
joueur_largeur = 100
joueur_hauteur = 20
joueur_vitesse = 10

blocs = []

jeu_actif = True
while jeu_actif:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_actif = False

    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        joueur_x -= joueur_vitesse
    if touches[pygame.K_RIGHT]:
        joueur_x += joueur_vitesse

    fenetre.fill(noir)

    if random.randint(1, 20) == 1:
        blocs.append(Bloc())

    for bloc in blocs[:]:
        bloc.deplacer()
        bloc.afficher()
        if bloc.y > hauteur:
            blocs.remove(bloc)
            score += 1
        if bloc.y + bloc.hauteur >= joueur_y and bloc.x in range(joueur_x, joueur_x + joueur_largeur):
            jeu_actif = False

    pygame.draw.rect(fenetre, bleu, (joueur_x, joueur_y, joueur_largeur, joueur_hauteur))

    score_texte = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, blanc)
    fenetre.blit(score_texte, (10, 10))

    pygame.display.flip()
    horloge.tick(60)

pygame.quit()
