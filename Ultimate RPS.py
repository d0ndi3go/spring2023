# File by Diego

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game box to play
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

choices = ["Rock", "Paper", "Scissors"]

def cpu_randchoice():
    choice = choices[randint(0,2)].upper()
    print("computer randomly decides..." + choice)
    return choice

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 50

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 300

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 500

you_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 500

running = True

player_choice = ""
cpu_choice = "scissors"

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        if event.type == pg.MOUSEBUTTONUP:
            # 
            print(pg.mouse.get_pos()[0])
            # 
            print(pg.mouse.get_pos()[1])
            # 
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            # 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
       
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                      
            else:
                print("you didn't click on anythin...")
    
    
    ########## update ###################

    ############ draw ###################
    screen.fill(BLACK)

    # screen.blit(scissors_image, scissors_image_rect)
    if player_choice == "":
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)

    if player_choice == "rock" and cpu_choice == "SCISSORS":
        screen.blit(rock_image, rock_image_rect)
        screen.blit(scissors_image, scissors_image_rect)

    if player_choice == "paper":
        screen.blit(paper_image, paper_image_rect)

    if player_choice == "scissors":
        screen.blit(scissors_image, scissors_image_rect)

    

    # if cpu_choice == "rock":
    #     screen.blit(rock_image, rock_image_rect)


    pg.display.flip()

pg.quit()