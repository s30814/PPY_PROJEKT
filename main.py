import tkinter as tk
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

#Wyjątki
#1. Wyjątek zwracany gdy użytkownik poda niepoprawny pesel
class WrongPeselError(Exception):
    def __init__(self, tekst="Nie poprawny pesel, pesel powinien składać się tylko z 11 cyfr"):
        self.tekst = tekst
        super().__init__(self.tekst)

#2. Wyjątek zwracany gdy użytkownik nie posiada ocen a ktoś chce obliczyć jego średnią
class BrakOcenError(Exception):
    def __init__(self, tekst="Uczeń nie posiada ocen"):
        self.tekst = tekst
        super().__init__(self.tekst)

#3. Wyjątek zwracany, gdy użytkownik podał osobę, której nie ma w naszej bazie
class NonExistingPersonError(Exception):
    def __init__(self, tekst="Taka osoba nie istnieje"):
        self.tekst = tekst
        super().__init__(self.tekst)

#4. Wyjątek zabezpieczający przed tworzeniem grup, które już istnieją i mają przypisanych uczniów
class ExistingGroupError(Exception):
    def __init__(self, tekst="Taka grupa już istnieje"):
        self.tekst = tekst
        super().__init__(self.tekst)

#5. Wyjątek powiadamiający użytkownika o próbie utworzenia oceny z zakresu innego niż 1-6 lub nieodpowiedniego formatu oceny
class GradeValueError(Exception):
    def __init__(self, tekst="Ocena może być tylko z zakresu od 1 do 6, zapisana liczbowo np. 4.5"):
        self.tekst = tekst
        super().__init__(self.tekst)

#6. Wyjątek powiadamiający o niepoprawnym podaniu daty lub użyciu złego typu
class WrongDateError(Exception):
    def __init__(self, tekst="Nie poprawna data, data przykładowa: 23.05.2024"):
        self.tekst = tekst
        super().__init__(self.tekst)

#7. Wyjątek powiadamiający o próbie dodania oceny, która już jest zapisana w systemie
class ExistingGradeError(Exception):
    def __init__(self, tekst="Taka ocena już została dodana dla tej osoby"):
        self.tekst = tekst
        super().__init__(self.tekst)

#8. Wyjątek powiadamiający o próbie edycji oceny, która nie istnieje
class NonExistingGradeError(Exception):
    def __init__(self, tekst="Taka ocena nie istnieje"):
        self.tekst = tekst
        super().__init__(self.tekst)

#9. Wyjątek powiadamiający o próbie wyświetlenia ocen ucznia, który nie posiada ocen
class NonExistingGradesError(Exception):
    def __init__(self, tekst="Ten uczeń nie ma ocen"):
        self.tekst = tekst
        super().__init__(self.tekst)

#10. Wyjątek powiadamiający użytkownika o użyciu niepoprawnego statusu obecności ucznia
class WrongStatusError(Exception):
    def __init__(self, tekst="Status obecności może być równy tylko: obecny, nieobecny, spóźniony lub usprawiedliwiony"):
        self.tekst = tekst
        super().__init__(self.tekst)

#11. Wyjątek powiadamiający użytkownika o istnieniu takiej obecności użytkownika w systemie
class ExistingPresenceOfStudentError(Exception):
    def __init__(self, tekst="Taka obecność już istnieje dla tej osoby"):
        self.tekst = tekst
        super().__init__(self.tekst)

#12. Wyjątek powiadamiający o wykorzystaniu nie istniejącej w systemie obecności ucznia
class NonExistingPresenceOfStudentError(Exception):
    def __init__(self, tekst="Taka obecność nie istnieje"):
        self.tekst = tekst
        super().__init__(self.tekst)

#13. Wyjątek powiadamiający o próbie wyświetlenia obecności ucznia, który jeszcze nie posiada obecności
class NonExistingPresencesOfStudentsError(Exception):
    def __init__(self, tekst="Ten uczeń jeszcze nie ma wpisanych obecności"):
        self.tekst = tekst
        super().__init__(self.tekst)

#14. Wyjątek powiadamiający o próbie dodania osoby, która już istnieje w naszej bazie
class ExistingPersonError(Exception):
    def __init__(self,tekst="Osoba o takim peselu już jest na liście"):
        self.tekst = tekst
        super().__init__(self.tekst)

#15. Wyjątek powiadamiający użytkownika, że wszystkie pola muszą być wypełnione i nie mogą być wartości None
class NoneUsageError(Exception):
    def __init__(self,tekst="Wszystkie pola muszą być wypełnione, nie mogą pozostać puste!"):
        self.tekst = tekst
        super().__init__(self.tekst)
#Klasy umożliwiające działanie funkcjonalności aplikacji oraz reprezentujące naszą bazę danych
#przechowywaną za pomocą plików .txt
#Klasa będąca reprezentacją uczniów
class Uczeń:
    #Lista klasowa odpowiadająca za wszystkie obiekty uczeń, pomaga w przeszukiwaniu obiektów uczeń oraz
    #dzięki niej po zamknięciu aplikacji uczniowie zostają zapisani do pliku .txt
    lista_uczniów = []
    #Konstruktor
    def __init__(self, imie:str, nazwisko:str, pesel:str, nazwa_grupy:str):
        if imie=="" or nazwa_grupy=="" or pesel=="" or nazwa_grupy=="":
            raise NoneUsageError()
        else:
            self.imie = imie
            self.nazwisko = nazwisko
            for i in Uczeń.lista_uczniów:
                if i.pesel == pesel:
                    raise ExistingPersonError()
            if len(pesel) == 11 and pesel.isdigit():
                self._pesel=pesel
            else:
                raise WrongPeselError()
            self.nazwa_grupy = nazwa_grupy
            self.zagrożenie = False

    #gettery i settery
    @property
    def imie(self):
        return self._imie
    @imie.setter
    def imie(self, nowe_imie):
        if nowe_imie=="":
            raise NoneUsageError()
        else:
            self._imie = nowe_imie
    @property
    def nazwisko(self):
        return self._nazwisko
    @nazwisko.setter
    def nazwisko(self, nowe_nazwisko):
        if nowe_nazwisko == "":
            raise NoneUsageError()
        else:
            self._nazwisko = nowe_nazwisko
    @property
    def pesel(self):
        return self._pesel
    @pesel.setter
    def pesel(self, nowy_pesel):
        if len(nowy_pesel) == 11 and nowy_pesel.isdigit():
            self._pesel = nowy_pesel
        else:
            raise WrongPeselError()
    @property
    def nazwa_grupy(self):
        return self._nazwa_grupy
    @nazwa_grupy.setter
    def nazwa_grupy(self, nowa_nazwa_grupy):
        if nowa_nazwa_grupy == "":
            raise NoneUsageError()
        else:
            self._nazwa_grupy = nowa_nazwa_grupy
    @property
    def zagrożenie(self):
        return self._zagrożenie
    @zagrożenie.setter
    def zagrożenie(self,nowa_wartosc):
        self._zagrożenie = nowa_wartosc

    #Funkcja służąca do obliczania średniej obiektu uczeń
    def oblicz_średnią(self):
        średnia=0.0
        liczba_ocen=0
        for i in Ocena.lista_ocen:
            if i.uczeń.pesel == self._pesel:
                średnia += i.wartość
                liczba_ocen += 1
        średnia = średnia/liczba_ocen
        if liczba_ocen == 0:
            return BrakOcenError()
        return średnia

    #Funkcja statyczna pozwalająca dodać ucznia do naszej bazy oraz zarazem tworząca grupę, do której
    #student należy lub dodająca go do już istniejącej grupy ucznia
    @staticmethod
    def dodaj_ucznia(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            grupa = trymer(entry_fields[3].get())
            nowy_uczen = Uczeń(imie=imie, nazwisko=nazwisko, pesel=pesel, nazwa_grupy=grupa)
            Uczeń.lista_uczniów.append(nowy_uczen)
            count=0
            for i in Grupa.lista_grup:
                if i.nazwa == grupa:
                    count += 1
            if count == 0:
                Grupa.lista_grup.append(Grupa(grupa, []))
            for i in Grupa.lista_grup:
                if i.nazwa == grupa:
                    i.uczniowie.append(nowy_uczen)
            print(f"Dodano ucznia: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
            for i in Uczeń.lista_uczniów:
                print(i.imie+" "+i.nazwisko+" "+i.pesel+" "+i.nazwa_grupy)
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Funkcja usuwająca ucznia z naszej bazy oraz wszystkie z nim związane inne obiekty, jeśli tylko on
    #należał do grupy to grupa również jest usuwana
    @staticmethod
    def usuń_ucznia(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            grupa = trymer(entry_fields[3].get())
            count=0
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel and i.nazwa_grupy == grupa:
                    Uczeń.lista_uczniów.remove(i)
                    for j in Grupa.lista_grup:
                        if j.nazwa == grupa:
                            Grupa.lista_grup.remove(j)
                    for j in Ocena.lista_ocen:
                        if j.uczeń.pesel == pesel:
                            Ocena.lista_ocen.remove(j)
                    for j in Obecność.lista_obecności:
                        if j.uczeń.pesel == pesel:
                            Obecność.lista_obecności.remove(j)
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            print(f"Usunięto ucznia: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
            for i in Uczeń.lista_uczniów:
                print(i.imie + " " + i.nazwisko + " " + i.pesel + " " + i.nazwa_grupy)
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Funkcja edytujaca dane wybranego ucznia
    @staticmethod
    def edytuj_ucznia(entry_fields):
        try:
            pesel= trymer(entry_fields[0].get())
            nowe_imie= trymer(entry_fields[1].get())
            nowe_nazwisko= trymer(entry_fields[2].get())
            nowa_grupa=trymer(entry_fields[3].get())
            nowy_pesel=trymer(entry_fields[4].get())
            count=0

            for i in Uczeń.lista_uczniów:
                if i.pesel==pesel:
                    count += 1
                    Uczeń.lista_uczniów.remove(i)

            if count == 0:
                raise NonExistingPersonError()

            count=0

            nowy_uczen= Uczeń(nowe_imie, nowe_nazwisko, nowy_pesel, nowa_grupa)
            Uczeń.lista_uczniów.append(nowy_uczen)

            print(f"Edytowane dane ucznia, nowe dane {nowe_imie}, {nowe_nazwisko}, {nowy_pesel}, {nowa_grupa}")

            for i in Uczeń.lista_uczniów:
                print(i.imie+" "+i.nazwisko+" "+i.pesel+" "+i.nazwa_grupy)
                wypisywanie_błędów("")

        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Funkcja statyczna wyszukująca w liście (reprezentacji bazy danych) poszukiwanego studenta oraz
    #zwracająca jego średnią, funkcja używana do GUI
    @staticmethod
    def wyświetl_średnią_ucznia(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel:
                    return i.oblicz_średnią()
            raise NonExistingPersonError()
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")
            return 0.0

    #Metoda statyczna wystawiająca zagrożenia wszystkim uczniom, którzy powinni je mieć
    @staticmethod
    def wystaw_zagrożenia():
        for j in Uczeń.lista_uczniów:
            liczba_lekcji=0
            liczba_nb=0
            liczba_sp=0
            for i in Obecność.lista_obecności:
                if j.pesel == i.uczeń.pesel:
                    liczba_lekcji += 1
                    if i.status.lower() == "nieobecny":
                        liczba_nb += 1
                    elif i.status.lower() == "spóźniony":
                        liczba_sp += 1
            if liczba_nb > 2:
                j.zagrożenie=True
            elif float(liczba_sp) >= float(liczba_lekcji)/2:
                j.zagrożenie=True
            elif j.oblicz_średnią()<3.0:
                j.zagrożenie=True

    #Metoda statyczna pokazująca w GUI nauczycielowi czy uczeń i dlaczego ma zagrożenie
    @staticmethod
    def czy_zagrożony(entry_fields):
        liczba_lekcji=0
        liczba_nb=0
        liczba_sp=0
        uczen=None
        imie=trymer(entry_fields[0].get())
        nazwisko=trymer(entry_fields[1].get())
        pesel = trymer(entry_fields[2].get())
        count=0
        for i in Obecność.lista_obecności:
            if i.uczeń.pesel == pesel and i.uczeń.imie == imie and i.uczeń.nazwisko == nazwisko:
                count+=1
                uczen=i.uczeń
                liczba_lekcji += 1
                if i.status.lower()=="nieobecny":
                    liczba_nb+=1
                elif i.status.lower()=="spóźniony":
                    liczba_sp+=1
        try:
            zwrot_do_konsoli=[]
            zwrot_do_konsoli.append("Liczba lekcji: "+str(liczba_lekcji))
            zwrot_do_konsoli.append("Liczba nieobecności: "+str(liczba_nb))
            zwrot_do_konsoli.append("Liczba spóźnień: "+str(liczba_sp))
            zwrot_do_konsoli.append("")
            if count==0:
                raise NonExistingPersonError()
            elif liczba_nb > 2:
                zwrot_do_konsoli.append("Uczeń jest zagrożony, ponieważ ma więcej niż 2 nieobecności.")
            elif float(liczba_sp) >= float(liczba_lekcji)/2:
                zwrot_do_konsoli.append("Uczeń jest zagrożony, ponieważ ma spóźnienia na conajmniej połowie lekcji.")
            elif uczen.oblicz_średnią()<3.0:
                zwrot_do_konsoli.append("Uczeń jest zagrożony, ponieważ ma średnią poniżej 3.0.")
            else:
                zwrot_do_konsoli.append("Uczeń nie jest zagrożony")
            wypisywanie_błędów("")
            return zwrot_do_konsoli
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")
            return []

#Klasa będąca reprezentacją grup/klas uczniów, to w niej są przypisane listy do grupy
class Grupa:
    lista_grup = []
    def __init__(self, nazwa:str, uczniowie:list):
        if nazwa == "":
            raise NoneUsageError()
        else:
            for i in Grupa.lista_grup:
                if i.nazwa == nazwa:
                    raise ExistingGroupError()
            self.nazwa = nazwa
            self.uczniowie = uczniowie

    #Gettery i settery
    @property
    def nazwa(self):
        return self._nazwa
    @nazwa.setter
    def nazwa(self, nowe_nazwa):
        if nowe_nazwa == "":
            raise NoneUsageError()
        else:
            self._nazwa = nowe_nazwa
    @property
    def uczniowie(self):
        return self._uczniowie
    @uczniowie.setter
    def uczniowie(self, nowe_uczniowie):
        self._uczniowie = nowe_uczniowie

#Klasa reprezentująca oceny uczniów, jest listą przypisanych ocen do ucznia
class Ocena:
    lista_ocen = []
    #konstruktor
    def __init__(self, uczeń:Uczeń, opis:str, data:str, wartość:str):
        if opis == "" or data == "" or wartość=="":
            raise NoneUsageError()
        else:
            if str(wartość).isdigit() and float(wartość)>=1.0 and float(wartość)<=6.0:
                self.wartość=wartość
            else:
                raise GradeValueError()
            self.uczeń=uczeń
            self.opis=opis
            try:
                datetime.strptime(data, "%d.%m.%Y")
                self.data=data
            except:
                raise WrongDateError()

    #gettery i settery
    @property
    def wartość(self):
        return self._wartość
    @wartość.setter
    def wartość(self, nowa_wartość):
        if str(nowa_wartość).isdigit() and float(nowa_wartość) >= 1.0 and float(nowa_wartość) <= 6.0:
            self._wartość = nowa_wartość
        else:
            raise GradeValueError()
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
        if nowy_opis == "":
            raise NoneUsageError()
        else:
            self._opis = nowy_opis
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, nowa_data):
        try:
            datetime.strptime(nowa_data, "%d.%m.%Y")
            self._data = nowa_data
        except:
            raise WrongDateError()

    #Metoda statyczna dodająca nowe oceny w powiązaniu z użytkownikiem
    @staticmethod
    def dodaj_ocene(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            grupa = trymer(entry_fields[3].get())
            count = 0
            nowy_uczen = None
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel and i.nazwa_grupy == grupa:
                    nowy_uczen=i
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            opis = entry_fields[4].get()
            data = entry_fields[5].get()
            wartość = entry_fields[6].get()
            for i in Ocena.lista_ocen:
                if i.uczeń.imie == imie and i.uczeń.nazwisko == nazwisko and i.uczeń.pesel == pesel and i.uczeń.nazwa_grupy == grupa and i.opis==opis and str(i.wartość)==str(wartość):
                    raise ExistingGradeError()
            nowa_ocena = Ocena(uczeń=nowy_uczen,opis=opis, data=data,wartość=wartość)
            Ocena.lista_ocen.append(nowa_ocena)
            print(f"Dodano ocenę {wartość} z: {opis} , dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa}")
            for i in Ocena.lista_ocen:
                print(i.uczeń.imie+" "+i.uczeń.nazwisko+" "+i.uczeń.pesel+" "+i.uczeń.nazwa_grupy+" "+i.opis+" "+i.data+" "+str(i.wartość))
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Metoda statyczna pozwalająca edytować oceny
    @staticmethod
    def edytuj_ocene(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            data = trymer(entry_fields[3].get())
            wartosc_oceny = trymer(entry_fields[4].get())
            opis_oceny = trymer(entry_fields[5].get())
            nowa_wartosc = trymer(entry_fields[6].get())
            nowy_opis = trymer(entry_fields[7].get())
            count=0
            nowy_uczen = None
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel:
                    nowy_uczen = i
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            count=0
            for i in Ocena.lista_ocen:
                if i.uczeń.pesel == pesel and str(i.wartość) == str(wartosc_oceny) and i.opis == opis_oceny and i.data == data:
                    count+=1
                    Ocena.lista_ocen.remove(i)
                    break
            if count == 0:
                raise NonExistingGradeError()
            nowa_ocena = Ocena(nowy_uczen, nowy_opis, data, nowa_wartosc)
            Ocena.lista_ocen.append(nowa_ocena)
            print(f"Dodano ocenę {nowa_wartosc} z: {nowy_opis} , dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}")
            for i in Ocena.lista_ocen:
                print(i.uczeń.imie + " " + i.uczeń.nazwisko + " " + i.uczeń.pesel + " " + i.uczeń.nazwa_grupy + " " + i.opis + " " + i.data + " " + str(i.wartość))
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Statyczna metoda wyświetlająca w gui wszystkie oceny ucznia, jeśli istnieją
    @staticmethod
    def wyświetl_oceny_ucznia(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            count = 0
            lista_ocen_ucznia=[]
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel:
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            for i in Ocena.lista_ocen:
                if i.uczeń.imie and i.uczeń.nazwisko == nazwisko and i.uczeń.pesel == pesel:
                    lista_ocen_ucznia.append(i.opis+"   "+i.data+"   "+str(i.wartość))
            if len(lista_ocen_ucznia) == 0:
                raise NonExistingGradesError()
            return lista_ocen_ucznia
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")
            return []

    #metoda generująca raport
    @staticmethod
    def generowanie_raportu():
        lista_slownikow_ocen= []
        for i in Ocena.lista_ocen:
            ocena_slownik = {'uczen': i.uczeń.pesel, 'opis': i.opis, 'data': i.data, 'wartosc': i.wartość}
            lista_slownikow_ocen.append(ocena_slownik)

        lista_slownikow_obecnosci=[]
        for i in Obecność.lista_obecności:
            obecnosc_slownik=  {'uczen': i.uczeń.pesel, 'data': i.data, 'status': i.status}
            lista_slownikow_obecnosci.append(obecnosc_slownik)

        df_oceny = pd.DataFrame(lista_slownikow_ocen)
        df_obecnosci = pd.DataFrame(lista_slownikow_obecnosci)

        raport = pd.merge(df_oceny, df_obecnosci, on=['uczen', 'data'], how='outer')

        raport.to_excel("Raport.xlsx")

    #metoda generowania statystyk oraz wizualizacja ich za pomoca wykresow
    @staticmethod
    def statystyki_wizualizacja():
        #wykres słupkowy ze srednimi ocenami uczniow
        uczen_srednia={}
        for i in Uczeń.lista_uczniów:
            uczen_srednia[f"{i.imie} {i.nazwisko} {i.pesel}"]=i.oblicz_średnią()

        uczniowie = list(uczen_srednia.keys())
        srednie_oceny = list(uczen_srednia.values())

        plt.bar(uczniowie, srednie_oceny, color='red')
        plt.xlabel("Uczniowie")
        plt.ylabel("Średnia ocen")
        plt.title("Wykres średnich ocen uczniów")
        plt.ylim(0,6)
        plt.xticks(rotation=90, ha="center")
        plt.tight_layout()
        plt.show()
        #wykres kolowy statusu obecnosci wskazanego ucznia


        #wykres ocen wskazanej klasy

#Klasa reprezentująca obiekty obecności uczniów, jest urzeczywistnieniem Obecności z bazy danych
class Obecność:
    lista_obecności = []
    #konstruktor
    def __init__(self, uczeń:Uczeń, data:str, status:str):
        if data == "" or status == "":
            raise NoneUsageError()
        else:
            self.uczeń=uczeń
            try:
                datetime.strptime(data, "%d.%m.%Y")
                self.data = data
            except:
                raise WrongDateError()
            if status.lower() != "obecny" and status.lower() != "nieobecny" and status.lower() != "spóźniony" and status.lower() != "usprawiedliwiony":
                raise WrongStatusError()
            else:
                self.status=status

    #gettery i settery
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
        try:
            datetime.strptime(nowa_data, "%d.%m.%Y")
            self._data = nowa_data
        except:
            raise WrongDateError()
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, nowy_status):
        if nowy_status.lower() != "obecny" and nowy_status.lower() != "nieobecny" and nowy_status.lower() != "spóźniony" and nowy_status.lower() != "usprawiedliwiony":
            raise WrongStatusError()
        else:
            self._status = nowy_status

    #Metoda statyczna odpowiadająca za dodawanie nowych obecności uczniom
    @staticmethod
    def sprawdzanie_obecnosci(entry_fields):
        try:
            grupa = trymer(entry_fields[0].get())
            imie = trymer(entry_fields[1].get())
            nazwisko = trymer(entry_fields[2].get())
            pesel = trymer(entry_fields[3].get())
            data = trymer(entry_fields[4].get())
            status= trymer(entry_fields[5].get())
            count = 0
            nowy_uczen = None
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel and i.nazwa_grupy == grupa:
                    nowy_uczen = i
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            for i in Obecność.lista_obecności:
                if i.uczeń.imie == imie and i.uczeń.nazwisko == nazwisko and i.uczeń.pesel == pesel and i.data == data:
                    raise ExistingPresenceOfStudentError()
            nowa_obecnosc= Obecność(nowy_uczen, data, status)
            Obecność.lista_obecności.append(nowa_obecnosc)
            print(f"Dodano obecność: {imie} {nazwisko}, PESEL: {pesel}, Grupa: {grupa},Data: {data} Status obecności {status}")
            for i in Obecność.lista_obecności:
                print(i.uczeń.imie +" "+i.uczeń.nazwisko+" "+i.uczeń.pesel+" "+i.uczeń.nazwa_grupy+" "+i.status)
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Statyczna metoda służąca do educji istniejących obecności uczniów
    @staticmethod
    def edytuj_obecnosc(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            data = trymer(entry_fields[3].get())
            obecnosc = trymer(entry_fields[4].get())
            nowa_obecnosc = trymer(entry_fields[5].get())
            count = 0
            nowy_uczen = None
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel:
                    nowy_uczen = i
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            dodawana_obecność = Obecność(nowy_uczen, data, nowa_obecnosc)
            count=0
            for i in Obecność.lista_obecności:
                if i.uczeń.pesel == pesel and i.status == obecnosc and i.data == data:
                    count += 1
                    Obecność.lista_obecności.remove(i)
                    break
            if count == 0:
                raise NonExistingPresenceOfStudentError()
            Obecność.lista_obecności.append(dodawana_obecność)

            print(f"Dodano obecność {nowa_obecnosc}, dnia: {data}. Uczniowi: {imie} {nazwisko}, PESEL: {pesel}")
            for i in Obecność.lista_obecności:
                print(i.uczeń.imie + " " + i.uczeń.nazwisko + " " + i.uczeń.pesel + " " + i.uczeń.nazwa_grupy + " " + i.data+ " " + i.status)
                wypisywanie_błędów("")
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")

    #Statyczna metoda zwracająca wszystkie obecności ucznia wraz z datą i statusem
    @staticmethod
    def wyświetl_obecności_ucznia(entry_fields):
        try:
            imie = trymer(entry_fields[0].get())
            nazwisko = trymer(entry_fields[1].get())
            pesel = trymer(entry_fields[2].get())
            count = 0
            lista_obecności_ucznia = []
            for i in Uczeń.lista_uczniów:
                if i.imie == imie and i.nazwisko == nazwisko and i.pesel == pesel:
                    count += 1
                    break
            if count == 0:
                raise NonExistingPersonError()
            for i in Obecność.lista_obecności:
                if i.uczeń.imie and i.uczeń.nazwisko == nazwisko and i.uczeń.pesel == pesel:
                    lista_obecności_ucznia.append(i.data + "   " + i.status)
            if len(lista_obecności_ucznia) == 0:
                raise NonExistingPresencesOfStudentsError()
            return lista_obecności_ucznia
        except Exception as e:
            wypisywanie_błędów(e)
            print(f"Błąd: {e}")
            return []

#Metody pomocnicze globalne
#Metoda służąca do wczytywania danych z bazy danych (plików .txt)
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

#Funkcja usuwająca znaki białe z końca i początku w zmiennej, używana by uniknąć pomyłek użytkownika
def trymer(zmienna):
    return zmienna.strip()

#Funkcja służąca do przekazywania do okna errorów wszystkich treści błędów, które wystąpią
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
def update_ocenaLubObecnosc():
    for widget in entries_frame.winfo_children():
        widget.destroy()
    ocenaLubObecnosc.clear()

opcjeOcLubOb = tk.StringVar(okno_aplikacji)
opcjeOcLubOb.set("Wybierz opcję")

options2 = ["Ocena", "Obecnosc"]

entry_fields = []
#Funkcja odpowiadająca za działanie GUI
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
                listbox.insert(tk.END, i.imie + "   " + i.nazwisko + "   " + i.pesel + "   " + i.nazwa_grupy)
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
                listbox.insert(tk.END, i.imie + "   " + i.nazwisko + "   " + i.pesel + "   " + i.nazwa_grupy)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        case "Edycja ucznia":
            labels= ["Pesel", "Nowe imię", "Nowe nazwisko", "Nowa nazwa grupy", "Nowy pesel"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=7, pady=10, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=2, padx=7, pady=10)
                entry_fields.append(entry)
            save_button = tk.Button(entries_frame, text="Edytuj ucznia", command=lambda: Uczeń.edytuj_ucznia(entry_fields))

            save_button.grid(row=2 + len(labels), column=2, pady=10)
            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista uczniów")
            label.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
            for i in Uczeń.lista_uczniów:
                listbox.insert(tk.END, i.imie + "   " + i.nazwisko + "   " + i.pesel + "   " + i.nazwa_grupy)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        case "Sprawdzanie obecności":
            labels = ["Grupa", "Imie", "Nazwisko", "Pesel", "Data", "Stan obecności"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=1, padx=7, pady=7, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=2, padx=7, pady=7)
                entry_fields.append(entry)

            save_button = tk.Button(entries_frame, text="Dodaj obecność", command=lambda: Obecność.sprawdzanie_obecnosci(entry_fields))
            save_button.grid(row=2 + len(labels), column=2, pady=10)

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=1)

            listbox = tk.Listbox(entries_frame)
            label = tk.Label(entries_frame, text="Lista uczniów")
            label.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
            for i in Obecność.lista_obecności:
                listbox.insert(tk.END, i.uczeń.imie + "   " + i.uczeń.nazwisko + "   " + i.uczeń.pesel + "   " + i.uczeń.nazwa_grupy + "   " +i.data+ "   " + i.status)
            listbox.grid(row=3, column=3, rowspan=5, padx=5, pady=5, sticky="nsew")
            return
        case "Wystawianie oceny":
            labels = ["Imię", "Nazwisko", "Pesel", "Nazwa grupy", "Tytuł oceny", "Data", "Ocena"]
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
        case "Edycja oceny/obecności danego dnia":
            option_var = tk.StringVar(value="ocena")

            def zmiana_opcji():
                #Czyszcze stare pola i widgety
                for widget in entries_frame.winfo_children():
                    widget.destroy()
                entry_fields.clear()

                #Dodaje RadioButtony
                tk.Label(entries_frame, text="Wybierz tryb edycji:").grid(row=0, column=0, pady=3, sticky="w")
                tk.Radiobutton(entries_frame, text="Edycja oceny", variable=option_var, value="ocena", command=zmiana_opcji).grid(row=0, column=1, sticky="w")
                tk.Radiobutton(entries_frame, text="Edycja obecności", variable=option_var, value="obecność", command=zmiana_opcji).grid(row=0, column=2, sticky="w")

                #Pola formularza + przycisk zapisu w zależności od wybranej opcji
                if option_var.get() == "ocena":
                    labels = ["Imię", "Nazwisko", "Pesel", "Data", "Wartość oceny", "Opis oceny", "Nowa wartość", "Nowy opis"]
                    for i in range(len(labels)):
                        label = tk.Label(entries_frame, text=labels[i])
                        label.grid(row=2 + i, column=1, padx=5, pady=3, sticky="e")
                        entry = tk.Entry(entries_frame, width=15)
                        entry.grid(row=2 + i, column=2, padx=5, pady=3)
                        entry_fields.append(entry)

                    save_button = tk.Button(entries_frame, text="Edytuj ocenę", command=lambda: Ocena.edytuj_ocene(entry_fields))
                    save_button.grid(row=2 + len(labels), column=2, pady=5)

                    # Lista ocen
                    label = tk.Label(entries_frame, text="Lista ocen")
                    label.grid(row=2, column=3, padx=5, pady=3, sticky="ew")

                    listbox = tk.Listbox(entries_frame)
                    for i in Ocena.lista_ocen:
                        listbox.insert(tk.END,f"{i.uczeń.imie}   {i.uczeń.nazwisko}   {i.uczeń.pesel}   {i.uczeń.nazwa_grupy}   {i.opis}   {i.data}   {i.wartość}")
                    listbox.grid(row=3, column=3, rowspan=10, padx=5, pady=3, sticky="nsew")

                else:
                    labels = ["Imię", "Nazwisko", "Pesel", "Data", "Obecność", "Nowa obecność"]
                    for i in range(len(labels)):
                        label = tk.Label(entries_frame, text=labels[i])
                        label.grid(row=2 + i, column=1, padx=5, pady=3, sticky="e")
                        entry = tk.Entry(entries_frame, width=15)
                        entry.grid(row=2 + i, column=2, padx=5, pady=3)
                        entry_fields.append(entry)

                    save_button = tk.Button(entries_frame, text="Edytuj obecność", command=lambda: Obecność.edytuj_obecnosc(entry_fields))
                    save_button.grid(row=2 + len(labels), column=2, pady=5)

                    # Lista obecności
                    label = tk.Label(entries_frame, text="Lista obecności")
                    label.grid(row=2, column=3, padx=5, pady=3, sticky="ew")

                    listbox = tk.Listbox(entries_frame)
                    for i in Obecność.lista_obecności:
                        listbox.insert(tk.END,f"{i.uczeń.imie}   {i.uczeń.nazwisko}   {i.uczeń.pesel}   {i.uczeń.nazwa_grupy}   {i.data}   {i.status}")
                    listbox.grid(row=3, column=3, rowspan=10, padx=5, pady=3, sticky="nsew")
                entries_frame.grid_columnconfigure(0, weight=0)
                entries_frame.grid_columnconfigure(1, weight=0)
                entries_frame.grid_columnconfigure(2, weight=0)
                entries_frame.grid_columnconfigure(3, weight=1)
            zmiana_opcji()
            return
        case "Wyświetlenie oceny/obecności danego ucznia":
            option_var = tk.StringVar(value="ocena")

            def zmiana_opcji():
                # Czyszcze stare pola i widgety
                for widget in entries_frame.winfo_children():
                    widget.destroy()
                entry_fields.clear()

                # Dodaje RadioButtony
                tk.Label(entries_frame, text="Wybierz opcję wyświetlania:").grid(row=0, column=0, pady=3, sticky="w")
                tk.Radiobutton(entries_frame, text="Wyświetlanie ocen", variable=option_var, value="ocena",
                               command=zmiana_opcji).grid(row=0, column=1, sticky="w")
                tk.Radiobutton(entries_frame, text="Wyświetlanie obecności", variable=option_var, value="obecność",
                               command=zmiana_opcji).grid(row=0, column=2, sticky="we")

                # Pola formularza + przycisk zapisu w zależności od wybranej opcji
                labels = ["Imię", "Nazwisko", "Pesel"]
                for i in range(len(labels)):
                    label = tk.Label(entries_frame, text=labels[i])
                    label.grid(row=2 + i, column=0, padx=5, pady=3, sticky="e")
                    entry = tk.Entry(entries_frame, width=15)
                    entry.grid(row=2 + i, column=1, padx=5, pady=3)
                    entry_fields.append(entry)

                def wyswietl_oceny():
                    lista_ucznia = Ocena.wyświetl_oceny_ucznia(entry_fields)
                    listbox.delete(0, tk.END)
                    if len(lista_ucznia)>0:
                        for i in lista_ucznia:
                            listbox.insert(tk.END, f"{i}")

                def wyswietl_obecności():
                    lista_ucznia = Obecność.wyświetl_obecności_ucznia(entry_fields)
                    listbox.delete(0, tk.END)
                    if len(lista_ucznia) > 0:
                        for i in lista_ucznia:
                            listbox.insert(tk.END, f"{i}")

                if option_var.get() == "ocena":
                    label = tk.Label(entries_frame, text="Lista ocen")
                    label.grid(row=2, column=2, padx=5, pady=3, sticky="ew")
                    save_button = tk.Button(entries_frame, text="Wyświetl oceny", command=wyswietl_oceny)
                    save_button.grid(row=2 + len(labels), column=1, pady=5)
                else:
                    label = tk.Label(entries_frame, text="Lista obecności")
                    label.grid(row=2, column=2, padx=5, pady=3, sticky="ew")
                    save_button = tk.Button(entries_frame, text="Wyświetl obecności", command=wyswietl_obecności)
                    save_button.grid(row=2 + len(labels), column=1, pady=5)
                listbox = tk.Listbox(entries_frame)
                listbox.grid(row=3, column=2, rowspan=10, padx=5, pady=3, sticky="nsew")
                entries_frame.grid_columnconfigure(0, weight=0)
                entries_frame.grid_columnconfigure(1, weight=0)
                entries_frame.grid_columnconfigure(2, weight=1)

            zmiana_opcji()
            return
        case "Wystaw zagrożenia":
            save_button = tk.Button(entries_frame, text="Wystaw zagrożenia",command=lambda: Uczeń.wystaw_zagrożenia())
            save_button.grid(row=2, column=1, pady=0)
        case "Wyświetl średnią ucznia":
            labels = ["Imię", "Nazwisko", "Pesel"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=0, padx=5, pady=5, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2+i, column=1, padx=7, pady=10)
                entry_fields.append(entry)

            def wyświetl_średnią():
                srednia = Uczeń.wyświetl_średnią_ucznia(entry_fields)
                srednia_label.config(text=f"{srednia}")

            save_button = tk.Button(entries_frame, text="Wyświetl średnią",
                                    command=lambda: wyświetl_średnią())
            save_button.grid(row=2 + len(labels), column=1, pady=0)

            label = tk.Label(entries_frame, text="Średnia:")
            label.grid(row=3, column=2, padx=5, pady=3, sticky="e")

            srednia_label = tk.Label(entries_frame, text="", relief="sunken", width=10, anchor="e")
            srednia_label.grid(row=3, column=3, padx=5, pady=3, sticky="w")

            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=0)
            entries_frame.grid_columnconfigure(3, weight=0)
            return
        case "Sprawdź status ucznia":
            labels = ["Imię", "Nazwisko", "Pesel"]
            for i in range(len(labels)):
                label = tk.Label(entries_frame, text=labels[i])
                label.grid(row=2 + i, column=0, padx=5, pady=5, sticky="e")
                entry = tk.Entry(entries_frame, width=15)
                entry.grid(row=2 + i, column=1, padx=7, pady=10)
                entry_fields.append(entry)
            def wyświetl_status_ucznia():
                status=Uczeń.czy_zagrożony(entry_fields)
                listbox.delete(0, tk.END)
                if len(status)>0:
                    for i in status:
                        listbox.insert(tk.END, i)

            label = tk.Label(entries_frame, text="Status ucznia")
            label.grid(row=2, column=2, padx=5, pady=3, sticky="ew")
            save_button = tk.Button(entries_frame, text="Wyświetl status ucznia", command=wyświetl_status_ucznia)
            save_button.grid(row=2 + len(labels), column=1, pady=5)
            listbox = tk.Listbox(entries_frame)
            listbox.grid(row=3, column=2, rowspan=10, padx=5, pady=3, sticky="nsew")
            entries_frame.grid_columnconfigure(0, weight=0)
            entries_frame.grid_columnconfigure(1, weight=0)
            entries_frame.grid_columnconfigure(2, weight=1)
            return
        case "Wygeneruj raport z ocen i obecności uczniów":
            save_button = tk.Button(entries_frame, text="Wygeneruj raport", command=lambda: Ocena.generowanie_raportu())
            save_button.grid(row=2, column=1, pady=5)
            return
        case "Generowanie statystyk":
            save_button = tk.Button(entries_frame, text="Pokaz wizualizacje", command=lambda: Ocena.statystyki_wizualizacja())
            save_button.grid(row=2, column=1, pady=5)
            return

#Główny dropdown
selected_option = tk.StringVar(okno_aplikacji)
selected_option.set("Wybierz opcję")
options = ["Dodawanie ucznia",
           "Usuwanie ucznia",
           "Edycja ucznia",
           "Sprawdzanie obecności",
           "Wystawianie oceny",
           "Edycja oceny/obecności danego dnia",
           "Wyświetlenie oceny/obecności danego ucznia",
           "Wyświetl średnią ucznia",
           "Sprawdź status ucznia",
           "Wystaw zagrożenia",
           "Wygeneruj raport z ocen i obecności uczniów",
           "Generowanie statystyk"]
dropdown = tk.OptionMenu(okno_aplikacji, selected_option, *options, command=update_entries)
dropdown.grid(row=0, column=0, columnspan=10,sticky="new",padx=10,pady=10)

okno_aplikacji.mainloop()

#Zapisywanie zmienionych list obiektów do plików (naszej bazy danych) po zamknięciu okna przez użytkownika
lista_plików=["Uczniowie.txt", "Grupy.txt","Oceny.txt","Obecności.txt"]
for i in lista_plików:
    try:
        with open(i, "w", encoding="utf-8") as plik:
            if i == "Uczniowie.txt":
                for uczen in Uczeń.lista_uczniów:
                    plik.write(f"{uczen.imie}\t{uczen.nazwisko}\t{uczen.pesel}\t{uczen.nazwa_grupy}\n")
            elif i == "Grupy.txt":
                for grupa in Grupa.lista_grup:
                    plik.write(f"{grupa.nazwa}\n")
            elif i == "Oceny.txt":
                for ocena in Ocena.lista_ocen:
                    plik.write(f"{ocena.uczeń.pesel}\t{ocena.opis}\t{ocena.data}\t{ocena.wartość}\n")
            elif i == "Obecności.txt":
                for obec in Obecność.lista_obecności:
                    plik.write(f"{obec.uczeń.pesel}\t{obec.data}\t{obec.status}\n")
    except Exception as e:
        print(e)