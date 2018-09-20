def choices():
    print("0 for Parks and Rec")
    print("1 for The Office")
    print("2 for Breaking Bad")
    print("3 for Friends")
    choose = input(": ")
    shows = [('parks_and_rec', 7), ('the_office', 9),
         ('breaking_bad', 5), ('Friends', 10)]
    print(shows[int(choose)])
    return shows[int(choose)]

def main():
    choices()

if __name__ == '__main__':
    main()


