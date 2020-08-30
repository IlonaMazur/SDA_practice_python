class MyComplex():
    def __init__(self, real_n: int, unreal_n = 0):
        self.rn = real_n
        self.un = unreal_n

    def show(self):
        print(f"{self.rn}+ {self.un} i")

    def __str__(self):
        return f"{self.rn}+ {self.un} i"
    # do tego miejsca jest real i unreal tylko
    def is_eqyal_to(self, other_complex: 'MyComplex'):
        if self.rn == other_complex.rn and\
                self.un == other_complex.un:
            return True
        return False

    def __eq__(self, other)->bool:
        if isinstance(other, MyComplex):
            if self.rn ==other.rn and\
                    self.un == other.un:
                return True
            return False

    @classmethod
    def add_two_complex(cls, one: 'MyComplex', two: 'MyComplex'):
        return cls(one.rn + two.rn. one.un + two.un) # powinno wywolac sume licz rzeczywistuch i urojonych rn i un

    def add_three_complex(self, one: 'MyComplex', two: 'MyComplex', three: 'MyComplex'):
        return cls(one.rn + two.rn + three.rn, one.un + two.un +three.un)

    def add_to_this_complex(self, new_complex: 'MyComplex'):
        self.rn += new_complex.rn
        self.un += new_complex.un
        return self

    def add_to_this_complex(self, rn:int, un: int):
        self.rn += rn
        self.un += un
        return self

    def add_my_value(cls, complex_value: list)-> 'MyComplex':
        rn = 0
        un = 0
        for vale in complex_values
            rn += value.rn
            un += value.un
        retirn cls(rn, un)
def main():
    my_complex = MyComplex(1, 2)
    my_complex.show()        #odpala metode powyzej, liczna zespolona1

# druga liczba zespolona
    other_complex = MyComplex(1, 2) # z 2,2 false
    print(my_complex.is_eqyal_to(other_complex))
    priny(my_complex == other_complex)
    new_complex = MyComplex.add_two_complex(my_complex, other_complex)
    print(new_complex)

    print(my_complex.add_to_this_complex(other_complex))
    print(my_complex.add_to_this_complex_by_value(5,5))

    print(MyComplex.add_three_complex(my_complex, other_complex, MyComplex(1, 1)))

    MyComplex.add_many_value([my_complex, other_complex, MyComplex(1, 1)], MyComplex(2, 2))
if __name__ == "__main__":
    main()