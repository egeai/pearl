from pandas import DataFrame


class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance


class Product:
    def __init__(self, *components):
        self.components = DataFrame([
            [x.manufacturer, x.resistance]
            for x in components
        ], columns=['manufacturer', 'resistance'], index=[x.number for x in components])

    def __getitem__(self, number):
        x = self.components.loc[number]
        return Resistor(number, x.manufacturer, x.resistance)


p = Product(Resistor('10-423-1234', 'honhai', 1),
            Resistor('10-423-1249', 'samsung', 5),
            Resistor('10-423-1230', 'honhai', 10),)

print(f'{p.components.resistance.mean() = }')
print(f'{p["10-423-1234"] = }')

"""
from collections import namedtuple
Resistor = namedtuple('Resistor', 'number manufacturer resistance')

Capacitor = namedtuple('Capacitor', 'number manufacturer capacitance')

x = Resistor(...,...,...)
if isinstance(x, Resistor):
    ...
elif isinstance(x, Capacitor):
    ...
"""

# top-level function or top-level syntax
# x + y   -> __add__
# init x  -> __init__
# repr(x) -> __repr__
# x()     -> __call__


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        """

        :return:
        """
        pass

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 4)
