watch_movie= True
vox_cinemas = {
    "Avengers": {
        "show_time": "10:00 AM",
        "seats": 10,
        "price": 5,
        "revenue": 0
    },
    "Batman": {
        "show_time": "01:00 PM",
        "seats": 8,
        "price": 4,
        "revenue": 0
    },
    "Spiderman": {
        "show_time": "04:00 PM",
        "seats": 12,
        "price": 6,
        "revenue": 0
    },
    "Johnwick": {
        "show_time": "07:00 PM",
        "seats": 15,
        "price": 7,
        "revenue": 0
    }
}

order = []

def modification():
    return


def query():
    user_movie = input("enter a movie :").capitalize()
    user_seats = int(input("enter seats needed :"))
    return user_movie,user_seats
print("===== VOX CINEMAS =====")
print("    Available Movies  ")
print("=======================")

#show all movies available
for movies, seat in vox_cinemas.items():
    print(f"{movies} -  ${vox_cinemas[movies]["price"]} ({vox_cinemas[movies]["seats"]} seats )")

#check seats available for show
def check_seat(movie_chosen, seat_chosen):
    movie = movie_chosen
    seat_status = True
    available_seats = vox_cinemas[movie]["seats"]
    if available_seats >= seat_chosen:
        vox_cinemas[movie]["seats"] = available_seats - seat_chosen
    elif available_seats < seat_chosen:
        print("no seats available ")
        seat_status = False
    return seat_status


#keep asking customer to choose show
while watch_movie:
    user_movie = input("choose a movie from above list :").capitalize()
    user_seats = int(input("how many seats you need :"))
    statu_seat = check_seat(movie_chosen=user_movie, seat_chosen=user_seats)
    if not statu_seat:
        next_order = input("Do you want to retry again :")
        if next_order == "yes":
           pass
        elif next_order == "no":
           print("thank you ")
           watch_movie = False
    elif statu_seat :
        print(vox_cinemas[user_movie]["seats"])
        movie_price = vox_cinemas[user_movie]["price"]
        grand_total = movie_price*user_seats
        print("✅ Booking Confirmed!")
        watch_movie = False
        print(f"Movie: {user_movie}")
        print(f"Tickets :{user_seats}")
        print(f"Total :{grand_total}")




