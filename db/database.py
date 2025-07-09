import sqlite3

# Database Manager Class
class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('hotel.db')
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT,
                EMAIL TEXT UNIQUE NOT NULL,
                PASSWORD TEXT,
                ROLE TEXT CHECK(ROLE IN ('CUSTOMER','ADMIN'))
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ROOMS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NUMBER TEXT,
                TYPE TEXT,
                PRICE REAL,
                IS_AVAILABLE INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS BOOKINGS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USER_ID INTEGER,
                ROOM_ID INTEGER,
                CHECK_IN TEXT,
                CHECK_OUT TEXT,
                FOREIGN KEY(USER_ID) REFERENCES USERS(ID),
                FOREIGN KEY(ROOM_ID) REFERENCES ROOMS(ID)
            )
        ''')
        self.conn.commit()

# Correct connection function (points to hotel.db)
def get_connection():
    conn = sqlite3.connect('hotel.db')  # <- Match this with DatabaseManager
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
