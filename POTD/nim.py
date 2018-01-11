# Charles Buyas cjb8qf


print("The Game of Nim")
tm = int(input("\nNumber of marbles are in the pile: "))
s = input("Who will start? (p or c): ")
if s.lower() == "p":
    print("The pile has", tm, "marbles in it.")
    while tm > 1:
        pg = int(input("How many marbles do you want to take? (1-" + str(tm//2) + "): "))
        if pg <= tm/2:
            tm -= pg
            if tm != 1:
                print("The pile has", tm, "marbles in it.")
            if tm == 1:
                print("The pile has 1 marbles in it.")
                print("The computer takes 1 marbles.")
                print("The player wins!")
                tm -= 1
            else:
                n = 0
                mta = 0
                while (2**n)-1 < tm:
                    mta = (2**n)-1
                    n += 1
                cg = tm - mta
                if cg > (tm/2):
                    cg = 1
                print("The computer takes", cg, "marbles.")
                tm -= cg
                if tm != 1:
                    print("The pile has", tm, "marbles in it.")
                if tm == 1:
                    pg = int(input("How many marbles do you want to take? (1-1): "))
                    print("The computer wins!")
                    tm -= 1
elif s.lower() == "c":
    print("The pile has", tm, "marbles in it.")
    while tm > 1:
        n = 0
        mta = 0
        while (2**n)-1 < tm:
            mta = (2**n)-1
            n += 1
        cg = tm - mta
        if cg > (tm/2):
            cg = 1
        print("The computer takes", cg, "marbles.")
        tm -= cg
        if tm != 1:
            print("The pile has", tm, "marbles in it.")
        if tm == 1:
            pg = int(input("How many marbles do you want to take? (1-1): "))
            print("The computer wins!")
            tm -= 1
        else:
            pg = int(input("How many marbles do you want to take? (1-" + str(tm//2) + "): "))
            if pg <= tm/2:
                tm -= pg
                if tm != 1:
                    print("The pile has", tm, "marbles in it.")
                if tm == 1:
                    print("The pile has 1 marbles in it.")
                    print("The computer takes 1 marbles.")
                    print("The player wins!")
                    tm -= 1
else:
    print("Invalid.")
