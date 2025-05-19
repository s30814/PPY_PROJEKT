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


#
# class Ocena:
#     Uczen
#     Opis
#     Data
#
#
# class Obecnosc:
#     Uczen
#     Data
#     Status