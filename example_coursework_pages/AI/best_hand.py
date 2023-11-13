from itertools import combinations

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

    if  count_diamonds == 5:
        flush = True
        fact = check_royal_flush(hand, "D")
        if fact == True:
            is_royal_flush = True
            
    if  count_hearts == 5:
        flush = True
        fact = check_royal_flush(hand, "H")
        if fact == True:
            is_royal_flush = True

    if  count_clubs == 5:
        flush = True
        fact = check_royal_flush(hand, "C")
        if fact == True:
            is_royal_flush = True

    if  count_spades == 5:
        flush = True
        fact = check_royal_flush(hand, "S") 
        if fact == True:
            is_royal_flush = True

    else:
        flush = False
    if is_royal_flush == True:
        return 2, hand
    elif flush == True:
        return 1, hand
    else:
        return 0, hand


def check_royal_flush(hand):
    # royal_flush = [1,10,11,12,13] (same suit)
    is_royal_flush = False
    if hand[0].get_value() == 1 and hand[1].get_value() == 10 and hand[2].get_value() == 11 and hand[3].get_value() == 12 and hand[4].get_value() == 13:
        is_royal_flush = True
    return is_royal_flush


def check_straight(hand):
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

    for value in range(1,13):
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
        num, winning_hand2 = check_straight(whole_hand)
        straight_flush = False
        if num == 1:
            straight_flush = True
            for i in range(len(winning_hand)):
                if winning_hand[i] != winning_hand2:
                    straight_flush = False
            if straight_flush == True:
                print("Straight Flush")
                for card in winning_hand:
                    print(card.get_value())
            else:
                print("Flush")
                for card in winning_hand:
                    print(card.get_value())
        else:
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

def find_best_hand(user_hand, table_cards):
    contains_straight_flush = False
    contains_four_kind = False
    contains_full_house = False
    contains_flush = False
    contains_straight = False
    contains_three_kind = False
    contains_two_pair = False
    contains_pair = False

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
            contains_four_kind = True
            four_kind = hand
        elif num == 4:
            contains_full_house = True
            full_house = True
        elif num == 3:
            contains_three_kind = True
            three_kind = hand
        elif num == 2:
            contains_two_pair = True
            two_pair = hand
        elif num == 1:
            contains_pair = True
            pair = hand
        else:
            high_card = hand

    if contains_straight_flush:
        print("Straight Flush")
        return straight_flush
    elif contains_four_kind:
        print("Four of a Kind")
        return four_kind
    elif contains_full_house:
        print("Full House")
        return full_house
    elif contains_flush:
        print("Flush")
        return flush
    elif contains_straight:
        print("Straight")
        return straight
    elif contains_three_kind:
        print("Three of a Kind")
        return three_kind
    elif contains_two_pair:
        print("Two Pair")
        return two_pair
    elif contains_pair:
        print("Pair")
        return pair
    else:
        print("High Card")
        return high_card
    




