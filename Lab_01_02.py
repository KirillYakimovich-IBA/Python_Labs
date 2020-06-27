import numpy

c = 2.1
r = 4 * 10 ** -4
m = 7
j = (4.2, 0.3, 1.7)
for i in range(len(j)):
    h = (10 * r - j[i]) / (c ** 2 + numpy.e ** (-m))
    y = (h * m - j[i] ** 2) + (0.1 * c) ** 2
    print(y)
print("\n")


j = 0
while j <= 1.7:
    h = (10 * r - j) / (c ** 2 + numpy.e ** (-m))
    y = (h * m - j ** 2) + (0.1 * c) ** 2
    j += 0.1
    print(y)
print("\n")


j = (9,1.8,15,-3)
for z in range (len(j)):
    m = 1
    while m <= 2:
        h = (10*r-j[z])/(c**2+numpy.e**(-m))
        y = (h*m-j[z]**2)+(0.1*c)**2
        m+=0.5
        print(y)
