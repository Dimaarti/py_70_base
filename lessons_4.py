# 1.
tup = (15, 13, 22, 15, 1, 3)
dif = max(tup) - min(tup)             #O(N)
print(dif)


# 2.
tup = (5, 2, -2, 7, -8, -9, 1)
change = 0
for i in range(len(tup)):             #O(N)
    if tup[i] * tup[i - 1] < 0:
        change = change + 1
print(f"Знак менялся {change} раза ")

# 3.

# 4.


# 5.
tup = (1, 2, 4, 1, 2, 6)
set1 = set()
repeated = set()
for i in tup:                         #O(N)
    if i in set1:
        repeated.add(i)               #O(1)
    else:
        set1.add(i)
print(repeated)


# 6.
lst_1 = [4,1,6,9,]
lst_2 = [8,1,2,4,9,5,7,6]
for i in lst_1:                     #O(N)
    if i not in set(lst_2):
        print(i)
else:
    print("Нет такого элемента, все элементы входят")


# 7.
lst_1 = [18, 42, 8, 122]
lst_2 = []
for i in lst_1:                 #O(N)
    lst_2.append(i)             #O(1)
    if i % 2 == 0:
        reversed_i = int(str(i)[::-1])
        lst_2.append(reversed_i)
print(lst_2)


# 8.
lst = [5,2,4,5,1,2]
dct = {}
for i in set(lst):
    dct[i] = lst.count(i)       #O(N)
print(dct)


#  9.
lst = [5, 2, 0, -2, -7, 1, 8, 0, -1]
pos = 0
for i in range (len(lst)):                          #O(N)
    if lst[i] > 0:
        lst[i], lst[pos] = lst[pos], lst[i]         #O(1)
        pos += 1
for i in range(len(lst)):                           #O(N)
    if lst[i] < 0:
        lst[i], lst[pos] = lst[pos], lst[i]         #O(1)
        pos += 1
        print(pos)
print(lst)


# 10.
lst = [5, 2, 7, 3, 8, 2, 4, 1, 6, 5]
set = set()
lst2 = []
for i in lst:                 #O(N)
    lst2.append(i)            #O(1)
    lst2.append(i)
    set.add(i)
print(lst2)


# 11.
numb = input()
str1 = numb.split()
set = set(str1)
print(set)
for i in str1:                #O(N)
    if i in set:
        print('YES')
    else:
        print('NO')
    set.add(i)                 #O(1)


# 13.
school = {
    '9a': 32,
    '9б': 42,
    '9в': 34,
    '9м': 12,
    '9ф': 32
}
# а)
school['9a'] = 30
# б)
school['9т'] = 21
# в)
school.pop('9в')
print(school)


# 14
concepts = {
    'DNS': '-компьютерная система для получения, хранения и обработки информации о доменных именах',
    'Интрасеть': '-это замкнутая внутренняя сеть какой-либо организации, работающая по Интернет-протоколу TCP/IP',
    'Фича': '-недокументированная дополнительная возможность, фишка',
    'Мейнфрейм': '-большой компьютер, имеющий высокую вычислительную мощность.'
    }
print(concepts.setdefault(input(), 'не найдено'))

#