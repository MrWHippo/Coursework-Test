from best_hand import PlayingCard, find_best_hand
from test_hands import games # further_test_cases

my_hand = [PlayingCard(3,"H"),PlayingCard(7,"H")]
table_cards = [PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(7,"D"), PlayingCard(8,"H"), PlayingCard(13,"S")]
# expected best hand = 2,3,4,5,6 - Striaght


def test_hand(whole_hand):
    my_hand = whole_hand[0]
    table_cards = whole_hand[1]
    best_hand = find_best_hand(my_hand, table_cards)
    return best_hand

def compare_ans(correct_ans, calc_ans):
    i = 0
    for card in correct_ans:
        if card.get_whole_card() != calc_ans[i].get_whole_card():
            return False
        else:
            i += 1
    return True

def run_through_hands(games):
    for hand in games:
        print("Next hand:")
        calc_ans = test_hand(hand[0])
        result = compare_ans(hand[1],calc_ans)
        if result:
            print(f'\033[0;32;40m{result} \033[0;0m')
        else:
            print(f'\033[0;31;40m{result} \033[0;0m')
            print("Calculated answer: ",print_hand(calc_ans),"Correct answer: " , print_hand(hand[1]))
    print("Done")

def print_hand(hand):
    vis_hand = []
    for card in hand:
        vis_hand.append(card.get_whole_card())
    return vis_hand
        

run_through_hands(games) #  or further_test_cases
