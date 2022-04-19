import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.geometry("900x250")
window.title("Databáze")


# vytvoreni DB v paměti PC

#con = sqlite3.connect(":memory:")

con = sqlite3.connect("example.db")

cur = con.cursor()

cur.executescript("""

    """)


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






def save_user():
    if jmeno.get() != "" and prijmeni.get() != "" and rodne_cislo.get() != "" and pohlavi.get() != "" and email.get() != "" and telefon.get() != "":
        print("aaa")

def exit():
    window.destroy()

def New_User():

    newuserframe = tk.Frame(window,width=900, height=250, bg="white")


    ljmeno=tk.Label(newuserframe,text="Jméno")
    ljmeno.grid(column=1, row=1)

    jmeno=tk.Entry(newuserframe,text="Jméno")
    jmeno.grid(column=2, row=1)

    lprijmeni = tk.Label(newuserframe,text="Příjmení")
    lprijmeni.grid(column=1, row=2)

    prijmeni = tk.Entry(newuserframe)
    prijmeni.grid(column=2, row=2)

    lrodne_cislo = tk.Label(newuserframe,text="Rodné číslo")
    lrodne_cislo.grid(column=1, row=3)

    rodne_cislo = tk.Entry(newuserframe)
    rodne_cislo.grid(column=2, row=3)

    lpohlavi = tk.Label(newuserframe,text="Pohlaví")
    lpohlavi.grid(column=1, row=4)

    pohlavi = tk.Entry(newuserframe)
    pohlavi.grid(column=2, row=4)

    lemail = tk.Label(newuserframe,text="Email")
    lemail.grid(column=1, row=5)

    email = tk.Entry(newuserframe)
    email.grid(column=2, row=5)

    ltelefon = tk.Label(newuserframe,text="Telefonní číslo")
    ltelefon.grid(column=1, row=6)

    telefon = tk.Entry(newuserframe)
    telefon.grid(column=2, row=6)

    submit = tk.Button(newuserframe,text="Přidat", command=save_user)
    submit.grid(column=2, row=7)

    newuserframe.grid(column=0, row=0)

# Hlavní konfigurace tkinteru



mainframe = tk.Frame(window,width=900, height=250, bg="white")

label1=tk.Label(mainframe,text = "Databáze uživatelů")
label1.pack()



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
    print(row)

    tv.insert("", tk.END, values=row)

data.close()
con.close()

tv.pack()


bluebutton = tk.Button(mainframe, text="Přidání uživatele", fg="black" , command=New_User)
bluebutton.pack( side = tk.LEFT )

blackbutton = tk.Button(mainframe, text="Odebrání uživatele", fg="black")
blackbutton.pack( side = tk.LEFT)

blackbutton = tk.Button(mainframe, text="Ukončit aplikaci", fg="black", command=exit)
blackbutton.pack(side=tk.LEFT)

mainframe.grid(row=0, column=0)


window.mainloop()
