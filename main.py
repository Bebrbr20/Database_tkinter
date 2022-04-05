import sqlite3
import tkinter as tk

# vytvoreni DB v paměti PC

#con = sqlite3.connect(":memory:")

con = sqlite3.connect("example.db")

cur = con.cursor()
cur.executescript("""
 insert into person(jmeno,prijmeni,rodne_cislo,pohlavi,email,telefon)
 values (
    'Jan',
    'Novák',
    '041107/4719',
    
    )
    """)

"""
create table person(
        jmeno,
        prijmeni,
        rodne_cislo,
        pohlavi,
        email,
        telefon
    );"""



data = cur.execute("SELECT * FROM person ORDER BY jmeno")

table = []

for row in data:
    print(row)
    table.append(row)
con.close()

print(table)

# Hlavní konfigurace tkinteru
window = tk.Tk()
window.geometry("570x300")
window.title("Databáze")

label1=tk.Label(text = "Databáze uživatelů")
label1.pack()




window.mainloop()