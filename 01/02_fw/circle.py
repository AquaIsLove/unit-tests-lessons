from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError(("Radius must be non-negative real number only"))
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return pi*radius**2

def circle_lenght(radius):
    if type(radius) not in [int,float]:
        raise TypeError("Radius must be non-negative real number only")
    if radius < 0:
        raise ValueError("Radius must be non-negative real number only")
    return 2*pi*radius