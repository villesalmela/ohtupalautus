from aly import Aly

class Tekoaly(Aly):
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        self._siirto = (self._siirto + 1) % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"
        
    @staticmethod
    def tulosta_siirto(siirto):
        print(f"Tietokone valitsi: {siirto}")
