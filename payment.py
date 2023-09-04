import Home
import sql_integrator as sql



def recipt(booking_id):
    details = sql.search_booking(booking_id)
    print("\n\n --------------------------------")
    print("		 Hotel AnCasa")
    print(" --------------------------------")
    print("			 Bill")
    print(" --------------------------------")
    print(" Name: ",details[1] ,"\t\n Phone No.: ",details[2] ,"\t\n Address: ",details[3] ,"\t")
    print("\n Check-In: ",details[4] ,"\t\n Check-Out: ",details[5],"\t")
    print("\n Room No.: ",details[6] ,"\t\n Room Charges: ",details[8]*details[10] ,"\t")
    print(" Restaurant Charges: \t",details[9])
    print(" --------------------------------")
    total_bill = (details[8]*details[10])+details[9]
    print("\n Total Amount: ",( total_bill,"\t"))
    print(" --------------------------------")
    print("		 Thank You")
    print("		 Visit Again :)")
    print(" --------------------------------\n")
    archive_details = details[0], details[6], details[1], details[2], details[3], details[4], details[5], total_bill
    sql.archive_booking(archive_details)
    sql.mydb.commit()

def Payment():
    booking_id = int(input("Booking Id: "))
    # Find the booking with the input booking id
    bookings = sql.totalbookings()
    if booking_id in bookings:
        booking = booking_id
    else:
        print("Invalid Customer Id")
        return
    print(" Payment")
    print(" --------------------------------")
    print(" MODE OF PAYMENT")
    print(" 1- Credit/Debit Card")
    print(" 2- Paytm/PhonePe")
    print(" 3- Using UPI")
    print(" 4- Cash")
    x=int(input("-> "))
    print("\n Amount: ",(sql.total_bill(booking)))
    print("\n		 Pay For AnCasa")
    print(" (y/n)")
    ch=str(input("->"))
    if ch=='y' or ch=='Y':
        recipt(booking)
        booking = [booking]
        sql.delete_bookings(booking)



    
    print("\n\tPayment has been Made :)\n\n")
	
    Home.Home()