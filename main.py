import tkinter as tk

class Uczeń:
    lista_uczniów = []
    def __init__(self, imie:str, nazwisko:str, pesel:str, nazwa_grupy:str):
        self.imie = imie
        self.nazwisko = nazwisko
        if len(pesel) == 11 and pesel.isdigit():
            self.pesel=pesel
        self.nazwa_grupy = nazwa_grupy

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, nowe_imie):
        self._imie = nowe_imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko):
        self._nazwisko = nowe_nazwisko

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, nowy_pesel):
        if len(nowy_pesel) == 11 and nowy_pesel.isdigit():
            self._pesel = nowy_pesel
        else:
            raise ValueError("Pesel składa się z 11 cyfr!")

    @property
    def nazwa_grupy(self):
        return self._nazwa_grupy

    @nazwa_grupy.setter
    def nazwa_grupy(self, nowa_nazwa_grupy):
        self._nazwa_grupy = nowa_nazwa_grupy

    def oblicz_średnią(self):
        średnia=0.0
        liczba_ocen=0
        for i in Ocena.lista_ocen:
            if i.uczeń.pesel == self._pesel:
                średnia += i
                liczba_ocen += 1
        średnia = średnia/len(self.lista_ocen)
        return średnia

    #def czy_zagrożony(self):


class Grupa:
    lista_grup = []
    def __init__(self, nazwa:str, uczniowie:list):
        self.nazwa = nazwa
        self.uczniowie = uczniowie

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nowe_nazwa):
        self._nazwa = nowe_nazwa

    @property
    def uczniowie(self):
        return self._uczniowie

    @uczniowie.setter
    def uczniowie(self, nowe_uczniowie):
        self._uczniowie = nowe_uczniowie

    def dodaj_ucznia(self, uczeń_imie:str,uczeń_nazwisko:str,uczeń_pesel:str):
        uczeń=Uczeń(imie=uczeń_imie, nazwisko=uczeń_nazwisko, pesel=uczeń_pesel, nazwa_grupy=self.nazwa)
        #w tym przypadku naleźy dodać takiego ucznia do istniejących uczniów w klasie uczeń lub dopisać do pliku txt
        self.uczniowie.append(uczeń)
    def usun_ucznia(self, uczeń):
        if uczeń in self.uczniowie:
            self.uczniowie.remove(uczeń)
        else:
            raise ValueError("Taki uczeń nie istnieje w tej grupie")

class Ocena:
    lista_ocen = []
    def __init__(self, uczeń:Uczeń, opis:str, data:str):
        self.uczeń=uczeń
        self.opis=opis
        self.data=data

    @property
    def uczeń(self):
        return self.uczeń

    @uczeń.setter
    def uczeń(self, nowy_uczeń):
        self._uczeń = nowy_uczeń

    @property
    def opis(self):
        return self.opis

    @opis.setter
    def opis(self, nowy_opis):
        self._opis = nowy_opis

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, nowa_data):
        self._data = nowa_data


class Obecność:
    lista_obecności = []
    def __init__(self, uczeń:Uczeń, data:str, status:str):
        self.uczeń=uczeń
        self.data=data
        self.status=status

    @property
    def uczeń(self):
        return self.uczeń

    @uczeń.setter
    def uczeń(self, nowy_uczeń):
        self._uczeń = nowy_uczeń

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, nowa_data):
        self._data = nowa_data

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, nowy_status):
        self._status = nowy_status

def wczytywanie_z_pliku(nazwa:str):
    try:
        with (open(nazwa, "r", encoding="utf-8") as plik):
            for linia in plik:
                dane = linia.strip().split("\t")
                if nazwa == "Uczniowie.txt":
                    uczen = Uczeń(imie=dane[0], nazwisko= dane[1], pesel= dane[2], nazwa_grupy= dane[3])
                    Uczeń.lista_uczniów.append(uczen)
                elif nazwa == "Grupy.txt":
                    uczen_grupa=[]
                    for i in Uczeń.lista_uczniów:
                        if i.nazwa_grupy == dane[0]:
                            uczen_grupa.append(i)
                    grupa = Grupa(nazwa= dane[0],uczniowie = uczen_grupa)
                    Grupa.lista_grup.append(grupa)
                elif nazwa == "Oceny.txt":
                    pesel = dane[0]
                    for i in Uczeń.lista_uczniów:
                        if i.pesel == pesel:
                            ocena = Ocena(uczeń=i, opis=dane[1], data=dane[2])
                            Ocena.lista_ocen.append(ocena)
                            break
                elif nazwa == "Obecności.txt":
                    pesel = dane[0]
                    for i in Uczeń.lista_uczniów:
                        if i.pesel == pesel:
                            obecność = Obecność(uczeń=i, data=dane[1], status=dane[2])
                            Obecność.lista_obecności.append(obecność)
                            break
    except FileNotFoundError:
        print(f"Plik '{nazwa}' nie istnieje.")

wczytywanie_z_pliku("Uczniowie.txt")
wczytywanie_z_pliku("Grupy.txt")
wczytywanie_z_pliku("Oceny.txt")
wczytywanie_z_pliku("Obecności.txt")

for i in Grupa.lista_grup:
    print(i.nazwa)


okno_aplikacji = tk.Tk()
okno_aplikacji.geometry("600x400")
okno_aplikacji.title("Dziennik nauczyciela")

entries_frame = tk.Frame(okno_aplikacji)
entries_frame.grid(row=1, column=0, padx=10, pady=20)

ocenaLubObecnosc=[]
def update_ocenaLubObecnosc(sel):
    for widget in entries_frame.winfo_children():
        widget.destroy()
    ocenaLubObecnosc.clear()

opcjeOcLubOb = tk.StringVar(okno_aplikacji)
opcjeOcLubOb.set("Wybierz opcję")
options2 = ["Ocena", "Obecnosc"]

entry_fields = []
def update_entries(selection):
    for widget in entries_frame.winfo_children():
        widget.destroy()
    entry_fields.clear()

    match(selection):
        case "Dodawanie ucznia":
            labels = ["Imię", "Nazwisko", "Pesel", "Nazwa grupy"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2+i, column=1, padx=7, pady=10,sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Sprawdzanie obecności":
            for i in range(3):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wystawianie oceny":
            for i in range(4):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            entry = tk.Entry(entries_frame, width=15)
            entry.grid(row=3, column=3, padx=7, pady=10)
            entry_fields.append(entry)
            return
        case "Edycja oceny/obecności danego dnia":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            dropdown = tk.OptionMenu(entries_frame, opcjeOcLubOb, *options2, command=update_ocenaLubObecnosc)
            dropdown.grid(row=4, column=2, padx=7,pady=10)
            entry = tk.Entry(entries_frame, width=15)
            entry.grid(row=5, column=2, padx=7, pady=10)
            entry_fields.append(entry)
            return
        case "Wyświetlenie oceny/obecności danego ucznia":
            for i in range(3):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wystawianie zagrożenia":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wyświetl średnią ucznia":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wygeneruj raport z ocen i obecności uczniów":
            entry = tk.Entry(entries_frame, width=15)
            entry.grid(row=2, column=2, padx=7, pady=10)
            entry_fields.append(entry)
            return
        case "Generowanie statystyk":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return




def show_values():
    print("Wprowadzone wartości:")
    for i, entry in enumerate(entry_fields):
        print(f"Pole {i + 1}: {entry.get()}")


selected_option = tk.StringVar(okno_aplikacji)
selected_option.set("Wybierz opcję")
options = ["Dodawanie ucznia", "Sprawdzanie obecności", "Wystawianie oceny",
           "Edycja oceny/obecności danego dnia",
           "Wyświetlenie oceny/obecności danego ucznia",
           "Wystawianie zagrożenia",
           "Wyświetl średnią ucznia",
           "Wygeneruj raport z ocen i obecności uczniów",
           "Generowanie statystyk"]
dropdown = tk.OptionMenu(okno_aplikacji, selected_option, *options, command=update_entries)
dropdown.grid(row=0, column=0, pady=10)

show_button = tk.Button(okno_aplikacji, text="Pokaż dane", command=show_values)
show_button.grid(row=2, column=4, pady=10)

okno_aplikacji.mainloop()