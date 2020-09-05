def csv_writer():
    lala = [('IDK', 'what', 'am', 'I', 'doing'),
            ('bits', 'and', 'bobs')]
    with open('lala.txt', 'w') as la:
        la.write(f" IDK if it works{lala}")


#def csv_read():
#    for row in open('./lala.txt', "r"):
#       yield row


class OpenFile():
    lala = [('IDK', 'what', 'am', 'I', 'doing'),
            ('bits', 'and', 'bobs')]
    with open('lala.txt', 'w') as la:
        la.write(f" IDK if it works{lala}")

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open('./lala.txt', 'w')
        return self.file

    print(f" opening file {'./lala.txt'}")


def __exit__(self, exc_type, exc_val, exc_tb):
    if self.file:
        self.file.close()
    print(f" closing file {'./lala.txt'}")


def main():
    csv_writer()
#    csv_read()


if __name__ == "__main__":
    main()
