people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

'''def f(person):
    return person["name"]

def g(person):
    return person["house"]

people.sort(key=f)
print(people)

people.sort(key=g)
print(people)'''

people.sort(key=lambda person: person["name"]) #Function f
print(people)

people.sort(key=lambda person: person["house"]) #Function g
print(people)
