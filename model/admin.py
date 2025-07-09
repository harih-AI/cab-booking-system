from model.User import User

class Admin(User):
    def add_room(self,number,room_type,price):
        self.conn.execute("INSERT INTO ROOMS(NUMBER,TYPE,PRICE,IS_AVAILABLE) VALUES(?,?,?,1)",(number,room_type,price))
        self.conn.commit()
    
    def delete_room(self,room_id):
        self.conn.execute("DELETE FROM rooms WHERE ID=?",(room_id,))
        self.conn.commit()
    def view_bookings(self):
        cursor=self.conn.execute(
            '''
            SELECT B.ID,U.NAME,R.NAME,B.CHECK_IN,B.CHECK_OUT
            FROM BOOKINGS B,
            JOIN USERS U ON B.USER_ID=U.ID
            JOIN ROOMS R ON B.ROOM_ID=R.ID
            '''
        )
        return cursor.fetchall()
    