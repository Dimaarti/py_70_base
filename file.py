# 1
with open('text.txt', 'w') as text_file:
    text_file.write(input("Введите 6 строк через запятую:"))
# 2
with open("text.txt", "a") as text_file:
    text_file.write(input("Введите 3 строки через запятую:"))

# 3
with open('text.txt', 'r') as file:
    data = file.read()
    print(len(data.replace('\n', '')))

# 4
with open('text.txt', 'r') as file:
    file_lst = file.readlines()
    file_lst_fix = [file.strip() for file in file_lst]
    print(file_lst_fix)

# 5

with open('text.txt', 'r') as file:
    for line in file:
        if line.strip().endswith('!'):
            print(line.strip())

# 6
import json
with open('flight.json','r', encoding= "UTF-8") as file:
    data = json.load(file)
    for value in data:
        if value['destination'] == 'Москва':
            print(value['flight_number'], value['departure_time'])


# 7
with open('student_grades.json', 'r', encoding="UTF-8") as file:
    student = json.load(file)
    for grades in student:
        avg_grade = sum(grades['grades']) / len(grades['grades'])
        if avg_grade > 7:
            print(grades['full_name'],avg_grade)