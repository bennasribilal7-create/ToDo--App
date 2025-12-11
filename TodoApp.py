#Übungsaufgabe: Mini-Todo-App mit JSON

#Ziel:
#Du baust eine kleine App, die Aufgaben speichern und laden kann. Du übst:
#Python-Funktionen
#einfache OOP (Klassen)
#JSON-Dateien lesen und schreiben
#Terminal-Input

#---TO DO APP--


import json
from datetime import datetime

class TodoApp: 
    def __init__(self):
        self.tasks = []
    def load(self):
        try:
            with open("tasks.json", "r", encoding="utf-8")as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
    def save(self):
        with open("tasks.json", "w", encoding="utf-8")as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)
    def save_new_ToDo(self):
        print ("\n-Neuer Eintrag-")
        user_in = input("Was ist zu Tun?: ")
        time = datetime.now().strftime("%d.%m.%Y %H:%M")
        self.tasks.append(f"{time}: {user_in}")
        print("Eintrag gespeichert.")
    def see_notes(self):
        if self.tasks:
            for i, n in enumerate(self.tasks, start=1):
                print(f"{i}: {n}")
        else:
            print ("Keine Einträge vorhanden.")
    def check_task(self):
        if self.tasks:
            for i, n in enumerate(self.tasks, start=1):
                print(f"{i}: {n}")
        else:
            print ("Keine Einträge vorhanden.")
        index = int(input("Nummerisch zu löschende Notiz angeben: "))
        if 1 <= index < len(self.tasks): 
            ded = index-1
            self.tasks.pop(ded)
            print ("Task erfolgreich abgehakt.")

app = TodoApp()
app.load()

while True:
 print("---ToDo App---")
 print()
 print("1: Neues Vorhaben eintragen")
 print("2: Einträge einsehen")
 print("3: Eintrag abhaken")
 print("4: Beenden")

 choice = int(input("Eingabe: "))


 if choice == 1:
     app.save_new_ToDo()
     app.save()
 elif choice == 2:
     app.see_notes()
 elif choice == 3:
     app.check_task()
     app.save()
 elif choice == 4:
     print("Programm beendet.")
     break
 else:
     print("Ungültige Eingabe!")