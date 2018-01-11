# Charles Buyas cjb8qf
# I asked Phoenix Jitpaisarnsook about double indexing for the fourth function


def read_data_file(filename):
    gop_data_list = []
    gop_data = open(filename, "r")
    for x in gop_data:
        x = x.strip()
        x = x.split(",")
        gop_data_list.append(x)
    for row in range(len(gop_data_list)):
        for i in range(len(gop_data_list[0])):
            if 2 <= i <= 7:
                gop_data_list[row][i] = int(gop_data_list[row][i])
    return gop_data_list


def poll_winner(poll_to_examine):
    kasich = 0
    cruz = 0
    rubio = 0
    trump = 0
    cruz += poll_to_examine[4]
    kasich += poll_to_examine[5]
    rubio += poll_to_examine[6]
    trump += poll_to_examine[7]
    winner = max(cruz, kasich, rubio, trump)
    margin = winner
    name = ''
    if winner == cruz:
        margin -= max(kasich, rubio, trump)
        name = 'Cruz'
    elif winner == kasich:
        margin -= max(cruz, rubio, trump)
        name = 'Kasich'
    elif winner == rubio:
        margin -= max(kasich, cruz, trump)
        name = 'Rubio'
    elif winner == trump:
        margin -= max(kasich, rubio, cruz)
        name = 'Trump'
    if margin == 0:
        return "TIE"
    else:
        margin = "+" + str(margin)
        return name, margin


def latest_poll_winner_by_state(state):
    read_data_file(state)
    gop_data_list = []
    filename = state
    gop_data = open(filename, "r")
    for x in gop_data:
        x = x.strip()
        x = x.split(",")
        gop_data_list.append(x)
    for row in range(len(gop_data_list)):
        for i in range(len(gop_data_list[0])):
            if 2 <= i <= 7:
                gop_data_list[row][i] = int(gop_data_list[row][i])
    poll_to_examine = gop_data_list[0]
    return poll_winner(poll_to_examine)


def average_of_polls(state, number_of_polls=5):
    gop_data_list = []
    filename = state
    gop_data = open(filename, "r")
    for x in gop_data:
        x = x.strip()
        x = x.split(",")
        gop_data_list.append(x)
    for row in range(len(gop_data_list)):
        for i in range(len(gop_data_list[0])):
            if 2 <= i <= 7:
                gop_data_list[row][i] = int(gop_data_list[row][i])
    average_list = ['Average Poll', number_of_polls]
    for i in range(2, 8):
        blank_list = []
        for y in range(0, number_of_polls):
            blank_list.append(gop_data_list[y][i])
        blank_list = [int(x) for x in blank_list]
        average = sum(blank_list)/len(blank_list)
        average_list.append(int(average))
        del blank_list
        average -= average
    return average_list
