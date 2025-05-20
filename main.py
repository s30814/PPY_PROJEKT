# class Uczen:
#     List < Ocena >
#     List < Obecnosc >
#     Grupa
#
#     def wyswietlSredniaUcznia():
#         srednia = 0
#         ile = 0
#         for i in Oceny:
#             srednia = +i
#             ile + +
#         return srednia / ile
#
#     def czyZagrozony(self):
#         if nieobecnosci > 3:
#             zagrozony

import tkinter as tk

class Uczeń:
    def __init__(self, imie:str, nazwisko:str, pesel:str, nazwa_grupy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel(pesel)
        self.nazwa_grupy = nazwa_grupy
        self.lista_ocen = []
        self.lista_obecności =[]

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

class Grupa:
    def __init__(self, nazwa:str):
        self.nazwa = nazwa
        self.uczniowie = []

    @property
    def nazwa(self):
        return self.uczniowie
    @nazwa.setter
    def nazwa(self, nowe_nazwa):
        self._nazwa = nowe_nazwa
    @property
    def uczniowie(self):
        return self.uczniowie

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
    def __innit__(self, uczen:Uczeń, opis:str, data:str):
        self.uczen=uczen
        self.opis=opis
        self.data=data

    @property
    def uczen(self):
        return self.uczen
    @uczen.setter
    def uczen(self, nowy_uczen):
        self._uczen = nowy_uczen

    @property
    def opis(self):
        return self.opi

    @opis.setter
    def opis(self, nowy_opis):
        self._opis = nowy_opis

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, nowy_data):
        self._data = nowy_data


class Obecnosc:
    def __init__(self, uczen:Uczeń, data:str, status:str):
        self.uczen=uczen
        self.data=data
        self.status=status

    @property
    def uczen(self):
        return self.uczen

    @uczen.setter
    def uczen(self, nowy_uczen):
        self._uczen = nowy_uczen

    @property
    def data(self):
        return self.data
    @data.setter
    def data(self, nowy_data):
        self._data = nowy_data

    @property
    def status(self):
        return self.status
    @status.setter
    def status(self, nowy_status):
        self._status = nowy_status

window = tk.Tk()
window.geometry("400x400")
window.title("Dynamiczne pola tekstowe")

entries_frame = tk.Frame(window)
entries_frame.grid(row=1, column=0, padx=10, pady=20)

ocenaLubObecnosc=[]
def update_ocenaLubObecnosc(sel):
    for widget in entries_frame.winfo_children():
        widget.destroy()
    ocenaLubObecnosc.clear()

opcjeOcLubOb = tk.StringVar(window)
opcjeOcLubOb.set("Wybierz opcję")
options2 = ["Ocena", "Obecnosc"]

entry_fields = []
def update_entries(selection):
    for widget in entries_frame.winfo_children():
        widget.destroy()
    entry_fields.clear()

    match(selection):
        case "Dodaj ucznia":
            for i in range(4):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Sprawdz obecnosc":
            for i in range(3):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wystawienie ocen":
            for i in range(4):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            entry = tk.Entry(entries_frame, width=15)
            entry.grid(row=3, column=3, padx=7, pady=10)
            entry_fields.append(entry)
            return
        case "Edycja oceny/obecnosci danego dnia":
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
        case "Wyswietlenie oceny/obecnosci danego ucznia":
            for i in range(3):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wystawienie zagrozenia":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wyswietl srednia ucznia":
            for i in range(2):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wygeneruj raport z ocen i obecnosci uczniow":
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


selected_option = tk.StringVar(window)
selected_option.set("Wybierz opcję")
options = ["Dodaj ucznia", "Sprawdz obecnosc", "Wystawienie ocen",
           "Edycja oceny/obecnosci danego dnia",
           "Wyswietlenie oceny/obecnosci danego ucznia",
           "Wystawienie zagrozenia",
           "Wyswietl srednia ucznia",
           "Wygeneruj raport z ocen i obecnosci uczniow",
           "Generowanie statystyk"
           ]
dropdown = tk.OptionMenu(window, selected_option, *options, command=update_entries)
dropdown.grid(row=0, column=0, pady=10)

show_button = tk.Button(window, text="Pokaż dane", command=show_values)
show_button.grid(row=2, column=4, pady=10)

window.mainloop()