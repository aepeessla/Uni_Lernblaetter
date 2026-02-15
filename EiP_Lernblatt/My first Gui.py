import tkinter as tk
from tkinter import messagebox
import random as r


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        # DoubleVar benutzen wir, wenn wir eine Kommazahl speichern möchten !
        # Ansonsten verw. wir IntVar() !

        self.wurzel = tk.DoubleVar()
        self.quadrat = tk.DoubleVar()
        self.text = tk.Text(self, font='Arial') # Hier wird der user irgendeine Zahl reinschrieben und wir müssen es dann zu einem echten float umf´wandeln !
        #Man kann auch den Innenabstand zum Text bestimmen mit padding:<int>
        self.button = tk.Button(text='Berechne', command=self.berechnen) #ohne (), weil es dann sofort ausgelöst wird, wenn d. Programm gestartet wird
        
        
        #wir sagen, dass es angezeigt werden soll mit .pack()
        self.text.pack(anchor="w")
        
        #Hier setzte ich meinen Button !
        # Man kann hier auch d. Pos. sagen:
            #.pack(side='left') oder gemplett auf der x-Achse: .pack(fill='left')
            # wenn es fest bleiben soll = anchor=himmelsrichtung !
                #n, ne, e, se, s, sw, w, nw, or center
        self.button.pack(anchor='ne')

        #Wir wollen das Ergebnis ausgeben:
            #textvariable = Anstatt es jedes Mal manuell zu öndern, guckt es sich immer diese eine Variabel an & ändert es automatisch
            #self.wurzel ist d. Var. d. es einnimt, welches bei def berechnen(self): berechnet wird !
                #D. Ergebnis wird also zu 'self.wurzel = tk.DoubleVar()' zurückgeg.
            #.pack() fügt es als Widget hinzu
        tk.Label(textvariable=self.wurzel).pack()
        tk.Label(textvariable=self.quadrat).pack()

    def berechnen(self):
        # "1.0": 1 = Zeile 1, 0 = Zeichen 0, -1c: Wir sagen d. d. autom. einegfügte \n ignoriert werden soll
        num = (self.text.get("1.0", "end-1c")) #wir wollen den Inhalt, v. dem was d. User in d. text-Widget eingetragen hat 
        #kann man meine Zahl in einen float umwandeln ?
       
        num = float(num)
        if num < 0:
            messagebox.showerror("Nur positive Zahlen !!!", "Bitte geben Sie nur positive Zahlen ein,.")
            self.wurzel.set(0.0)
            self.quadrat.set(0.0)
        else:
            self.wurzel.set(round(float(num)**0.5, 2))
            self.quadrat.set(round(float(num)**2, 2))
        
class GUI2(tk.Tk):
    # pack macht es wie eine Stufe(Moodle Startseit)
    # grid: Wir können die Flächen teilen in Spalten und Zeilen
        #Man kann auch von den einzelnen Spalten/Zellen d. Höhe und Breite bestimmen
        #Man platziert dann d. Widgets in diese Spalten/Zeilen
        #Man bestimmt wie viele Spalten/Zeilen d. Widget einnehmen soll

        #Im normalen Zustand ist d. widget in d. Bitte:
            #mit den Himmelsrichtungen kann man d. an eine Seite binden -> man kann 'ns' machen & es 
            # wird d. Höhe v. d. zelle einnehmen
                #d. größe bleibt zunächst gleich !



    def __init__(self):
        super().__init__()
        self.button = tk.Button(text='Button').pack(anchor="ne")

        self.x = tk.IntVar()
        #Wenn option 1 ausgewählt ist, dann x = 1 also != option 2 und deswegen kann man nur eines auswählen 
        self.option1 = tk.Radiobutton(text="Option 1",variable=x, value=1)
        self.option2 = tk.Radiobutton(text="Option 2", variable=x, value=2)

        self.text = tk.Text()

        #Wenn ich "self.option1 = tk.Radiobutton(text="Option 1",variable=x, value=1).pack()" mache, dann
        # ist self.option1 == None
        self.option1.pack(anchor="nw")  
        self.option2.pack(anchor="nw")

        self.option1.select()
        self.option2.select()
        self.text.pack(anchor='s', fill='x', expand=True)
    
    def __init__(self):
        super().__init__()
        
        self.x = tk.IntVar()

        self.opt1 = tk.Radiobutton(text='Option 1', variable=self.x, value=1, bg="yellow")
        self.opt2 = tk.Radiobutton(text='Option 2', variable=self.x, value=2, bg="yellow")

        self.button = tk.Button(text="Button")
        self.text = tk.Text()
        #somit geben wir d. Spalte eine Eigenschaft
        #weight sagt, wer d. Stärkere ist:
            #columconfigurate(0, weight=0) ist "schächer" als columconfigurate(1, weight=1)
            #weight = 0 ist einfahc nur so groß wie d. Wdget selbst
                #weight = 1 nimmt somit den Platz, welches Option 1 gehört weg, weil opt1 nur seinen Größenplatz möchte !
    
        self.columnconfigure(0, weight=1) # Linke Spalte dehnt sich aus
        self.columnconfigure(1, weight=0) # Rechte Spalte bleibt fest
        self.rowconfigure(0) #obere Seite die Sominantere = 1
        self.rowconfigure(1) #obere Seite die Sominantere = 1
        self.rowconfigure(2, weight=1) #untere Seite schächer = 0

        self.button.grid(row=0, column=1, sticky="ne")

        self.opt1.grid(row= 0, column=0, sticky="w")
        self.opt2.grid(row=1, column=0, sticky="w")

        self.text.grid(columnspan=2, row=3, sticky="nesw")
        
        
        #D. sorgt dafür, dass am Anfang bereits eine Option ausgewählt wird !
        self.opt1.select()
        
class GUI3(tk.Tk):
    def __init__(self):
        super().__init__()
        self.text_eingabe = tk.Text()

        self.gemischter_text = tk.StringVar()
        self.label = tk.Label(self, textvariable=self.gemischter_text)

        #D. Anlegen
        self.text_eingabe.grid(row=0)
        self.label.grid(row=1)

        self.text_eingabe.bind("<KeyRelease>", self.shuffle_text)



    def shuffle_text(self, event):
        #somit gucken wir, ob es ALphabet oder NUMber ist !
        if event.char.isalnum():
            # 1. Gesamten Text aus dem Widget holen (Indices beachten!)
            inhalt = self.text_eingabe.get("1.0", "end-1c")

            # 2. Text in eine Liste umwandeln (Strings sind unveränderlich)
            buchstaben_liste = list(inhalt)

            # 3. Mischen (z.B. mit random.sample oder random.shuffle)
            # random.sample gibt eine neue Liste zurück 
            gemischt = r.sample(buchstaben_liste, len(buchstaben_liste))

            # 4. Liste wieder zu einem String zusammenfügen
            ergebnis = "".join(gemischt)

            # 5. Die StringVar aktualisieren
            self.gemischter_text.set(ergebnis)
        
      
        


        

        


if __name__ == "__main__":
    # Hier wird das Fenster-Objekt erstellt
    app = GUI3()

    #Hier sagen wir wie groß d. Fenster am Start sein soll!
    app.geometry("500x500")

    #hier gebe ich meinem Fenster einen Namen 
    app.title("aepeessla first GUi")

    # Hier wird es angezeigt und bleibt offen
    app.mainloop()     