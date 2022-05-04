#!/usr/bin/env python3

class Polynomial():

    def __init__(self, *args):
        self.list = list()  # seznam pro ulozeni cisel

        # byl zadan seznam
        if args and type(args[0]) == list:
            self.list = args[0]

        # byly zadana cisla
        if not self.list:
            for num in args:
                self.list.append(num)
        self.len = len(self.list)

        # maze nuly od nejvyssich radu
        for num in range(self.rad -1, 0, -1):
            if self.list[num] == 0:
                self.list.pop(num)
            else:
                break

        self.rad = len(self.list)


    def __str__(self):
        """ Výpis polynomu v řádném tvaru """
        poly = ""
        if len(self.list) == 1:
            poly = poly + str(self.list[0])
            return poly  # polynom se skládá pouze z absolutního členu
        for i in reversed(range(len(self.list))):
            if self.list[i] == 0:
                continue  # nulový koeficient je žádoucí při výpisu přeskočit
            if poly:
                if self.list[i] > 0:  # ošetření znaménka
                    poly += " + "
                else:
                    poly += " - "
            if i == 0:
                poly += "{0}".format(str(abs(int((self.list[0])))))
                # výpis aboslutního členu + výmaz znaménka
                return poly
            if i == 1:
                if abs(self.list[1]) == 1:
                    poly += "x"
                    # výpis lineárního členu v případě, že jeho koeficient je 1
                else:
                    poly += "{0}x".format(str(abs(int(self.list[1]))))
                    # výpis lineárního členu + výmaz znaménka
            else:
                if abs(self.list[i]) == 1:
                    poly += "x^{0}".format(i)
                    # výpis členu vyšší mocniny v případě, že koeficient je 1
                else:
                    poly += "{0}x^{1}".format(str(abs(int(self.list[i]))), i)
                    # výpis členu vyšší mocniny + výmaz znaménka
        return poly

    def __eq__(self):
        pass

    def __add__(self, other):
        pass


print(str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)))
print(str(Polynomial([1,-3,0,2])))
print(str(Polynomial(x0=1,x3=2,x1=-3)))
