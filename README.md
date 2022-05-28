# COMPUTORV1 (@42Paris)

A simple equation solving program.

## Usage
```
$ git clone https://github.com/adbenoit-9/42_computorv1.git
$ cd 42_computorv1
$ python3 computor.py [equation]
```

## Example
```
$ python3 computor.py "4 * X^2 + 4 * X + 1 = 0"
Reduced form: 1 * X^0 + 4 * X^1 + 4 * X^2 = 0
Polynomial degree: 2

Δ = 4^2 - 4 * 4 * 1 = 0

Discriminant equal to zero, the solution is:
x = -4 / (2 * 4)
x = -4 / 8
x = -1 / 2
x = -0.5
```
```
$ python3 computor.py "13 * X^2 + 2 * X^1 + 4 = 2" 
Reduced form: 2 * X^0 + 2 * X^1 + 13 * X^2 = 0
Polynomial degree: 2

Δ = 2^2 - 4 * 13 * 2 = -100

Discriminant is strictly negative, the two solutions are:
x1 = (-2 - i * sqrt(100)) / (2 * 13)
x1 = (-2 - i * sqrt(100)) / 26
x1 = (-2 - i * 10) / 26

x2 = (-2 + i * sqrt(100)) / (2 * 13)
x2 = (-2 + i * sqrt(100)) / 26
x2 = (-2 + i * 10) / 26
```
