## Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
import decimal
import numpy as np
from decimal import Decimal

F = Decimal(input("unesite iznos sile: "))
m = Decimal(input("Unesite masu: "))

