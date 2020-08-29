class MyCat:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> str:
        return f"{self.name} meow"

    def eat_mouse(self) -> str:
        self.eat_mouse += 1
        if self.eat_mouse == 1:

            print(f"{self.name} ate 1 mouse")
        else:
            return f"{self.name} ate {self.eat_mouse} mice!"


class MyDog:
    def __init__(self, named: str):
        self.named = named

    def make_sound(self) -> str:
        return f"{self.named} bark!"

class animals:
    def __init__(self, names: str):
        self.names = names

    def make_sound(self) -> str:
        if animal = 