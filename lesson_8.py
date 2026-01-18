# 1
try:
    x = (1, 2, 5, 7)
    x = x / 2
    print(x)
except TypeError:
    print("TypeError")

# 2
try:
    lst = [1, 2, 3, 4]
    print(lst[5])
except IndexError:
    print("IndexError")


# 3
a = int(input())
b = int(input())
c = int(input())
if a == 0 or b == 0 or c == 0:
    raise ArithmeticError
else:
    p = (a + b + c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    print(S)


# 4
lst = [13, 14, 15]
try:
    lst.remove(11)
except ValueError:
    print("ValueError")



# 5
dct = {"11":"aa", "22":"bb", "33":"cc"}
try:
    k = dct["12"]
except KeyError:
    print("KeyError")


#6
str = "10 5 abc 3"
s = 0
number_lst = str.split()
for i in number_lst:
    try:
        number = int(i)
        s += number
    except ValueError:
        continue
print(s)

#7
number = input()
str = "aa bb ss rra aa b"
dct = {}
try:
    for i in str:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    dct.pop(' ')
    print(dct)
    if number.isdigit():
        raise TypeError
except TypeError:
    print("TypeError")













