# Charles Buyas cjb8qf


print("TITLE: ZOMBIE LOGIC.")
print("\nBasic instructions. The way you play the game is simple: you are given a choice of sorts,"
      "\nand based on what you pick, you will be directed to a separate path of the game. The name"
      "\nof the game? Make it to each checkpoint in the most logical way possible. One last thing:"
      "\ndon't be clumsy, because you only have one life! Good luck.")


life = 1

while life != 0:
    try:
        choice_1 = int(input("\nFirst step. You are in the middle of a zombie apocalypse. Your neighborhood house is"
                             "\ngetting overrun by a team of 8 zombies. You have 3 weapons of choice: 1. Hack Saw,"
                             "\n2. Sawed off double barrel shotgun, and 3. A Broad Sword. You only have time to grab"
                             "\none item. Which do you choose?: "))
        if choice_1 == 1:
            print("\nHack Saw? Really?"
                  "\nGAME OVER.")
            life -= 1
        elif choice_1 == 2:
            print("\nFair enough. But reloading is a bitch, and you only have two shots before you have to load more"
                  "\nshells."
                  "\nGAME OVER.")
            life -= 1
        elif choice_1 == 3:
            print("\nNow that's what I'm talking about! 30 pounds of Irish death. I like it.")

            while life != 0:
                try:
                    choice_2 = int(input("\nSecond step. While the broad sword finished the job, let's be real,"
                                         "\nyou were never trained to use a sword. In the battle you got a nasty"
                                         "\ngash on your leg, and you've got to stop the bleeding before you get the"
                                         "\ninfection. Do you: 1. Take off your shirt and wrap the wound, 2. Take a"
                                         "\nround from the shotgun and stuff gunpowder in the wound, or 3. Tie a cord"
                                         "\ntightly around your leg to try and limit the blood flow?: "))
                    if choice_2 == 1:
                        print("\nWhen you cut the zombies to pieces, did you think their grime wasn't going to get on"
                              "\nyour shirt?"
                              "\nGAME OVER.")
                        life -= 1
                    elif choice_2 == 2:
                        print("\nI'm impressed. The good ol' military trick with gunpowder. Hurts like hell,"
                              "\nbut it works.")

                        while life != 0:
                            try:
                                choice_3 = int(input("\nThird step. You've got some smarts, eh? Well as you may have realized,"
                                                     "\njust pushing gray powder in a wound won't do shit. You have to cauterize"
                                                     "\nthe wound in order for it to be safe. Three things catch your eye:"
                                                     "\n1. A gas stove, 2. A blow torch, and 3. Two shiny grey rocks. So what'll it be?: "))
                                if choice_3 == 1:
                                    print("\nVery good. Turn the stove on high and the flame can get the tip of the Broad Sword hot enough to ignite gunpowder.")

                                    while life != 0:
                                        try:
                                            choice_4 = int(input("\nNumber four. You're getting somewhere now, but you can only hold out in"
                                                                 "\nyour little base for so long. There happens to be an embassy not 10 miles"
                                                                 "\nup the road. You quickly pack a sack with the necessary items and grab your"
                                                                 "\nshotgun and sword, looking out the front windows to check your options."
                                                                 "\nat a glance, you notice three options: 1. Make a break for it through the woods"
                                                                 "\non your left, 2. Hop in the car that's sitting across the street from you,"
                                                                 "\nor 3. Chop down every zombie in sight until you cut your path to the embassy?: "))
                                            if choice_4 == 1:
                                                print("\nCompared to your other options, this was the smartest choice. The trees offer cover,"
                                                      "\nand since you live here you know them well.")

                                                while life != 0:
                                                    try:
                                                        choice_5 = int(input("\nChoice five. Starting to get difficult now. After walking through the woods"
                                                                             "\nfor a while, your leg starts to burn and your progress slows. By now it's getting dark."
                                                                             "\nWhen you finally see the edge of the tree line, you see a corn field separating"
                                                                             "\nthe woods from the road. You aren't sure how large the corn field is, but you know that"
                                                                             "\nthe road just past it leads to the embassy. Your choice: 1. Set up camp and build a fire so"
                                                                             "\nyou can rest your leg and wait until next light, 2. Set the whole damn field on fire to reveal"
                                                                             "\nthe road and also give you a chance to rest, or 3. Head straight into the corn field and"
                                                                             "\nhope you make it to the other side. Well?: "))
                                                        if choice_5 == 1:
                                                            print("\nSleeping next to a bright light isn't the best idea. It's only a matter"
                                                                  "\nof time until a group of zombies discovers you sleeping in your camp."
                                                                  "\nGAME OVER.")
                                                            life -= 1
                                                        elif choice_5 == 2:
                                                            print("\nThis doesn't even work in the movies. Sorry not sorry."
                                                                  "\nGAME OVER.")
                                                            life -= 1
                                                        elif choice_5 == 3:
                                                            print("\nWhile this may seem like a bad idea, cornfields are actually quite easy"
                                                                  "\nto navigate, even in the dark, since all of the stalks are in perfect rows."
                                                                  "\nNice choice.")
                                                            life -= 1
                                                        else:
                                                            print("\nPlease choose 1, 2, or 3.")
                                                    except ValueError:
                                                        print("\nPlease choose 1, 2, or 3!")
                                            elif choice_4 == 2:
                                                print("\nSince you're in the middle of an apocalypse, the car hasn't been driven"
                                                      "\nin ages. The battery is dead. And so are you."
                                                      "\nGAME OVER.")
                                                life -= 1
                                            elif choice_4 == 3:
                                                print("\nThat's just not going to happen."
                                                      "\nGAME OVER.")
                                                life -= 1
                                            else:
                                                print("Please choose 1, 2, or 3.")
                                        except ValueError:
                                            print("\nPlease choose 1, 2, or 3!")
                                elif choice_3 == 2:
                                    print("\nLOL."
                                          "\nGAME OVER.")
                                    life -= 1
                                elif choice_3 == 3:
                                    print("\nWould've been smart. However, you just picked up two ingots of Aluminum."
                                          "\nGood luck sparking that."
                                          "\nGAME OVER.")
                                    life -= 1
                                else:
                                    print("\nPlease choose 1, 2, or 3.")
                            except ValueError:
                                print("\nPlease choose 1, 2, or 3!")
                    elif choice_2 == 3:
                        print("\nSounds like a smart idea, but I'll give you ten minutes before you lose that leg."
                              "\nGAME OVER.")
                        life -= 1
                    else:
                        print("\nPlease choose 1, 2, or 3.")
                except ValueError:
                    print("\nPlease choose 1, 2, or 3!")
        else:
            print("\nPlease choose 1, 2, or 3.")
    except ValueError:
        print("\nPlease choose 1, 2, or 3!")
