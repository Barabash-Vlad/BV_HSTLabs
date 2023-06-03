import math


class Data:
    def __init__(self,kfacp,fmax,kmaxacp,p0,kpacp,koacp,y1max,ymax,pmax,typesensor):
        self.__Kfacp = kfacp
        self.__Fmax = fmax
        self.__Kmaxacp = kmaxacp
        self.__P0 = p0
        self.__Kpacp = kpacp
        self.__Koacp = koacp
        self.__y1max = y1max
        self.__ymax = ymax
        self.__pmax = pmax
        self.__P = 0.0
        self.__Knp = 0.0
        self.__O = 0.0
        self.__pg = 0.0
        self.__Kp = 0.0
        self.__F = 0.0
        self.__typesensor = typesensor
        self.Expenses()


    def set_Kfacp(self,x):
        self.__Kfacp = x

    def set_Fmax(self,x):
        self.__Fmax = x

    def set_Kmaxacp(self,x):
        self.__Kmaxacp = x

    def set_P0(self,x):
        self.__P0 = x

    def set_P0(self,x):
        self.__P0 = x

    def set_Kpacp(self,x):
        self.__Kpacp = x

    def set_Koacp(self,x):
        self.__Koacp = x

    def set_y1max(self,x):
        self.__y1max = x

    def set_ymax(self,x):
        self.__ymax = x

    def set_pmax(self,x):
        self.__pmax = x

    def set_type(self,type):
        self.__typesensor = type

    def Calc_P(self):
        self.__P = self.__Kpacp / self.__Kmaxacp * self.__pmax

    def Calc_Knp(self):
        self.__Knp = self.__y1max / self.__ymax


    def Temperature(self):
        self.Calc_Knp()
        type = self.__typesensor
        y = self.__Koacp * self.__y1max / (self.__Kmaxacp * self.__Knp)
        if type == 2:
            self.__O = 3.01 + (13.75 * y) - (0.03 * math.pow(y, 2))
        if type == 3:
            self.__O = 4.87 + (23.6 * y) - (0.0011 * math.pow(y, 2))
        if type == 4:
            self.__O = (4.99 * y) + (0.0054 * math.pow(y, 2)) - 41.25
        if type == 5:
            self.__O = (2.34 * y) + (0.0011 * math.pow(y, 2)) - 241.3
        #print(type)

    def Density(self):
        self.Calc_P()
        self.Temperature()
        self.__pg = 1.2 - (0.013 * self.__O) + (0.72 * self.__P) + (0.36 * math.pow(10, -4) * math.pow(self.__O, 2)) + \
               (0.24 * math.pow(10, -2) * math.pow(self.__P, 2)) - (0.14 * math.pow(10, -2) * self.__O * self.__P)

    def Calc_Kp(self):
        self.Density()
        self.__Kp = math.sqrt(self.__pg / self.__P0)

    def Expenses(self):
        self.Calc_Kp()
        self.__F = math.sqrt(self.__Kfacp / self.__Kmaxacp) * self.__Fmax * self.__Kp

    def Get_Main_Values(self):
        return [self.__Kfacp,self.__Fmax,self.__Kmaxacp,self.__P0,self.__Kpacp,self.__Koacp,self.__y1max,self.__ymax,self.__pmax]


    def Get_Values(self):
        return [self.__P,self.__Knp,self.__O,self.__pg,self.__Kp,self.__F]

    def Show_Result(self):
        self.Expenses()
        arr = self.Get_Values()
        #print(self.__Knp)
        return F"Тиск: {arr[0]:10.2f} кгс/см^2\n" \
               F"Kнп: {arr[1]:10.2f}\n" \
               F"Θ(температура в об'єкті): {arr[2]:10.2f} C\n" \
               F"Густину пари в умовах вимірювання pg: {arr[3]:10.2f} кг/м^3\n" \
               F"Поправочний коефіцієнт Kp: {arr[4]:10.2f}\n" \
               F"Фактичне значення витрати F: {arr[5]:10.2f}"

if __name__ == '__main__':
    test = Data(512,630,1024,3.02,768,512,10,16.39,10,3)
    print(test.Get_Values())

