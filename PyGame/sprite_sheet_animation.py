# Mark Sherriff animated sprite using a sprite sheet

# import pygame
import gamebox

camera = gamebox.Camera(800,600)
sheet = gamebox.load_sprite_sheet("http://estelle.github.io/10/files/sprite.png", 1, 22)
frame = 0
direction = 0
sprite_counter = 0
character = gamebox.from_image(200, 200, sheet[frame])


def tick(keys):
    global frame
    global direction
    global sprite_counter

    frame += 1
    sprite_counter += 1
    if frame == 10:
        frame = 0
    if sprite_counter % 1 == 0:
        character.image = sheet[frame+direction*10]

    camera.clear("white")
    camera.draw(character)
    camera.display()



ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
