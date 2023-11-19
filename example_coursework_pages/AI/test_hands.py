<<<<<<< Updated upstream
from best_hand import PlayingCard

# format = [ [ [user cards, tables cards ], [best hand] ] ]
games = [  [ [[PlayingCard(1,"H"),PlayingCard(2,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]],[PlayingCard(2,"H"), PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H")]  ],
  [ [[PlayingCard(3,"H"),PlayingCard(7,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(7,"D"), PlayingCard(8,"H"), PlayingCard(13,"S")]],[PlayingCard(3,"C"), PlayingCard(3,"H"), PlayingCard(7,"D"), PlayingCard(7,"H"), PlayingCard(13,"S")]  ],
   [ [[PlayingCard(2,"H"),PlayingCard(2,"D")],[PlayingCard(3,"C"), PlayingCard(3,"D"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(2,"H"), PlayingCard(2,"D"), PlayingCard(13,"H"), PlayingCard(13,"D"), PlayingCard(13,"S")]  ],
    [ [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"S")]  ], 
     [ [[PlayingCard(1,"S"),PlayingCard(10,"S")],[PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"S"), PlayingCard(10,"S"), PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"S")]  ], # says straight not royal flush
     [  [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]  ], 
      [  [[PlayingCard(10,"H"),PlayingCard(10,"D")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"C"), PlayingCard(10,"D"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")] ] ]

further_test_cases = [[ [[PlayingCard(1,"S"),PlayingCard(10,"S")],[PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"S"), PlayingCard(10,"S"), PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"S")]  ]] # 3
=======
from best_hand import PlayingCard

# format = [ [ [user cards, tables cards ], [best hand] ] ]

games = [ [ [[PlayingCard(1,"H"),PlayingCard(2,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H"), PlayingCard(7,"S")]],[PlayingCard(2,"H"), PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(5,"D"), PlayingCard(6,"H")] ],
  [ [[PlayingCard(3,"H"),PlayingCard(7,"H")],[PlayingCard(3,"C"), PlayingCard(4,"C"), PlayingCard(7,"D"), PlayingCard(8,"H"), PlayingCard(13,"S")]],[PlayingCard(4,"H"), PlayingCard(7,"C"), PlayingCard(7,"C"), PlayingCard(8,"D"), PlayingCard(13,"H")]],
  [ [[PlayingCard(2,"H"),PlayingCard(2,"D")],[PlayingCard(3,"C"), PlayingCard(3,"C"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(2,"H"), PlayingCard(2,"D"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],
  [ [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"C"), PlayingCard(12,"C"), PlayingCard(13,"S")]],
  [ [[PlayingCard(1,"S"),PlayingCard(10,"S")],[PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"D"), PlayingCard(13,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"S"), PlayingCard(10,"S"), PlayingCard(11,"S"), PlayingCard(12,"S"), PlayingCard(13,"S")]],
  [ [[PlayingCard(1,"H"),PlayingCard(10,"H")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(1,"H"), PlayingCard(10,"H"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],
  [ [[PlayingCard(10,"H"),PlayingCard(10,"D")],[PlayingCard(1,"C"), PlayingCard(10,"C"), PlayingCard(11,"D"), PlayingCard(12,"H"), PlayingCard(13,"S")]],[PlayingCard(10,"H"), PlayingCard(10,"D"), PlayingCard(10,"C"), PlayingCard(12,"C"), PlayingCard(13,"S")]]]
>>>>>>> Stashed changes
