import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import  datetime

window = tk.Tk()
window.geometry("900x250")
window.title("Databáze")



#con = sqlite3.connect(":memory:")

"""
 insert into person(jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon)
 values (
    'Jan',
    'Novák',
    '041107/4719',
    'muz',
    'jan@novak.cz',
    '123456789'
    )
"""


def validaceRC(rc):
    x = list(rc)
    if len(rc) == 11:
        if x[6] == '/':
            count = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[7]+x[8]+x[9]+x[10]
            if int(count)%11 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def save_user(newuserframe,jmeno, prijmeni, rodne_cislo, pohlavi, email, telefon):
    if jmeno.get() == '':
        jmeno.config(bg='red')
    else:
        jmeno.config(bg='white')
    if prijmeni.get() == '':
        prijmeni.config(bg='red')
    else:
        prijmeni.config(bg='white')
    if rodne_cislo.get() == '' or not validaceRC(rodne_cislo.get()):
        rodne_cislo.config(bg='red')
    else:
        rodne_cislo.config(bg='white')
    if pohlavi.get() == '':
        pohlavi.config(bg='red')
    else:
        pohlavi.config(bg='white')
    if email.get() == '':
        email.config(bg='red')
    else:
        email.config(bg='white')
    if telefon.get() == '':
        telefon.config(bg='red')
    else:
        telefon.config(bg='white')

    if jmeno.get() != '' or prijmeni.get() != '' or rodne_cislo.get() != '' or pohlavi.get() != '' or email.get() != '' or telefon.get() != '':
        if validaceRC(rodne_cislo.get()):
            try:

                con = sqlite3.connect("example.db")

                cur = con.cursor()
                cur.execute("insert into person(jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon) values(?,?,?,?,?,?)",(jmeno.get(), prijmeni.get(), rodne_cislo.get(), pohlavi.get(), email.get(), telefon.get()))
                con.commit()
                tv.insert("", tk.END, values=(jmeno.get(), prijmeni.get(), rodne_cislo.get(), pohlavi.get(), email.get(), telefon.get()))
                newuserframe.grid_forget()


            except:
                print("ERROR PŘI ZAPISOVÁNÍ")
                return "ERROR PŘI ZAPISOVÁNÍ"

def update_user(edituserframe,jmeno,prijmeni,rodne_cislo, pohlavi, email, telefon):
    if jmeno.get() == '':
        jmeno.config(bg='red')
    else:
        jmeno.config(bg='white')
    if prijmeni.get() == '':
        prijmeni.config(bg='red')
    else:
        prijmeni.config(bg='white')
    if rodne_cislo.get() == '' or not validaceRC(rodne_cislo.get()):
        rodne_cislo.config(bg='red')
    else:
        rodne_cislo.config(bg='white')
    if pohlavi.get() == '':
        pohlavi.config(bg='red')
    else:
        pohlavi.config(bg='white')
    if email.get() == '':
        email.config(bg='red')
    else:
        email.config(bg='white')
    if telefon.get() == '':
        telefon.config(bg='red')
    else:
        telefon.config(bg='white')

    if jmeno.get() != '' or prijmeni.get() != '' or rodne_cislo.get() != '' or pohlavi.get() != '' or email.get() != '' or telefon.get() != '':
        if validaceRC(rodne_cislo.get()):
            try:

                con = sqlite3.connect("example.db")

                cur = con.cursor()
                cur.execute("UPDATE person SET (jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon) = (?,?,?,?,?,?) WHERE (jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon) = (?,?,?,?,?,?)",(jmeno.get(), prijmeni.get(), rodne_cislo.get(), pohlavi.get(), email.get(), telefon.get(), str(selected_item['values'][0]), str(selected_item['values'][1]), str(selected_item['values'][2]), str(selected_item['values'][3]), str(selected_item['values'][4]), str(selected_item['values'][5])))
                con.commit()

                tv.delete(*tv.get_children())

                con = sqlite3.connect("example.db")

                cur = con.cursor()

                data = cur.execute("SELECT * FROM person ORDER BY jmeno")

                rows = data.fetchall()

                for row in rows:
                    tv.insert("", tk.END, values=row)

                data.close()
                con.close()

                edituserframe.grid_forget()
            except:
                print("ERROR PŘI ZAPISOVÁNÍ")


def select_item(event):
    global selected_item

    rowid = tv.identify_row(event.y)
    selected_item = tv.item(tv.focus())

    print (selected_item['values'])


    edituserframe = tk.Frame(window, width=900, height=250)

    edituserframe.grid(row=0, column=0)
    edituserframe.grid_propagate(0)

    ljmeno=tk.Label(edituserframe,text="Jméno")
    ljmeno.grid(column=4, row=1)

    jmeno=tk.Entry(edituserframe,text="Jméno")
    jmeno.grid(column=5, row=1)

    lprijmeni = tk.Label(edituserframe,text="Příjmení")
    lprijmeni.grid(column=4, row=2)

    prijmeni = tk.Entry(edituserframe)
    prijmeni.grid(column=5, row=2)

    lrodne_cislo = tk.Label(edituserframe,text="Rodné číslo")
    lrodne_cislo.grid(column=4, row=3)

    rodne_cislo = tk.Entry(edituserframe)
    rodne_cislo.grid(column=5, row=3)

    lpohlavi = tk.Label(edituserframe,text="Pohlaví")
    lpohlavi.grid(column=4, row=4)

    pohlavi = tk.Entry(edituserframe)
    pohlavi.grid(column=5, row=4)

    lemail = tk.Label(edituserframe,text="Email")
    lemail.grid(column=4, row=5)

    email = tk.Entry(edituserframe)
    email.grid(column=5, row=5)

    ltelefon = tk.Label(edituserframe,text="Telefonní číslo")
    ltelefon.grid(column=4, row=6)

    telefon = tk.Entry(edituserframe)
    telefon.grid(column=5, row=6)

    jmeno.insert(tk.END, selected_item['values'][0])
    prijmeni.insert(tk.END, selected_item['values'][1])
    rodne_cislo.insert(tk.END, selected_item['values'][2])
    pohlavi.insert(tk.END, selected_item['values'][3])
    email.insert(tk.END, selected_item['values'][4])
    telefon.insert(tk.END, selected_item['values'][5])

    submit = tk.Button(
        edituserframe,
        text="Přidat",
        command=lambda: update_user(edituserframe,jmeno,prijmeni,rodne_cislo, pohlavi, email, telefon))
    submit.grid(column=0, row=9, sticky='w')

    backbutton = tk.Button(edituserframe, text="Zpět", fg="black", command=lambda:edituserframe.grid_forget())
    backbutton.grid(row=9, column=1, sticky='w')

    exitbutton = tk.Button(edituserframe, text="Ukončit aplikaci", fg="black", command=exit)
    exitbutton.grid(row=9, column=2, sticky='w')

def focus_user(event):
    global focus_item
    rowid = tv.identify_row(event.y)
    delete_item = tv.item(tv.focus())
    focus_item = delete_item['values']
    print(focus_item)


def delete_user():
    try:
        con2 = sqlite3.connect("example.db")

        cur2 = con2.cursor()
        cur2.execute("DELETE FROM person WHERE (jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon) = (?,?,?,?,?,?)", (str(focus_item[0]), str(focus_item[1]), str(focus_item[2]),str(focus_item[3]),str(focus_item[4]), str(focus_item[5])))
        con2.commit()
        con2.close()

        tv.delete(*tv.get_children())

        con = sqlite3.connect("example.db")

        cur = con.cursor()

        data = cur.execute("SELECT * FROM person ORDER BY jmeno")

        rows = data.fetchall()

        for row in rows:
            tv.insert("", tk.END, values=row)

        data.close()
        con.close()

    except:
        print ("není vybrán žádný uživatel")


def exit():
    window.destroy()


def New_User():

    newuserframe = tk.Frame(window, width=900, height=250)

    newuserframe.grid(row=0, column=0)
    newuserframe.grid_propagate(0)



    ljmeno=tk.Label(newuserframe,text="Jméno")
    ljmeno.grid(column=4, row=1)

    jmeno=tk.Entry(newuserframe,text="Jméno")
    jmeno.grid(column=5, row=1)

    lprijmeni = tk.Label(newuserframe,text="Příjmení")
    lprijmeni.grid(column=4, row=2)

    prijmeni = tk.Entry(newuserframe)
    prijmeni.grid(column=5, row=2)

    lrodne_cislo = tk.Label(newuserframe,text="Rodné číslo")
    lrodne_cislo.grid(column=4, row=3)

    rodne_cislo = tk.Entry(newuserframe)
    rodne_cislo.grid(column=5, row=3)

    lpohlavi = tk.Label(newuserframe,text="Pohlaví")
    lpohlavi.grid(column=4, row=4)

    pohlavi = tk.Entry(newuserframe)
    pohlavi.grid(column=5, row=4)

    lemail = tk.Label(newuserframe,text="Email")
    lemail.grid(column=4, row=5)

    email = tk.Entry(newuserframe)
    email.grid(column=5, row=5)

    ltelefon = tk.Label(newuserframe,text="Telefonní číslo")
    ltelefon.grid(column=4, row=6)

    telefon = tk.Entry(newuserframe)
    telefon.grid(column=5, row=6)

    submit = tk.Button(
        newuserframe,
        text="Přidat",
        command=lambda: save_user(newuserframe, jmeno,prijmeni,rodne_cislo, pohlavi, email, telefon))
    submit.grid(column=0, row=9, sticky='w')

    backbutton = tk.Button(newuserframe, text="Zpět", fg="black", command=lambda:newuserframe.grid_forget())
    backbutton.grid(row=9, column=1, sticky='w')

    exitbutton = tk.Button(newuserframe, text="Ukončit aplikaci", fg="black", command=exit)
    exitbutton.grid(row=9, column=2, sticky='w')






# Hlavní konfigurace tkinteru



mainframe = tk.Frame(window,width=900, height=250)

label1=tk.Label(mainframe,text = "Databáze uživatelů")
label1.pack()


con = sqlite3.connect("example.db")

cur = con.cursor()

tv = ttk.Treeview(mainframe)
tv['columns'] = ('jmeno', 'prijmeni', 'rodne_cislo', 'pohlavi', 'email', 'telefon')
tv.column('#0', width=0, stretch=tk.NO)
tv.column('jmeno', anchor=tk.CENTER, width=150)
tv.column('prijmeni', anchor=tk.CENTER, width=150)
tv.column('rodne_cislo', anchor=tk.CENTER, width=150)
tv.column('pohlavi', anchor=tk.CENTER, width=150)
tv.column('email', anchor=tk.CENTER, width=150)
tv.column('telefon', anchor=tk.CENTER, width=150)

tv.heading('#0', text='', anchor=tk.CENTER)
tv.heading('jmeno', text='Jméno', anchor=tk.CENTER)
tv.heading('prijmeni', text='Příjmení', anchor=tk.CENTER)
tv.heading('rodne_cislo', text='Rodné číslo', anchor=tk.CENTER)
tv.heading('pohlavi', text='Pohlaví', anchor=tk.CENTER)
tv.heading('email', text='E-mail', anchor=tk.CENTER)
tv.heading('telefon', text='Telefon', anchor=tk.CENTER)
data = cur.execute("SELECT * FROM person ORDER BY jmeno")

rows = data.fetchall()

for row in rows:
    tv.insert("", tk.END, values=row)

data.close()
con.close()

tv.bind('<Double-1>', select_item)
tv.bind('<ButtonRelease-1>', focus_user)
tv.pack()



bluebutton = tk.Button(mainframe, text="Přidání uživatele", fg="black" , command=New_User)
bluebutton.pack( side = tk.LEFT )

blackbutton = tk.Button(mainframe, text="Odebrání uživatele", fg="black", command=delete_user)
blackbutton.pack( side = tk.LEFT)

blackbutton = tk.Button(mainframe, text="Ukončit aplikaci", fg="black", command=exit)
blackbutton.pack(side=tk.LEFT)

mainframe.grid(row=0, column=0)



window.mainloop()
