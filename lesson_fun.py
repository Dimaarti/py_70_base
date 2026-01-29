# 1


# def fun_culc_min(a, b):
#     if a < b:
#         return a
#     elif b < a:
#         return b
#     elif a == b:
#         return a
#
# lst = [25, 14, 31, 16]
# result = fun_culc_min(lst[0], lst[1])
# result1 = fun_culc_min(lst[2], lst[3])
# result_finally = fun_culc_min(result, result1)
# print(result_finally)


# 2

# def fun_perf_number(n):
#     if n <= 0:
#         return False
#     sum_dig = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum_dig += i
#     return "Yes" if sum_dig == n else "No"
#
#
# result = fun_perf_number(int(input()))
# print(result)


# 3




# 4

# def fun_closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     else:
#         y = x % 5
#         return x + (5 - y)
# result = fun_closest_mod_5(int(input()))
# print(result)


# 5

# def chek_veriable(v):
#     for i in v:
#         if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i.isdigit() or i == '_'):
#             return False
#
#     return True
#
# while True:
#     i = input()
#     if chek_veriable(i):
#          print("Можно использовать")
#     else:
#         print("Нельзя использовать")

# 6

# two_dig_number = [number for number in range(11, 100, 2)]
# print(two_dig_number)

# 7

# three_dig_number = [number for number in range(105, 1000, 15)]
# print(three_dig_number)

# 8
#
# def count_elem(lst):
#     new_list = []
#     for item in lst:
#         if item not in new_list:
#             new_list.append(item)
#     return len(new_list)
#
#
# listen = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 'dasda']
# print(count_elem(listen))

#9

# number =  list(map(int, input().split()))
# if len(number) == 1:
#     print(number[0])
# else:
#     lst = []
# for i in range (len(number)):
#     sum_dig = number[i - 1] + number[(i + 1) % len(number)]
#     lst.append(sum_dig)
# print(lst)

#10
# lst = ['abcfsdfdfd', 'abcd', 'abcdedasdasdasdasd']
# def sorted(id):
#     for id in range (len(lst)):
#         lst.sort(key=len, reverse=True)
#         return lst
# new_lst = sorted(id)
# print(new_lst)

#11
