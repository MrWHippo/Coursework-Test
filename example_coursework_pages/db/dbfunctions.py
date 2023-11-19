import sqlite3

def insert_user(username, password, id):
    conn = sqlite3.connect('poker.db')
    try:
        conn.execute(f"INSERT INTO ACCOUNTS (USERNAME,PASSWORD,ID) \
                    VALUES ('{username}','{password}',{id});")
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False

def set_stats_for_new_user(id):
    conn = sqlite3.connect('poker.db')
    conn.execute(f"INSERT INTO STATS (ID, WIN_PERCENTAGE, NUMBER_OF_GAMES, LARGEST_POT, BIGGEST_LOSS, VPIP, PFR, PF_RAISE_TALLY, NUMBER_OF_BETS, NUMBER_OF_RAISES, TOTAL_CHOICE_COUNT, AGGRESSION_STAT, NUMBER_OF_WINS, NUMBER_OF_HANDS, VPIP_COUNT ) \
                 VALUES ({id}, 0 ,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);")
    conn.commit()
    conn.close()

def create_new_account(username, password, id):
    if insert_user(username, password, id):
        set_stats_for_new_user(id)
        print(f"{username} inserted successfully.")
    else:
        print(f"Error inserting user: {username}.")

def read_whole_db():
    conn = sqlite3.connect('poker.db')
    db = conn.execute("SELECT USERNAME, PASSWORD, ID from ACCOUNTS;")
    for value in db:
        print("--------------")
        print("ID = ", value[2])
        print("Username = ", value[0])
        print("Password = ", value[1])
    db = conn.execute("SELECT ID, WIN_PERCENTAGE, NUMBER_OF_GAMES, LARGEST_POT, BIGGEST_LOSS, VPIP, PFR, PF_RAISE_TALLY, NUMBER_OF_BETS, NUMBER_OF_RAISES, TOTAL_CHOICE_COUNT, AGGRESSION_STAT, NUMBER_OF_WINS, NUMBER_OF_HANDS, VPIP_COUNT from STATS;")
    for value in db:
        print("--------------")
        print("ID = ", value[0])
        print("Win Percentage = ", value[1])
        print("Number Of Games = ", value[2])
        print("Largest Pot Won = ", value[3])
        print("Biggest Loss = ", value[4])
        print("VPIP = ", value[5])
        print("PFR = ", value[6])
        print("PF Raise Tally = ", value[7])
        print("Number Of Bets = ", value[8])
        print("Number Of Raises = ", value[9])
        print("Total Choice Count= ", value[10])
        print("Aggression Stat = ", value[11])
        print("Number of Wins = ", value[12])
        print("Number of Hands = ", value[13])
        print("VPIP Count = ", value[14])
    conn.close()

def check_if_username_available(username):
    conn = sqlite3.connect('poker.db')
    check = list(conn.execute(f"SELECT USERNAME from ACCOUNTS where USERNAME == {username};"))
    conn.close()
    return (check[0][0] == None)

### Gets

def get_username(id):
    conn = sqlite3.connect('poker.db')
    username = list(conn.execute(f"SELECT username from ACCOUNTS where ID ={id};"))
    conn.close()
    return username[0][0]

def get_password(username):
    conn = sqlite3.connect('poker.db')
    password = list(conn.execute(f"SELECT password from ACCOUNTS where USERNAME == {username};"))
    conn.close()
    return password[0][0]

def get_id(username):
    conn = sqlite3.connect('poker.db')
    id = list(conn.execute(f"SELECT ID from ACCOUNTS where USERNAME == {username};"))
    conn.close()
    return id[0][0]

def get_user_stats(id):
    conn = sqlite3.connect('poker.db')
    stats = list(conn.execute(f"SELECT * from STATS where ID == {id};"))
    conn.close()
    return stats

def get_win_percentage(id):
    conn = sqlite3.connect('poker.db')
    winper = list(conn.execute(f"SELECT WIN_PERCENTAGE from STATS where ID == {id};"))
    conn.close()
    return winper[0][0]

def get_num_Games(id):
    conn = sqlite3.connect('poker.db')
    NGame = list(conn.execute(f"SELECT NUMBER_OF_GAMES from STATS where ID == {id};"))
    conn.close()
    return NGame[0][0]

def get_largest_pot(id):
    conn = sqlite3.connect('poker.db')
    Lpot = list(conn.execute(f"SELECT LARGEST_POT from STATS where ID == {id};"))
    conn.close()
    return Lpot[0][0]

def get_biggest_loss(id):
    conn = sqlite3.connect('poker.db')
    BLoss = list(conn.execute(f"SELECT BIGGEST_LOSS from STATS where ID == {id};"))
    conn.close()
    return BLoss[0][0]

def get_VPIP(id):
    conn = sqlite3.connect('poker.db')
    VPIP = list(conn.execute(f"SELECT VPIP from STATS where ID == {id};"))
    conn.close()
    return VPIP[0][0]

def get_PFR(id):
    conn = sqlite3.connect('poker.db')
    PFR = list(conn.execute(f"SELECT PFR from STATS where ID == {id};"))
    conn.close()
    return PFR[0][0]

def get_pf_raise_tally(id):
    conn = sqlite3.connect('poker.db')
    RaiseT = list(conn.execute(f"SELECT PF_RAISE_TALLY from STATS where ID == {id};"))
    conn.close()
    return RaiseT[0][0]

def get_num_bets(id):
    conn = sqlite3.connect('poker.db')
    NumBets = list(conn.execute(f"SELECT NUMBER_OF_BETS from STATS where ID == {id};"))
    conn.close()
    return NumBets[0][0]

def get_num_raises(id):
    conn = sqlite3.connect('poker.db')
    NumRaise = list(conn.execute(f"SELECT NUMBER_OF_RAISES from STATS where ID == {id};"))
    conn.close()
    return NumRaise[0][0]

def get_num_total_choice_count(id):
    conn = sqlite3.connect('poker.db')
    TotalChoiceCount = list(conn.execute(f"SELECT TOTAL_CHOICE_COUNT from STATS where ID == {id};"))
    conn.close()
    return TotalChoiceCount[0][0]

def get_aggression_stat(id):
    conn = sqlite3.connect('poker.db')
    AggressionStat = list(conn.execute(f"SELECT AGGRESSION_STAT from STATS where ID == {id};"))
    conn.close()
    return AggressionStat[0][0]

def get_num_wins(id):
    conn = sqlite3.connect('poker.db')
    NumWins = list(conn.execute(f"SELECT NUMBER_OF_WINS from STATS where ID == {id};"))
    conn.close()
    return NumWins[0][0]

def get_num_hands(id):
    conn = sqlite3.connect('poker.db')
    NumHands = list(conn.execute(f"SELECT NUMBER_OF_HANDS from STATS where ID == {id};"))
    conn.close()
    return NumHands[0][0]

def get_vpip_count(id):
    conn = sqlite3.connect('poker.db')
    VPIPCount = list(conn.execute(f"SELECT VPIP_COUNT from STATS where ID == {id};"))
    conn.close()
    return VPIPCount[0][0]

### Recalculations

def recalculate_win_percentage(id):
    WinPer = (get_num_wins(id)/get_num_Games(id))*100
    return WinPer

def recalculate_PFR(id):
    new_PFR =  (get_pf_raise_tally(id)/get_num_hands(id))*100
    return new_PFR

def recalculate_VPIP(id):
    new_VPIP =  (get_vpip_count(id)/get_num_hands(id))*100
    return new_VPIP
# later -> -1 hands if there is a walk (play wins during big blind as everyone else folds)

def recalculate_aggression(id):
    new_aggression = (get_num_bets(id)+get_num_raises(id))/get_num_total_choice_count(id)
    return new_aggression

### updating/increasing stats

def update_win_percentage(id, WinPercentage):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET WIN_PERCENTAGE == {WinPercentage} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_PFR(id, PFR):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET PFR == {PFR} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_VPIP(id, VPIP):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET VPIP == {VPIP} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_aggression_stat(id, Aggression):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET AGGRESSION_STAT == {Aggression} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def increase_number_of_games(id):
    NumGames = get_num_Games(id) + 1
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET NUMBER_OF_GAMES == {NumGames} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_largest_pot(id, LargestPot):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET LARGEST_POT == {LargestPot} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_biggest_loss(id, BiggestLoss):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET BIGGEST_LOSS == {BiggestLoss} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def increase_pf_raise_tally(id):
    pfRaiseTally = get_pf_raise_tally(id) + 1
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET PF_RAISE_TALLY == {pfRaiseTally} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_number_of_bets(id, NumBets):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET NUMBER_OF_BETS == {NumBets} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_number_of_raises(id, NumRaises):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET NUMBER_OF_RAISES == {NumRaises} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def update_number_of_choices(id, NumChoiceCount):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET TOTAL_CHOICE_COUNT == {NumChoiceCount} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def increase_number_of_wins(id):
    NumWins = get_num_wins(id) + 1
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET NUMBER_OF_WINS == {NumWins} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def increase_number_of_hands(id):
    NumHands = get_num_hands(id) + 1
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET NUMBER_OF_HANDS == {NumHands} WHERE ID == {id};''')
    conn.commit()
    conn.close()

def increase_vpip_count(id):
    vpipCount = get_vpip_count(id) + 1
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET VPIP_COUNT == {vpipCount} WHERE ID == {id};''')
    conn.commit()
    conn.close()

### delete and reset stats 

def delete_account(id):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''DELETE FROM STATS WHERE ID == {id};''')
    conn.commit()
    conn.execute(f'''DELETE FROM ACCOUNTS WHERE ID == {id};''')
    conn.commit()
    conn.close()

def reset_account(id):
    conn = sqlite3.connect('poker.db')
    conn.execute(f'''UPDATE STATS SET WIN_PERCENTAGE = 0, NUMBER_OF_GAMES = 0, LARGEST_POT = 0, BIGGEST_LOSS = 0, VPIP = 0, PFR = 0, PF_RAISE_TALLY = 0, NUMBER_OF_BETS = 0, NUMBER_OF_RAISES = 0, TOTAL_CHOICE_COUNT = 0, AGGRESSION_STAT = 0, NUMBER_OF_WINS = 0, NUMBER_OF_HANDS = 0, VPIP_COUNT = 0 FROM STATS WHERE ID == {id};''')
    conn.commit()
    conn.close()


#create_new_account("Jonty","88", 1)
#create_new_account("Daniel","its_dan123", 2)
#create_new_account("BOBBY12","bob900", 3)

