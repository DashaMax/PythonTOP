from json import load, dump
from random import randint, choice
from string import ascii_lowercase, digits


def get_person() -> dict:
    name = ''.join(choice(ascii_lowercase) for _ in range(randint(3, 7))).capitalize()
    telephone = '+79' + ''.join(choice(digits) for _ in range(9))
    person = {
        'name': name,
        'telephone': telephone
    }
    return person


def write_person_json(person: dict):
    try:
        with open('person.json') as file:
            data = load(file)

    except FileNotFoundError:
        data = {}

    ids = list(data.keys())

    if ids:
        data[int(ids[-1]) + 1] = person
    else:
        data[1] = person

    with open('person.json', 'w') as file:
        dump(data, file, indent=2)


for _ in range(10):
    write_person_json(get_person())