from kps import KiviPaperiSakset

OHJEET = "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus not in ["a", "b", "c"]:
            break

        print(OHJEET)
        peli = KiviPaperiSakset.luo_peli(vastaus)
        peli.pelaa()

if __name__ == "__main__":
    main()
