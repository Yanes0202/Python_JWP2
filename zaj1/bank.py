class Bank:
    def __init__(self):
        self.__konta = {}

    def utworzKonto(self):
        nowy_numer = list(self.__konta.keys())[-1] + 1 if self.__konta else 0
        self.__konta[nowy_numer] = 0
        return nowy_numer

    def wplac(self, nrKonta, kwota):
        if nrKonta in self.__konta:
            self.__konta[nrKonta] = kwota
            print(f"Masz na koncie {self.__konta[nrKonta]}")
        else:
            print("Nie ma takiego konta!!!")
    def sprawdzKonta(self):
        print(self.__konta)

bank = Bank()
nrKonta = bank.utworzKonto()
bank.wplac(nrKonta, 1000)
bank.sprawdzKonta()