from best_hand import PlayingCard, find_best_hand

my_hand = [PlayingCard(1,"H"),PlayingCard(2,"H")]
table_cards = [PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]
# expected best hand = 2,3,4,5,6 - Striaght

best_hand = find_best_hand(my_hand, table_cards)

best_hand_view = []
for card in best_hand:
    best_hand_view.append(card.get_value())

print(best_hand_view)
