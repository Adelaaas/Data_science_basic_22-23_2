x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = 0

for i in range(0, 9, 1):
    if i % 2 == 1:
        a = x[i]
        x[i] = x[-i]
        x[-i] = a
print (x)