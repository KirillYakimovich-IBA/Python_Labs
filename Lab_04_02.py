import time
import numpy


class Leibniz:
    z = i = 1
    t = 1.00

    def __init__(self):
        print("Ряд Лейбница:")

    def __iter__(self):
        while round(self.t, 2) != round(numpy.pi / 4, 2):
            if self.i > 0:
                self.t -= (1.00 / (self.z + 2))
            else:
                self.t += (1.00 / (self.z + 2))
            self.z += 2
            self.i *= -1
            yield round(self.t, 2)

main_series = Leibniz()
for line in main_series:
    print(line)
    time.sleep(0.25)
