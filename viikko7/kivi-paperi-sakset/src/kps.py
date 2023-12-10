from tuomari import Tuomari
from ihmisaly import Ihmisaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from aly import Aly

class KiviPaperiSakset:

    def __init__(self, aly: Aly) -> None:
        self.aly = aly

    @classmethod
    def luo_peli(cls, tyyppi):
        match tyyppi:
            case "a":
                return cls(Ihmisaly())
            case "b":
                return cls(Tekoaly())
            case "c":
                return cls(TekoalyParannettu())
            case _:
                raise ValueError

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto, tokan_siirto = self._kysy_siirrot()
        self.aly.tulosta_siirto(tokan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto, tokan_siirto = self._kysy_siirrot()

            self.aly.tulosta_siirto(tokan_siirto)
            
            if self.aly:
                self.aly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _kysy_siirrot(self):
        eka = input("Ensimmäisen pelaajan siirto: ")
        toka = self.aly.anna_siirto()
        return eka, toka
