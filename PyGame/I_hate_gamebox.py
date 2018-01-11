# Charles Buyas cjb8qf


import gamebox
import random
import pygame

counter = 0
camera = gamebox.Camera(800, 600)
x_location = 400
y_location = 300
character = pygame.image.load("ship.png")
enemy = gamebox.from_color(random.randint(0, 800), random.randint(0, 600), "blue", 15, 30)
enemy.yspeed = 10


def tick(keys):
    global x_location
    global y_location
    global counter
    counter += 1
    if counter % 5 == 0:
        camera.clear("lightblue")
    if counter % 4 == 0 and counter % 5 != 0:
        camera.clear("yellow")
    if counter % 3 == 0 and counter % 5 != 0 and counter % 4 != 0:
        camera.clear("lightgreen")
    if counter % 2 == 0 and counter % 5 != 0 and counter % 4 != 0 and counter % 3 != 0:
        camera.clear("white")
    if counter % 1 == 0 and counter % 5 != 0 and counter % 4 != 0 and counter % 3 != 0 and counter % 2 != 0:
        camera.clear("black")
    camera.draw(character, x_location, y_location)
    if pygame.K_LEFT in keys:
        x_location -= 20
        if x_location <= 32:
            x_location = 32
    if pygame.K_RIGHT in keys:
        x_location += 20
        if x_location >= 768:
            x_location = 768
    if pygame.K_UP in keys:
        y_location -= 20
        if y_location <= 32:
            y_location = 32
    if pygame.K_DOWN in keys:
        y_location += 20
        if y_location >= 568:
            y_location = 568

    # camera.draw(enemy)
    # while counter % 30 == 0:
    #     enemy.y += random.randint(-10, 10)
    # while counter % 30 == 0:
    #     enemy.x += random.randint(-10, 10)

    camera.display()

TICKS_PER_SECOND = 30
gamebox.timer_loop(TICKS_PER_SECOND, tick)
