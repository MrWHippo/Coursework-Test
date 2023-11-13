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

my_hand = [PlayingCard(1,"H"),PlayingCard(2,"H")]
table_cards = [PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]

whole_hand = get_whole_hand(my_hand, table_cards)
hands = generate_all_combinations(whole_hand, my_hand)

for hand in hands:
    this_hand = []
    for card in hand:
        this_hand.append(card.get_value())
    print(this_hand)

print(len(hands))