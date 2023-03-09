# Домашнее задание к лекции 5.«Функции — использование встроенных и создание собственных»

# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
# Внимание: p, s, l, a, d, m , as - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name(docs, number):
    for docs in documents:
        if docs.get('number') == number:
            return docs.get('name')
    else: 
        return 'Документ не найден!'
    
def get_directory(value, number):
    for value in directories:
        dir = directories[value]
        for item in dir:
            if item == number:
                return value
    else:
        return 'Полка с таким документом не найдена!'

def get_list(docs_list):
    for docs in docs_list:
        print(docs['type'], docs['number'], docs['name'])

def add_document(docs, shelfs, shelf, type, number, name):
    doc = {'type' : type,
           'number' : number,
           'name' : name}
    docs.append(doc)
    shelfs[shelf].append(doc['number'])
    return 'Документ добавлен!'

def move_doc(doc_number, shelf_user):
    if shelf_user not in directories:
        return 'Полка с таким номером не найдена!'
    for shelf, value in directories.items():
        if doc_number in value:
            if shelf == shelf_user:
                return 'Документ находится на этой полке!'
            value.remove(doc_number)
            directories[shelf_user].append(doc_number)
            return 'Документ перемещен!'
    return 'Документ не найден!'
    
def delete_doc(docs, shelfs, number):
    for doc in docs:
        if doc.get('number') == number:
            documents.remove(doc)
    for shelf in shelfs:
        dir = shelfs[shelf]
        for item in dir:
            if item == number:
                dir.remove(number)
                return 'Документ удален!'
    else: 
        return 'Документ не найден!'

def add_dir(new_shelf):
    if new_shelf in directories:
        return 'Такая полка уже существует!'
    directories[f'{new_shelf}'] = []
    return 'Полка успешно добавлена!'

def my_function():
    while True:
        print('Возможные пользовательские команды - p, s, l, a, d, m, as')
        print('Введите "help" чтобы получить справку по командам')
            
        command = input('Введите пользовательскую команду - ')
        if command == 'help':
            print("""
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
    l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    a – add – команда, которая добавит новый документ в каталог и в pперечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться
    d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень    
            """)
        elif command == 'p':
            number = input('Введите номер документа - ')
            print(get_name(documents, number))
        elif command == 's':
            number = input('Введите номер документа - ')
            print(get_directory(directories, number))
        elif command == 'l':
            print(get_list(documents))
        elif command == 'a':
            shelf = input('Введите требуемый номер полки - ')
            if shelf in directories.keys():
                type = input('Введите тип документа - ')
                number = input('Введите номер документа - ')
                name = input('Введите имя и фамилию владельца - ')
                print(add_document(documents, directories, shelf, type, number, name))
            else:
                print('Номер полки введен неверно!')
        elif command == 'd':
            number = input('Введите номер документа - ')
            print(delete_doc(documents, directories, number))
        elif command == 'm':
            number = input('Введите номер документа - ')
            shelf = input('Введите номер полки - ')
            print(move_doc(number, shelf))
        elif command == 'as':
            shelf = input('Введите номер полки - ')
            print(add_dir(shelf))
        else: 
            print('Команда введена неверно!')

if __name__ == '__main__':
    my_function()
    


    



