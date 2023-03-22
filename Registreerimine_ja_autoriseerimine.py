


import random
from tkinter import *

kasutajad = {'kasutaja': 'salasona'}

import random
import string
kasutajad = [] 
salasona=[]


#def salasona(valik,k: int):
#  sala="*"
#  for i in range(k):
#   t=valik(string.ascii_letters) #Aa...Zz
#   num=valik([1,2,3,4,5,6,7,8,9,0])
#   t_num=[t,str(num)]
#   sala+=valik(t_num)
#  return sala


aken = Tk()
aken.geometry('550x600')
aken.title('Kasutaja registreerimine ja autoriseerimine')


def salasona(kasutajad,salasona):
    if not validate_input():
        return
    kasutajad = entry_username.get()
    salasona = entry_passw.get()
    if kasutaja in kasutajad:
        lbl_status.config(text='Kasutajanimi on juba võetud.')
    else:
        kasutajad[kasutaja] = salasona
        lbl_status.config(text='Kasutaja registreerimine õnnestus.')

def change_password(kasutajad,salasona):
    kasutaja = entry_username.get()
    vana_passw = entry_passw.get()
    new_passw = entry_passw.get()

    if kasutaja not in kasutajad:
        lbl_status.config(text='Kasutajanime ei leitud.')
    elif kasutaja[kasutajad]!= vana_passw:
        lbl_status.config(text='Vale salasõna.')
    else:
        kasutaja[kasutajad] = new_passw
        lbl_status.config(text='Salasõna muutmine õnnestus.')

def automaatne_parool(psword:list):
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
# Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
    print(psword)



def registreerimine(kasutajad,salasona):
    kasutajanimi = input("Sisesta kasutajanimi: ")
    if kasutajanimi in kasutajad:
        print("Kasutajanimi on juba võetud.")
        return
    valik = input("Kas soovid ise luua parooli või lasta programmil selle automaatselt genereerida? (Ise/Automaatne): ")
    if valik.lower() == "ise":
        while True:
            salasona = input("Sisesta parool: ")
            if vale_salasona(salasona):
                break
            else:
                print("Parool peab sisaldama vähemalt üht numbrit, üht väiketähte, üht suurtähte ja ühte erimärki.")
    else:
        salasona = loo_salasona()
        print("Automaatselt genereeritud parool: ", salasona)
    kasutajad.append(kasutajad)
    salasona.append(salasona)




lbl_username = Label(aken, text='Kasutajanimi:', font='Times 14')
lbl_username.pack()
entry_username = Entry(aken, font='Times 14', bg='#6f5a70')
entry_username.pack()

lbl_pass = Label(aken, text='Salasõna:', font='Times 14')
lbl_pass.pack()
entry_passw = Entry(aken, show='*', font='Times 14', bg='#6f5a70')
entry_passw.pack()

btn_reg = Button(aken, text='Registreeri', command=registreerimine, font='Times 14')
btn_reg.pack()
btn_login = Button(aken, text='Logi sisse', command=salasona, font='Times 14')
btn_login.pack()

lbl_status = Label(aken, text='', font='Times 14', bg='#6f5a70')
lbl_status.pack()

btn_generate = Button(aken, text='Loo parool', command=automaatne_parool, font='Times 14')
btn_generate.pack()

btn_recover = Button(aken, text='Taasta parool', command=change_password, font='Times 14')
btn_recover.pack()

#btn_change = Button(aken, text='Muuda salasõna', command=salasona_muutmine, font='Times 14')
#btn_change.pack()

aken.config(bg='#b9c797')
aken.mainloop()



