import tkinter
from tkinter import *
from tkinter import ttk
from main import *

defalt = Consumption_NitricAcid(12.1, 11.6, 12.4, 34.5, 1.5, 0.3, 0.2, 0.35, 0.33, 0.45, 0.65)

window = Tk()
window.title("Лабораторна №4")
window.geometry("1200x600")

arr_value = defalt.get_all_fields()

##creating widgets



entry_text1 = tkinter.StringVar(window,arr_value[0])
lab_x1 = ttk.Label(text="х̃1=", font="Arial 12 normal roman")
ent_x1 = ttk.Entry(textvariable = entry_text1, font="Arial 12 normal roman")


entry_text2 = tkinter.StringVar(window,arr_value[1])
lab_x2 = ttk.Label(text="х̃2=", font="Arial 12 normal roman")
ent_x2 = ttk.Entry(textvariable = entry_text2, font="Arial 12 normal roman")

entry_text3 = tkinter.StringVar(window,arr_value[2])
lab_x3 = ttk.Label(text="х̃3=", font="Arial 12 normal roman")
ent_x3 = ttk.Entry(textvariable = entry_text3, font="Arial 12 normal roman")

entry_text4 = tkinter.StringVar(window,arr_value[3])
lab_x4 = ttk.Label(text="х̃4=", font="Arial 12 normal roman")
ent_x4 = ttk.Entry(textvariable = entry_text4, font="Arial 12 normal roman")

entry_text11 = tkinter.StringVar(window,arr_value[4])
lab_l = ttk.Label(text="l=", font="Arial 12 normal roman")
ent_l = ttk.Entry(textvariable = entry_text11, font="Arial 12 normal roman")

entry_text5 = tkinter.StringVar(window,arr_value[5])
lab_dx123 = ttk.Label(text="Δx1=Δx2=Δx3=", font="Arial 12 normal roman")
ent_dx123 = ttk.Entry(textvariable = entry_text5, font="Arial 12 normal roman")

entry_text6 = tkinter.StringVar(window,arr_value[6])
lab_dx4 = ttk.Label(text="Δx4=", font="Arial 12 normal roman")
ent_dx4 = ttk.Entry(textvariable = entry_text6, font="Arial 12 normal roman")

entry_text7 = tkinter.StringVar(window,arr_value[7])
lab_o1 = ttk.Label(text="σ1=", font="Arial 12 normal roman")
ent_o1 = ttk.Entry(textvariable = entry_text7, font="Arial 12 normal roman")

entry_text8 = tkinter.StringVar(window,arr_value[8])
lab_o2 = ttk.Label(text="σ2=", font="Arial 12 normal roman")
ent_o2 = ttk.Entry(textvariable = entry_text8, font="Arial 12 normal roman")

entry_text9 = tkinter.StringVar(window,arr_value[9])
lab_o3 = ttk.Label(text="σ3=", font="Arial 12 normal roman")
ent_o3 = ttk.Entry(textvariable = entry_text9, font="Arial 12 normal roman")

entry_text10 = tkinter.StringVar(window,arr_value[10])
lab_o4 = ttk.Label(text="σ4=", font="Arial 12 normal roman")
ent_o4 = ttk.Entry(textvariable = entry_text10, font="Arial 12 normal roman")

result = Text(font="Arial 12 normal roman")

arr_lab = [lab_x1,lab_x2,lab_x3,lab_x4,lab_l,lab_dx123,lab_dx4,lab_o1,lab_o2,lab_o3,lab_o4]
arr_ent = [ent_x1,ent_x2,ent_x3,ent_x4,ent_l,ent_dx123,ent_dx4,ent_o1,ent_o2,ent_o3,ent_o4]


for r in range(len(arr_ent)):
        arr_lab[r].place(x=5, y=50*r+10)
        arr_ent[r].place(x=150, y=50*r+10)

result.place(x=350, y=10, height=700, width=1000)



def set_values():
    defalt.set_x1(float(ent_x1.get()))
    defalt.set_x2(float(ent_x2.get()))
    defalt.set_x3(float(ent_x3.get()))
    defalt.set_x4(float(ent_x4.get()))
    defalt.set_l(float(ent_l.get()))
    defalt.set_dx123(float(ent_dx123.get()))
    defalt.set_dx4(float(ent_dx4.get()))
    defalt.set_o1(float(ent_o1.get()))
    defalt.set_o2(float(ent_o2.get()))
    defalt.set_o3(float(ent_o3.get()))
    defalt.set_o4(float(ent_o4.get()))

def get_data():
    set_values()

    result.delete("1.0", END)
    result.insert("1.0",defalt.Show_Data())

style_python_button = ttk.Style()
style_python_button.configure("MyPythonButton.TButton",
                              font=('Arial', 12),
                              foreground='black',
                              background='#3776AB',
                              padding=10)

btn_calc = ttk.Button(text="Розрахувати", command=get_data, style="MyPythonButton.TButton")
btn_calc.place(x=150, y=550, height= 50, width=185)

window.mainloop()

