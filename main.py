import tkinter as tk
from datetime import datetime
from time import strptime


class Uczeń:
    lista_uczniów = []
    def __init__(self, imie:str, nazwisko:str, pesel:str, nazwa_grupy:str):
        self.imie = imie
        self.nazwisko = nazwisko
        for i in Uczeń.lista_uczniów:
            if i.pesel == pesel:
                raise ValueError("Osoba o takim peselu już jest na liście")
        if len(pesel) == 11 and pesel.isdigit():
            self._pesel=pesel
        else:
            raise ValueError("Niepoprawny pesel")
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

    @staticmethod
    def dodaj_ucznia(entry_fields):
        try:
            with (open("Uczniowie.txt", "a", encoding="utf-8") as plik):
                imie = entry_fields[0].get()
                imie.lstrip()
                imie.rstrip()
                nazwisko = entry_fields[1].get()
                nazwisko.lstrip()
                nazwisko.rstrip()
                pesel = entry_fields[2].get()
                pesel.lstrip()
                pesel.rstrip()
                grupa = entry_fields[3].get()
                grupa.lstrip()
                grupa.rstrip()
                nowy_uczen = Uczeń(imie=imie, nazwisko=nazwisko, pesel=pesel, nazwa_grupy=grupa)
                Uczeń.lista_uczniów.append(nowy_uczen)
                print(f"Dodano ucznia: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
                for i in Uczeń.lista_uczniów:
                    print(i.imie+" "+i.nazwisko+" "+i.pesel+" "+i.nazwa_grupy)
                    wypisywanie_błędów("")
                plik.write("\n"+imie+"\t"+nazwisko+"\t"+pesel+"\t"+grupa+"\n")
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    @staticmethod
    def usuń_ucznia(entry_fields):
        try:
            with (open("Uczniowie.txt", "w", encoding="utf-8") as plik):
                imie = entry_fields[0].get()
                imie.lstrip()
                imie.rstrip()
                nazwisko = entry_fields[1].get()
                nazwisko.lstrip()
                nazwisko.rstrip()
                pesel = entry_fields[2].get()
                pesel.lstrip()
                pesel.rstrip()
                grupa = entry_fields[3].get()
                grupa.lstrip()
                grupa.rstrip()
                count=0
                for i in Uczeń.lista_uczniów:
                    if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel and i.nazwa_grupy == grupa:
                        Uczeń.lista_uczniów.remove(i)
                        count += 1
                for i in Uczeń.lista_uczniów:
                    plik.write(i.imie+"\t"+i.nazwisko+"\t"+i.pesel+"\t"+i.nazwa_grupy+"\n")
            if count == 0:
                raise ValueError("Nieistnieje taka osoba")
            print(f"Usunięto ucznia: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
            Grupa.czyszczenie_grup()


            for i in Uczeń.lista_uczniów:
                print(i.imie + " " + i.nazwisko + " " + i.pesel + " " + i.nazwa_grupy)
                wypisywanie_błędów("")
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    def czy_zagrożony(self):
        liczba_lekcji=0
        liczba_nb=0
        liczba_sp=0
        uczen=self
        for i in Obecność.lista_obecności:
            if i.uczeń.pesel == self._pesel:
                liczba_lekcji += 1
                if i.status.lower()=="nieobecny":
                    liczba_nb+=1
                elif i.status.lower() == "spóźniony":
                    liczba_sp+=1
        if liczba_nb > 2:
            raise ValueError("Uczeń jest zagrożony, ponieważ ma więcej niż 2 nieobecności")
        elif float(liczba_sp) >= float(liczba_sp)/2:
            raise ValueError("Uczeń jest zagrożony, ponieważ ma spóźnienia na conajmniej połowie lekcji")
        elif self.oblicz_średnią()<3.0:
            raise ValueError("Uczeń jest zagrożony, ponieważ ma średnią poniżej 3.0")

class Grupa:
    lista_grup = []
    def __init__(self, nazwa:str, uczniowie:list):
        for i in Grupa.lista_grup:
            if i.nazwa == nazwa:
                raise ValueError("Taka grupa już istnieje")
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

    @staticmethod
    def czyszczenie_grup():
        for i in Grupa.lista_grup:
            if len(i.uczniowie) == 0:
                Grupa.lista_grup.remove(i)

class Ocena:
    lista_ocen = []
    def __init__(self, uczeń:Uczeń, opis:str, data:str, wartość:str):
        if str(wartość).isdigit() and float(wartość)>=1.0 and float(wartość)<=6.0:
            self.wartość=wartość
        else:
            raise ValueError("Ocena może być tylko z zakresu od 1 do 6, zapisana liczbowo np. 4.5")
        self.uczeń=uczeń
        self.opis=opis
        try:
            datetime.strptime(data, "%d.%m.%Y")
            self.data=data
        except:
            raise ValueError("Niepoprawna data")

    @property
    def wartość(self):
        return self._wartość

    @wartość.setter
    def wartość(self, nowa_wartość):
        self._wartość = nowa_wartość

    @property
    def uczeń(self):
        return self._uczeń

    @uczeń.setter
    def uczeń(self, nowy_uczeń):
        self._uczeń = nowy_uczeń

    @property
    def opis(self):
        return self._opis

    @opis.setter
    def opis(self, nowy_opis):
        self._opis = nowy_opis

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nowa_data):
        self._data = nowa_data

    def dodaj_ocene(entry_fields):
        try:
            with (open("Oceny.txt", "a", encoding="utf-8") as plik):
                imie = entry_fields[0].get()
                nazwisko = entry_fields[1].get()
                pesel = entry_fields[2].get()
                grupa = entry_fields[3].get()
                count = 0
                nowy_uczen = None
                for i in Uczeń.lista_uczniów:
                    if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel and i.nazwa_grupy == grupa:
                        nowy_uczen=i
                        count += 1
                if count == 0:
                    raise ValueError("Nieistnieje taka osoba")
                opis = entry_fields[4].get()
                data = entry_fields[5].get()
                wartość = entry_fields[6].get()
                for i in Ocena.lista_ocen:
                    if i.uczeń.imie == imie and i.uczeń.nazwisko == nazwisko and i.uczeń.pesel == pesel and i.uczeń.nazwa_grupy == grupa and i.opis==opis and i.wartość==wartość:
                        raise ValueError("Taka ocena już została dodana dla tej osoby")
                nowa_ocena = Ocena(uczeń=nowy_uczen,opis=opis, data=data,wartość=wartość)
                Ocena.lista_ocen.append(nowa_ocena)
                print(f"Dodano ocenę {wartość} z: {opis} , dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
                for i in Ocena.lista_ocen:
                    print(i.uczeń.imie+" "+i.uczeń.nazwisko+" "+i.uczeń.pesel+" "+i.uczeń.nazwa_grupy+" "+i.opis+" "+i.data+" "+str(i.wartość))
                    wypisywanie_błędów("")
                plik.write("\n"+pesel+"\t"+opis+"\t"+data+"\t"+wartość)
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    def edytuj_ocene(self_fields):
        try:
            with (open("Uczniowie.txt", "w", encoding="utf-8") as plik):
                imie = entry_fields[0].get()
                nazwisko = entry_fields[1].get()
                pesel = entry_fields[2].get()

                nowy_uczen = None
                for i in Uczeń.lista_uczniów:
                    if i.pesel == pesel:
                        nowy_uczen = i

                data = entry_fields[3].get()
                wartosc_oceny = entry_fields[4].get()
                opis_oceny = entry_fields[5].get()
                nowa_wartosc = entry_fields[6].get()
                nowy_opis = entry_fields[7].get()
                for i in Ocena.lista_ocen:
                    if (i.uczeń.pesel == pesel and i.wartość == wartosc_oceny and i.opis == opis_oceny and i.data == data):
                        Ocena.lista_ocen.remove(i)
                nowa_ocena = Ocena(nowy_uczen, nowy_opis, data, nowa_wartosc)
                Ocena.lista_ocen.append(nowa_ocena)

                print(
                f"Dodano ocenę {nowa_wartosc} z: {nowy_opis} , dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}")
                for i in Ocena.lista_ocen:
                    print(
                    i.uczeń.imie + " " + i.uczeń.nazwisko + " " + i.uczeń.pesel + " " + i.uczeń.nazwa_grupy + " " + i.opis + " " + i.data + " " + str(
                        i.wartość))
                    wypisywanie_błędów("")
                for i in Ocena.lista_ocen:
                    plik.write(i.uczeń.pesel+"\t"+i.opis+"\t"+i.data+"\t"+i.wartość+"\n")
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")



class Obecność:
    lista_obecności = []
    def __init__(self, uczeń:Uczeń, data:str, status:str):
        self.uczeń=uczeń
        self.data=data
        self.status=status

    @property
    def uczeń(self):
        return self._uczeń

    @uczeń.setter
    def uczeń(self, nowy_uczeń):
        self._uczeń = nowy_uczeń

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, nowa_data):
        self._data = nowa_data

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nowy_status):
        self._status = nowy_status

    def sprawdzanie_obecnosci(entry_fields):
        try:
            with (open("Obecności.txt", "a", encoding="utf-8") as plik):
                grupa = entry_fields[0].get()
                imie = entry_fields[1].get()
                nazwisko = entry_fields[2].get()
                pesel = entry_fields[3].get()
                data = entry_fields[4].get()
                obecnosc= entry_fields[5].get()

                nowy_uczen= None
                for i in Uczeń.lista_uczniów:
                    if(i.pesel==pesel):
                        nowy_uczen=i
                nowa_obecnosc= Obecność(nowy_uczen, data, obecnosc)
                Obecność.lista_obecności.append(nowa_obecnosc)
                print(f"Dodano obecnosc: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa},Data: {data} Obecnosc {obecnosc}")
                for i in Obecność.lista_obecności:
                    print(i.uczeń.imie +" "+i.uczeń.nazwisko+" "+i.uczeń.nazwa_grupy+" "+i.status)
                    wypisywanie_błędów("")
                plik.write("\n" +  pesel + "\t" + data + "\t"+ obecnosc +"\n")
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    def edytuj_obecnosc(self_fields):
        try:
            with (open("Obecności.txt", "w", encoding="utf-8") as plik):
                imie = entry_fields[0].get()
                nazwisko = entry_fields[1].get()
                pesel = entry_fields[2].get()

                nowy_uczen = None
                for i in Uczeń.lista_uczniów:
                    if i.pesel == pesel:
                        nowy_uczen = i

                data = entry_fields[3].get()
                obecnosc = entry_fields[4].get()
                nowa_obecnosc = entry_fields[5].get()
                for i in Obecność.lista_obecności:
                    if (i.uczeń.pesel == pesel and i.status== obecnosc and i.data == data):
                        Obecność.lista_obecności.remove(i)
                nowa_obecnosc2= Obecność(nowy_uczen, data, nowa_obecnosc)
                Obecność.lista_obecności.append(nowa_obecnosc2)

                print(
                f"Dodano obecnosc {nowa_obecnosc}, dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}")
                for i in Obecność.lista_obecności:
                    print(
                    i.uczeń.imie + " " + i.uczeń.nazwisko + " " + i.uczeń.pesel + " " + i.uczeń.nazwa_grupy + " " + i.data+ " " + i.status)
                    wypisywanie_błędów("")
                for i in Obecność.lista_obecności:
                    plik.write(i.uczeń.pesel+"\t"+i.data+"\t"+i.status+"\n")
        except ValueError as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")


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
                            ocena = Ocena(uczeń=i, opis=dane[1], data=dane[2],wartość=3)
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

def wypisywanie_błędów(treść):
    if error_box:
        error_box.delete("1.0", tk.END)
        error_box.insert(tk.END, treść)

wczytywanie_z_pliku("Uczniowie.txt")
wczytywanie_z_pliku("Grupy.txt")
wczytywanie_z_pliku("Oceny.txt")
wczytywanie_z_pliku("Obecności.txt")

okno_aplikacji = tk.Tk()
okno_aplikacji.geometry("720x430")
okno_aplikacji.title("Dziennik nauczyciela")

entries_frame = tk.Frame(okno_aplikacji)
entries_frame.grid(row=1, column=0, sticky="nsew")

okno_aplikacji.grid_columnconfigure(0, weight=1)
okno_aplikacji.grid_rowconfigure(1, weight=1)

global error_box
error_box = tk.Text(okno_aplikacji, height=5, fg="red", wrap="word")
error_box.grid(row=2, column=0, columnspan=5, sticky="we", padx=10, pady=5)


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
                label.grid(row=2 + i, column=1, padx=7, pady=10, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            save_button = tk.Button(entries_frame, text="Zapisz ucznia",command=lambda: Uczeń.dodaj_ucznia(entry_fields))
            save_button.grid(row=2 + len(labels), column=2, pady=10)

            entries_frame.grid_columnconfigure(0,weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista uczniów")
            label.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
            for i in Uczeń.lista_uczniów:
                listbox.insert(tk.END, i.imie + '   ' + i.nazwisko + "   " + i.pesel + "   " + i.nazwa_grupy)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        case "Usuwanie ucznia":
            labels = ["Imię", "Nazwisko", "Pesel", "Nazwa grupy"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=7, pady=10, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            save_button = tk.Button(entries_frame, text="Usuń ucznia", command=lambda: Uczeń.usuń_ucznia(entry_fields))
            save_button.grid(row=2 + len(labels), column=2, pady=10)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista uczniów")
            label.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
            for i in Uczeń.lista_uczniów:
                listbox.insert(tk.END, i.imie + '   ' + i.nazwisko + "   " + i.pesel + "   " + i.nazwa_grupy)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        #edytowanie ucznia

        case "Sprawdzanie obecności":
            labels = ["Grupa", "Imie", "Nazwisko", "Pesel", "Data", "Stan obecności"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=7, pady=7, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=7)
                entry_fields.append(entry)

            save_button = tk.Button(entries_frame, text="Dodaj obecnosc", command=lambda: Obecność.sprawdzanie_obecnosci(entry_fields))
            save_button.grid(row=2 + len(labels), column=2, pady=10)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista uczniów")
            label.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
            for i in Obecność.lista_obecności:
                listbox.insert(tk.END, i.uczeń.imie + '   ' + i.uczeń.nazwisko + "   " + i.uczeń.nazwa_grupy+"   " +" "+i.data+" "+ i.status)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        case "Wystawianie oceny":
            labels = ["Imię", "Nazwisko", "Pesel", "Nazwa grupy","Tytuł oceny","Data","Ocena"]
            for i in range(7):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=5, pady=5, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=5, pady=5)
                entry_fields.append(entry)

            save_button = tk.Button(entries_frame, text="Dodaj ocenę", command=lambda: Ocena.dodaj_ocene(entry_fields))
            save_button.grid(row=2 + len(labels), column=3, pady=0)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista ocen")
            label.grid(row=2, column=3, padx=5, pady=3, sticky="ew")
            for i in Ocena.lista_ocen:
                listbox.insert(tk.END, i.uczeń.imie + '   ' + i.uczeń.nazwisko + "   " + i.uczeń.pesel + "   " + i.uczeń.nazwa_grupy + "   " + i.opis + "   " + i.data + "   " + str(i.wartość))
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=3, sticky="nsew")
            return
        case "Edycja oceny danego dnia":
            labels=["Imię", "Nazwisko", "Pesel", "Data", "Wartość oceny", "Opis oceny", "Nowa wartość", "Nowy opis"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=5, pady=3, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=2, padx=5, pady=3)
                entry_fields.append(entry)

            save_button = tk.Button(entries_frame, text="Edytuj ocenę", command=lambda: Ocena.edytuj_ocene(entry_fields))
            save_button.grid(row=2 + len(labels), column=3, pady=0)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista ocen")
            label.grid(row=2, column=3, padx=5, pady=3, sticky="ew")
            for i in Ocena.lista_ocen:
                listbox.insert(tk.END,
                               i.uczeń.imie + '   ' + i.uczeń.nazwisko + "   " + i.uczeń.pesel + "   " + i.uczeń.nazwa_grupy + "   " + i.opis + "   " + i.data + "   " + str(
                                   i.wartość))
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=3, sticky="nsew")
            return
        case "Edycja obecności danego dnia":
            labels = ["Imie", "Nazwisko", "pesel", "Data", "Obecnosc",  "Nowa obecnosc"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=5, pady=5, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=2, padx=5, pady=5)
                entry_fields.append(entry)

            save_button = tk.Button(entries_frame, text="Edytuj obecność",
                                    command=lambda: Ocena.edytuj_ocene(entry_fields))
            save_button.grid(row=2 + len(labels), column=3, pady=0)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista ocen")
            label.grid(row=2, column=3, padx=5, pady=3, sticky="ew")
            for i in Ocena.lista_ocen:
                listbox.insert(tk.END,
                               i.uczeń.imie + '   ' + i.uczeń.nazwisko + "   " + i.uczeń.pesel + "   " + i.uczeń.nazwa_grupy + "   " + i.opis + "   " + i.data + "   " + str(
                                   i.wartość))
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=3, sticky="nsew")
            return
        case "Wyświetlenie oceny danego ucznia":
            for i in range(3):
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            return
        case "Wyświetlenie obecności danego ucznia":
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
options = ["Dodawanie ucznia",
           "Usuwanie ucznia",
           "Edycja ucznia",
           "Sprawdzanie obecności",
           "Wystawianie oceny",
           "Edycja oceny danego dnia",
           "Edycja obecności danego dnia",
           "Wyświetlenie oceny danego ucznia",
           "Wyświetlenie obecności danego ucznia",
           "Wyświetl średnią ucznia",
           "Wygeneruj raport z ocen i obecności uczniów",
           "Generowanie statystyk"]
dropdown = tk.OptionMenu(okno_aplikacji, selected_option, *options, command=update_entries)
dropdown.grid(row=0, column=0, columnspan=10,sticky="new",padx=10,pady=10)


okno_aplikacji.mainloop()