import Home
import sql_integrator as sql

records = sql.total_records()

def all_records():
     print("    *** HOTEL RECORD ***\n")
     print("| Bookking ID | Room No.  | Name          | Phone No.               | Address              | Check-In        | Check-Out    | ")
     print("----------------------------------------------------------------------------------------------------------------------")
        
     for x in records:
          print("|", x[0],"       |", x[6],"      |", x[1], "       |", x[2], "       |", x[3],"       |", x[4], "    |",x[5], "|" )#, booking['room_type'], " |", booking['price']
     print("----------------------------------------------------------------------------------------------------------------------")

     Home.Home()