# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
# структуры; записи должны быть упорядочены по возрастанию номера группы; вывод на
# дисплей фамилий и номеров групп для всех студентов, включенных в массив, если средний
# балл студента больше 4.0; если таких студентов нет, вывести соответствующее сообщение.

students = []
# def add():
#     name = input('Введите Фамилию и инициалы >')
#     group = input('Введите номер группы > ')
#     academic_performance = [input('Введите пять оценок (через ",")').split(',')]

#     student = {
#         'name': name,
#         'group': group,
#         'academic_performance':academic_performance
#     }
#     students.append(student)

# def journal():
#     for x in students:
#         s = 0
#         for y in x['academic_performance']:
#             s += y
#         if s/5 > 4:
#             print(x)
print('Введите help для вывода списка команд')
while 1:
    command = input('>>> ').lower()

    if command == 'exit':
        break
    
    elif command == 'add':
        name = input('Введите Фамилию и инициалы > ')
        group = input('Введите номер группы > ')
        academic_performance = input('Введите пять оценок (через ",") > ').split(',')

        student = {
            'name': name,
            'group': group,
            'academic_performance':academic_performance
        }
        students.append(student)
        students.sort(key=lambda item: item.get('group', ''))
    
    elif command == 'list':
        f = 0
        for x in students:
            s = 0
            for y in x['academic_performance']:
                s += int(y)
            if s/5 > 4:
                f += 1
                print(x['name'], x['group'])
        if f == 0:
            print('Нет студентов со средним балом выше 4.0')
    
    elif command == 'help':
        print('add - добавить данные')
        print('list - список студентов со средним баллом выше 4.0')
        print('exit - завершить работу программы')