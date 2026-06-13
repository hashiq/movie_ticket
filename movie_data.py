vox_cinemas = {
    "running": {
        "Avengers": {
            "show_time": "10:00 AM",
            "language": "English",
            "seats": {"Standard": 20, "Premium": 15, "VIP": 10}
        },

        "Karuppu": {
            "show_time": "1:00 PM",
            "language": "Tamil",
            "seats": {"Standard": 25, "Premium": 18, "VIP": 12}
        },

        "Batman": {
            "show_time": "4:00 PM",
            "language": "English",
            "seats": {"Standard": 30, "Premium": 20, "VIP": 10}
        },

        "Star Wars": {
            "show_time": "7:00 PM",
            "language": "English",
            "seats": {"Standard": 35, "Premium": 25, "VIP": 15}
        }
    },

    "food_beverage": {
        "food": {
            "Popcorn Small": {"price": 3, "stock": 100},
            "Popcorn Medium": {"price": 5, "stock": 80},
            "Popcorn Large": {"price": 7, "stock": 50},
            "Nachos": {"price": 6, "stock": 40},
            "Burger": {"price": 10, "stock": 25}
        },

        "drinks": {
            "Water": {"price": 2, "stock": 200},
            "Coca Cola": {"price": 4, "stock": 100},
            "Pepsi": {"price": 4, "stock": 100},
            "Sprite": {"price": 4, "stock": 100},
            "Coffee": {"price": 6, "stock": 40}
        }
    }
}

for key,values in vox_cinemas.items():
    print(values)
