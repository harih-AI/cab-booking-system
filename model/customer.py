from model.User import User

class Customer(User):
    def book_room(self, user_id, room_id, check_in, check_out):
        cursor = self.conn.execute("SELECT * FROM ROOMS WHERE ID=? AND IS_AVAILABLE=1", (room_id,))
        room = cursor.fetchone()
        if room:
            self.conn.execute('''
                INSERT INTO BOOKINGS(USER_ID, ROOM_ID, CHECK_IN, CHECK_OUT)
                VALUES (?, ?, ?, ?)
            ''', (user_id, room_id, check_in, check_out))
            self.conn.execute("UPDATE ROOMS SET IS_AVAILABLE = 0 WHERE ID = ?", (room_id,))
            self.conn.commit()
            print("✅ Room booked successfully.")
        else:
            print("❌ Room not available.")

    def view_my_bookings(self, user_id):
        cursor = self.conn.execute('''
            SELECT B.ID, R.NUMBER, B.CHECK_IN, B.CHECK_OUT
            FROM BOOKINGS B
            JOIN ROOMS R ON B.ROOM_ID = R.ID
            WHERE B.USER_ID = ?
        ''', (user_id,))
        return cursor.fetchall()

    def get_available_rooms(self):
        cursor = self.conn.execute('''
            SELECT ID, NUMBER, TYPE, PRICE
            FROM ROOMS
            WHERE IS_AVAILABLE = 1
        ''')
        return cursor.fetchall()
