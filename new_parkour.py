import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()


blanc = pygame.Color(255,255,255)
rouge = pygame.Color(230,0,0)
gris = pygame.Color(140,140,140)

x , y = 50 , 400
x_change , y_change = 0 , 0

continuer = True

temps_saut = 40
act_temps_saut = False
touche_gris_re_saut = False

block_saut = False
continuer_tomber = False
cpt_continuer_tomber_physique = 0
act_physique = False

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				x_change = -3
			if event.key == K_RIGHT:
				x_change = 3
			if event.key == K_UP:
				if block_saut == False:
					y_change = -3
					act_temps_saut = True
		if event.type == KEYUP:
			if event.key == K_RIGHT or event.key == K_LEFT:
				x_change = 0
			if event.key == K_UP:
				act_physique = True
				temps_saut = 40
				y_change = 2
				act_temps_saut = False
				touche_gris_re_saut = True
				block_saut = True
	
	#~ si le joueur a sauter le plus longtemps possible :
	if act_temps_saut:
		temps_saut -= 1
		if temps_saut == 0:
			y_change = 2
			block_saut = True
			touche_gris_re_saut = True
			act_physique = True
		
	
	if touche_gris_re_saut == True:
		if window.get_at((x,y+41)) == gris or window.get_at((x+20,y+41)) == gris or window.get_at((x+41,y+41)) == gris:
			y_change = 0
			block_saut = False
			touche_gris_re_saut = False
			temps_saut = 40
			act_physique = False
			cpt_continuer_tomber_physique = 0
			act_temps_saut = False
	
	if act_temps_saut == False:
		if window.get_at((x,y+41)) == blanc and window.get_at((x+20,y+41)) == blanc and window.get_at((x+41,y+41)) == blanc:
			block_saut = True
			touche_gris_re_saut = True
			y_change = 2
			act_physique = True
		
	
	if act_physique:
		cpt_continuer_tomber_physique += 1
		if cpt_continuer_tomber_physique == 5:
			y_change += 1
			cpt_continuer_tomber_physique = 0
	
	x += x_change
	y += y_change
	
	if x > 774:
		x -=3
		x_change = 0
	if x < 26:
		x += 3
		x_change = 0
	if y > 474:
		y -= 2
		y_change = 0
	if y < 26:
		y += 2
		y_change = 0
	
	window.fill(blanc)
	pygame.draw.rect(window, gris,(0,440,800,60))
	pygame.draw.rect(window, gris,(70,370,400,40))
	pygame.draw.rect(window, rouge,(x,y,40,40))
	pygame.display.update()
	clock.tick(30)
	
	
