from itertools import combinations

class PlayingCard():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.whole_card = f"{value}{suit}"
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value

    def get_whole_card(self):
        return self.whole_card

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

def generate_all_combinations(cards, hand):
    wanted_combos = []
    all_combintations =  list(combinations(cards, 5))
    for combo in all_combintations:
        if any(card in combo for card in hand):
            wanted_combos.append(combo)
    return wanted_combos


def check_flush(hand):
    flush = False
    is_royal_flush = False
    count_diamonds = 0
    count_hearts = 0 
    count_clubs = 0 
    count_spades = 0

    for card in hand:
        if card.get_suit() == "D":
            count_diamonds += 1
        elif card.get_suit() == "H":
            count_hearts += 1
        elif card.get_suit() == "C":
            count_clubs += 1  
        else:
            count_spades += 1

    if  count_diamonds == 5 or count_hearts == 5 or count_clubs == 5 or count_spades == 5:
        flush = True
        fact = check_royal_flush(hand)
        if fact == True:
            is_royal_flush = True

    if is_royal_flush == True:
        return 2
    elif flush == True:
        return 1
    else:
        return 0


def check_royal_flush(hand):
    # royal_flush = [1,10,11,12,13] (same suit)
    is_royal_flush = False
    if hand[0].get_value() == 1 and hand[1].get_value() == 10 and hand[2].get_value() == 11 and hand[3].get_value() == 12 and hand[4].get_value() == 13:
        is_royal_flush = True
    return is_royal_flush


def check_straight(hand):
    if hand[0].get_value() == 1 and hand[1].get_value() == 10 and hand[2].get_value() == 11  and hand[3].get_value() == 12 and hand[4].get_value() == 13:
        return True
    
    prev = hand[0].get_value()
    count = 1
    for card in hand[1:]:
        if card.get_value() == prev + 1:
            count += 1
            prev = card.get_value()
        else:
            break

    if count == 5:
        return True
    else:
        return False



def check_matches(hand):
    matches = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
    for card in hand:
        matches[card.get_value()] += 1
    
    three_kind = False
    two_pair = False
    pair  = False

    for value in range(1,14):
        if matches[value] == 4:
            return 5
        elif matches[value] == 3:
            three_kind = True
        elif matches[value] == 2:
            if pair == True:
                two_pair = True
            else:
                pair = True
    if three_kind == True:
        if pair == True:
            return 4
        else:
            return 3
    elif two_pair == True:
        return 2
    elif pair == True:
        return 1
    else:
        return 0
    
def contains_ace(hand):
    if hand[0].get_value() == 1:
        return True
    else:
        return False

def find_best_hand(user_hand, table_cards):
    contains_straight_flush = False
    ace_and_SF_bool = False
    contains_four_kind = False
    ace_and_4K_bool = False
    contains_full_house = False
    ace_and_FH_bool = False
    contains_flush = False
    ace_and_F_bool = False
    contains_straight = False
    contains_three_kind = False
    ace_and_3K_bool = False
    contains_two_pair = False
    ace_and_twopair_bool = False
    contains_pair = False
    ace_high_card = None

    whole_hand = get_whole_hand(user_hand, table_cards)
    hands = generate_all_combinations(whole_hand, user_hand)
    for hand in hands:
        #check for flush
        num = check_flush(hand)
        if num == 2: # royal flush
            print("Royal Flush")
            return hand
        elif num == 1: # flush
            ans = check_straight(hand)
            if ans:
                contains_straight_flush = True
                straight_flush = hand
            else:
                if contains_ace(hand):
                    ace_and_F_bool = True
                    ace_and_F = hand
                contains_flush = True
                flush = hand
        else:
            # straight
            ans = check_straight(hand)
            if ans:
                contains_straight = True
                straight = hand
        
        #matches
        num = check_matches(hand)
        if num == 5:
            if contains_ace(hand):
                ace_and_4K_bool = True
                ace_and_4K = hand
            contains_four_kind = True
            four_kind = hand
        elif num == 4:
            if contains_ace(hand):
                ace_and_FH_bool = True
                ace_and_FH = hand
            contains_full_house = True
            full_house = hand
        elif num == 3:
            if contains_ace(hand):
                ace_and_3K_bool = True
                ace_and_3K = hand
            contains_three_kind = True
            three_kind = hand
        elif num == 2:
            if contains_ace(hand):
                ace_and_twopair_bool = True
                ace_and_twopair = hand
            contains_two_pair = True
            two_pair = hand
        elif num == 1:
            if contains_ace(hand):
                ace_and_pair_bool = True
                ace_and_pair = hand
            contains_pair = True
            pair = hand
        else:
            if contains_ace(hand):
                ace_high_card = hand
            high_card = hand

    if contains_straight_flush:
        print("Straight Flush")
        return straight_flush
    elif contains_four_kind:
        print("Four of a Kind")
        if ace_and_4K_bool:
            return ace_and_4K
        return four_kind
    elif contains_full_house:
        print("Full House")
        if ace_and_FH_bool:
            return ace_and_FH
        return full_house
    elif contains_flush:
        print("Flush")
        if ace_and_F_bool:
            return ace_and_F
        return flush
    elif contains_straight:
        print("Straight")
        return straight
    elif contains_three_kind:
        print("Three of a Kind")
        if ace_and_3K_bool:
            return ace_and_3K
        return three_kind
    elif contains_two_pair:
        print("Two Pair")
        if ace_and_twopair_bool:
            return ace_and_twopair
        return two_pair
    elif contains_pair:
        print("Pair")
        if ace_and_pair_bool:
            return ace_and_pair
        return pair
    else:
        print("High Card")
        if ace_high_card != None:
            return ace_high_card
        else:
            return high_card