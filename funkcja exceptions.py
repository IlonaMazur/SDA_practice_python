def exception_f4():
    agd = {'items': 'cooker', 'vacuum'}
    print (agd.keys())
    if not agd.keys():
        raise KeyError("Missing Key")


def main():

    try:
         exception_f4()
    except KeyError as e:
        print( f"key error, more infor {e.args}")