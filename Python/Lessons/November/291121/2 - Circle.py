import math
radius = 42
S = round(math.pi * radius**2, 4)
print(S)


point_1 = (23, 34)

t_1 = math.sqrt(23 ** 2 + 34 ** 2)
if t_1 < radius:
    print(True)
else:
    print(False)

point_2 = (30, 30)
t_2 = math.sqrt(30 ** 2 + 30 ** 2)
if t_2 < radius:
    print(True)
else:
    print(False)

# Evaluation: OK