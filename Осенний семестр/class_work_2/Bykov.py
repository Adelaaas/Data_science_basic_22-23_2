s = ''
def season(month):
    global s
    if month < 3 or month == 12:
        s = '����'
    elif 3 <= month < 6:
        s = '�����'
    elif 6 <= month < 9:
        s = '����'
    else:
        s = '�����'

month = int(input())
season(month)
print(s)