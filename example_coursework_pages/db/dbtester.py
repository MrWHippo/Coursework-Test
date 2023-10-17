import sqlite3

conn = sqlite3.connect('poker.db')

def insert_user(username, password, id):
    conn.execute(f"INSERT INTO ACCOUNTS (USERNAME,PASSWORD,ID) \
                 VALUES ('{username}','{password}',{id})")
    conn.commit()

def set_stats_for_new_user(id):
    conn.execute(f"INSERT INTO STATS (ID, WIN_PERCENTAGE, NUMBER_OF_GAMES, LARGEST_POT, BIGGEST_LOSS,VPIP,PFR,CHOICE_TALLY,RAISE_TALLY,NUMBER_OF_BETS,NUMBER_OF_RAISES,TOTAL_CHOICE_COUNT,AGGRESSION_STAT) \
                 VALUES ({id}, 0 ,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
    conn.commit()

def read_db():
    db = conn.execute("SELECT USERNAME, PASSWORD, ID from ACCOUNTS")
    for value in db:
        print("--------------")
        print("ID = ", value[2])
        print("Username = ", value[0])
        print("Password = ", value[1])
    db = conn.execute("SELECT ID, WIN_PERCENTAGE, NUMBER_OF_GAMES, LARGEST_POT, BIGGEST_LOSS,VPIP,PFR,CHOICE_TALLY,RAISE_TALLY,NUMBER_OF_BETS,NUMBER_OF_RAISES,TOTAL_CHOICE_COUNT,AGGRESSION_STAT from STATS")
    for value in db:
        print("--------------")
        print("ID = ", value[0])
        print("Win Percentage = ", value[1])
        print("Number Of Games = ", value[2])
        print("Largest Pot Won = ", value[3])
        print("Biggest Loss = ", value[4])
        print("VPIP = ", value[5])
        print("PFR = ", value[6])
        print("Choice Tally = ", value[7])
        print("Raise Tally = ", value[8])
        print("Number Of Bets = ", value[9])
        print("Number Of Raises = ", value[10])
        print("Total Choice Count= ", value[11])
        print("Aggression Stat = ", value[12])

insert_user('Daniel','its_dan123',2)
set_stats_for_new_user(2)
read_db()

conn.close()