
class PlayingCard():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value

def merge(A,B):
    pA = 0
    pB = 0
    result = []
    lenA = len(A)
    lenB = len(B)
    A.append(PlayingCard(float("inf"),"H"))
    B.append(PlayingCard(float("inf"),"H"))
    while pA < lenA or pB < lenB:
        if A[pA].get_value() < B[pB].get_value():
            result.append(A[pA])
            pA += 1
        else:
            result.append(B[pB])
            pB += 1
    return result

def sort(A):
    lenA = len(A)
    if lenA == 1:
        return A
    left = sort(A[:lenA//2])
    right = sort(A[lenA//2:])
    return merge(left,right)


def get_whole_hand(my_hand, table_cards):
    whole_hand = []

    for i in range(2):
        whole_hand.append(my_hand[i-1])

    for i in range(5):
        whole_hand.append(table_cards[i-1])

    whole_hand = sort(whole_hand)
    return whole_hand


def check_flush(whole_hand):
    flush = False
    is_royal_flush = False
    count_diamonds = 0
    count_hearts = 0 
    count_clubs = 0 
    count_spades = 0
    diamonds = []
    hearts = []
    clubs = []
    spades = []
    winning_hand = []

    for card in whole_hand:
        if card.get_suit() == "D":
            count_diamonds += 1
            diamonds.append(card)
        elif card.get_suit() == "H":
            count_hearts += 1
            hearts.append(card)
        elif card.get_suit() == "C":
            count_clubs += 1
            clubs.append(card)
        else:
            count_spades += 1
            spades.append(card)

    if  count_diamonds == 5:
        flush = True
        fact, win_cards = check_royal_flush(whole_hand, "D")
        if fact == True:
            is_royal_flush = True
            for card in win_cards:
                winning_hand.append(card)
        else:
            for card in diamonds:
                winning_hand.append(card)
        
    if  count_hearts == 5:
        flush = True
        fact, win_cards = check_royal_flush(whole_hand, "H")
        if fact == True:
            is_royal_flush = True
            for card in win_cards:
                winning_hand.append(card)
        else:
            for card in hearts:
                winning_hand.append(card)

    if  count_clubs == 5:
        flush = True
        fact, win_cards = check_royal_flush(whole_hand, "C")
        if fact == True:
            is_royal_flush = True
            for card in win_cards:
                winning_hand.append(card)
        else:
            for card in clubs:
                winning_hand.append(card)

    if  count_spades == 5:
        flush = True
        fact, win_cards = check_royal_flush(whole_hand, "S")
        if fact == True:
            is_royal_flush = True
            for card in win_cards:
                winning_hand.append(card)
        else:
            for card in hearts:
                winning_hand.append(card)

    else:
        flush = False
    
    if is_royal_flush == True:
        return 2, winning_hand
    elif flush == True:
        return 1, winning_hand
    else:
        return 0, winning_hand


def check_royal_flush(whole_hand, suit):
    # royal_flush = [1,10,11,12,13]
    is_royal_flush = False
    winning_hand = []
    #get correct suit
    for card in whole_hand:
        if card.get_suit() == suit:
            winning_hand.append(card)
    if winning_hand[0].get_value() == 1 and winning_hand[1].get_value() == 10 and winning_hand[2].get_value() == 11 and winning_hand[3].get_value() == 12 and winning_hand[4].get_value() == 13:
        is_royal_flush = True
    return is_royal_flush, winning_hand


def check_straight(hand):
    prev = hand[0].get_value()
    count = 1
    winning_hand = []
    for card in hand[1:]:
        if card.get_value() == prev + 1:
            winning_hand.append(card)
            count += 1
        elif count < 5:
            count = 1
            winning_hand = [card]

    if count >= 5:
        winning_hand = [winning_hand[-5],winning_hand[-4],winning_hand[-3],winning_hand[-2],winning_hand[-1]]
        return 1, winning_hand
    else:
        return 0, None



def check_matches(hand):
    poss_winning_cards = []
    poss_high_cards = []
    matches = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[]}
    for card in hand:
        matches[card.get_value()].append(card)

    four_kind = False
    three_kind = False
    pair = False
    two_pair = False
    
    for value in range(1,13):
        if len(matches[value]) == 4:
            poss_winning_cards.append(matches[value])
            four_kind = True
        elif len(matches[value]) == 3:
            poss_winning_cards.append(matches[value])
            three_kind = True
        elif len(matches[value]) == 2:
            poss_winning_cards.append(matches[value])
            if pair == True:
                two_pair = True
            else:
                pair = True
        elif len(matches[value]) == 1:
            poss_high_cards.append(matches[value])

    if four_kind == True:
        for i in poss_winning_cards:
            if len(i) == 4:
                four_cards = i
        high_card = poss_high_cards[-1]
        if high_card[0].get_value() > four_cards[0].get_value():
            winning_hand = [four_cards[0], four_cards[1], four_cards[2], four_cards[3], high_card[0]]
        else:
            winning_hand = [high_card[0] , four_cards[0], four_cards[1], four_cards[2], four_cards[3]]
        
        return 5, winning_hand

    elif three_kind == True and pair == True:
        for i in poss_winning_cards:
            if len(i) == 3:
                three_cards = i
            elif len(i) == 2:
                pair = i
        
        if pair[0].get_value() > three_cards[0].get_value():
            winning_hand = [three_cards[0], three_cards[1], three_cards[2], pair[0], pair[1]]
        else:
            winning_hand = [pair[0], pair[1], three_cards[0], three_cards[1], three_cards[2]]
        
        return 4, winning_hand
    
    elif three_kind == True and pair == False:
        for i in poss_winning_cards:
            if len(i) == 3:
                three_cards = i
        high_card_1 = poss_high_cards[-1]
        high_card_2 = poss_high_cards[-2]
        if high_card_1 > three_cards:
            if high_card_2[0].get_value() > three_cards[0].get_value():
                winning_hand = [three_cards[0], three_cards[1], three_cards[2], high_card_2[0], high_card_1[0]]
            else:
                winning_hand = [high_card_2[0], three_cards[0], three_cards[1], three_cards[2], high_card_1[0]]
        else:
            winning_hand = [high_card_2[0], high_card_1[0], three_cards[0], three_cards[1], three_cards[1]]
        
        return 3, winning_hand

    elif two_pair == True:
        pair_list = []
        for i in poss_winning_cards:
            if len(i) == 2:
                pair_list.append(i)
        high_card = poss_high_cards[-1]
        if high_card[0].get_value() > pair_list[1][0].get_value():
            winning_hand = [pair_list[0][0], pair_list[0][1], pair_list[1][0], pair_list[1][1], high_card[0]]
        elif high_card[0].get_value() > pair_list[0][0].get_value():
            winning_hand = [pair_list[0][1], pair_list[0][1], high_card[0], pair_list[1][0], pair_list[1][1]]
        else:
            winning_hand = [high_card[0], pair_list[0][1], pair_list[0][1], pair_list[1][0], pair_list[1][1]]

        return 2, winning_hand

    elif pair == True:
        for i in poss_winning_cards:
            if len(i) == 2:
                pair_cards = i
        high_card_1 = poss_high_cards[-1]
        high_card_2 = poss_high_cards[-2]
        high_card_3 = poss_high_cards[-3]
        if pair[0].get_value() > high_card_1.get_value():
            winning_hand = [high_card_3[0], high_card_2[0], high_card_1[0], pair_cards[0], pair_cards[1]]
        elif pair[0].get_value() > high_card_2.get_value():
            winning_hand = [high_card_3[0], high_card_2[0], pair_cards[0], pair_cards[1], high_card_1[0]]
        elif pair[0].get_value() > high_card_3.get_value():
            winning_hand = [high_card_3[0], pair_cards[0], pair_cards[1], high_card_2[0], high_card_1[0]]
        else:
            winning_hand = [pair_cards[0], pair_cards[1], high_card_3[0], high_card_2[0], high_card_1[0]]
        
        return 1, winning_hand
    
    else:
        return 0, None       


def find_best_hand(my_hand, table_cards):
    whole_hand = get_whole_hand(my_hand, table_cards)
    for card in whole_hand:
        print(card.get_value())
    # flush and royal flush
    num, winning_hand = check_flush(whole_hand)
    if num == 2:
        print("Royal Flush")
        for card in winning_hand:
            print(card.get_value())
    elif num == 1:
        print("Flush")
        for card in winning_hand:
            print(card.get_value())
    else:
        # straight
        num, winning_hand = check_straight(whole_hand)
        if num == 1:
            print("Straight")
            for card in winning_hand:
                print(card.get_value())
        else:
        #matches
            num, winning_hand = check_matches(whole_hand)
            if num == 5:
                print("Four of a Kind")
                for card in winning_hand:
                    print(card.get_value())
            elif num == 4:
                print("Full House")
                for card in winning_hand:
                    print(card.get_value())
            elif num == 3:
                print("Three of a Kind")
                for card in winning_hand:
                    print(card.get_value())
            elif num == 2:
                print("Two Pair")
                for card in winning_hand:
                    print(card.get_value())
            elif num == 1:
                print("Pair")
                for card in winning_hand:
                    print(card.get_value())
            else:
                print("High Card")

