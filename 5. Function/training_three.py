#Тренажер 3
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    # get_name — функция. Принимает номер документа и выводит имя человека, которому он принадлежит. 
    # Если такого документа не существует вывести “Документ не найден”.
    for document in documents:
        if document.get('number') == doc_number:
            return document.get('name')
    else:
        return 'Документ не найден'
        

def get_directory(doc_number):
    # get_directory — функция. Принимает номер документа и выводит номер полки, на которой он находится. 
    # Если такой документ не найден на полках вывести “Полки с таким документом не найдено”.
    for value in directories:
        dir = directories[value]
        for item in dir:
            if item == doc_number:
                return value
    else:
        return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number):
    # функция, которая добавит новый документ в каталог и перечень полок.
    add_document = {
        'type': document_type,
        'number': number,
        'name': name,
        }
    documents.append(add_document)  

    for value in directories:
        if int(value) == shelf_number:
            dir = directories[value]
            dir.append(number)
            return value

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))