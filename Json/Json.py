info = {}

info['person1'] = {
    "name" : "anik",
    "age" : "18+",
    "id" : 73
}

info['person2'] = {
    "name" : "sabuj",
    "age" : "20",
    "id" : 51
}

info['person3'] = {
    "name" : "atik",
    "age" : "19",
    "id" : 64
}

import json
str = json.dumps(info, indent=4)

f = open('jsonfile.txt', 'w')
f.write(str)
f.close()

f = open('jsonfile.txt', 'r')
str = f.read()
print("JSON Format : ", str)


# Now this JSON convert into a dictionary
dictionary = json.loads(str)
print("Person1 info : ", dictionary['person1'])

lst = ["anik", "oni", "rafiq", "jotti", "saifi"]
str = json.dumps(lst)
print("List to json : ", lst)


tuple = ("anik", "ononna", "ritu", "puspo")
str = json.dumps(tuple)
print("tuple to json : ", tuple)
