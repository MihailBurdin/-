# 1
def distance(x1, y1, x2, y2):
    dist = (((x1 - x2)  2) + ((y1 - y2)  2)) ** 0.5
    return dist


x1, y1, x2, y2 = [float(input()) for i in range(4)]

print(distance(x1, y1, x2, y2))



# 2
def power(y, z):
    res = 1

    if z > 0:
        for i in range(int(z)):
            res *= y
        return res
    elif z < 0:
        for i in range(abs(int(z))):
            res *= y
        return 1 / res
    else:
        return res


y , z = [float(input()) for i in range(2)]

print(power(y, z))




# 3
def fib(z):
    if z == 1 or z == 2:
        return 1
    else:
        return fib(z - 1) + fib(z - 2)


z = int(input())
print(fib(z))





# 4
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Yes')
else:
    print('No')


# 5
def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k


print(square(16))


# 6
def season(month):
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"


# 7
def bank():
    stavka = 10
    x = int(input("\x""-> "))
    years = int(input("\x""-> "))

    for i in range(years):
        x = int(x + stavka * x / 100)
        print( x)


bank()


# 8
def is_prime(x):
    f = True
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            f = False
        return (f)


a = int(input("ввести число: "))
print(is_prime)

#9
def check_date(d,m,y):
        if d < 0 or m < 0 or n < 0:
            return False
        pip = [31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or ((y%4==0) and (y%100 != 0)):
            pip[1] = 29
        if m > =1 and m < = 12:
        if d > 0 and d < = pip[m-1]:
            return True
        return False
