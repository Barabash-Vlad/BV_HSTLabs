import tkinter
from tkinter import *
from tkinter import ttk
from main import *

id_type_sensor = 3

default = Data(256.0,500.0,1024.0,2.88,768.0,512.0,10.0,16.39,10.0,3)
arr_value = default.Get_Main_Values()

window = Tk()
window.title("Лабораторна №5")
window.geometry("1200x600")

style_button = ttk.Style().configure("MyPythonButton.TButton",
                                    font=('Arial', 16),
                                    foreground='black',
                                    background='#3776AB',
                                    padding=10)


entry_text1 = tkinter.StringVar(window,arr_value[0])
lab_Kfacp = ttk.Label(text="КF_ацп=", font="Arial 12 normal roman")
ent_Kfacp = ttk.Entry(textvariable = entry_text1, font="Arial 12 normal roman")


entry_text2 = tkinter.StringVar(window,arr_value[1])
lab_Fmax = ttk.Label(text="Fmax=", font="Arial 12 normal roman")
ent_Fmax = ttk.Entry(textvariable = entry_text2, font="Arial 12 normal roman")

entry_text3 = tkinter.StringVar(window,arr_value[2])
lab_Kmaxacp = ttk.Label(text="Kmax_ацп=", font="Arial 12 normal roman")
ent_Kmaxacp = ttk.Entry(textvariable = entry_text3, font="Arial 12 normal roman")

entry_text4 = tkinter.StringVar(window,arr_value[3])
lab_P0 = ttk.Label(text="ρ0=", font="Arial 12 normal roman")
ent_P0 = ttk.Entry(textvariable = entry_text4, font="Arial 12 normal roman")

entry_text5 = tkinter.StringVar(window,arr_value[4])
lab_Kpacp = ttk.Label(text="Кp_ацп=", font="Arial 12 normal roman")
ent_Kpacp = ttk.Entry(textvariable = entry_text5, font="Arial 12 normal roman")

entry_text6 = tkinter.StringVar(window,arr_value[5])
lab_Koacp = ttk.Label(text="Ко_ацп=", font="Arial 12 normal roman")
ent_Koacp = ttk.Entry(textvariable = entry_text6, font="Arial 12 normal roman")

entry_text7 = tkinter.StringVar(window,arr_value[6])
lab_y1max = ttk.Label(text="Y1max=", font="Arial 12 normal roman")
ent_y1max = ttk.Entry(textvariable = entry_text7, font="Arial 12 normal roman")

entry_text8 = tkinter.StringVar(window,arr_value[7])
lab_ymax = ttk.Label(text="Ymax=", font="Arial 12 normal roman")
ent_ymax = ttk.Entry(textvariable = entry_text8, font="Arial 12 normal roman")

entry_text9 = tkinter.StringVar(window,arr_value[8])
lab_pmax = ttk.Label(text="pmax=", font="Arial 12 normal roman")
ent_pmax = ttk.Entry(textvariable = entry_text9, font="Arial 12 normal roman")

sensor_type = ["Термопара хромель-копель", "Термопара хромель-алюмель", "Платиновий термометр опору Пa №1", "Платиновий термометр опору Пa №2"]
sensor = StringVar(value=sensor_type[1])

comb_sensor = ttk.Combobox(textvariable=sensor, values=sensor_type, font="Arial 13 normal roman")

result = Text(font="Arial 14 normal roman")

arr_lab = [lab_Kfacp,lab_Fmax,lab_Kmaxacp,lab_P0,lab_Kpacp,lab_Koacp,lab_y1max,lab_ymax,lab_pmax]
arr_ent = [ent_Kfacp,ent_Fmax,ent_Kmaxacp,ent_P0,ent_Kpacp,ent_Koacp,ent_y1max,ent_ymax,ent_pmax]


for r in range(len(arr_ent)):
        arr_lab[r].place(x=5, y=50*r+10)
        arr_ent[r].place(x=150, y=50*r+10)



comb_sensor.place(x=5, y=450, width=330)
result.place(x=350, y=10, height=700, width=1000)

def set_values():
    default.set_Kfacp(float(ent_Kfacp.get()))
    default.set_Fmax(float(ent_Fmax.get()))
    default.set_Kmaxacp(float(ent_Kmaxacp.get()))
    default.set_P0(float(ent_P0.get()))
    default.set_Kpacp(float(ent_Kpacp.get()))
    default.set_Koacp(float(ent_Koacp.get()))
    default.set_y1max(float(ent_y1max.get()))
    default.set_ymax(float(ent_ymax.get()))
    default.set_pmax(float(ent_pmax.get()))



def get_data():
    set_values()
    #print(default.Show_Result())
    result.delete("1.0", END)
    result.insert("1.0",default.Show_Result())

def get_index(tp):
    n = len(sensor_type)
    for i in range(n):
        if str(sensor_type[i]) == str(tp):
            return i+2

def selected(event):
    id_type_sensor = get_index(sensor.get())
    default.set_type(int(id_type_sensor))
    #print(id_type_sensor)


comb_sensor.bind("<<ComboboxSelected>>", selected)

btn_calc = ttk.Button(text="Розрахувати", command=get_data, style="MyPythonButton.TButton")
btn_calc.place(x=150, y=495, height= 50, width=185)

window.mainloop()