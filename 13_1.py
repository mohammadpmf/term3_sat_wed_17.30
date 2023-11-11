# term 1 => scratch
# term 2 => python basic
# term 3 => tkinter  json   thread
# term 4 => class database  python advance programming
# term 5 => html css js                                           *
# term 6 => web backend design django framework by python
# term 7 => dart programming language framework flutter
# term 8 => web backend design laravel framework by php
# term 9 => web backend design laravel framework by php
from json import dump, load
# contacts = {
#     'ali': '09115468752',
#     'reza': '09112547898',
#     'mohammad': '09365587412',
#     'علی': '09875487747'
# }
# f = open('contacts.json', 'w')
# dump(contacts, f, indent=4, ensure_ascii=False)
f = open('contacts.json', 'r')
contacts = load(f)
f.close()
print(contacts, type(contacts))
