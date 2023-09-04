import booking
import rooms_info
import restaurant
import payment
import records



# Driver Code

def Home():
    print("\t\t\t\t\t\t WELCOME TO HOTEL ANCASA\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service(Menu Card)\n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit\n")

    ch = int(input("->"))
        
    if ch == 1:
        print(" ")
        booking.Booking()
            
    elif ch == 2:
        print(" ")
        rooms_info.room_desc()
            
    elif ch == 3:
        print(" ")
        restaurant.menu()
            
    elif ch == 4:
        print(" ")
        payment.Payment()
            
    elif ch == 5:
        print(" ")
        records.all_records()
            
    elif ch == 0:
        exit()
            
    else:
        print("Invalid option, please try again.")

if __name__ == "__main__":
    Home()

