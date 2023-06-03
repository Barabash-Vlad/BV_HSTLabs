import math
import matplotlib.pyplot as plt

class Data:
    def __init__(self,m_x,x_ti,d_x,t_u,t,k,xt_0):
        self.__m_x = m_x
        self.__x_ti = x_ti
        self.__d_x = d_x
        self.__t_u = t_u
        self.__t = t
        self.__k = k
        self.__xt_0 = xt_0

    def set_mx(self,m_x):
        self.__m_x = m_x
    def set_x_ti(self,x_ti):
        self.__x_ti = x_ti
    def set_d_x(self,d_x):
        self.__d_x = d_x
    def set_t_u(self,t_u):
        self.__t_u = t_u
    def set_t(self,t):
        self.__t = t
    def set_k(self,k):
        self.__k = k
    def set_xt_0(self,xt_0):
        self.__xt_0 = xt_0

    def Get_Main_Values(self):
        return [self.__m_x,self.__x_ti,self.__d_x,self.__t_u,self.__t,self.__k,self.__xt_0]

    def variance_forecast_error(self):
        a = math.exp(-1*self.__t_u/self.__t)
        return a

    def numerator_denominator_extrapolation(self):
        a = self.variance_forecast_error()
        k__ = self.__t_u/self.__t
        #print(k)
        Numerator = (self.__x_ti - self.__m_x) * pow(a,k__)
        print(Numerator)
        Denominator = 1 - pow(a,k__) + 0.12
        return [Numerator,Denominator]

    def temp_moment(self):
        return self.__xt_0 * self.__t_u

    def stepwise_extrapolation(self):
        return self.__m_x + self.numerator_denominator_extrapolation()[0]/self.numerator_denominator_extrapolation()[1]


    def correlation_function(self,t__):
        return self.__d_x * (1 - pow(t__,self.__k))

    def stochastic_extrapolation(self):
        return self.correlation_function((self.__xt_0 * self.__t_u/self.__t))/self.correlation_function(0) * (self.__x_ti - self.__m_x) + self.__m_x

    def arr_for_grahp(self):
        i = 1
        arr = [0.0]
        n = int(self.__t)
        while i < n+1:
            arr.append(self.correlation_function((self.__xt_0 * self.__t_u/i))/self.correlation_function(0) * (self.__x_ti - self.__m_x) + self.__m_x)
            i = i + 1
        return arr

    def arr_for_stup(self):
        i = 1
        arr = [0.0]
        n = int(self.__t)
        while i < n + 1:
            self.__t = float(i)
            arr.append(self.stepwise_extrapolation())
            i = i + 1
        return arr

    def extrapolation_plot(self):
        arrt = []
        arrsto = []
        arrstep = []
        n = int(self.__t)
        i = 0.0
        while i < n+1:
            arrt.append(i)
            i = i + 1
        arrsto = self.arr_for_grahp()
        arrstep = self.arr_for_stup()
        plt.plot(arrt,arrsto)
        plt.plot(arrt,arrstep)
        plt.xlabel('t')
        plt.ylabel('T')
        plt.legend(['стохастична','ступінчаста'])
        plt.show()





    def Get_Result(self):
        return f"Метод ступінчастої екстраполяції\n" \
               f"Визначення значення температури на момент t = ti + 0.5tц: {self.temp_moment():1.2f}\n" \
               f"Визначення чисельника та знаменника для екстраполяції:\n" \
               f"Numerator = {self.numerator_denominator_extrapolation()[0]:1.2f} та " \
               f"Denominator = {self.numerator_denominator_extrapolation()[1]:1.2f}\n" \
                   f"Знайдене значення температури: {self.stepwise_extrapolation():4.3f} °C\n\n" \
               f"Метод стохастичної екстраполяції\n" \
               f"Автокореляційна функція КХ(t) = DХ[1 − (t/τ)k] = {self.correlation_function((self.__xt_0 * self.__t_u/self.__t)):4.3f}\n" \
               f"Знайдене значення температури: {self.stochastic_extrapolation():4.3f} °C\n\n"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    M_x = 205
    x_ti = 220
    D_x = 30
    t_u = 10
    t = 20
    k = 1.5
    xt_0 = 0.5
    test = Data(M_x, x_ti, D_x, t_u, t, k, xt_0)
    test.extrapolation_plot()

    #print(stochastic_extrapolation(M_x, x_ti, D_x, t_u, t, k, xt_0))
    #print(test.stochastic_extrapolation())
    #print(test.stepwise_extrapolation())
