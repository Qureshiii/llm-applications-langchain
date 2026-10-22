from typing import TypedDict

class person(TypedDict):

    name : str
    age : int

new_person: person = {'name':'nitish', 'age': 41 }


print(new_person)