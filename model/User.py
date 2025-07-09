from db.database import get_connection

class User:
    def __init__(self):
        self.conn = get_connection()

    def register(self, name, email, password, role='CUSTOMER'):
        try:
            self.conn.execute("INSERT INTO USERS(NAME, EMAIL, PASSWORD, ROLE) VALUES (?, ?, ?, ?)",
                              (name, email, password, role.upper()))
            self.conn.commit()
            print("User registered.")
        except Exception as e:
            print("Error:", e)

    def login(self, email, password):
        cursor = self.conn.execute("SELECT * FROM USERS WHERE EMAIL=? AND PASSWORD=?", (email, password))
        return cursor.fetchone()
