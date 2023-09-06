class Hotel:
    sortParam ='name'
    def __init__(self) -> None:
        self.name = ''
        self.roomavl = 0
        self.loc = ''
        self.rating=int
        self.price=0

    def __lt__(self, other):
        getattr(self,Hotel.sortParam)<getattr(other,Hotel.sortParam)

    @classmethod
    def sortByName(cls):
        cls.sortParam='name'

    @classmethod
    def sortByRate(cls):
        cls.sortParam='rating'

    @classmethod
    def sortByRoomAvailability(cls):
        cls.sortParam='roomavl'

    def __repr__(self) -> str:
        return "PRHOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPricePer Room:{}".format(
            self.name, self.roomavl, self.loc, self.rating, self.price)

class User:
    def __init__(self) -> None:
        self.uname=''
        self.uid=0
        self.cost=0

    def __repr__(self) -> str:
        return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname, self.uid, self.cost)

def PrintHotelData(hotels):
    for h in hotels:
        print(h)
def SortHotelByName(hotels):
    print("sort by name: ")
    Hotel.sortByName()
    hotels.sort()
    PrintHotelData((hotels))
    print()
def SortHotelByRating(hotels):
    print("sort by ratings: ")
    Hotel.sortByRate()
    hotels.sort()
    PrintHotelData(hotels)
    print()
def PrintHotelByCity(s,hotels):
    print("Hotels for {} location are: ".format(s))
    hotelsByLoc = [h for h in hotels if h.loc==s]
    PrintHotelData(hotelsByLoc)
    print()
def SortByRoomAvailable(hotels):
    print("Sort by room avalaibility: ")
    Hotel.sortByRoomAvailability()
    hotels.sort()
    PrintHotelData(hotels)
    print()
def PrintUserData(userName,UserId,bookingCost,hotels):
    users =[]
    for i in range(3):
        u=User()
        u.uname = userName[i]
        u.uid = UserId[i]
        u.cost = bookingCost[i]
        users.append(u)
    for i in range(len(users)):
        print(users[i],"\tHotel name: ",hotels[i].name)

def HotelManagement(userName,UserID,hotelName,bookinCost,rooms,locations,ratings,prices):
    hotels =[]

    for i in range(3):
        h=Hotel()
        h.name=hotelName[i]
        h.roomavl=rooms[i]
        h.loc=locations[i]
        h.rating=ratings[i]
        h.price=prices[i]
        hotels.append(h)
    print()

    PrintHotelData(hotels)
    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelByCity("Bangalore",hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(userName,UserID,bookinCost,hotels)

if __name__ == '__main__':
    userName = ["u1","u2","u3"]
    userID = [2,3,4]
    hotelName = ["H1","H2","H3"]
    bookingCost = [1000,1200,4333]
    rooms = [2,3,4]
    locations =["Bangalore","Bangalore","Hyderabad"]
    ratings = [3,4,5]
    prices = [100,332,566]

    HotelManagement(userName,userID,hotelName,bookingCost,rooms,locations,ratings,prices)