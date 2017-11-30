import random

heads_counter, tails_counter, tries = 0, 0, 0


def roll(r):
    global heads_counter
    global tails_counter

    if r == 0:
        if tails_counter == 0:
            print('adding to heads, on a streak')
            heads_counter += 1

        if tails_counter > 0:
            print('adding to heads, no streak')
            heads_counter += 1
            tails_counter = 0

    if r == 1:
        if heads_counter == 0:
            print('adding to tails, on a streak')
            tails_counter += 1

        if heads_counter > 0:
            print('adding to tails, no streak')
            heads_counter = 0
            tails_counter += 1

while heads_counter < 5 and tails_counter < 5:
    random_num = random.randrange(0,2)
    print('ran',random_num)
    roll(random_num)
    tries += 1

print(tries)