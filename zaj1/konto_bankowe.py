class KontoBankowe:
    def __init__(self, numer_konta, poczatkowy_stan=0):
        self.__numer_konta = numer_konta  # Prywatny atrybut
        self.__stan_konta = poczatkowy_stan  # Prywatny atrybut

    def wplac_pieniadze(self, kwota):
        if kwota > 0:
            self.__stan_konta += kwota
            print(f"Wpłacono {kwota} PLN.")
        else:
            print("Kwota wpłaty musi być większa od zera.")

    def wyplac_pieniadze(self, kwota):
        if 0 < kwota <= self.__stan_konta:
            self.__stan_konta -= kwota
            print(f"Wypłacono {kwota} PLN.")
        else:
            print("Nieprawidłowa kwota wypłaty.")

    def pokaz_stan_konta(self):
        print(f"Stan konta: {self.__stan_konta} PLN.")

# Użycie klasy
konto = KontoBankowe('123456789', 1000)
konto.wplac_pieniadze(500)
konto.wyplac_pieniadze(200)
konto.pokaz_stan_konta()  # Wypisze aktualny stan konta
#