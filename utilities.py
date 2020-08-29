
from Zad_oop_1_mz import MyCat, MyDog


def make_cat_list():
    cat1 = MyCat('Fuzzy')
    cat2 = MyCat('Stripes')
    cat3 = MyCat('Puszkin')
    cats = [cat1, cat2, cat3]

    for cat in cats:
        cat.make_sound()


def animal_creator() -> list:
    animals = []
    cat1 = MyCat("Fuzzy")
    cat2 = MyCat("Stripes")
    cat3 = MyCat("Puszkin")
    dog1 = MyDog("Buddy")
    dog2 = MyDog("Sparks")
    animals.append(cat1)
    animals.append(cat2)
    animals.append(cat3)
    animals.append(dog1)
    animals.append(dog2)
    return animals


def main():
    pass
    cat = MyCat('Fuzzy')
    # print(cat.name)
    # cat.name = "Stripes"
    cat.make_sound()
    print(f"{cat.name} meow!")
    cat.eat_mouse()
