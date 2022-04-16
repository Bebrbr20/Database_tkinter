import sqlite3
import tkinter as tk

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

def New_User():
    label1.pack_forget()
    create.pack_forget()
    ljmeno=tk.Label(text="Jméno")
    jmeno=tk.Entry(text="Jméno")
    prijmeni = tk.Entry(text="Jméno")
    rodne_cislo = tk.Entry(text="Jméno")
    pohlavi = tk.Entry(text="Jméno")
    email = tk.Entry(text="Jméno")
    telefon = tk.Entry(text="Jméno")

    ljmeno.pack()
    jmeno.pack()
    prijmeni.pack()
    rodne_cislo.pack()
    pohlavi.pack()
    email.pack()
    telefon.pack()
print(table)

# Hlavní konfigurace tkinteru
window = tk.Tk()
window.geometry("570x300")
window.title("Databáze")

label1=tk.Label(text = "Databáze uživatelů")
label1.pack()

create=tk.Button(text= "Přidání uživatele", command=New_User)
create.pack()


window.mainloop()
