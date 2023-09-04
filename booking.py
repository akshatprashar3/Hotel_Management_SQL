import Home
import random
import datetime
import sql_integrator as sql

# Function to check date validity
def is_valid_date(date):
    try:
        day, month, year = map(int, date.split('/'))
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

# Function for booking interface
def Booking():
    booking_id = 1000
    s = sql.totalbookings()
    while booking_id in s:
        booking_id = random.randint(1000,10000)

    print(" BOOKING ROOMS")
    print(" ")
    name = input("Name: ")
    while name.isnumeric():
         print("Incorrect Name")
         name = input("Re-Enter Name: ")
    phone_number = input("Phone No.: ")
    while len(phone_number) != 10:
         print("Incorrct Phone")
         phone_number = input("Re-Enter Phone Number: ")
    address = input("Address: ")
    while len(address) == 0:
         address = input("Please Enter Address: ")
    checkin_date = input("Check-In (dd/mm/yyyy): ")
    while not is_valid_date(checkin_date):
         print("\tInvalid date")
         checkin_date = input("Check-In (dd/mm/yyyy): ")
    checkout_date = input("Check-Out (dd/mm/yyyy): ")
    while not is_valid_date(checkout_date):
         print("\tInvalid date")
         checkout_date = input("Check-In (dd/mm/yyyy): ")
    # Validate input
    checkin_date = datetime.datetime.strptime(checkin_date, "%d/%m/%Y")
    checkout_date = datetime.datetime.strptime(checkout_date, "%d/%m/%Y")
    while checkout_date <= checkin_date:
        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        checkin_date = input("Check-In (dd/mm/yyyy): ")
        checkout_date = input("Check-Out (dd/mm/yyyy): ")
    days = checkout_date - checkin_date
    listt = [booking_id, name, phone_number, address, checkin_date, checkout_date]
    sql.insert_booking(listt)

    
    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC, Price : 3500")
    print(" 2. Standard AC, Price : 4000")
    print(" 3. 3-Bed Non-AC, Price : 4500")
    print(" 4. 3-Bed AC, Price : 5000")
    room_type = int(input("->"))
    rooms = sql.rooms_avaliable(room_type)
    while not rooms:
        print("Sorry No Rooms Avaliable")
        return
    while room_type not in range(1,5): 
        print(" Wrong choice..!!")
        print("----PLEASE SELECT ROOM TYPE FROM THE OPTIONS BELOW----")
        print(" 1. Standard Non-AC, Price : 3500")
        print(" 2. Standard AC, Price : 4000")
        print(" 3. 3-Bed Non-AC, Price : 4500")
        print(" 4. 3-Bed AC, Price : 5000")
        room_type = int(input("->"))
    room_id = random.choice(list(rooms))
    list_room = booking_id, days.days, room_id
    sql.update_rooms(list_room)
    sql.mydb.commit()

    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Booking_ID -> ",  booking_id,"\nRoom No -> ", room_id, "\nName -> ", name, "\nPhone Number -> ", phone_number, "\nCheck In Date -> ", checkin_date.date(), "\nCheck Out Date -> ", checkout_date.date())    

    Home.Home()







#rooms table intergation completed