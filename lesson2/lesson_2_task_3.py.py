import math

def square(side):
    area = side ** 2
    return math.ceil(area)

side_length = 5.3
print(f"Площадь квадрата со стороной {side_length} = {square(side_length)}")
