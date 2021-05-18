import pygame
from datetime import datetime
import sys

pygame.init()

def load_sprite(chemin_image):
	sprite = pygame.image.load("images/" + chemin_image + '.png').convert_alpha()

	return sprite


def move_players(keys, link_rectangle, link_R, link_L):
	link = link_R
	if keys[pygame.K_RIGHT]:
		link_rectangle = link_rectangle.move((1, 0))

	if keys[pygame.K_LEFT]:
		link = link_L
		link_rectangle = link_rectangle.move((-1, 0))

	if keys[pygame.K_LSHIFT]:
		if keys[pygame.K_RIGHT]:
			link_rectangle = link_rectangle.move((3, 0))

		if keys[pygame.K_LEFT]:
			link = link_L
			link_rectangle = link_rectangle.move((-3, 0))

	return (link_rectangle, link)

def read_map(adresse):
	fichier = open(adresse)
	carte = fichier.read()
	fichier.close()
	return carte

def afficherMap(carte, P, P_rectangle, C, T):
	collisions = []
	P_rectangle.x = 0
	P_rectangle.y = 0
	for caractere in carte:

		if caractere == "P":
			screen.blit(P, P_rectangle)
			collisions.append(pygame.Rect(P_rectangle))
		elif caractere == "C":
			screen.blit(C, P_rectangle)
			pos_clef = P_rectangle
		elif caractere == "T":
			screen.blit(T, P_rectangle)
		elif caractere == "\n":
			P_rectangle.x = -48
			P_rectangle.y += 48

		P_rectangle.x += 48
	return (collisions, P_rectangle)

screen = pygame.display.set_mode((672,768))



block = load_sprite("images")
block = pygame.transform.scale(block, (48, 48))

link_R = load_sprite("link_droite_R")
link_L = load_sprite("link_droite_L")

link_R = pygame.transform.scale(link_R, (24, 36))
link_L = pygame.transform.scale(link_L, (24, 36))

clef = load_sprite("clef")
clef = pygame.transform.scale(clef, (26, 36))

tresor = load_sprite("resor")
tresor = pygame.transform.scale(tresor, (48, 48))

clef_rectangle = clef.get_rect()
block_rectangle = block.get_rect()
link_rectangle = link_R.get_rect()

link_rectangle.y = 672
link_rectangle.x = 48

y = 0
dy = 0

carte = read_map("Carte/map")

j = 0
color = pygame.Color('white')
while True:
	color.hsva = (j%360,100,100,100)
	j += 1
	screen.fill(color)
	pygame.time.delay(20)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			sys.exit(0)
	pos_ant = pygame.Rect(link_rectangle)
	keys = pygame.key.get_pressed()
	plateformes, pos_clef = afficherMap(carte, block, block_rectangle, clef, tresor)

	link_rectangle, link = move_players(keys, link_rectangle, link_R, link_L)
	if (link_rectangle.x - pos_clef.x) ** 2 + (link_rectangle.y - pos_clef.y)**2 < 20**2:
		carte[1][1] = " "

	for plate in plateformes:
		Bool = link_rectangle.colliderect(plate)
		if Bool == True:
                        link_rectangle = pos_ant
	pos_ant = pygame.Rect(link_rectangle)

	if keys[pygame.K_SPACE] and y == 0:
		y = 1
		dy = -15

	dy += 1
	link_rectangle.y += dy

	for idCollisions in range(len(plateformes)):
		Bool = link_rectangle.colliderect(plateformes[idCollisions])
		if Bool == True:
				link_rectangle = pos_ant
				y = 0
				dy = 0

	screen.blit(link, link_rectangle)
	pygame.display.flip()
