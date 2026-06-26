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
        "Revenue": {
            "Today": 9000,
            "Profit": 0
        }
    },
    "Karuppu": {
        "Language": "Tamil",
        "Genre": "Drama",
        "Movie": {"Director": "Arun Kumar",
                  "Cast": ["Surya","Indratrance"]},
        "Ticket": {"Seat": 150,"Price": 120 },
        "Revenue": {"Today": 15600,"Profit": 0} }}

def bookShow(movie,ticket):
    for key , value in vox_cinemas.items():
        if key == movie:
            availableSeat =  value["Ticket"]["Seat"]
            cost = value["Ticket"]["Price"]
            if availableSeat >= ticket:
               print(f"current seat{value["Ticket"]["Seat"]}")
               print(f"reduce seat : {availableSeat-ticket}")
               grandTotal = ticket * cost
               return grandTotal

userChoiceMovie = input("enter a movie name: ").title()
userChoiceTicket = int(input("ticket qty :"))
print(bookShow(movie=userChoiceMovie,ticket=userChoiceTicket))
print(vox_cinemas[userChoiceMovie])