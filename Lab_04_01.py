import time


class Tribonacci:
    t = [0, 0, 1]

    def __init__(self, size):
        self.size = size

    def __iter__(self):
        a = i = 0
        b = 1
        c = 2

        while i < self.size:
            self.t.append(self.t[a] + self.t[b] + self.t[c])
            a += 1
            b += 1
            c += 1
            i += 1
            yield self.t[i]


main_tribonacci = Tribonacci(35)
for line in main_tribonacci:
    print(line)
    time.sleep(0.25)
