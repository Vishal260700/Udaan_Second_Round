from datetime import datetime, date
import calendar

class Bus():

    def _init_(self, company, number, src, dest, start_time, end_time, active_days, seats):
        self.company = company
        self.number = number
        self.name = self.company + self.number
        self.src = src
        self.dest = dest
        self.start_time = start_time
        self.end_time = end_time
        self.active_days = active_days
        self.seats = seats
        self.booking_log = dict()
    
    def is_available(self, src, dest, date):
        if self.src == src and self.dest == dest and date.weekday() in self.active_days:
            return True
        return False
        
    def reserve_seats(self, src, dest, date, seats):
        if date not in self.booking_log.keys():
            self.booking_log[date] = self.seats

        if self.booking_log[date] >= seats and self.booking_log[date] >0:
            self.booking_log[date] -= seats
            return True
        return False

    
class User():

    def _init_(self, username):
        self.username = username
        self.reservation_logs = []

    def view_reservations(self):
        print(self.reservation_logs)
    
    def reserve_seats(self, bus, src, dest, date, seats):
        bus.reserve_seats(src, dest, date, seats)
        self.reservation_logs.append({'bus_name': bus.name, 'src': src, 'dest':dest, 'date':date, 'seats': seats})

class Bus_Repo():

    def _init_(self):
        self.buses = dict()
        self.fill_repo()

    def fill_repo(self):
        bus1 = Bus('AirBus', '345', 'jaipur', 'kota', 1, 2, [0,1,2], 100)
        bus2 = Bus('AirBus', '346', 'kota', 'ajmer', 1, 2, [3,4,5], 100)
        self.buses[bus1.name] = bus1
        self.buses[bus2.name] = bus2

class API():

    def _init_(self):
        self.repository = Bus_Repo()
    
    def search_bus(self, src, dest, date):
        available_buses = []
        for bus_name in self.repository.buses.keys():
            if self.repository.buses[bus_name].is_available(src, dest, date):
                available_buses.append(bus_name)
    
        if len(available_buses) != 0:
            print("Following buses are available")
            print(available_buses)
        else:
            print("No Buses Found :)")
        
        # return available_buses
        
    def book_seats(self, user, bus_name, src, dest, date, seats):
        
        if self.repository.buses[bus_name].is_available(src, dest, date):
            user.reserve_seats(self.repository.buses[bus_name], src, dest, date, seats)
            print("Success")
        else:
            print("Failure")
    
    def view_reservations(self, user):
        return user.view_reservations()


if _name_ == '_main_':

    api = API()

    user_repo = dict()

    run = True
    while(run):
        print("Welcome")
        username = input('Enter your username\n')   
        user = None
        if username in user_repo.keys():
            user = user_repo[username]
        else:
            user = User(username)
        
        val = int(input(("Press 1 to search buses\n Press 2 to book tickets\n Press 3 to view reservation history\n"))

        if val == 1 or val == 2:
            src = input("Enter src\n")
            dest = input("Enter dest\n")
            date_entry = input('Enter a date (i.e. 2020,11,1)')
            year, month, day = map(int, date_entry.split(','))
            date = datetime(year, month, day)


        if val == 1:
            api.search_bus(src, dest, date)

        if val == 2:
            bus_name = input("Enter bus_name\n")
            seats = int(input("Enter number of seats\n"))
            api.book_seats(user, bus_name, src, dest, date, seats)

        if val == 3:
            api.view_reservations(user)
        
        if int(input("Press 0 to exit.\n")) == 0:
            break