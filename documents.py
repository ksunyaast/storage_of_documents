documents = [
   {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
   {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
   {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
   {"type": "id", "number": "5-86"},
   {"type": "id", "number": "5-0"}
   ]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
  }


print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;')
print('l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";')
print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
print('a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')


def search_people(documents):
  """Вывод имени человека по номеру документа"""
  doc_number = input('Введите номер документа для поиска человека: ')
  for document in documents:
    if document['number'] == doc_number:
      print('Документ с номером: {}, принадлежит человеку с именем - {}'.format(doc_number, document['name']))
      break 
  else:
    print('Документ не найден!')
    

def doc_list(documents):
  """Вывод списка всех документов"""
  print('Список всех документов:')
  for i, document in enumerate(documents):
    print('{}. {} "{}" "{}"'.format(i+1, document['type'], document['number'], document['name']))


def search_shelf(directories):
  """Вывод номера полки, на которой хранится документ"""
  doc_number = input('Введите номер документа для поиска номера полки: ')
  for shelf in directories.keys():
    if doc_number in directories[shelf]:
      print('Документ с номером "{}" находится на полке №{}'.format(doc_number, shelf))
      break 
  else:
    print('Документ не найден!')


def add_new(documents, directories):
  """Добавление нового документа"""
  print('Добавление нового документа:')
  new_doc_number = input('Введите номер для нового документа: ')
  new_doc_type = input('Введите тип для нового документа: ')
  new_doc_name = input('Введите имя владельца для нового документа: ')
  for document in documents:
    if new_doc_number == document['number'] and new_doc_type == document['type'] and new_doc_name == document['name']:
      print('Такой документ уже существует!')
      break
  else:
    documents.append({"type": new_doc_type, "number": new_doc_number, "name": new_doc_name})
    new_doc_shelf = input('Введите полку для хранения для нового документа: ')
    if new_doc_shelf not in directories.keys():
      directories[new_doc_shelf] = [new_doc_number]
      print('Полок с таким номером нет, поэтому создана новая!')
    else:
      directories[new_doc_shelf].append(new_doc_number)
    print('Добавлен новый документ: номер документа "{}", тип документа "{}", имя владельца "{}", помещен на полку №{}'.format(new_doc_number, new_doc_type, new_doc_name, new_doc_shelf))
    print('Обновленный каталог:')
    print(documents)
    print('Обновленные полки:')
    print(directories)


#Задача№2
print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;')
print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;')
print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;')


def delete_doc(documents, directories):
  """Удаление документа из каталога и полок по номеру"""
  doc_number = input('Введите номер документа, чтобы удалить его из каталога и перечня полок: ')
  for shelf in directories.keys():
    if doc_number in directories[shelf]:
      directories[shelf].remove(doc_number)
      print('Документ удален с полок!')
      print('Обновленные полки:')
      print(directories)
      break
  else:
      print('Документ не найден на полках!')
  print('')
  for i, document in enumerate(documents):
    if document['number'] == doc_number:
      documents.pop(i)
      print('Документ удален из каталога!')
      print('Обновленный каталог:')
      print(documents)
      break 
  else:
    print('Документ не найден в каталоге!')


def move_doc(directories):
  """Перемещение документа с полки на полку"""
  doc_number = input('Введите номер документа, чтобы переместить его: ')
  for shelf in directories.keys():
    if doc_number in directories[shelf]:
      directories[shelf].remove(doc_number)
      shelf_number = input('Введите номер полки, на которую хотите переместить документ: ')
      if shelf_number not in directories.keys():
        directories[shelf_number] = [doc_number]
        print('Полок с таким номером нет, поэтому создана новая!')
      else:
        directories[shelf_number].append(doc_number)
      print('Обновленные полки:')
      print(directories)
      break
  else:
      print('Документ не найден на полках!')


def new_shelf(directories):
  """Добавление новой полки"""
  new_shelf = input('Введите номер для новой полки: ')
  if new_shelf not in directories.keys():
    directories[new_shelf] = []
    print('Создана новая полка - №', new_shelf)
    print('Обновленные полки:')
    print(directories)
  else:
    print('Полка с таким номером уже есть!')
    print(directories)

# Задача №4 с лекции «Исключения»
print('w – owners – команда, выводит имена всех владельцев документов')
print('')


def owners_list(documents):
  """Вывод списка всех документов"""
  print('Список всех владельцев документов:')
  for i, document in enumerate(documents):
    try:
      print('{}. {}'.format(i+1, document['name']))
    except KeyError:
      print('У документа с номером {} не указан владелец'.format(document['number']))

def input_command():
  command = input('Введите команду: ')
  if command == 'p':
    search_people(documents)
  elif command == 'l':
    doc_list(documents)
  elif command == 's':
    search_shelf(directories)
  elif command == 'a':
    add_new(documents, directories)
  elif command == 'd':
    delete_doc(documents, directories)
  elif command == 'm':
    move_doc(directories)
  elif command == 'as':
    new_shelf(directories)
  elif command == 'w':
    owners_list(documents)
  else:
    print('Некорректная команда!')
  print('')
  input_command()

input_command()