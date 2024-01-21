import random
from fractions import Fraction

def roll_die(sides = 6):
    return random.randint(1,sides)


def roll_dice(dice_cnt = 1):
    the_roll = []
    for i in range(dice_cnt):
        the_roll.append(roll_die())
    return tuple(the_roll)


def display_rolls(a_roll, denom = 1):
    for key in sorted(a_roll.keys()):
        print(f'{key}: {a_roll[key]:5d} --- {a_roll[key]/denom:02.5f}')


def check_three(dice):
    match = True
    #print(dice)
    for i in range(1,len(dice)):
        if dice[i] == 1:
            break # already counted 1's
        if dice[i-1] != dice[i]:
            match = False
            break
    if match == True:
        print("found")


def check_three(hand):
    # make sure no 1's or 5's are present
    if 1 in hand or 5 in hand:
        return 0
    handset = set(hand)
    if len(handset) == 1:
        return 1
    return 0

def check_four(hand):
    if 1 in hand or 5 in hand:
        return 0
    handset = set(hand)
    handtup = tuple(handset)
    if len(handset) == 1: # all dice match
        return 1
    if len(handset) == 2: # could have 3 of a kind
        if hand.count(int(handtup[0])) == 3 or hand.count(int(handtup[1])) == 3:
            return 1
    return 0


def check_five(hand):
    if 1 in hand or 5 in hand:
        return 0
    handset = set(hand)
    handtup = tuple(handset)
    # 2 2 2 2 2 -> (2)
    if len(handset) == 1: # all dice match
        return 1
    # 2 2 2 3 3 -> (2, 3)
    if len(handset) == 2: # could have 3/2 match
        if hand.count(int(handtup[0])) == 3 or hand.count(int(handtup[1])) == 3:
            return 1
    # 2 2 2 3 4 -> (2, 3, 4)
    if len(handset) == 3: # could have 3/1/1 match
        if hand.count(int(handtup[0])) == 3 \
            or hand.count(int(handtup[1])) == 3 \
            or hand.count(int(handtup[2])) == 3:
            return 1            
    return 0






def check_six(hand):
    if 1 in hand or 5 in hand:
        return 0
    handset = set(hand)
    handtup = tuple(handset)
    # 2 2 2 2 2 2
    if len(handset) == 1: # all dice match
        return 1
    # 2 2 2 3 3 3 -> (2, 3)    
    if len(handset) == 2:
        if hand.count(int(handtup[0])) == 3 and hand.count(int(handtup[1])) == 3:
            return 1
        # 2 2 2 2 3 3 -> (2, 3)
        elif hand.count(int(handtup[0])) == 4 or hand.count(int(handtup[1])) == 4:
            return 1            
    # 2 2 3 3 4 4 -> (2, 3, 4)
    if len(handset) == 3: 
        if hand.count(int(handtup[0])) == 2 \
            and hand.count(int(handtup[1])) == 2 \
            and hand.count(int(handtup[2])) == 2:
            return 1 
        # 2 2 2 2 3 4 -> (2, 3, 4)        
        elif hand.count(int(handtup[0])) == 4 \
            or hand.count(int(handtup[1])) == 4 \
            or hand.count(int(handtup[2])) == 4:
            return 1 
        # 2 2 2 3 3 4 -> (2, 3, 4)
        elif hand.count(int(handtup[0])) == 3 \
            and hand.count(int(handtup[1])) == 3 \
            and hand.count(int(handtup[2])) == 3:
            return 1 
    # 2 2 2 3 4 6 -> (2, 3, 4, 6)
    if len(handset) == 4:
        if hand.count(int(handtup[0])) == 3 \
            or hand.count(int(handtup[1])) == 3 \
            or hand.count(int(handtup[2])) == 3 \
            or hand.count(int(handtup[3])) == 3:
            return 1                      
    return 0


def count_good_rolls(dice):
    # 1's and 5's always good
    good = 0
    for k in dice:
        if 1 in k or 5 in k:
            good += int(dice[k])
            continue
        if len(k) == 3:
            good += check_three(k)
        if len(k) == 4:
            good += check_four(k)
        if len(k) == 5:
            good += check_five(k)     
        if len(k) == 6:
            good += check_six(k)                   
    return good


def roll(num_die = 1, times = 2000000):
    dice = {}
    for i in range(times):
        roll_result = roll_dice(num_die)
        try:
            dice[roll_result] = dice[roll_result] + 1
        except KeyError:
            dice[roll_result] = 1  
    good = count_good_rolls(dice)     
    print(f'{num_die}: {good}/{times} = {good/times:2.4f}')


if __name__ == "__main__":
    #test()
    roll(1)
    roll(2)
    roll(3)
    roll(4)
    roll(5)
    roll(6)
