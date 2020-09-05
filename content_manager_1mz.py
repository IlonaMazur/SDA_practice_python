def csv_writer():
    lala = [('IDK', 'what', 'am', 'I', 'doing'),
            ('bits', 'and', 'bobs')]
    with open('lala.txt', 'w') as la:
        la.write(f" IDK if it works{lala}")


#def csv_read():
#    for row in open('./lala.txt', "r"):
#       yield row


class OpenFile:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f" opening file {'./lala.txt'}")
        self.file = open('./lala.txt', 'w')
        return self.file


    def __exit__(self, *args):
        print(f" closing file {'./lala.txt'}")
        self.file.close()



def main():
    csv_writer()
#    csv_read()


if __name__ == "__main__":
    main()
