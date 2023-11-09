from best_hand import PlayingCard, find_best_hand





my_hand = [PlayingCard(1,"H"),PlayingCard(2,"H")]
table_cards = [PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]

find_best_hand(my_hand, table_cards)