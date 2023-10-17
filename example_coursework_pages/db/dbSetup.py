import sqlite3

conn = sqlite3.connect('poker.db')

conn.execute('''CREATE TABLE ACCOUNTS
             (USERNAME          TEXT NOT NULL PRIMARY KEY,
             PASSWORD           PASSWORD NOT NULL,
             ID                 INTEGER NOT NULL UNIQUE);''')

conn.execute('''CREATE TABLE STATS
             (ID                INTEGER NOT NULL PRIMARY KEY,
             WIN_PERCENTAGE     INTEGER,
             NUMBER_OF_GAMES    INTEGER,
             LARGEST_POT        INTEGER,
             BIGGEST_LOSS       INTEGER,
             VPIP               INTEGER,
             PFR                INTEGER,
             CHOICE_TALLY       INTEGER,
             RAISE_TALLY        INTEGER,
             NUMBER_OF_BETS     INTEGER,
             NUMBER_OF_RAISES   INTEGER,
             TOTAL_CHOICE_COUNT INTEGER,
             AGGRESSION_STAT    INTEGER,
             FOREIGN KEY(ID) REFERENCES ACCOUNTS(ID));''')

print("Table created successfully")

conn.close()
