from random import *
for x in range(0,5):
    prize_list = []
    prize_list += 3 * [["Lead", 0]]
    prize_list += 5 * [["Copper", 1]]
    prize_list += 3 * [["Silver", 2]]
    prize_list += [["Gold", 5]]
    payout = 0

    for x in range(0,100):
        prize_1 = prize_list[randint(0, 11)]
        prize_2 = prize_list[randint(0, 11)]
        prize_3 = prize_list[randint(0, 11)]
        payout += prize_1[1] + prize_2[1] + prize_3[1]

    print(payout)

