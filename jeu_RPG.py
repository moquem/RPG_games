import pygame
from datetime import datetime
import sys

pygame.init()


def load_sprite(chemin_image):
    sprite = pygame.image.load("images/" + chemin_image + ".png").convert_alpha()
    return sprite



def move_players_R(image_rectangle, y):
    if y == 0:
        Nino = Nino_Droite_1
    else:
        Nino = Nino_Droite_2
    if keys[pygame.K_LSHIFT]:
        image_rectangle = image_rectangle.move((3, 0))
    else:
        image_rectangle = image_rectangle.move((2, 0))
    return Nino, image_rectangle, 2


def move_players_H(image_rectangle, y):
    if y == 0:
        Nino = Nino_Haut_Droit
    else:
        Nino = Nino_Haut_Gauche
    if keys[pygame.K_LSHIFT]:
        image_rectangle = image_rectangle.move((0, -3))
    else:
        image_rectangle = image_rectangle.move((0, -2))
    return Nino, image_rectangle, 0

def move_players_L(image_rectangle, y):
    if y == 0:
        Nino = Nino_Gauche_1
    else:
        Nino = Nino_Gauche_2
    if keys[pygame.K_LSHIFT]:
        image_rectangle = image_rectangle.move((-3, 0))
    else:
        image_rectangle = image_rectangle.move((-2, 0))
    return Nino, image_rectangle, 1

def move_players_B(image_rectangle, y):
    if y == 0:
        Nino = Nino_Avant_Droit
    else:
        Nino = Nino_Avant_Gauche
    if keys[pygame.K_LSHIFT]:
        image_rectangle = image_rectangle.move((0, 3))
    else:
        image_rectangle = image_rectangle.move((0, 2))
    return Nino, image_rectangle, 3


def deplacement(Nino_rectangle, y, direction):

            pos_ant = pygame.Rect(Nino_rectangle)

            if keys[pygame.K_UP]:
                Nino, Nino_rectangle, direction = move_players_H(Nino_rectangle, y)

            elif keys[pygame.K_LEFT]:
                Nino, Nino_rectangle, direction = move_players_L(Nino_rectangle, y)

            elif keys[pygame.K_RIGHT]:
                Nino, Nino_rectangle, direction = move_players_R(Nino_rectangle, y)

            elif keys[pygame.K_DOWN]:
                Nino, Nino_rectangle, direction = move_players_B(Nino_rectangle, y)

            else:
                if direction == 0:
                    Nino = Nino_Haut
                elif direction == 1:
                    Nino = Nino_Gauche
                elif direction == 2:
                    Nino = Nino_Droite
                else:
                    Nino = Nino_Avant

            return pos_ant, Nino, direction, Nino_rectangle





def load_sound(chemin_sound):
    musique = pygame.mixer.Sound("sound/" + chemin_sound + ".wav")
    return musique


def read_map(adresse):
	fichier = open("Carte/" + adresse + ".txt")
	carte = fichier.read()
	fichier.close()
	return carte


def afficherMap(carte, P_rectangle):
        collisions_M = []
        collisions_A = []
        collisions_B = []
        P_rectangle.x = -20
        P_rectangle.y = -2
        for caractere in carte:
            if caractere == "M":
                collisions_M.append(pygame.Rect(P_rectangle))

            elif caractere == "B":
                collisions_B.append(pygame.Rect(P_rectangle))

            elif caractere == "A":
                collisions_A.append(pygame.Rect(P_rectangle))

            elif caractere == "\n":
                P_rectangle.x = -20
                P_rectangle.y += 2

            P_rectangle.x += 10
        return (collisions_M, collisions_A, collisions_B)


screen = pygame.display.set_mode((600,400))

################################################### images ###############################################################

#Moe
mae = load_sprite("Mae_Avant_Droit")
Mae_Avant_Droit = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("Mae_Avant_Gauche")
Mae_Avant_Gauche = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("Mae_Avant")
Mae_Avant = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("Mae_Arriere")
Mae_Haut = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("Mae_Arriere_Gauche")
Mae_Haut_Gauche = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("Mae_Arriere_Droit")
Mae_Haut_Droit = pygame.transform.scale(mae, (34, 52))
mae = load_sprite("maena")
Mae_image = pygame.transform.scale(mae, (240, 360))



#Nino
nino = load_sprite("Nino_Avant_Droit")
Nino_Avant_Droit = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Avant_Gauche")
Nino_Avant_Gauche = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Avant")
Nino_Avant = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Arriere")
Nino_Haut = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Arriere_Gauche")
Nino_Haut_Gauche = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Arriere_Droit")
Nino_Haut_Droit = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Droite_1")
Nino_Droite_1 = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Droite_2")
Nino_Droite_2 = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Gauche_1")
Nino_Gauche_1 = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Gauche_2")
Nino_Gauche_2 = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Gauche")
Nino_Gauche = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("Nino_Droite")
Nino_Droite = pygame.transform.scale(nino, (34, 52))
nino = load_sprite("nino")
Nino_image = pygame.transform.scale(nino, (240, 360))




#Map Entrées
ecran_entree = load_sprite("ecran_entree")
ecran_entree = pygame.transform.scale(ecran_entree, (600, 832))



#Map Grotte
halo = load_sprite("halo")
grotte_intro = load_sprite("grotte_intro")
grotte_intro = pygame.transform.scale(grotte_intro, (600, 400))
grotte_intro2 = load_sprite("grotte_intro2")
grotte_intro2 = pygame.transform.scale(grotte_intro2, (600, 400))
grotte_lab_1 = load_sprite("grotte_lab_1")
grotte_lab_1 = pygame.transform.scale(grotte_lab_1, (600, 400))
grotte_lab_2 = load_sprite("grotte_lab_2")
grotte_lab_2 = pygame.transform.scale(grotte_lab_2, (600, 400))

#Map Prairie
prairie_1 = load_sprite("prairie_1")
prairie_1 = pygame.transform.scale(prairie_1, (610, 400))
monstre = load_sprite("monstre1_Haut")
monstre1_Haut = pygame.transform.scale(monstre, (47, 52))
monstre = load_sprite("monstre1_Bas")
monstre1_Bas = pygame.transform.scale(monstre, (47, 52))
monstre = load_sprite("monstre1_Bas_Gauche")
monstre1_Bas_Gauche = pygame.transform.scale(monstre, (47, 52))
monstre = load_sprite("monstre1_Bas_Droite")
monstre1_Bas_Droit = pygame.transform.scale(monstre, (47, 52))

#Map Village
maison_1 = load_sprite("maison_1")
maison_1 = pygame.transform.scale(maison_1, (600, 400))


#Map Autres
text_box = load_sprite("text_box")
text_box = pygame.transform.scale(text_box, (600, 75))
case = load_sprite("case")
case = pygame.transform.scale(case, (10, 2))
emoticone_interro = load_sprite("emoticone_interro")
emoticone_exclam = load_sprite("emoticone_exclam")
fond = load_sprite("fond")
case_menu = load_sprite("case_menu")




# coordonnées images
Nino_rectangle = Nino_Avant.get_rect()
Mae_rectangle = Mae_Avant.get_rect()
case_rectangle = case.get_rect()
text_rectangle = text_box.get_rect()
text_rectangle.x = 0
text_rectangle.y = 325
text_coord = (10, 330)
prairie = prairie_1.get_rect()
prairie.x = -5
prairie.y = 0
Monstre_rectangle = monstre1_Haut.get_rect()



# audio
child_of_light = load_sound("child_of_light")
son_Intro = load_sound("intro")
son_Part_1 = load_sound("part_1")
oiseaux = load_sound("oiseaux")
home = load_sound("home")
battle_1 = load_sound("battle_1")
game_over = load_sound("game_over")
julia = load_sound("julia")


son_Intro.set_volume(0.3)


color = pygame.Color("black")

y = 0

police = "ressource_police/police.ttf"

######Enlever après

x = 1300
Nino = Nino_Avant
Maena = Mae_Avant
dialogue = 1
direction = 0
Nino_rectangle.x = 300
Nino_rectangle.y = 200
partie = 0

#######################################################################  JEU \o/  ####################################################################################


while True:
    screen.fill(color)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()




    # Première page
    if partie == 0:
        child_of_light.play()
        text = pygame.font.Font(police, 14)
        text = text.render("Appuyez sur entrée", 1, (255, 255, 255))
        screen.blit(text, (413, 370))
        if keys[pygame.K_RETURN]:
                child_of_light.stop()
                son_Intro.play()
                partie = 1
                y = 0
                x = 0
                sous_Partie = 0



    # Intro
    if partie == 1:

        pygame.time.delay(15)
        screen.blit(ecran_entree, (0, -(x%416)))

        if y == 0:
            screen.blit(Mae_Avant_Droit, (275, 150))
            screen.blit(Nino_Avant_Droit, (310, 149))
            x += 1

            if x % 20 == 0:
                y = 1

        else:
             screen.blit(Mae_Avant_Gauche, (275, 150))
             screen.blit(Nino_Avant_Gauche, (310, 149))
             x += 1
             if x % 20 == 0:
                 y = 0

        if sous_Partie == 0:

            if keys[pygame.K_RETURN] and x > 30:
                partie += 1
                Nino_rectangle.x = 282
                Nino_rectangle.y = 177
                Nino = Nino_Avant
                sous_Part = 0
                x = 0
                son_Intro.stop()
                son_Part_1.play()

            elif keys[pygame.K_e] and x > 30:
                sous_Partie = 1

            screen.blit(case_menu,(205, 260))
            screen.blit(case_menu,(205, 295))
            text1 = pygame.font.Font(police, 14)
            text1 = text1.render("Entrée : commencer le jeu", 1, (255, 255, 255))
            text2 = pygame.font.Font(police, 14)
            text2 = text2.render("Bouton E : Menu d'aide", 1, (255, 255, 255))
            screen.blit(text1, (210, 261))
            screen.blit(text2, (212, 296))

        elif sous_Partie == 1:
            screen.blit(fond, (0,0))
            if keys[pygame.K_ESCAPE]:
                sous_Partie = 0
            text = pygame.font.Font(police, 14)
            echap = text.render("<- ECHAP", 1, (255, 255, 255))
            screen.blit(echap, (10, 10))
            text = pygame.font.Font(police, 14)
            sauvegarde = text.render("- Le jeu n'inclut pas de système de sauvegarde.", 1, (255, 255, 255))
            text = pygame.font.Font(police, 14)
            acc = text.render("- Appuyez sur SHIFT pour accélérer.", 1, (255, 255, 255))
            text = pygame.font.Font(police, 14)
            dialogue = text.render("- Appuyez sur ENTREE lors des dialogues pour continuer.", 1, (255, 255, 255))
            text = pygame.font.Font(police, 14)
            direction = text.render("- Déplacez-vous avec les touches directionnelles.", 1, (255, 255, 255))
            screen.blit(sauvegarde, (50,180))
            screen.blit(direction, (50,210))
            screen.blit(acc, (50, 240))
            screen.blit(dialogue, (50, 270))












    # Début Grotte
    if partie == 2:
        x += 1
        if x > 1500:
            pygame.time.delay(10)
            screen.blit(grotte_intro, (0, 0))
            screen.blit(halo, (226, 187))
            carte = read_map("grotte_intro")
            collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)

            if sous_Part == 0:
                text = pygame.font.Font(police, 14)
                text = text.render("Nino : ... Où suis-je ?", 1, (255, 255, 255))
                screen.blit(text_box, text_rectangle)
                screen.blit(text, text_coord)
                if keys[pygame.K_RETURN] and x > 50:
                    sous_Part = 1
                    direction = 0

            else:
                if x % 18 == 0:
                    if y == 1:
                        y = 0
                    else:
                        y = 1
                pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)

                for mur in collisions_M:
                    Bool = Nino_rectangle.colliderect(mur)
                    if Bool:
                        Nino_rectangle = pos_ant


                for porte in collisions_A:
                    Bool = Nino_rectangle.colliderect(porte)
                    if Bool:
                        Nino_rectangle.x = 282
                        Nino_rectangle.y = 330
                        Maena = Mae_Haut
                        Mae_rectangle.x = 282
                        Mae_rectangle.y = 120
                        x = 0
                        partie = 3


            screen.blit(Nino, Nino_rectangle)


    if partie == 3:
        x += 1
        pygame.time.delay(10)
        screen.blit(grotte_intro2, (0, 0))
        screen.blit(halo, (226, 130))
        carte = read_map("grotte_intro_2")
        collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)

        if sous_Part == 1:
            if x % 18 == 0:
                if y == 1:
                    y = 0
                else:
                    y = 1
            pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)

            for mur in collisions_M:
                Bool = Nino_rectangle.colliderect(mur)
                if Bool:
                    Nino_rectangle = pos_ant


            for porte in collisions_B:
                Bool = Nino_rectangle.colliderect(porte)
                if Bool:
                    x = 0
                    sous_Part = 2
                    dialogue = 0
                    Nino = Nino_Haut
                    z = 0


            screen.blit(Maena, Mae_rectangle)
            screen.blit(Nino, Nino_rectangle)

        if sous_Part == 2:
            z += 1
            if x < 80:
                Maena = Mae_Avant
                screen.blit(emoticone_interro, (305, 110))
                screen.blit(Maena, Mae_rectangle)
                screen.blit(Nino, Nino_rectangle)

            else:

                screen.blit(Maena, Mae_rectangle)
                screen.blit(Nino, Nino_rectangle)
                screen.blit(fond, (0,0))
                screen.blit(Nino_image, (5, 40))
                screen.blit(Mae_image, (345, 45))
                screen.blit(text_box, text_rectangle)
                text = pygame.font.Font(police, 14)
                text2 = pygame.font.Font(police, 14)

                if dialogue == 0:
                    texte = text.render("Moe : Bienvenue Lucie, je m'appelle Moe et je serai ton gui...", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 1
                        z = 0
                elif dialogue == 1:
                    texte = text.render("Moe : Euh, tu n'es pas vraiment Lucie ?", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 2
                        z = 0
                elif dialogue == 2:
                    texte = text.render("Nino : ...Euh non, je m'appelle Nino.", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 3
                        z = 0
                elif dialogue == 3:
                    texte = text.render("Moe : Mince, ce n'est pas normal.", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 4
                        z = 0
                elif dialogue == 4:
                    texte = text.render("Nino : Pourquoi ? Où sommes-nous ?", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 5
                        z = 0
                elif dialogue == 5:
                    texte = text.render("Moe: Nous sommes au Trib... hum dans un rêve, oui c'est ça,", 1, (255, 255, 255))
                    texte2 = text2.render("tu es dans un rêve, mais je vais te sortir d'ici.", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 6
                        z = 0
                elif dialogue == 6:
                    texte = text.render("Nino : Pourquoi ? Si ce n'est qu'un rêve je n'ai qu'à", 1, (255, 255, 255))
                    texte2 = text2.render("attendre.", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 7
                        z = 0
                elif dialogue == 7:
                    texte = text.render("Moe : Ce n'est pas si simple. Un rêve peut vite devenir", 1, (255, 255, 255))
                    texte2 = text2.render("un cauchemar", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 8
                        z = 0

                elif dialogue ==8:
                    texte = text.render("Moe : Mais ne t'inquiète pas, suis moi !", 1, (255, 255, 255))
                    texte2 = text2.render("", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN] and z > 20:
                        dialogue = 9

                elif keys[pygame.K_RETURN] and dialogue == 9:

                    sous_Part = 3
                    x = 0
                    y = 0
                    w = 0

                screen.blit(texte, text_coord)
                screen.blit(texte2, (10, 347))

        if sous_Part == 3:
            if Mae_rectangle.y > 35:
                screen.blit(Maena, Mae_rectangle)
            if x % 18 == 0 :
                if w == 0:
                    w = 1
                else:
                    w = 0
            if w == 0:
                Maena = Mae_Haut_Gauche
            else:
                Maena = Mae_Haut_Droit

            Mae_rectangle = Mae_rectangle.move((0, -1.5))


            if x % 23 == 0:
                if y == 1:
                    y = 0
                else:
                    y = 1

            pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)


            for mur in collisions_M:
                Bool = Nino_rectangle.colliderect(mur)
                if Bool:
                    Nino_rectangle = pos_ant


            for porte in collisions_A:
                Bool = Nino_rectangle.colliderect(porte)
                if Bool:
                    partie = 4
                    Nino_rectangle.y = 338
                    Nino = Nino_Haut
                    direction = 0
                    labyrinthe = 0
                    x = 0
                    a = 0

            Bool = Nino_rectangle.colliderect(Mae_rectangle)
            if Bool:
            	Nino_rectangle = pos_ant

            screen.blit(Nino, Nino_rectangle)



    #Grotte Labyrinthe

    if partie == 4:
        x += 1
        pygame.time.delay(10)
        if x > 35:
            if labyrinthe == 0:
                carte = read_map("grotte_1")
                collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)
                screen.blit(grotte_lab_1, (0,0))



            else:
                screen.blit(grotte_lab_2, (0,0))
                if labyrinthe == 1:
                    carte = read_map("grotte_2")
                elif labyrinthe == 2:
                    carte = read_map("grotte_1")
                elif labyrinthe == 3:
                    carte = read_map("grotte_3")
                elif labyrinthe == 4:
                    partie += 1
                    Nino_rectangle.x = 285
                    Nino_rectangle.y = 338
                    Maena = Mae_Avant
                    Mae_rectangle.x = 285
                    Mae_rectangle.y = 100
                    sous_Partie = 1
                    Monstre_rectangle.x = -50
                    Monstre_rectangle.y = -50
                    Monstre = monstre1_Haut
                    prairie.x = -5
                    prairie.y = 0
                    son_Part_1.stop()
                    home.play()


                collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)



            if x % 18 == 0:
                if y == 1:
                    y = 0
                else:
                    y = 1

            pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)

            for mur in collisions_M:
                Bool = Nino_rectangle.colliderect(mur)
                if Bool:
                    Nino_rectangle = pos_ant


            for porte in collisions_A:
                Bool = Nino_rectangle.colliderect(porte)
                if Bool:
                    labyrinthe += 1
                    Nino_rectangle.x = 282
                    Nino_rectangle.y = 338
                    x = 0


            for porte in collisions_B:
                Bool = Nino_rectangle.colliderect(porte)
                if Bool:
                    labyrinthe = 0
                    Nino_rectangle.x = 282
                    Nino_rectangle.y = 338
                    x = 0
                    a += 1


            screen.blit(Nino, Nino_rectangle)
            if labyrinthe == 0 and a > 0:
                screen.blit(text_box, text_rectangle)
                text = pygame.font.Font(police, 14)
                text = text.render("Nino : Me revoilà au point de départ ...", 1, (255, 255, 255))
                screen.blit(text, text_coord)

            if labyrinthe == 3:
                screen.blit(text_box, text_rectangle)
                text = pygame.font.Font(police, 14)
                text = text.render("Nino : Je pense que la sortie n'est plus loin !", 1, (255, 255, 255))
                screen.blit(text, text_coord)



    ##Prairie/Premier combat

    if partie == 5:
        x += 1
        pygame.time.delay(10)
        screen.blit(prairie_1, prairie)

        if sous_Partie == 1:
            pos_ant = pygame.Rect(Nino_rectangle)

            carte = read_map("prairie_1")
            collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)


            if x % 18 == 0:
                if y == 1:
                    y = 0
                else:
                    y = 1

            pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)

            for mur in collisions_M:
                Bool = Nino_rectangle.colliderect(mur)
                if Bool:
                    Nino_rectangle = pos_ant

            for m in collisions_A:
                Bool = Nino_rectangle.colliderect(m)
                if Bool:
                    sous_Partie = 2
                    x = 0
                    Nino = Nino_Haut


        elif sous_Partie == 2:
            if x < 60:
                screen.blit(emoticone_exclam, (315, 95))
            else:
                screen.blit(text_box, text_rectangle)
                text = pygame.font.Font(police, 14)
                text = text.render("Moe : Te voilà enfin ! Tu en as mis du temps.", 1, (255, 255, 255))
                screen.blit(text, text_coord)



            if keys[pygame.K_RETURN]:
                sous_Partie = 3
                y = 0
                home.stop()
                x = 0
                battle_1.play()

        elif sous_Partie == 3:
            if x < 100:
                if x % 5 == 0:
                    if y == 0:
                        y = 1
                        Nino_rectangle = Nino_rectangle.move((5,0))
                        Mae_rectangle = Mae_rectangle.move((5, 0))
                        prairie = prairie.move((5, 0))
                    else:
                        y = 0
                        Nino_rectangle = Nino_rectangle.move((-5,0))
                        Mae_rectangle = Mae_rectangle.move((-5, 0))
                        prairie = prairie.move((-5, 0))
            else:
                screen.blit(text_box, text_rectangle)
                texte = pygame.font.Font(police, 14)
                texte = texte.render("Moe : Aaah, qu'est-ce que c'est ??", 1, (255, 255, 255))
                screen.blit(texte, text_coord)
                Monstre_rectangle.x = 284
                Monstre_rectangle.y = 150

                if keys[pygame.K_RETURN]:
                    sous_Partie = 4
        elif sous_Partie == 4:
            text1 = pygame.font.Font(police, 14)
            text1 = text1.render("Appuyez sur A ou R", 1, (255, 255, 255))
            text2 = pygame.font.Font(police, 14)
            text2 = text2.render("A ou Q : Aider Moe.        R : S'enfuir.", 1, (255, 255, 255))
            screen.blit(text_box, text_rectangle)
            screen.blit(text1, text_coord)
            screen.blit(text2, (10, 350))

            if keys[pygame.K_q]:
                sous_Partie = 5
            elif keys[pygame.K_r]:
                sous_Partie = 6
                x = 0

        elif sous_Partie == 5:
            if x % 15 == 0:
                if y == 0:
                    y = 1
                else:
                    y = 0
            if y == 1:
                Nino = Nino_Haut_Droit
            else:
                Nino = Nino_Haut_Gauche

            if Nino_rectangle.y < 158 :
                partie = 6
                x = 0
                dialogue = 0
                battle_1.stop()
                julia.play()

            Nino_rectangle = Nino_rectangle.move((0, -2))


        elif sous_Partie == 6:
            if x %15 == 0:
                if y == 0:
                    y = 1
                else:
                    y = 0
            if y == 1:
                Monstre = monstre1_Bas_Droit
                Nino = Nino_Avant_Droit
            else:
                Monstre = monstre1_Bas_Gauche
                Nino = Nino_Avant_Gauche
            if Monstre_rectangle.colliderect(Nino_rectangle):
                partie = 1000
                battle_1.stop()
            Monstre_rectangle = Monstre_rectangle.move((0, 2))
            Nino_rectangle = Nino_rectangle.move((0, 1))
        screen.blit(Maena, Mae_rectangle)
        screen.blit(Monstre, Monstre_rectangle)
        screen.blit(Nino, Nino_rectangle)

    #######Maison

    if partie == 6:
        pygame.time.delay(4)
        x += 1
        if x > 200 and x < 600:
            text = pygame.font.Font(police, 14)
            text = text.render("..Nino ? Niinooo ?", 1, (255, 255, 255))
            screen.blit(text, (230, 193))
        elif x > 700 and x < 1200:
            text = pygame.font.Font(police, 14)
            text = text.render("Hé ! Nino, réveille-toi ... !", 1, (255, 255, 255))
            screen.blit(text, (205, 193))
        elif x > 1600:
            screen.blit(maison_1, (0,0))
            screen.blit(Nino, Nino_rectangle)
            screen.blit(Maena, Mae_rectangle)

            if dialogue < 1:
                screen.blit(fond, (0,0))
                screen.blit(Nino_image, (5, 40))
                screen.blit(Mae_image, (345, 45))
                screen.blit(text_box, text_rectangle)
                text_1 = pygame.font.Font(police, 14)
                text_2 = pygame.font.Font(police, 14)
                text_2 = text_2.render("", 1, (255, 255, 255))

                if dialogue == 0:

                    text_1 = text_1.render("Moe : Tu te réveilles enfin ! Tu m'as fait peur idiot.", 1, (255, 255, 255))
                    if keys[pygame.K_RETURN]:
                        dialogue = 1

                screen.blit(text_1, text_coord)
                screen.blit(text_2, (10, 347))

            elif dialogue > 0:
                pos_ant = pygame.Rect(Nino_rectangle)

                carte = read_map("maison_1")
                collisions_M, collisions_A, collisions_B = afficherMap(carte, case_rectangle)


                if x % 18 == 0:
                    if y == 1:
                        y = 0
                    else:
                        y = 1

                pos_ant, Nino, direction, Nino_rectangle = deplacement(Nino_rectangle, y, direction)

                for mur in collisions_M:
                    Bool = Nino_rectangle.colliderect(mur)
                    if Bool:
                        Nino_rectangle = pos_ant

                Bool = Nino_rectangle.colliderect(Mae_rectangle)
                if Bool:
                    Nino_rectangle = pos_ant

                for porte in collisions_A:
                    Bool = Nino_rectangle.colliderect(porte)
                    if Bool:
                        partie = 7


    if partie == 7:
        text = pygame.font.Font(police, 16)
        text = text.render("Fin du prologue", 1, (255, 255, 255))
        text2 = pygame.font.Font(police, 13)
        text2 = text2.render("Prêt pour l'aventure ?", 1, (255, 255, 255))
        screen.blit(text2, (210, 200))
        screen.blit(text, (225, 160))

    if partie == 1000:
        game_over.play()
        text = pygame.font.Font(police, 30)
        text = text.render("Game Over", 1, (255, 255, 255))
        text2 = pygame.font.Font(police, 14)
        text2 = text2.render("Appuyez sur entrée pour recommencer", 1, (255, 255, 255))
        screen.blit(text2, (150, 220))
        screen.blit(text, (220, 140))
        if keys[pygame.K_RETURN]:
            partie = 1
            sous_Partie = 0
            x = 0
            game_over.stop()
            son_Intro.play()


    pygame.display.flip()
