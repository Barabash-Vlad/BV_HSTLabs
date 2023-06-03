import numpy as np
import matplotlib.pyplot as plt

class Data:
    def __init__(self,TempXmax,TempXhyzm,PressXmax,PressXhyzm,length,speed,TempCorArr,PressCorArr,RandProcArr):
        self.__TempXmax = TempXmax
        self.__TempXhyzm = TempXhyzm
        self.__PressXmax = PressXmax
        self.__PressXhyzm = PressXhyzm
        self.__length = length
        self.__speed = speed
        self.__TempCorArr = TempCorArr
        self.__PressCorArr = PressCorArr
        self.__RandProcArr = RandProcArr

    def TimeCrossN(self):
        return self.__length/self.__speed

    def NumCroosProc(self):
        return len(self.__RandProcArr)/self.TimeCrossN()

    def ValSampStep(self):
        return 0.15/self.NumCroosProc()

    def calculateMathematicalExpectation(self,Arr):
        return np.mean(Arr)

    def CalcDispersion(self,Arr):
        return np.var(Arr)

    def CalcKx(self,Arr, Max, Hyzm):
        Dx = self.CalcDispersion(Arr)
        return (2 * Dx - (Max ** 2 - Hyzm ** 2)) / 2

    def CalcRiseKx(self):
        ArrXmax = []
        ArrXhyzm = []
        for step in np.arange(0, 1, 0.1):
            ArrXmax.append(self.CalcKx(self.__TempCorArr, step, self.__TempXmax).round(2))
            ArrXhyzm.append(self.CalcKx(self.__TempCorArr, step, self.__TempXhyzm).round(2))
        return [ArrXmax,ArrXhyzm]

    def CalcDeclineKx(self):
        ArrXmax = []
        ArrXhyzm = []
        for step in np.arange(1, 0, -0.1):
            ArrXmax.append(self.CalcKx(self.__TempCorArr, step, self.__TempXmax).round(2))
            ArrXhyzm.append(self.CalcKx(self.__TempCorArr, step, self.__TempXhyzm).round(2))
        return [ArrXmax,ArrXhyzm]

    def CalrMathExpectation(self,array):
        return np.mean(array)

    def CrossRandProc(self):
        resultArr = []
        for i in range(1, len(self.__RandProcArr)):
            resultArr.append(self.CalcKx(self.__RandProcArr[:i], self.__TempXmax, self.__TempXhyzm))
        return resultArr

    def CalcJ(self):
        return (np.mean(self.CrossRandProc()) / len(self.CrossRandProc())) * self.ValSampStep()

    def CalcSurPer(self):
        return self.ValSampStep() * self.CalcJ()

    def CalSumSurPerAndArrT(self):
        t = self.ValSampStep()
        for i in range(len(self.__RandProcArr)):
            t += self.ValSampStep()
        return t

    def CalcOrdin(self):
        num_points = len(self.__RandProcArr)
        num_time_points = int(num_points * self.ValSampStep())
        time_point_indices = np.linspace(0, num_points - 1, num_time_points, dtype=int)
        return [self.__RandProcArr[i] for i in time_point_indices]

    def CalcCorrWithOrd(self):
        delta_t = self.ValSampStep()
        arr = self.__RandProcArr
        slice_1 = arr[::int(1 / delta_t)]
        slice_2 = arr[1::int(1 / delta_t)]
        return np.correlate(slice_1, slice_2, mode='full')



    def PlotCorrWithOrd(self,CorArr):
        correlation_function_positive = np.where(CorArr > 0, CorArr, 0)
        time = np.arange(len(CorArr))
        plt.plot(time, correlation_function_positive)
        plt.xlabel('Час')
        plt.ylabel('Кореляційна функція')
        plt.title('Графік кореляційної функції випадкового процесу')
        plt.grid(True)
        plt.show()


    ## перевірка бібліотеки numpy
    # def CalcRandMath(self):
    #     ArrX = self.__RandProcArr
    #     N = len(ArrX)
    #     sum = 0.0
    #     for I in range (N):
    #         sum +=ArrX[I]
    #     return 1/N * sum

    def CalcRandCorrKx(self):
        ArrX = self.__RandProcArr
        J = round(self.CalcJ())
        N = len(ArrX)
        sumKx = 0.0
        arrI = []
        for I in range(N - J):
            sumKx += ArrX[I] * ArrX[I + J]
            arrI.append(I)
        return (1 / (N - J)) * sumKx




    def GetDataTempAndPress(self):
        return  f"Визначення періоду опитування датчиків з реалізації випадкових процесів за температурою і тиском\n" \
                f"За тиском:\n" \
                f"Kx = {self.CalcKx(self.__PressCorArr,self.__PressXmax,self.__PressXhyzm)}\n" \
                f"Значення періодів опитування тиском T= {self.__PressCorArr}\n" \
                f"За температурою:\n" \
                f"Kx = {self.CalcKx(self.__TempCorArr,self.__TempXmax,self.__TempXhyzm)}\n" \
                f"Значення періодів опитування температури T= {self.__TempCorArr}\n" \
                f"T при постійному значенні σ-max  при зростаючих σ-хизм: {self.CalcRiseKx()[0]}\n" \
                f"                                 при спадаючих σ-хизм:  {self.CalcDeclineKx()[0]}\n" \
                f"T при постійному значенні σ-хизм при зростаючих σ-max:  {self.CalcRiseKx()[1]}\n" \
                f"                                 при спадаючих σ-max:   {self.CalcDeclineKx()[1]}\n"

    def GetDataRandomProc(self):
        return f"Визначення періоду опитування датчиків за кривими реалізації випадкового процесу\n" \
               f"Крок дискретизації випадкового процесу Δτ = {round(self.ValSampStep(),2)}\n" \
               f"Визначаємо кількість перетинів N випадковим процесом {len(self.__RandProcArr)}\n" \
               f"Визначаємо довжину реалізації {self.__speed}\n" \
               f"Визначаємо час, протягом якого відбулося N перетинів, τn = {round(self.TimeCrossN(),2)}\n" \
               f"Визначаємо середнє число нулів за одиницю часу nср = {round(self.NumCroosProc(),2)}\n" \
               f"Лінія математичного очікування Mx = {round(self.CalrMathExpectation(self.__RandProcArr), 2)}\n" \
               f"Визначаємо дисперсію випадкового процесу Dx = {round(self.CalcDispersion(self.__RandProcArr),2)}\n" \
               f"Визначаємо ординати для перерізу: {self.CalcOrdin()[0:int(len(self.CalcOrdin())/2)-2]}\n" \
               f"                                  {self.CalcOrdin()[int(len(self.CalcOrdin())/2)-2:len(self.CalcOrdin())-1]}\n" \
               f"За значеннями цих ординат знаходимо кореляційну функцію в дискретні моменти часу:\n" \
               f"{self.CalcCorrWithOrd()}\n" \
               f"Визначаємо кореляційну функцію випадкового процесу Kx = {round(self.CalcRandCorrKx(),2)}\n" \
               f"За відомими значеннями σ-max, σ-хизм та Dx визначаємо з величину для температури Kx = {round(self.CalcKx(self.__RandProcArr,self.__TempXmax,self.__TempXhyzm),2)}\n" \
               f"                                                                 для тиску       Kx = {round(self.CalcKx(self.__RandProcArr,self.__PressXmax,self.__PressXhyzm),2)}\n" \
               f"Шуканий період опитування датчиків τ0 = {round(self.CalSumSurPerAndArrT(),2)}"

if __name__ == '__main__':
    MaxT = 4.0
    HyzmT = 1.0
    MaxP = 3.6
    Hyzmp = 0.8
    length = 242
    speed = 0.6
    TempCorArr = [46, 42, 30, 18, 7, 1, 0]
    PressCorArr = [23, 22, 15, 7, 2, 0]

    RandProcArr = [145, 117, 122, 118, 120, 110, 112, 111, 115, 96, 116, 100, 119, 120, 117, 119,
                   116, 130, 120, 125, 126, 113, 101, 111, 105, 100, 105, 95, 103, 93, 101, 75, 94,
                   91, 93, 77, 77, 105, 80, 102, 96, 102, 97, 101, 98, 100, 96, 110, 113, 108, 113,
                   95, 98, 97, 111, 96, 108, 98, 99, 95, 100, 100, 107, 80, 83, 74, 102, 93, 78,
                   97, 100, 97, 103, 104, 99, 104, 126, 73, 101, 93, 99, 96, 95, 75, 87, 81, 82,
                   76, 80, 77, 82, 83, 78, 81, 78, 82, 83, 74, 80, 83, 80, 84, 79, 82, 80, 73, 76, 77, 74, 76,
                   75, 82, 80, 78, 79, 77, 78, 99, 78, 76, 92, 104, 97, 102, 87, 100, 88, 101, 91, 92, 101,
                   92, 93, 88, 104, 88, 90, 91, 87, 88, 75, 88, 102, 97, 79, 104, 81, 83, 75, 82, 78, 80, 81, 73,
                   84, 70, 82, 71, 79, 82, 77, 78, 73, 61, 63]


    test = Data(MaxT,HyzmT,MaxP,Hyzmp,length,speed,TempCorArr,PressCorArr,RandProcArr)

    print(test.GetDataTempAndPress())
    print(test.GetDataRandomProc())
    test.PlotCorrWithOrd(test.CalcCorrWithOrd())