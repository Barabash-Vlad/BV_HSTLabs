from sympy import symbols, Eq, solve
from multipledispatch import dispatch

multi = 0.397658173734610
data = []

class Consumption_NitricAcid:
    def __init__(self,x1,x2,x3,x4,l,o1,o2,o3,o4,dx123,dx4):
        self.__x1 = x1
        self.__x2 = x2
        self.__x3 = x3
        self.__x4 = x4
        self.__l = l
        self.__o1 = o1
        self.__o2 = o2
        self.__o3 = o3
        self.__o4 = o4
        self.__dx123 = dx123
        self.__dx4 = dx4

    def set_x1(self,x):
        self.__x1 = x

    def set_x2(self,x):
        self.__x2 = x

    def set_x3(self,x):
        self.__x3 = x

    def set_x4(self,x):
        self.__x4 = x

    def set_l(self,l):
        self.__l = l

    def set_o1(self,o):
        self.__o1 = o

    def set_o2(self,o):
        self.__o2 = o

    def set_o3(self,o):
        self.__o3 = o

    def set_dx123(self,o):
        self.__dx123 = o

    def set_dx4(self,o):
        self.__dx4 = o

    def set_o4(self,o):
        self.__o4 = o

    def fault_f(self):
        if abs(self.__x1 + self.__x2 + self.__x3 - self.__x4) <= self.__l:
            return True
        else:
            return False

    def fault_result(self,x):
        if abs(x) <= self.__l:
            return True
        else:
            return False

    def fault_x123(self,q):
        if abs(q) <= self.__dx123:
            return True
        else:
            return False

    def fault_x4(self,q):
        if abs(q) <= self.__dx4:
            return True
        else:
            return False

    def pof(self, x):
        return 1 / pow(x, 2)

    def weight_factors(self):
        return 1 / (self.pof(self.__o1) + self.pof(self.__o2) + self.pof(self.__o3) + self.pof(self.__o4))

    def get_all_fields(self):
        return [self.__x1,self.__x2,self.__x3,self.__x4,self.__l,self.__dx123,self.__dx4,self.__o1,self.__o2,self.__o3,self.__o4]

    def Lagrange_multiplier(self):
        q1, q2, q3, q4, i = symbols('q1 q2 q3 q4 l')

        eq1 = Eq(2 * self.weight_factors() * self.pof(self.__o1) * q1 + i, 0)
        eq2 = Eq(2 * self.weight_factors() * self.pof(self.__o2) * q2 + i, 0)
        eq3 = Eq(2 * self.weight_factors() * self.pof(self.__o3) * q3 + i, 0)
        eq4 = Eq(2 * self.weight_factors() * self.pof(self.__o4) * q4 + i, 0)
        eq5 = Eq(q1 + q2 + q3 - q4, self.__l)
        solution = solve((eq1, eq2, eq3, eq4, eq5), (q1, q2, q3, q4, i))
        return [multi * solution[q1], multi * solution[q2], multi * solution[q3], -1*multi * solution[q4], multi * solution[i]]

    def Revised(self):
        arr = self.Lagrange_multiplier()
        return [self.__x1-arr[0],self.__x2-arr[1],self.__x3-arr[2],self.__x4-arr[3]]


    def sumX(self):
        return self.__x1 + self.__x2 + self.__x3 - self.__x4



    def Show_Data(self):
        if self.fault_f():
            return F"Перевіряємо виконання умови |lj| ≤ lj*. Маємо: |{self.__x1 + self.__x2 + self.__x3 - self.__x4:1.1f}| ≤ {self.__l}, тобто - {self.fault_f()}\n\n" \
                   F"Умова виконується, коригування не потрібне"
        else:
            return F"Перевіряємо виконання умови |lj| ≤ lj*. Маємо: |{self.__x1 + self.__x2 + self.__x3 - self.__x4:1.1f}| ≤ {self.__l}, тобто - {self.fault_f()}\n\n" \
                   F"Складаємо систему рівнянь:\n" \
                   F"                 \t\t\t          2*{self.weight_factors() * self.pof(self.__o1):0.3f}*Δq1 + λ = 0\n" \
                   F"                 \t\t\t          2*{self.weight_factors() * self.pof(self.__o2):0.3f}*Δq2 + λ = 0\n" \
                   F"                 \t\t\t          2*{self.weight_factors() * self.pof(self.__o3):0.3f}*Δq3 + λ = 0\n" \
                   F"                 \t\t\t          2*{self.weight_factors() * self.pof(self.__o4):0.3f}*Δq4 + λ = 0\n" \
                   F"                 \t\t\t          Δq1 + Δq2 + Δq3 - Δq4 = {self.__l}\n\n" \
                   F"Отримуємо рішення: λ={self.Lagrange_multiplier()[4]:0.3f} Δq1={self.Lagrange_multiplier()[0]:0.3f} " \
                   F"Δq2={self.Lagrange_multiplier()[1]:0.3f} Δq3={self.Lagrange_multiplier()[2]:0.3f} Δq4={self.Lagrange_multiplier()[3]:0.3f}\n" \
                   F"Перевіряємо виконання умови  |Δxi| ≤ xi*. Маємо:\n" \
                   F"                 \t\t\t          x1:|{self.Lagrange_multiplier()[0]:0.3f}| ≤ {self.__dx123}, тобто - {self.fault_x123(self.Lagrange_multiplier()[0])}\n" \
                   F"                 \t\t\t          x2:|{self.Lagrange_multiplier()[1]:0.3f}| ≤ {self.__dx123}, тобто - {self.fault_x123(self.Lagrange_multiplier()[1])}\n" \
                   F"                 \t\t\t          x3:|{self.Lagrange_multiplier()[2]:0.3f}| ≤ {self.__dx123}, тобто - {self.fault_x123(self.Lagrange_multiplier()[2])}\n" \
                   F"                 \t\t\t          x4:|{self.Lagrange_multiplier()[3]:0.3f}| ≤ {self.__dx4}, тобто - {self.fault_x4(self.Lagrange_multiplier()[3])}\n\n" \
                   F"Проводимо кориговання значень вимірюваних величин: q1={self.Revised()[0]:3.3f} q2={self.Revised()[1]:3.3f} " \
                   F"q3={self.Revised()[2]:3.3f} q4={self.Revised()[3]:3.3f}\n" \
                   F"Перевіряємо виконання умови |lj| ≤ lj*. Маємо: |{self.Revised()[0] + self.Revised()[1] + self.Revised()[2] - self.Revised()[3]:1.1f}| " \
                   F"≤ {self.__l}, тобто - {self.fault_result(self.Revised()[0] + self.Revised()[1] + self.Revised()[2] - self.Revised()[3])}"