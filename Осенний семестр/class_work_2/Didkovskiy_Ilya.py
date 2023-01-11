def is_prime(a):
    flag = True
    if a > 0:
        for i in range(2, a - 1):
            if a%i == 0:
                flag = False
    return flag

a = int(input())
print(is_prime(a))
