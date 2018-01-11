# Charles Buyas cjb8qf


# my first game
import pygame
import gamebox
import random

stars = []
counter = 0
score = 0
touch_count = 0
camera = gamebox.Camera(800, 600)
character = gamebox.from_color(50, 50, "red", 30, 60)
character.yspeed = 10
ground = gamebox.from_color(-100, 600, "white", 3000, 100)
enemy = gamebox.from_color(750, 600, "blue", 15, 30)
enemy.yspeed = 10

# platform = gamebox.from_color(random.randint(75, 700), random.randint(50, 600), "white", random.randint(60, 150), 5)
walls = [
    gamebox.from_color(50, 250, "white", 75, 5),
    gamebox.from_color(400, 150, "white", 60, 5),
    gamebox.from_color(600, 25, "white", 100, 5),
]


def tick(keys):
    global score
    global counter
    global touch_count
    counter += 1
    if counter % 5 == 0:
        num_stars = random.randint(0, 7)
        for i in range(num_stars):
            stars.append(gamebox.from_color(random.randint(5, 795), camera.y-300, "white", 3, 3))
    camera.clear("black")
    for star in stars:
        # move the star
        star.y += 3
        if star.y > 600:
            stars.remove(star)
        # draw the star
        camera.draw(star)

    if counter % 50 == 0:
        new_wall = gamebox.from_color(random.randint(75, 700), camera.y-300,  "white", random.randint(60, 150), 5)
        walls.append(new_wall)
    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            score += 1
            if pygame.K_SPACE in keys:
                character.yspeed = -20
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    if pygame.K_RIGHT in keys:
        character.x += 20
    if pygame.K_LEFT in keys:
        character.x -= 20
    character.yspeed += 1
    enemy.yspeed += 1

    # if enemy.touches(character) == False:
    #     enemy.xspeed -= 1
    #     enemy.x = enemy.x + enemy.xspeed

    character.y = character.y + character.yspeed
    # enemy.y = enemy.y + enemy.yspeed
    camera.draw(character)
    camera.draw(ground)
    camera.draw(enemy)
    # camera.draw(platform)

    if enemy.bottom_touches(ground):
        enemy.yspeed = 0
    if enemy.touches(ground):
        enemy.move_to_stop_overlapping(ground)
    if enemy.touches(character):
        score -= 10
    if character.bottom_touches(ground):
        character.yspeed = 0
    if character.touches(ground):
        character.move_to_stop_overlapping(ground)
        if pygame.K_SPACE in keys:
            character.yspeed = -15

    if character.x > enemy.x:
        enemy.x += 2
    if character.x < enemy.x:
        enemy.x -= 2
    if character.y > enemy.y:
        enemy.y += 4
    if character.y < enemy.y:
        enemy.y -= 4

    camera.draw("Score:", "Georgia", 36, "red", 725, 250)
    camera.draw(str(score), "Georgia", 36, "red", 725, 300)

    camera.y -= 3
    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
