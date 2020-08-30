import pickle


def pickle_write():
    strings = ['cat', 'dog', 'eagle']
    try:
        with open('./pickling.pickle', 'wb') as fd:
            pickle.dump(strings, fd)  # dwa argumenty - co zapisac i jak zapisac
            print(pickle.dumps(strings))

    except (IOError, pickle.PickleError, BaseException) as e:
        print(f"exception while pickling; more info {e.args}")


def pickle_read():
    strings = []
    try:
        with open("./pickling.pickle", "rb") as fd:
            pickle.load(fd)
        print(strings)

    except (IOError, pickle.PickleError, BaseException) as e:
        print(f"exception while pickling; more info {e.args}")


def main():
    pickle_write()
    pickle_read()


if __name__ == "__main__":
    main()
