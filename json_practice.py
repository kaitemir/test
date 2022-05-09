""" 
dump(), dumps()
"""
# import json

# info = {
#     'name':'Alice',
#     'age': 79,
#     'book': 'Chamber of Secrets'
# }

# with open('info.json', 'w') as my_file: 
#     json.dump(info, my_file)
    
# json_object = json.dumps(info)
# print(json_object)

import json

""" 
load(), loads()

"""

# with open('info.json') as my_file:
#     python_object = json.load(my_file)
#     print(python_object)
    
# python_object['name'] = 'John'
# print(python_object)

# with open('info.json', 'w') as my_file:
#     json.dump(python_object, my_file)

json_str = '{"name": "Alice", "age": 79, "book": "Chamber of Secrets"}'
python_object = json.loads(json_str)
print(json_str)
print(python_object)
 
 JSON.
JSON, или JavaScript Object Notation - это формат для обмена данными.

Несмотря на то, что в названии присутствует слово JavaScript, JSON является абсолютно независимым от языка программирования.

Поэтому, с помощью данного формата можно обмениваться информацией с любым языком программирования, например передавать данные языка С на Java, либо с Perl на Python, с C# на JavaScript и.т.д.

JSON формат основан на двух структурах данных:

Коллекция пар ключ/значение, в Python это словарь
Упорядоченный список значений, в Python это список
Аналоги этих двух структур данных существуют почти во всех языках программирования, поэтому JSON может легко переводить данные сохраненные в этих структурах из одного языка в другой.

Допустим, у нас есть JSON файл - file.json, в которой хранится JSON строка, и нам нужно перевести данную строку в формат понятный Python.

Для этого существует два метода:

load(), десериализует файл, т.е принимает целый файл и переводит его из формата JSON в формат Python

loads(), десериализует строку, т.е принимает строку из файла и переводит ее из формата JSON в формат Python(для использования loads(), придется сперва прочитать строку методом read)
Для нашего примера подходит второй метод:

import json  
with open('file.json', 'r') as f: 
    result = json.loads(f.read()) 
Чтобы считать строку, в начале открыли файл file.json в режиме чтения r, файл обозначили переменной f.

Затем, считали содержимое файла f методом read() и передали в метод json.loads().

Результат сохранили в переменную result.

Задание 1
Вам даны два файла task1.json и task1.py.

В task1.json хранятся определенные данные, вам нужно прочитать данный файл, затем сохранить содержимое в переменной python_obj.

После, откройте файл task1.py и запишите туда содержимое переменной python_obj.

# import json

# with open('task1.json') as my_file:
#     python_obj = json.load(my_file)
# with open('task1.py', 'w') as my_file:
#     my_file.write(str(python_obj))

JSON.
Задание 2
В task2.json хранятся данные в формате JSON.

Напишите программу Python которая будет считывать данные с файла и сохранять их в переменной json_obj.

Затем, преобразуйте это обьект в объект Python и запишите результат в переменную python_obj.

import json

with open('task2.json') as file:
    date = json.load(file)
    print(date)
    json_obj = json.dumps(date)
    print(json_obj)
    python_obj = json.loads(json_obj)
    print(python_obj)
    
    JSON.
Процесс перевода Python объектов в формат JSON, называется сериализацией.

Для этого используют два метода:

dump(), записывает Python объекты в файл JSON, первым аргументом принимает название Python объекта, а вторым переменную обозначающую наш файл:
import json
      
obj = {'1': 'makers', '2': 'bootcamp'}      
with open("example.json", "w") as my_file:
   json.dump(obj, my_file)
Создали и открыли файл "example.json" для записи режимом w, обозначили наш файл переменной my_file.

Используя, метод dump(), мы сохранили словарь Python obj в нашем файле в перемнной my_file.

В результате, в нашей рабочей папке появится файл example.json, содержимое которого будет выглядеть данным образом:

{"1": "makers", "2": "bootcamp"} 

dumps(), сериализует Python объект в JSON строку, первым аргументом принимает название Python объекта, а вторым именованным аргументом количество отступов - indent:
import json 
     
obj = {'1': 'makers', '2': 'bootcamp'}        
json_obj = json.dumps(obj, indent=4)  
print(json_obj) 
используя метод dumps(), передали словарь Python и количество отступов 4, затем распечатали результат, в терминале получим:

{ 
 "1": "makers", 
 "2": "bootcamp" 
}
Заметьте, что в Python можно использовать одинарные кавычки, при переводе словаря в JSON формат, кавычки заменились на двойные.

Задание 3
Вам дан объект Python сохраненный в переменной python_obj и имеющий значение None.

Преобразуйте данный объект в формат JSON и сохраните в переменной json_obj.

Ввод должен быть:

python_obj = None  
#ваш остальной код 
print(json_obj)  
Вывод:

null 