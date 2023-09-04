import Home
import sql_integrator as sql

def menu():
    booking_id = int(input("Booking Id: "))
    # Find the booking with the input booking id
    bookings = sql.totalbookings()
    if booking_id in bookings:
        booking = booking_id
    else:
        print("Invalid Customer Id")
        return
    
    print("-------------------------------------------------------------------------")
    print("						 Hotel AnCasa")
    print("-------------------------------------------------------------------------")
    print("						 Menu Card")
    print("-------------------------------------------------------------------------")
    print("\n BEVARAGES							 26 Dal Fry................ 140.00")
    print("----------------------------------	 27 Dal Makhani............ 150.00")
    print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
    print(" 2 Masala Tea.............. 25.00")
    print(" 3 Coffee.................. 25.00	 ROTI")
    print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
    print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
    print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
    print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
    print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
    print(" 9 Cheese Toast Sandwich... 70.00")
    print(" 10 Grilled Sandwich........ 70.00	 RICE")
    print("									 ----------------------------------")
    print(" SOUPS								 33 Plain Rice.............. 90.00")
    print("----------------------------------	 34 Jeera Rice.............. 90.00")
    print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
    print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
    print(" 13 Veg. Noodle Soup....... 110.00")
    print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
    print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
    print("									 37 Plain Dosa............. 100.00")
    print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
    print("----------------------------------	 39 Masala Dosa............ 130.00")
    print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
    print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
    print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
    print(" 19 Palak Paneer........... 120.00")
    print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
    print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
    print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
    print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
    print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
    print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
    print("Press 0 -to end ")
    
    
    total_price = 0
    while True:
        ch = int(input(" -> "))
        if ch == 0:
            break

        # if-elif-conditions to assign item prices listed in menu card
        # Assuming the menu items are priced according to the same rules
        if ch in [1, 31, 32]:
            rs = 20
        elif ch in range(2, 5):
            rs = 25
        elif ch in range(5, 7):
            rs = 30
        elif ch in range(7, 9):
            rs = 50
        elif ch in range(9, 11):
            rs = 70
        elif ch in range(11, 18) or ch in [35, 36, 38]:
            rs = 110
        elif ch in range(18, 20):
            rs = 120
        elif ch in range(20, 27) or ch == 42:
            rs = 140
        elif ch in range(27, 29):
            rs = 150
        elif ch in range(29, 31):
            rs = 15
        elif ch in [33, 34]:
            rs = 90
        elif ch == 37:
            rs = 100
        elif ch in range(39, 42):
            rs = 130
        elif ch in range(43, 47):
            rs = 60
        else:
            print("Wrong Choice..!!")
            continue  # Go to the next iteration of the loop

        total_price += rs

    print("Total Bill: ", total_price)
    # Update the restaurant charges in the booking
    sql.update_restaurant(total_price, booking)
    sql.mydb.commit()

    Home.Home()


