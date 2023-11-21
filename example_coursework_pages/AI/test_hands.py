from best_hand import PlayingCard

# format = [ [ [user cards, tables cards ], [best hand] ] ]
games = [  [ [[PlayingCard(1,"H"),PlayingCard(2,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]],[PlayingCard(2,"H"), PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H")]  ], # straight
  [ [[PlayingCard(3,"H"),PlayingCard(7,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(7,"D"), PlayingCard(8,"H"), PlayingCard(13,"S")]],[PlayingCard(3,"C"), PlayingCard(3,"H"), PlayingCard(7,"D"), PlayingCard(7,"H"), PlayingCard(13,"S")]  ], # two pair
   [ [[PlayingCard(2,"H"),PlayingCard(2,"D")],[PlayingCard(3,"C"), PlayingCard(3,"D"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(2,"H"), PlayingCard(2,"D"), PlayingCard(13,"H"), PlayingCard(13,"D"), PlayingCard(13,"S")]  ], # full house
    [ [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"S")]  ], # straight
     [ [[PlayingCard(1,"S"),PlayingCard(10,"S")],[PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"S"), PlayingCard(10,"S"), PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"S")]  ], # royal flush
     [  [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]  ], # straight
      [  [[PlayingCard(10,"H"),PlayingCard(10,"D")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"C"), PlayingCard(10,"D"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")] ], # straight
       [ [[PlayingCard(4,'H'),PlayingCard(5,'H')],[PlayingCard(6,'H'),PlayingCard(7,'H'),PlayingCard(8,'H'),PlayingCard(11,'C'),PlayingCard(13,'H')]],[PlayingCard(4,'H'),PlayingCard(5,'H'),PlayingCard(6,'H'),PlayingCard(7,'H'),PlayingCard(8,'H')] ], # straight flush
       [ [[PlayingCard(2,'H'),PlayingCard(3,'D')],[PlayingCard(3,'C'),PlayingCard(7,'H'),PlayingCard(8,'H'),PlayingCard(10,'D'),PlayingCard(1,'C')]],[PlayingCard(1,'H'),PlayingCard(3,'D'),PlayingCard(3,'C'),PlayingCard(8,'H'),PlayingCard(10,'D')] ], # pair
       [ [[PlayingCard(1,'H'),PlayingCard(2,'H')],[PlayingCard(3,'C'),PlayingCard(7,'H'),PlayingCard(8,'H'),PlayingCard(10,'D'),PlayingCard(11,'C')]],[PlayingCard(1,'H'),PlayingCard(7,'H'),PlayingCard(8,'H'),PlayingCard(10,'D'),PlayingCard(11,'C')] ], #high card
       [ [[PlayingCard(1,'C'),PlayingCard(2,'C')],[PlayingCard(3,'C'),PlayingCard(7,'H'),PlayingCard(8,'C'),PlayingCard(10,'D'),PlayingCard(11,'C')]],[PlayingCard(1,'C'),PlayingCard(2,'C'),PlayingCard(3,'C'),PlayingCard(8,'C'),PlayingCard(11,'C')] ], #flush
       [ [[PlayingCard(1,'C'),PlayingCard(2,'C')],[PlayingCard(2,'H'),PlayingCard(2,'D'),PlayingCard(8,'C'),PlayingCard(10,'D'),PlayingCard(11,'C')]],[PlayingCard(2,'D'),PlayingCard(2,'H'),PlayingCard(2,'C'),PlayingCard(10,'D'),PlayingCard(11,'C')] ] ,# three of a kind
       [ [[PlayingCard(1,'C'),PlayingCard(2,'C')],[PlayingCard(2,'H'),PlayingCard(2,'D'),PlayingCard(2,'S'),PlayingCard(10,'D'),PlayingCard(11,'C')]],[PlayingCard(2,'S'),PlayingCard(2,'D'),PlayingCard(2,'H'),PlayingCard(2,'C'),PlayingCard(11,'C')] ],# four of a kind
       [ [[PlayingCard(1,'C'),PlayingCard(2,'C')],[PlayingCard(1,'H'),PlayingCard(1,'D'),PlayingCard(3,'H'),PlayingCard(3,'D'),PlayingCard(3,'C')]],[PlayingCard(1,'H'),PlayingCard(1,'C'),PlayingCard(3,'D'),PlayingCard(3,'H'),PlayingCard(3,'C')] ],# full house
       ] 

further_test_cases = [[ [[PlayingCard(1,"S"),PlayingCard(10,"S")],[PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"S"), PlayingCard(10,"S"), PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"S")]  ]] # 3



