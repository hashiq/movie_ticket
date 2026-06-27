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
    "KGF": {
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
         "Revenue": 0 },

}

def bookShow(movie,ticket):
    for key , value in vox_cinemas.items():
        availableSeat =  value["Ticket"]["Seat"]
        cost = value["Ticket"]["Price"]
        if key == movie:
           print("----------------")
           if availableSeat >= ticket:
               value["Ticket"]["Seat"] = availableSeat - ticket
               grand_total = ticket * cost
               print(grand_total)
               print("--------1--------")
           elif availableSeat <=ticket:
               print(f"there is no {ticket}, we have {availableSeat} ")
               print("--------2--------")

def allShow():
    for key , value in vox_cinemas.items():
        print(key)


choice = input(f"1:List all movie \n2:Book a movie \nChoose your option:")
if choice == "1":
    print("\n"*2)
    print("*** All shows ***")
    allShow()
elif choice == "2":
    print("\n" * 2)
    print("*** All shows ***")
    allShow()
    print("\n" * 1)
    userChoiceMovie = input("enter a movie name: ").title()
    userChoiceTicket = int(input("ticket :"))
    bookShow(movie=userChoiceMovie, ticket=userChoiceTicket)