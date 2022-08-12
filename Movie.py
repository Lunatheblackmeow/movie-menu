import os
from socket import SO_RCVLOWAT
import textwrap as tr


raw_data = [
    ["The Slow and Confused 9", "Comedy",
        "The original team from The Slow and Confused are back! Join them in their slow walk around town.", 9.80],
    ["Somebody", "Action",
        "You thought you knew Somebody... until he turns out to be actually… nobody.", 8.8],
    ["Gorilla vs. King", "Action",
        "A giant ape fights against the leader of an ancient civilisation. Who will survive?", 10.90],
    ["The Blundering 3: Boss Made Me Do It", "Horror",
     "An office worker does all the wrong things and is fired. Was he really the one that made the mistakes?", 11.8],
    ["A Noisy Place Part III", "Horror",
        "Freshly out from the night club... James struggles to find a phone to call home. No phone? No ride.", 13.9],
    ["The Revengers: Personal War", "Comedy",
        "Revengers Resemble! A mad cap comedy featuring your favourite pals from the classic: Revengers of Earth.", 18.9]
]

movie_list = []  # required, list for all movie objects

class Movie:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = float(price)
        self.price_and_gst = price

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_description(self):
        return self.description

    def get_price(self):
        # to make it to have 2 decimal pts
        return float("{:.2f}".format(self.price))

    def get_price_and_gst(self):
        self.gst = self.price*1.07
        # to make it to have 2 decimal pts
        return float("{:.2f}".format(self.gst))

    def set_name(self, newname):
        self.name = newname

    def set_category(self, newcategory):
        self.category = newcategory

    def set_description(self, newdsc):
        self.description = newdsc

    def set_price(self, newprice):
        self.price = float(newprice)

def data_from_array():
        for row in raw_data:
            movie_list.append(Movie(row[0],row[1],row[2],row[3]))

main_list = ["1. Display all movie available",
             "2. Display full details from movie",
             "3. Name, Category and Description Search",
             "Q. Enter Q to quit"]
