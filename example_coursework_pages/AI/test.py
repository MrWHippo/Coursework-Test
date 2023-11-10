def check_straight1(hand, count=1, prev=None):
    if hand == []:
        return False
    
    if count == 5:
        return True

    if prev is None or hand[0] == prev + 1:
        return check_straight1(hand[1:], count + 1, hand[0])
    else:
        return check_straight1(hand[1:], 1, hand[0])


def check_straight2(hand):
    straight = False
    count = 1
    winning_hand = []
    if hand[0] == 1 and hand[6] == 13: # ace and a king in the hand
        for card in hand:
            if card == 1 or card == 10 or card == 11 or card == 12 or card == 13:
                winning_hand.append(card)
        if len(winning_hand) >= 5:
            straight = True

    if straight == False:
        count = 1
        winning_hand = [hand[0]]
        prev = hand[0]
        count = 1
        winning_hand = [hand[0]]
        for card in hand[1:]:
            if card == prev + 1:
                winning_hand.append(card)
                count += 1
                prev = card
            elif count < 5:
                count = 1
                winning_hand = [card]
                prev = card

    if count >= 5:
        winning_hand = [winning_hand[-5],winning_hand[-4],winning_hand[-3],winning_hand[-2],winning_hand[-1]]
        return 1, winning_hand
    else:
        return 0, None


sorted_list = [1, 2, 3, 4, 5, 6, 7]
result = check_straight2(sorted_list)
print(result)  # True

sorted_list = [4, 8, 9, 10, 11, 12, 13]
result = check_straight2(sorted_list)
print(result)  # True

sorted_list = [1, 2, 3, 4, 5, 8, 9]
result = check_straight2(sorted_list)
print(result)  # True

sorted_list = [1, 5, 7, 10, 11, 12, 13]
result = check_straight2(sorted_list)
print(result)  # True

sorted_list = [1, 3, 5, 6, 7, 7, 13]
result = check_straight2(sorted_list)
print(result)  # False