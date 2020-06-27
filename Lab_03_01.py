from math import sqrt


class Triangle:
    type = Ax = Ay = Bx = By = Cx = Cy = AB = BC = CA = P = 0

    def __init__(self, a_x=0, a_y=0, b_x=0, b_y=0, c_x=0, c_y=0, triangle_type='unknow'):
        self.type = triangle_type
        self.Ax = a_x
        self.Ay = a_y
        self.Bx = b_x
        self.By = b_y
        self.Cx = c_x
        self.Cy = c_y
        print("Вызван конструктор, создан объект")

    def __del__(self):
        print("Вызван деструктор, объект разрушен")

    def __setattr__(self, attr, value):
        if attr == 'type' or 'Ax' or 'Ay' or 'Bx' or 'By' or 'Cx' or 'Cy' or 'AB' or 'BC' or 'CA':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def set_A(self, x, y):
        self.Ax = x
        self.Ay = y
        if self.Ax < 0:
            print("Вы ввели отрицательное число! Значение \"x\" домножено на \"-1\"")
            self.Ax *= -1
        if self.Ay < 0:
            print("Вы ввели отрицательное число! Значение \"y\" домножено на \"-1\"")
            self.Ay *= -1

    def set_B(self, x, y):
        self.Bx = x
        self.By = y
        if self.Bx < 0:
            print("Вы ввели отрицательное число! Значение \"x\" домножено на \"-1\"")
            self.Bx *= -1
        if self.By < 0:
            print("Вы ввели отрицательное число! Значение \"y\" домножено на \"-1\"")
            self.By *= -1

    def set_C(self, x, y):
        self.Cx = x
        self.Cy = y
        if self.Cx < 0:
            print("Вы ввели отрицательное число! Значение \"x\" домножено на \"-1\"")
            self.Cx *= -1
        if self.Cy < 0:
            print("Вы ввели отрицательное число! Значение \"y\" домножено на \"-1\"")
            self.Cy *= -1

    def get_A(self):
        return "Координаты точки А: х=" + str(self.Ax) + " ,y=" + str(self.Ay)

    def get_B(self):
        return "Координаты точки B: х=" + str(self.Bx) + " ,y=" + str(self.By)

    def get_C(self):
        return "Координаты точки C: х=" + str(self.Cx) + " ,y=" + str(self.Cy)

    def length(self):
        self.AB = round(sqrt(abs((self.Bx - self.Ax)**2 + (self.By - self.Ay)**2)),2)
        self.BC = round(sqrt(abs((self.Cx - self.Bx)**2 + (self.Cy - self.By)**2)),2)
        self.CA = round(sqrt(abs((self.Ax - self.Cx)**2 + (self.Ay - self.Cy)**2)),2)
        print("Сторона AB = " + str(self.AB) + ", сторона BC = " + str(self.BC) + ", сторона CA = " + str(self.CA) + ".")

    def perimeter(self):
        self.P = self.AB + self.BC + self.CA
        return round(self.P,2)


myList = [Triangle(),
          Triangle(0, 1, 3, 2, 0, 4),
          Triangle(1, 1, 1, 2, 9, 1, 'rectangular'),
          Triangle(1, 1, 2, 5, 3, 1, 'isosceles'),
          Triangle(3, 3, 3, 10, 10, 3, 'rectangular')]

rectangular = isosceles = unknow = 0

for z in myList:
    z.length()

for i in myList:
    if i.type == 'rectangular':
        rectangular += 1
    elif i.type == 'isosceles':
        isosceles += 1
    else:
        unknow += 1

print("Количество прямоугольных треугольников = " + str(rectangular) +
      "; количество равнобедренных треугольников = " + str(isosceles) +
      "; количество неопределенных треугольников = " + str(unknow))

rectangularPerimeters = []
isoscelesPerimeters = []
unknowPerimeters = []

for i in myList:
    if i.type == 'rectangular':
        rectangularPerimeters.append(i.perimeter())
    elif i.type == 'isosceles':
        isoscelesPerimeters.append(i.perimeter())
    else:
        unknowPerimeters.append(i.perimeter())


print("Площадь наибольшего прямоугольного треугольника равна " + str(max(rectangularPerimeters)) + ", наименьшего - " +
      str(min(rectangularPerimeters)) + "; площадь наибольшего равнобедренного треугольника равна " +
      str(max(isoscelesPerimeters)) + ", наименьшего - " + str(min(isoscelesPerimeters)) +
      "; площадь наибольшего неопределенного треугольника равна " + str(max(unknowPerimeters)) + ", наименьшего - " +
      str(min(unknowPerimeters)))

for i in myList:
    del i
