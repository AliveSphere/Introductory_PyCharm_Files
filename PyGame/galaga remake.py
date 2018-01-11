# Charles Buyas cjb8qf


import pygame
import gamebox
import random

stars = []
enemies = []
counter = 0
score = 0
camera = gamebox.Camera(800, 600)
character = pygame.image.load("ship.png")
enemy = gamebox.from_image(random.randint(25, 775), 0, "alien.png")
sound1 = gamebox.load_sound("ACDC - Shoot To Thrill.wav")
sound1.play()
x_loc = 400
# enemy_x = random.randint(25, 775)
# enemy_y = 0
bulletList = []
bulletCounter = 0


def tick(keys):
    global counter
    global score
    global x_loc
    global bulletList
    global bulletCounter
    # global enemy_x
    # global enemy_y
    counter += 1
    for bullet in bulletList:
        bullet.y -= 15
        if bullet.y < 0:
            bulletList.remove(bullet)
    if counter % 5 == 0:
        num_stars = random.randint(0, 7)
        for i in range(num_stars):
            stars.append(gamebox.from_color(random.randint(5, 795), camera.y-300, "white", 3, 3))
    if counter >= 17:
        if counter % 20 == 0:
            num_enemies = random.randint(0, 7)
            for x in range(num_enemies):
                enemies.append(enemy)
                # camera.draw(enemy, enemy_x, enemy_y)
                # enemies.append(gamebox.from_color(random.randint(15, 785), 0, enemy, 25, 25))
    camera.clear("black")
    for star in stars:
        # move the star
        star.y += 3
        if star.y > 600:
            stars.remove(star)
        # draw the star
        camera.draw(star)
    # enemy.y += 6
    for enemy_a in enemies:
        # enemy.y += 4
        if enemy.y > 600:
            enemies.remove(enemy_a)
        camera.draw(enemy_a)
    enemy.y += 6
    y_loc = 500
    camera.draw(character, x_loc, y_loc)
    for bullet in bulletList:
        bullet.draw(camera)

    if pygame.K_LEFT in keys:
        x_loc -= 20
        if x_loc <= 32:
            x_loc = 32
    if pygame.K_RIGHT in keys:
        x_loc += 20
        if x_loc >= 768:
            x_loc = 768

    if pygame.K_SPACE in keys:
        bul = gamebox.SpriteBox(x_loc, y_loc, None, "green", 3, 6)
        if bulletCounter == 0:
            bulletList.append(bul)
        bulletCounter += 1
    else:
        bulletCounter = 0

    # if bullet.touches(enemy):
    #     enemies.remove(enemy)

    # if character.x > enemy.x:
    #     enemy.x += 2
    # if character.x < enemy.x:
    #     enemy.x -= 2
    # if character.y > enemy.y:
    #     enemy.y += 4
    # if character.y < enemy.y:
    #     enemy.y -= 4
    if counter < 175:
        camera.draw("GALAGA", "Georgia", 96, "green", 400, 300)

    camera.display()

TICKS_PER_SECOND = 30
gamebox.timer_loop(TICKS_PER_SECOND, tick)
