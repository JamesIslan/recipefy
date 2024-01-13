# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


dummy = Faker("pt_BR")
# print(signature(fake.random_number))


def make_recipe():
    dummy_info:dict = {
        "title": dummy.sentence(nb_words=6),
        "description": dummy.sentence(nb_words=12),
        "preparation_time": dummy.random_number(digits=2, fix_len=True),
        "preparation_time_unit": "Minutos",
        "servings": dummy.random_number(digits=2, fix_len=True),
        "servings_unit": "Porção",
        "preparation_steps": dummy.text(3000),
        "created_at": dummy.date_time(),
        "author": {
            "first_name": dummy.first_name(),
            "last_name": dummy.last_name(),
        },
        "category": {"name": dummy.word()},
        "cover": {
            "url": "https://loremflickr.com/%s/%s/food,cook" % rand_ratio(),
        },
    }
    return dummy_info


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())
