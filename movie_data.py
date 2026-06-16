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
    "Spider-Man": {
        "show_time": "04:00 PM",
        "seats": 12,
        "price": 6,
        "revenue": 0
    },
    "John Wick": {
        "show_time": "07:00 PM",
        "seats": 15,
        "price": 7,
        "revenue": 0
    }
}


def seat(movie,seats):
    for key, value in vox_cinemas:
        if value["seats"] >= seats:
            pass
    return "watch the movie"


movie =  input("enter movie name :")
seats = int(input("enter no.of seats :"))
seat(movie,seats)