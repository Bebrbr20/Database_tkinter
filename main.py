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






def save_user(jmeno, prijmeni, rodne_cislo, pohlavi, email, telefon):
    if jmeno != "" and prijmeni != "" and rodne_cislo != "" and pohlavi != "" and email != "" and telefon != "":
        print("aaa")
    else:
        errorLabel=tk.Label( text="ERROR")
        errorLabel.grid(row=1, column= 5)

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
        command=lambda: save_user(jmeno.get(),prijmeni.get(),rodne_cislo.get(), pohlavi.get(), email.get(), telefon.get()))
    submit.grid(column=0, row=9, sticky='w')

    backbutton = tk.Button(newuserframe, text="Zpět", fg="black", command=lambda:newuserframe.grid_forget())
    backbutton.grid(row=9, column=1, sticky='w')

    exitbutton = tk.Button(newuserframe, text="Ukončit aplikaci", fg="black", command=exit)
    exitbutton.grid(row=9, column=2, sticky='w')

# Hlavní konfigurace tkinteru



mainframe = tk.Frame(window,width=900, height=250)

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
