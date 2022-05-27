import math
from re import X

def ft_sqrt(n):
    sqrt = n / 2.
    while sqrt * sqrt < n:
        sqrt += 1.
    if sqrt * sqrt == n:
        return True, sqrt
    sqrt -= 1.
    tmp = 0.
    while tmp != sqrt:
        tmp = sqrt
        sqrt = (n / tmp + tmp) / 2
    return False, sqrt


def ft_abs(n):
    if n > 0:
        return n
    return n * -1


class Polynomial:
    def __init__(self, polynomial) -> None:
        if isinstance(polynomial, str) is False:
            raise TypeError("Only str is accepted")
        operators = "+-/*"
        a = 1
        n = 0
        side = 1
        state = 0
        try:
            split_p = polynomial.split()
            for x in split_p:
                if x.startswith('X^') and int(x[2:]) > n:
                    n = int(x[2:])
            self.values = [0.] * (n + 1)
            for x in split_p:
                if x.startswith('X^'):
                    if state != 2:
                        raise ValueError('Invalid Polynomial')
                    self.values[int(x[2:])] += a
                    a = 1
                    state = 0
                elif x.startswith('X'):
                    if state != 2:
                        raise ValueError('Invalid Polynomial')
                    self.values[1] += a
                    a = 1
                    state = 0
                elif x in operators:
                    if x == '-':
                        a = -1 * side
                    elif x == '+':
                        a = 1 * side
                    else:
                        if state != 1:
                            raise ValueError('Invalid Polynomial')
                        state += 1
                elif x == '=':
                    if side == -1 or state > 1:
                        raise ValueError('Invalid Polynomial')
                    side = -1
                    a = -1
                else:
                    if state != 0:
                        self.values[0] += tmp
                        a = 1
                        state = 0
                    state += 1
                    a *= float(x)
                    tmp = a
            self.degree = len(self.values) - 1
            while self.values[self.degree] == 0. and self.degree > 0:
                self.degree -= 1
        except Exception:
            raise ValueError('Invalid Polynomial')

    def reduce_form(self):
        return self.__str__()

    def resolve(self):
        if self.degree > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return False
        elif self.degree == 0:
            if self.values[0] != 0.:
                print("No solution.")
            else:
                print('Each real number is a solution')
            return True
        elif self.degree == 1:
            x = self.values[0] * -1. / self.values[1]
            print("The solution is:\n{}".format(x))
            return True
        delta = self.values[1] * self.values[1] - 4 * self.values[2] * self.values[0]
        print("delta = {}^2 - 4 * {} * {} = {}".format(self.values[1],
                                                  self.values[2],
                                                  self.values[0],
                                                  delta))
        if delta > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            print("x1 = ({} - sqrt({})) / (2 * {})".format(self.values[1] * -1,
                                                           delta,
                                                           self.values[2]))
            x1 = (self.values[1] * -1 - ft_sqrt(delta)[1]) / (2 * self.values[2])
            print("   = {}".format(x1))
            print("x2 = ({} + sqrt({})) / (2 * {})".format(self.values[1] * -1,
                                                           delta,
                                                           self.values[2]))
            x2 = (self.values[1] * -1 + ft_sqrt(delta)[1]) / (2 * self.values[2])
            print("   = {}".format(x2))
        elif delta == 0:
            x = (self.values[1] * -1) / (2 * self.values[2])
            print("Discriminant equal to zero, the solution is:\n{}".format(x))
        else:
            print('Discriminant is strictly negative, the two solutions are:')
            is_int, sqrt_delta = ft_sqrt(delta * -1)
            print("x1 = ({} - i * sqrt({})) / (2 * {})".format(self.values[1] * -1,
                                                           delta * -1,
                                                           self.values[2]))
            if is_int is True:
                print("   = ({} - i * {:.0f}) / {}".format(self.values[1] * -1,
                    sqrt_delta, self.values[2] * 2))
            else:
                print("   = ({} - i * sqrt({})) / {}".format(self.values[1] * -1,
                    -1 * delta, self.values[2] * 2))
            print("x2 = ({} + i * sqrt({})) / (2 * {})".format(self.values[1] * -1,
                                                           delta * -1,
                                                           self.values[2]))
            if is_int is True:
                print("   = ({} + i * {:.0f}) / {}".format(self.values[1] * -1,
                    sqrt_delta, self.values[2] * 2))
            else:
                print("   = ({} + i * sqrt({})) / {}".format(self.values[1] * -1,
                    -1 * delta, self.values[2] * 2))
        return True

    def show_info(self):
        print('Reduced form: {}'.format(self.reduce_form()))
        print('Polynomial degree: {}'.format(self.degree))

    def __str__(self):
        polynomial = ""
        for i, val in enumerate(self.values):
            op = '-' if val < 0 else '+'
            if val != 0.:
                if i != 0 or op == '-':
                    polynomial += "{} ".format(op)
                polynomial += "{} * X^{} ".format(ft_abs(val), i)
        if len(polynomial) == 0:
            polynomial += "0 * X^0 "
        polynomial += "= 0"
        return polynomial
