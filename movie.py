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
    status = True
    if vox_cinemas[] >= ticket:
        value["Ticket"]["Seat"] -= ticket
        grand_total = ticket * cost
        value["Revenue"] += grand_total
        print(f"{movie} x {ticket}:$ {grand_total}")
    elif availableSeat <= ticket:
        print(f"there is only {availableSeat} seats , you request {ticket} seats ")
        status = False

    return status

def allShow(user_):
    revenue_total=0
    if user_ == "1":
        for key, value in vox_cinemas.items():
            print(key)
    elif user_ == "3":
        for key, value in vox_cinemas.items():
            revenue_total += value['Revenue']
            print(f"Movie :{key}"
                 f"\nprofit :{value['Revenue']}"
                 # f"\nseats remain : {value['Ticket']['Seat']}"
                  f"")
        print(f"over all profit:{revenue_total}")
        print("\n"*1)


while run_booking:
    all_movies = []
    choice = input(f"1:List all movie \n2:Book a movie \n3:Report \nChoose your option:")
    if choice == "1":
        print("\n" * 2)
        print("*** All shows ***")
        allShow(choice)
    elif choice == "2":
        print("\n" * 1)

        for key, value in vox_cinemas.items():
            all_movies.append(key)
        userChoiceMovie = input("enter a movie name:").title()
        if userChoiceMovie  in all_movies:
                try:
                    userChoiceTicket = int(input("ticket :"))
                    if userChoiceTicket >= 1:
                        booking_status = bookShow(movie=userChoiceMovie, ticket=userChoiceTicket)
                        if booking_status == True:
                            BookingContinue = input("Do you want to continue: ").lower()
                            if BookingContinue == "no":
                                run_booking = False
                                print("Thank you Enjoy your movie")
                    elif userChoiceTicket <= 0:
                        print("\n" * 2)
                        print("You cant go ticket less than '1'")
                except:
                    print("You enter string not numbers for tickets ")
        else:
            print("Movie Not founded, Lets restart again")
            print("\n"*1)
    elif choice == "3":
         print("**reports**")
         allShow(choice)






