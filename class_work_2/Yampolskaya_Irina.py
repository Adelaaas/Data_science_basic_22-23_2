def season(month):
    global s
    if month  == 1 or month == 2 or month == 12:
        print("Winter")
    if month == 3 or month == 4 or month == 5:
        print("Spring")
    if month == 6 or month ==7 or month ==8:
        print ("Summer")
    if month == 9 or month ==10 or month ==11:
        print("Auterm")

s = int(input())
season(s)