import mysql.connector

mydb = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "12341234ribu",
     database = "hotelmanagement"
)
# Databse Declaration
cursor = mydb.cursor()
def totalbookings():
    cursor.execute("SELECT booking_id FROM names")
    s = cursor.fetchall()
    return {x[0] for x in s}

def search_booking(booking_id):
    cursor.execute("SELECT * FROM names INNER JOIN rooms ON names.booking_id = rooms.booking_id")
    bookings = cursor.fetchall()
    for x in bookings:
        if x[0] == booking_id:
            lis = list(x)
            return lis

def rooms_avaliable(room_type):
    cursor.execute("SELECT room_no, booking_id, price FROM rooms")
    r = cursor.fetchall()
    rooms_avaliable = set()
    for x in r:
        if room_type == 4 and x[2] == 5000 and  x[1] == None:
            rooms_avaliable.add(x[0])
        elif room_type == 3 and x[2] == 4500 and  x[1] == None:
            rooms_avaliable.add(x[0])
        elif room_type == 2 and x[2] == 4000 and  x[1] == None:
            rooms_avaliable.add(x[0])
        elif room_type == 1 and x[2] == 3500 and x[1] == None:
            rooms_avaliable.add(x[0])
    return rooms_avaliable

def insert_booking(listt):
    cursor.execute("INSERT INTO names(booking_id, name, phone, address, check_in, check_out) VALUES(%s, %s, %s, %s, DATE(%s), DATE(%s))", listt)
    
def update_rooms(list_room):
    cursor.execute("UPDATE rooms SET booking_id = %s, days = %s WHERE room_no = %s", list_room)

def update_restaurant(total_price, booking):
    cursor.execute("UPDATE rooms SET restaurant_charges = %s WHERE booking_id = %s", (total_price, booking))

def delete_bookings(booking):
    cursor.execute("DELETE FROM names WHERE booking_id = %s", (booking))
    cursor.execute("UPDATE rooms SET booking_id = null, restaurant_charges = 0, days = 0 WHERE booking_id = %s", (booking))
    mydb.commit()

def total_records():
    cursor.execute("SELECT * FROM names INNER JOIN rooms ON names.booking_id = rooms.booking_id")
    records = cursor.fetchall()
    return records

def total_bill(booking):
    cursor.execute("SELECT * FROM names INNER JOIN rooms ON names.booking_id = rooms.booking_id")
    bookings = cursor.fetchall()
    for x in bookings:
        if x[0] == booking:
            return int((x[8]*x[10]) + x[9])

def archive_booking(archive_details):
    cursor.execute("INSERT INTO archive (booking_id, room_no, name, phone, address, check_in, check_out, total_bill) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (archive_details))