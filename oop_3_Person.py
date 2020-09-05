class MyComplex:  # od zad 3-10 Napisz klasę COMPLEX do obsługi liczb zespolonych
    # zad3 a, b
    def __init__(self, real_n: int, unreal_n=0):  # real_n - konstr. z jednym parametrem-- unreal_n wartosc domyslna 0
        self.rn = real_n
        self.un = unreal_n  # czesc urojona jest domyslna gdy = 0

    # zad 3 c
    def show(self):
        print(f"{self.rn} + {self.un} i")

    # zad 4
    def __str__(self):
        return f"{self.rn} + {self.un} i"

    # zad 5
    def is_equal_to(self, other_complex: 'MyComplex'):
        if self.rn == other_complex.rn and \
                self.un == other_complex.un:
            return True
        return False

    # zad 6
    def __eq__(self, other) -> bool:
        if isinstance(other, MyComplex):
            if self.rn == other.rn and \
                    self.un == other.un:
                return True
            return False

    @classmethod
    def add_two_complex(cls, one: 'MyComplex', two: 'MyComplex'):  # zad 7 method adds two complex numbers
        return cls(one.rn + two.rn, one.un + two.un)  # powinno wywolac sume licz rzeczywistuch i urojonych rn i un

    # zad 9 method adds three complex numbers
    def add_three_complex(self, one: 'MyComplex', two: 'MyComplex', three: 'MyComplex'):
        return self(one.rn + two.rn + three.rn, one.un + two.un + three.un)

    def add_to_this_complex(self, new_complex: 'MyComplex') -> MyComplex:
        self.rn += new_complex.rn
        self.un += new_complex.un
        return self

    def add_to_this_complex(self, rn: int, un: int):
        self.rn += rn
        self.un += un
        return self

    # zad 10 adds many complex numbers
    def add_many_value(cls, complex_value: list) -> 'MyComplex':
        rn = 0
        un = 0
        for value in complex_value:
            rn += value.rn
            un += value.un
        return
        cls(rn, un)


def main():
    my_complex = MyComplex(1, 2)
    my_complex.show()  #

    # druga liczba zespolona
    other_complex = MyComplex(1, 2)  # z 2,2 false
    print(my_complex.is_equal_to(other_complex))
    print(my_complex == other_complex)
    new_complex = MyComplex.add_two_complex(my_complex, other_complex)
    print(new_complex)

    print(my_complex.add_to_this_complex(other_complex))
    print(my_complex.add_to_this_complex_by_value(5, 5))

    print(MyComplex.add_three_complex(my_complex, other_complex, MyComplex(1, 1)))

    MyComplex.add_many_value([my_complex, other_complex, MyComplex(1, 1)], MyComplex(2, 2))


if __name__ == "__main__":
    main()
