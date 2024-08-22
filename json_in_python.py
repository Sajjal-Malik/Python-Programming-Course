book = {}

book["Tom"] = {
    "name": "tom",
    "address": "nyc",
    "phone":3123023
}

book["bob"] = {
    "name": "bob",
    "address": "brk",
    "phone":6546456
}


import json

json_string = json.dumps(book)     # json.dumps   convert the    python dictionary to json format string    ( now we can read this json string  from any other language that support json format)

print(json_string)

print(type(json_string))

# with open("json_string.txt", "w") as file:
#     file.write(json_string)


dict_back = json.loads(json_string)     # json.loads    convert the   json format string back to python dictionary

print(dict_back)

print(type(dict_back))