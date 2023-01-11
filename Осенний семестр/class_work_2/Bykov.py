s = ''
def season(month):
    global s
    if month < 3 or month == 12:
        s = 'гхлю'
    elif 3 <= month < 6:
        s = 'беямю'
    elif 6 <= month < 9:
        s = 'керн'
    else:
        s = 'няемэ'

month = int(input())
season(month)
print(s)