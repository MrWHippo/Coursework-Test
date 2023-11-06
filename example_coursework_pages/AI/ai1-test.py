
my_hand = []
table_cards = []


def get_whole_hand(my_hand, table_cards):
    whole_hand = []

    for i in range(2):
        whole_hand.append(my_hand[i-1])

    for i in range(5):
        whole_hand.append(table_cards[i-1])

    return whole_hand


def check_flush(whole_hand):
    flush = False
    count_diamonds, count_hearts, count_clubs, count_spades = 0

    for card in whole_hand:
        if card[0] == "D":
            count_diamonds += 1
        elif card[0] == "H":
            count_hearts += 1
        elif card[0] == "C":
            count_clubs += 1
        else:
            count_spades += 1

    if count_diamonds == 5:
        flush = True
        # check for a royal flush
        if check_royal_flush(whole_hand, "D") == True:
            is_royal_flush = True
        
    if count_hearts == 5:
        flush = True
        # check for a royal flush
        if check_royal_flush(whole_hand, "H") == True:
            is_royal_flush = True

    if count_clubs == 5:
        flush = True
        # check for a royal flush
        if check_royal_flush(whole_hand, "C") == True:
            is_royal_flush = True

    if  count_spades == 5:
        flush = True
        # check for a royal flush
        if check_royal_flush(whole_hand, "F") == True:
            is_royal_flush = True
        
    else:
        flush = False
    
    if is_royal_flush == True:
        return 2
    elif flush == True:
        return 1
    else:
        0

def check_royal_flush(whole_hand, suit):
    # royal_flush = [1,10,11,12,13]
    is_royal_flush = False
    winning_hand = []
    #get correct suit
    for card in whole_hand:
        if card[0] == suit:
            winning_hand.append(card)
    if winning_hand[0] == 1 and winning_hand[10] == 10 and winning_hand[2] == 11 and winning_hand[3] == 12 and winning_hand[4] == 13:
        is_royal_flush = True
    return is_royal_flush

def check_straight(hand, count=1, prev=None):
    if hand == []:
        return False
    
    if count == 5:
        return True

    if prev is None or hand[0] == prev + 1:
        return check_straight(hand[1:], count + 1, hand[0])
    else:
        return check_straight(hand[1:], 1, hand[0])
    
def check_matches(hand):
    poss_winning_cards = []
    poss_high_cards = []
    matches = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
    for card in hand:
        matches[card[1]] += 1
    
    for value in range(1,13):
        if matches[value] == 4:
            poss_winning_cards.append((value, 4))
            four_kind = True
        elif matches[value] == 3:
            poss_winning_cards.append((value, 3))
            three_pair = True
        elif matches[value] == 2:
            poss_winning_cards.append((value, 2))
            pair = True
        elif matches[value] == 1:
            poss_high_cards.append((value))
    
    if four_kind == True:
        for i in poss_high_cards:
            if i[1] == 4:
                four_cards = i[0]
        high_card = poss_high_cards[-1]
        if high_card > four_cards:
            winning_hand = [four_cards, four_cards, four_cards, four_cards, high_card]
        
