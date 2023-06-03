import time
import tkinter
from tkinter import *
from tkinter import ttk, scrolledtext
import subprocess
import tkinter as tk
from tkinter import Text
from tkinter.messagebox import showinfo

FlagSensor = False
FlagValue = False
FlagPriority = False

main_process = None
window = None
Flag1 = False
Flag2 = False
Flag3 = False

Timing = 0

testByPriority = False
testByInterval = False

def GetDataFileMain(Timing,name,vidj):
    with open(name, "r") as file:
        new_sensor_data = file.read()
    vidj.delete("1.0", tk.END)
    vidj.insert(tk.END, new_sensor_data)
    vidj.after(int(Timing / 2000), GetDataFileMain, Timing, name, vidj)

def start_main():
    global main_process, Timing
    Timing = int(ent_T.get()) * 1000
    main_process = subprocess.Popen(['python', 'main.py'])
    GetDataFileMain(Timing,"maindata.txt", main_result)



def stop_main():
    global main_process
    if main_process:
        main_process.terminate()
        main_process.wait()
        main_process = None


def GetDataFile(name,vidj):
    with open(name, "r") as file:
        new_sensor_data = file.read()
    vidj.delete("1.0", END)
    vidj.insert(END, new_sensor_data)

def GetSensorData():
    file = open("flag1.txt", "w")
    file.write(str(True))
    file.close()
    time.sleep(Timing / 2000)
    GetDataFile("sensordata.txt",sensor_data)

def GetOverValue():
    file = open("flag2.txt", "w")
    file.write(str(True))
    file.close()
    time.sleep(Timing / 2000)
    GetDataFile("overvalue.txt", over_data)

def ChangePreo():
    file = open("flag3.txt", "w")
    file.write(str(True))
    file.close()
    global testByPriority,testByInterval
    if testByPriority == False:
        testByPriority = not testByPriority
        showinfo(title="Пріорітет", message="Тестування по пріорітету ")
    elif testByInterval == False:
        testByPriority = not testByPriority
        showinfo(title="Пріорітет", message="Тестування по інтервалу")

def deflFile(file,flag):
    file.write(str(Flag1))
    file.close()

def RefreshData():
    1

if __name__ == "__main__":
    with open("maindata.txt", "w") as file:
        pass
    with open("sensordata.txt", "w") as file:
        pass
    with open("overvalue.txt", "w") as file:
        pass
    deflFile(open("flag1.txt", "w"),Flag1)
    deflFile(open("flag2.txt", "w"), Flag2)
    deflFile(open("flag3.txt", "w"), Flag3)
    window = Tk()
    window.title("Лабораторна №1")
    window.geometry("1600x800")



    style_button = ttk.Style().configure("MyPythonButton.TButton",
                                         font=('Arial', 12),
                                         foreground='black',
                                         background='#3776AB',
                                         padding=7)

    entry_N = tkinter.StringVar(window, "5")
    lab_N = ttk.Label(text="Kількість датчиків: ", font="Arial 12 normal roman")
    ent_N = ttk.Entry(textvariable=entry_N, font="Arial 12 normal roman")

    entry_T = tkinter.StringVar(window, "2")
    lab_T = ttk.Label(text="Період опитування: ", font="Arial 12 normal roman")
    ent_T = ttk.Entry(textvariable=entry_T, font="Arial 12 normal roman")

    entry_ExP = tkinter.StringVar(window, "5,3,4,2,7")
    lab_ExP = ttk.Label(text="Період обстеження: ", font="Arial 12 normal roman")
    ent_ExP = ttk.Entry(textvariable=entry_ExP, font="Arial 12 normal roman")

    entry_SP = tkinter.StringVar(window, "0,5,1,2,3")
    lab_SP = ttk.Label(text="Період обстеження: ", font="Arial 12 normal roman")
    ent_SP = ttk.Entry(textvariable=entry_SP, font="Arial 12 normal roman")

    lab_SD = ttk.Label(text="Дані з датчиків: ", font="Arial 12 normal roman")
    lab_OD = ttk.Label(text="Перевищені значення: ", font="Arial 12 normal roman")


    btn_Start = ttk.Button(text="Почати", command=start_main, style="MyPythonButton.TButton")
    btn_Stop = ttk.Button(text="Зупинити", command=stop_main, style="MyPythonButton.TButton")

    btn_Sensor_Data = ttk.Button(text="Дані з датчиків",command=GetSensorData , style="MyPythonButton.TButton")
    btn_OverData = ttk.Button(text="Перевищені значення",command=GetOverValue ,style="MyPythonButton.TButton")
    btn_Preority = ttk.Button(text="Зміна прiоритету",command=ChangePreo ,style="MyPythonButton.TButton")


    main_result = Text(font="Arial 12 normal roman")


    sensor_data = Text(font="Arial 12 normal roman")
    over_data = Text(font="Arial 12 normal roman")

    lab_N.place(x=5, y=5)
    ent_N.place(x=200, y=5)

    lab_T.place(x=5, y=30)
    ent_T.place(x=200, y=30)

    lab_ExP.place(x=5, y=55)
    ent_ExP.place(x=200, y=55)

    lab_SP.place(x=5, y=80)
    ent_SP.place(x=200, y=80)

    lab_SD.place(x=710, y=5)
    lab_OD.place(x=710, y=360)

    btn_Start.place(x=500, y=5, height=45, width=185)
    btn_Stop.place(x=500, y=55, height=45, width=185)

    btn_Sensor_Data.place(x=5, y=120, height=45, width=185)


    btn_OverData.place(x=252.5, y=120, height=45, width=185)
    btn_Preority.place(x=500, y=120, height=45, width=185)

    main_result = scrolledtext.ScrolledText(window, font="Arial 12 normal roman")
    main_result.place(x=5, y=200, height=800, width=680)
    #scrollbar = Scrollbar(window)
    #scrollbar.place(x=685, y=200, height=800)
    #scrollbar.config(command=main_result.yview)
    #main_result.config(yscrollcommand=scrollbar.set)

    sensor_data.place(x=710, y=30, height=300)
    over_data.place(x=710, y=385, height=300)


    window.mainloop()