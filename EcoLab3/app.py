import tkinter
from tkinter import *
from tkinter import ttk
from main import *
default = Data(205,220,30,10,20,1.5,0.5)
arr_value = default.Get_Main_Values()
window = Tk()
window.title("Лабораторна №3")
window.geometry("1200x600")

style_button = ttk.Style().configure("MyPythonButton.TButton",
                                    font=('Arial', 16),
                                    foreground='black',
                                    background='#3776AB',
                                    padding=10)

entry_text1 = tkinter.StringVar(window,arr_value[0])
lab_Kfacp = ttk.Label(text="M[x]=", font="Arial 12 normal roman")
ent_Kfacp = ttk.Entry(textvariable = entry_text1, font="Arial 12 normal roman")


entry_text2 = tkinter.StringVar(window,arr_value[1])
lab_Fmax = ttk.Label(text="x(ti)=", font="Arial 12 normal roman")
ent_Fmax = ttk.Entry(textvariable = entry_text2, font="Arial 12 normal roman")

entry_text3 = tkinter.StringVar(window,arr_value[2])
lab_Kmaxacp = ttk.Label(text="Dx=", font="Arial 12 normal roman")
ent_Kmaxacp = ttk.Entry(textvariable = entry_text3, font="Arial 12 normal roman")

entry_text4 = tkinter.StringVar(window,arr_value[3])
lab_P0 = ttk.Label(text="tц=τ0 =", font="Arial 12 normal roman")
ent_P0 = ttk.Entry(textvariable = entry_text4, font="Arial 12 normal roman")

entry_text5 = tkinter.StringVar(window,arr_value[4])
lab_Kpacp = ttk.Label(text="τ=", font="Arial 12 normal roman")
ent_Kpacp = ttk.Entry(textvariable = entry_text5, font="Arial 12 normal roman")

entry_text6 = tkinter.StringVar(window,arr_value[5])
lab_Koacp = ttk.Label(text="К=", font="Arial 12 normal roman")
ent_Koacp = ttk.Entry(textvariable = entry_text6, font="Arial 12 normal roman")

entry_text7 = tkinter.StringVar(window,arr_value[6])
lab_y1max = ttk.Label(text=" t=ti+xτ0, x=", font="Arial 12 normal roman")
ent_y1max = ttk.Entry(textvariable = entry_text7, font="Arial 12 normal roman")

arr_lab = [lab_Kfacp,lab_Fmax,lab_Kmaxacp,lab_P0,lab_Kpacp,lab_Koacp,lab_y1max]
arr_ent = [ent_Kfacp,ent_Fmax,ent_Kmaxacp,ent_P0,ent_Kpacp,ent_Koacp,ent_y1max]


result = Text(font="Arial 14 normal roman")

for r in range(len(arr_ent)):
        arr_lab[r].place(x=5, y=50*r+10)
        arr_ent[r].place(x=150, y=50*r+10)

result.place(x=350, y=10, height=500, width=700)

def set_values():
    default.set_mx(float(ent_Kfacp.get()))
    default.set_x_ti(float(ent_Fmax.get()))
    default.set_d_x(float(ent_Kmaxacp.get()))
    default.set_t_u(float(ent_P0.get()))
    default.set_t(float(ent_Kpacp.get()))
    default.set_k(float(ent_Koacp.get()))
    default.set_xt_0(float(ent_y1max.get()))

def get_data():
    set_values()
    result.delete("1.0", END)
    result.insert("1.0", default.Get_Result())
    default.extrapolation_plot()

btn_calc = ttk.Button(text="Розрахувати", command=get_data, style="MyPythonButton.TButton")
btn_calc.place(x=150, y=365, height= 50, width=185)

window.mainloop()