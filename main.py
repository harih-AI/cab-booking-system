from db.database import DatabaseManager
from model.admin import Admin
from model.customer import Customer
from model.User import User

def main():
    db = DatabaseManager()
    db.create_table()

    while True:
        print("\n===== Hotel Reservation System =====")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose option: ").strip()

        if choice == '1':
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role (admin/customer): ").strip().lower()

            if role not in ['admin', 'customer']:
                print("Invalid role! Must be 'admin' or 'customer'.")
                continue

            user = Admin() if role == 'admin' else Customer()
            user.register(name, email, password, role.upper())

        elif choice == '2':
            email = input("Email: ")
            password = input("Password: ")

            base_user = User()
            user_data = base_user.login(email, password)

            if user_data:
                user_id, _, _, _, role = user_data
                role = role.lower()

                if role == 'admin':
                    admin = Admin()
                    bookings = admin.view_bookings()
                    print("\nAll Bookings:")
                    for b in bookings:
                        print(f"Booking ID: {b[0]}, User: {b[1]}, Room: {b[2]}, Check-in: {b[3]}, Check-out: {b[4]}")

                elif role == 'customer':
                    customer = Customer()
                    while True:
                        print("\n1. Book Room\n2. View My Bookings\n3. Logout")
                        ch = input("Enter choice: ").strip()

                        if ch == '1':
                            # ✅ Show available rooms before booking
                            rooms = customer.get_available_rooms()
                            if not rooms:
                                print("No available rooms.")
                                continue

                            print("\nAvailable Rooms:")
                            for r in rooms:
                                print(f"Room ID: {r[0]}, Number: {r[1]}, Type: {r[2]}, Price: {r[3]}")

                            room_id = int(input("Enter Room ID from the list above: "))
                            check_in = input("Check-in (YYYY-MM-DD): ")
                            check_out = input("Check-out (YYYY-MM-DD): ")
                            customer.book_room(user_id, room_id, check_in, check_out)

                        elif ch == '2':
                            bookings = customer.view_my_bookings(user_id)
                            print("\nYour Bookings:")
                            for b in bookings:
                                print(f"Booking ID: {b[0]}, Room: {b[1]}, Check-in: {b[2]}, Check-out: {b[3]}")
                        elif ch == '3':
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice.")
            else:
                print("Invalid login credentials.")

        elif choice == '3':
            print("Thank you for using the Hotel Reservation System. Goodbye!")
            break

        else:
            print("Invalid option selected.")

if __name__ == '__main__':
    main()
