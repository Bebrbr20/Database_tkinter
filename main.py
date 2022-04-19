import sqlite3
import tkinter as tk
import time

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


data = cur.execute("SELECT * FROM person ORDER BY jmeno")

table = []

for row in data:
    print(row)
    table.append(row)
con.close()

def save_user():
    if jmeno.get() != "" and prijmeni.get() != "" and rodne_cislo.get() != "" and pohlavi.get() != "" and email.get() != "" and telefon.get() != "":
        print("aaa")


def New_User():
    label1.pack_forget()
    create.pack_forget()
    ljmeno=tk.Label(text="Jméno")
    jmeno=tk.Entry(text="Jméno")
    lprijmeni = tk.Label(text="Příjmení")
    prijmeni = tk.Entry()
    lrodne_cislo = tk.Label(text="Rodné číslo")
    rodne_cislo = tk.Entry()
    lpohlavi = tk.Label(text="Pohlaví")
    pohlavi = tk.Entry()
    lemail = tk.Label(text="Email")
    email = tk.Entry()
    ltelefon = tk.Label(text="Telefonní číslo")
    telefon = tk.Entry()

    ljmeno.pack()
    jmeno.pack()
    lprijmeni.pack()
    prijmeni.pack()
    lrodne_cislo.pack()
    rodne_cislo.pack()
    lpohlavi.pack()
    pohlavi.pack()
    lemail.pack()
    email.pack()
    ltelefon.pack()
    telefon.pack()

    submit = tk.Button(text="Přidat", command=save_user)
    submit.pack()

print(table)

# Hlavní konfigurace tkinteru
window = tk.Tk()
window.geometry("570x350")
window.title("Databáze")

label1=tk.Label(text = "Databáze uživatelů")
label1.pack()

create=tk.Button(text= "Přidání uživatele", command=New_User)
create.pack()


window.mainloop()
