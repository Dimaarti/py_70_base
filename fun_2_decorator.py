#1
def decorator(number):
    def log_result(*args):
        res = number(*args)
        print(res)
        return res
    return log_result
@decorator
def dig_pro(s):
    return s ** 2

dig_pro(2)

#2


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def dig_pro(n):
     print("Hello world")

dig_pro(print)

#3

def bench(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка {type(e).__name__}")
    return wrapper

@bench
def func(n, n1):
    return n / n1


print(func(10, 0))


#4

lst = ['dada','dasda', 'dasdasdasd']
lst_new = [len (lst) for lst in lst ]
print(lst_new)

#5

lst = ['apple', 'Banana', 'cherry', 'DATE']
new_lst = [lst for lst in lst if lst.lower() in lst]
print(new_lst)

#6

lst = [('Ivan', 18), ('Petr', 17), ('Dima', 28)]
filter_lst = filter(lambda item: item[1] > 18, lst)
print(list(filter_lst))

#7

from functools import reduce
lst = [[1,2],[3,4],[5,6]]
new_lst = reduce(lambda x, y: x + y, lst)
print(new_lst)

#8

lst = ['cat', 'car', 'mouse', 'dog', 'snake', 'cow']
dict = {}
for lst in lst:
    key = lst[0]
    if key not in dict:
        dict[key] = []
    dict[key].append(lst)
print(dict)

#9

lst = [('Шампунь', 10.1, 14), ('Мыло', 5.69, 3), ('Порошок', 12, 10)]
lst_sums = [price * quantity for _, price, quantity in lst]
print(lst_sums)

#11.





