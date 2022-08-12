from re import search
from sqlite3 import Row
import textwrap as tr
from Movie import Movie
import os

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

def readfromfile():
    with open('moviedetails.txt', 'r') as file:
        raw_lines = file.readlines()

        prep_lines = []
        ready_lines = []

        for i in raw_lines:
            prep_lines.append(i.replace('\n', ''))

        for pos, line in enumerate(prep_lines):
            if line not in ready_lines:
                ready_lines.append(prep_lines[pos].split(','))

    for row in ready_lines:
        if row not in movie_list:
            movie_list.append(Movie(row[0],row[1],row[2],row[3]))


def data_from_array():
    for row in raw_data:
            movie_list.append(Movie(row[0],row[1],row[2],row[3]))

def clear_screen():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "mac" or os.name == "posix":
            os.system("clear")

def print_movie_details(movie:Movie):
    # this is to get the index and the length so it can print out the item positions
    for index, item in enumerate(movie_list):
        if item == movie:
            get_index = index + 1
    get_len = len(movie_list)
    # text wrap will linebreak after 55 width and subsequent_indent adds the additional spacing format
    text_test = tr.fill(movie.get_description(), width=55, subsequent_indent="\t\t ")
    print("{:=^70s}".format(" Item {} of {} ".format(get_index, get_len)))
    print("{:15s}: {:55s}".format("Name", movie.get_name())) #15 spacing and character limit
    print("{:15s}: {:55s}".format("Category", movie.get_category()))
    print("{:15s}: {:55s}".format("Description", text_test))
    print("{:15s}: $ {:.2f}".format("Price + GST", movie.get_price_and_gst()))
    print("{0:=^70s}".format("")) #repeat the * symbol for 70 spaces

def print_search(movie:Movie, searchlist):
    # this is to get the index and the length so it can print out the item positions
    for index, item in enumerate(movie_list):
        if item == movie:
            get_index = index + 1
    get_len = len(movie_list)
    # text wrap will linebreak after 55 width and subsequent_indent adds the additional spacing format
    text_test = tr.fill(movie.get_description(), width=55, subsequent_indent="\t\t ")

    print("{:=^70s}".format(" Item {} of {} ".format(get_index, get_len)))
    print("{:15s}: {:55s}".format("Name", movie.get_name()))
    print("{:15s}: {:55s}".format("Category", movie.get_category()))
    print("{:15s}: {:55s}".format("Description", text_test))
    print("{:15s}: $ {:.2f}".format("Price + GST", movie.get_price_and_gst()))
    print("{0:=^70s}".format(""))

def main_menu():
    clear_screen()
    print("*************")
    print("# Main Menu #")
    print("*************")
    print("1. Display all movie avaliable")
    print("2. Display full details from movie")
    print("3. Name, Catergory and Description Search")
    print("4. Filter by Price or Catergory")
    print("Q. Enter Q to quit")
    x=input("Please input your selection : ")
    if x=="3":
        search_function()
    elif x=="Q" or x == "q":
        exit()
    elif x =="1":
        all_movies()
    elif x=="2":
        full_details()
    elif x=="4":
        sorting()

def full_details():
    clear_screen()
    print("{:*^31s}".format(""))
    print("# Display full details from movie #")
    print("{:*^31s}".format(""))
    list_count = 0
    for i in movie_list:
        list_count += 1
        print("{} -> {}".format(list_count, i.get_name()))

    #keep looping until we hit m
    alive = True
    while alive:
        thisChoice = input("Enter item number to see details, [M] to return to Main menu : ").lower()
        if thisChoice.isdigit(): #to check if they are digits
            choiceNum = int(thisChoice)-1 #force cast into int
            try: #this try block is capturing the IndexError
                if choiceNum <= len(movie_list):  # range check
                    print_movie_details(movie_list[choiceNum]) #if object position 0, its doing object[0]
                if choiceNum > len(movie_list):
                    print_movie_details(movie_list[len(movie_list)-1]) #forever default to the last elem in the movie_list
            except IndexError: #as long as index error appears, do the following
                    print_movie_details(movie_list[len(movie_list)-1])
                    pass
        elif thisChoice == 'm':
                alive = False
                main_menu()       

def search_function():
    print("******************************************")
    print("# Name, Catergory and Description Search #")
    print("******************************************")
    searchkey=input("Please enter a word to search : ")
    search_name_catergory_description(searchkey)

def all_movies():
    count=0
    userChoice=""
    clear_screen()
    print("***********************************")
    print("#  Display all movies avaliable   #")
    print("***********************************")
    
    # print the first item and wait for next input
    while userChoice != 'm':
        print_movie_details(movie_list[count])
        print("Enter 'N' for Next item, 'P' for Previous item, 'M' for Main menu:")
        userChoice = input("Please enter N/P/M : ").lower()
        if userChoice == 'n':    
            count += 1
            if count == len(movie_list):
                count= 0
        if userChoice == 'p':
            count -= 1
            if count < 0:
                count=0
        if userChoice == 'm':
            main_menu()
    

def no_results():
    print("====== No results found ======")
    x=input("Enter [M] to Main Menu, Any key for another search : ").lower()
    if x == "m":
        main_menu()
    else:
        search_name_catergory_description(x)

def search_name_catergory_description(search):
    search_item = search.lower()

    search_result = [i for i in movie_list if search_item in i.get_name().lower().split() or search_item in i.get_category().lower().split() or search_item in i.get_description().lower().split()]
    # using list comprehension method
    # to get a string within a subs string, string = movie_list, substring = search_results
    if search_result:
        for all in search_result:
            print_search(all, search_result)
        x=input("Enter [M] to Main Menu, Any key for another search : ").lower()
        if x == "m":
            main_menu()
        else:
            search_name_catergory_description(x)
    else:
        no_results()

def sorting():
    clear_screen()
    userChoice=""
    print("{:*^20s}".format(""))
    print("# Filter Movies #")
    print("{:*^20s}".format(""))
    print("1 -> View all Movie Categories Available")
    print("2 -> View by Price")

    catChoice = input("Please enter selection, [M] for Main Menu : ")
    while userChoice != "m":
        if catChoice == "1":
            #get a list of categories and present
            raw_cat =[]
            cat_result = []

            for i in movie_list:
                if i not in raw_cat:
                    raw_cat.append(i.get_category())

            #removing dupes
            for x in raw_cat:
                if x not in cat_result:
                    cat_result.append(x)

            cat_count = 0
            print("Types of Movies")
            for x in cat_result:
                cat_count +=1
                print("{} -> {}".format(cat_count, x))

            catChoice = input("Please type a category, [M] for Main Menu : ").lower()
            search_name_catergory_description(catChoice)

        if catChoice == "2":
            print("Most Expensive to Cheapest")
            movie_list.sort(key=lambda x: x.price_and_gst, reverse=True)

            for i in movie_list:    
                print_movie_details(i)
            catChoice = input("Please enter selection, [M] for Main Menu : ").lower()
        
        if catChoice == "m":
                main_menu()

readfromfile()
# data_from_array()
main_menu()




exit()
