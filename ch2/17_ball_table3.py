# Exercise 2.17: Store data in a nested list

"""
SAMPLE RUN:
------------
y(0.00) = 0.00
y(0.20) = 1.83
y(0.41) = 3.26
y(0.61) = 4.28
y(0.82) = 4.89
y(1.02) = 5.10
y(1.22) = 4.89
y(1.43) = 4.28
y(1.63) = 3.26
y(1.83) = 1.83
y(2.04) = 0.00
------------
y(0.00) = 0.00
y(0.20) = 1.83
y(0.41) = 3.26
y(0.61) = 4.28
y(0.82) = 4.89
y(1.02) = 5.10
y(1.22) = 4.89
y(1.43) = 4.28
y(1.63) = 3.26
y(1.83) = 1.83
y(2.04) = 0.00
------------
"""

v_0 = 10  # Initial velocity
g = 9.81  # Gravity

a = 0; b = 2*v_0/g; n = 10; h = (b-a)/n

intervals = [a+i*h for i in range(0, n+1)]  # t

values = [v_0*t - 0.5*g*t**2 for t in intervals]  # y

print("------------")

# a
ty1 = [[], []]
for t in intervals:
    ty1[0].append(t)

for y in values:
    ty1[1].append(y)

for t, y in zip(ty1[0], ty1[1]):
    print("y({:.2f}) = {:.2f}".format(t, y))

print("------------")

# b
ty2 = [[t, y] for t, y in zip(intervals, values)]
for t, y in ty2:
    print("y({:.2f}) = {:.2f}".format(t, y))

print("------------")
