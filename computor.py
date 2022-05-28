import sys
from polynomial import Polynomial

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            eq = Polynomial(sys.argv[1])
            eq.show_info()
            print()
            eq.resolve()
        except Exception as err:
            print('Error: {}'.format(err))
    else:
        print('Usage:\n\tpython3 computor.py [polynomial]')
