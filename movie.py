run_booking = True
vox_cinemas = {
    "Athiradi": {
        "Language": "Malayalam",
        "Genre": "Comedy",
        "Movie": {
            "Director": "Rahul",
            "Cast": ["Basil Joseph", "Tovino"]
        },
        "Ticket": {
            "Seat": 120,
            "Price": 100
        },
        "Revenue": 0 },
    "Karuppu": {
        "Language": "Tamil",
        "Genre": "Drama",
        "Movie": {"Director": "Arun Kumar",
                  "Cast": ["Surya","R.j Balaji"]},
        "Ticket": {"Seat": 150,"Price": 120 },
         "Revenue": 0 },
    "Batman": {
        "Language": "English",
        "Genre": "Action",
        "Movie": {"Director": "James Cameroon",
                  "Cast": ["Ben flack"]},
        "Ticket": {"Seat": 10, "Price": 120},
         "Revenue": 0 },
    "Superman": {
        "Language": "English",
        "Genre": "Action",
        "Movie": {"Director": "James Cameroon","Cast": ["Henry Cavil"]},
        "Ticket": {"Seat": 5, "Price": 300},
         "Revenue": 0 },
    "Kgf": {
        "Language": "Telung",
        "Genre": "Action",
        "Movie": {"Director": "Prashand Neel","Cast": ["Yash"]},
        "Ticket": {"Seat": 2, "Price": 250},
         "Revenue": 0 },
    "F1": {
        "Language": "English",
        "Genre": "Sports",
        "Movie": {"Director": "Micky wan","Cast": ["Brad Pitt"]},
        "Ticket": {"Seat": 1, "Price": 150},
         "Revenue": 0 },}

def bookShow(movie,ticket):
    for key , value in vox_cinemas.items():
        status = True
        availableSeat =  value["Ticket"]["Seat"]
        cost = value["Ticket"]["Price"]
        if key == movie:
           if availableSeat >= ticket:
               value["Ticket"]["Seat"] = availableSeat - ticket
               grand_total = ticket * cost
               print(f"{movie} x {ticket}:$ {grand_total}")
           elif availableSeat <=ticket:
               print(f"there is only {availableSeat} seats , you request {ticket} seats ")
               status = False
    return status
def allShow(user_):
    if user_ == "1":
        for key, value in vox_cinemas.items():

    elif user_ =="3":


while run_booking:
    choice = input(f"1:List all movie \n2:Book a movie \n3:Report \nChoose your option:")
    if choice == "1":
        print("\n" * 2)
        print("*** All shows ***")
        allShow()
    elif choice == "2":
        print("\n" * 2)
        print("*** All shows ***")
        allShow()
        print("\n" * 1)
        userChoiceMovie = input("enter a movie name:").title()
        userChoiceTicket = int(input("ticket :"))
        booking_status = bookShow(movie=userChoiceMovie, ticket=userChoiceTicket)
        if booking_status == True:
            BookingContinue = input("Do you want to continue: ").lower()
            if BookingContinue == "no":
                run_booking = False
                print("Thank you Enjoy your movie")
        else:
            run_booking = booking_status
    elif choice=="3"


