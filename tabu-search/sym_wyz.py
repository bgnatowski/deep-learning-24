import math
import random
import matplotlib.pyplot as plt

# Gnatowski Bartosz i Piotr Grochala
# Definiujemy funkcję f(x)
def f(x):
    return 3 * math.sin(math.pi * x / 5) + math.sin(math.pi * x)

# Parametry algorytmu symulowanego wyżarzania
T = 1.0               # Temperatura początkowa
alfa = 0.9            # Współczynnik stygnięcia
epoki = 5             # Liczba epok (warunek stopu)
proby_na_epoke = 3    # Liczba prób w jednej epoce
min_x = 0.0           # Minimalna wartość x
max_x = 10.0          # Maksymalna wartość x

# Inicjalizacja punktu początkowego
aktualne_x = random.uniform(min_x, max_x)
aktualne_f = f(aktualne_x)
najlepsze_x = aktualne_x
najlepsze_f = aktualne_f

print(f"Początkowe x: {aktualne_x:.3f}, f(x): {aktualne_f:.3f}")

for epoka in range(1, epoki + 1):
    print(f"\nEpoka {epoka}, Temperatura: {T:.3f}")
    for proba in range(1, proby_na_epoke + 1):
        # Generujemy nowe rozwiązanie w pobliżu aktualnego x
        delta = 2 * T
        dolny_zakres = max(aktualne_x - delta, min_x)
        gorny_zakres = min(aktualne_x + delta, max_x)
        kandydat_x = random.uniform(dolny_zakres, gorny_zakres)
        kandydat_f = f(kandydat_x)
        delta_f = kandydat_f - aktualne_f

        print(f"Próba {proba}:")
        print(f"  Kandydat x': {kandydat_x:.3f}, f(x'): {kandydat_f:.3f}")

        if kandydat_f > aktualne_f:
            # Akceptujemy nowe rozwiązanie jeśli jest lepsze
            aktualne_x = kandydat_x
            aktualne_f = kandydat_f
            print("  Nowe rozwiązanie jest lepsze. Akceptujemy.")
            if kandydat_f > najlepsze_f:
                najlepsze_x = kandydat_x
                najlepsze_f = kandydat_f
        else:
            # Obliczamy prawdopodobieństwo akceptacji gorszego rozwiązania
            prawdopodobienstwo = math.exp(delta_f / T)
            wartosc_losowa = random.random() # .random() zwraca [0:1]
            print(f"  Nowe rozwiązanie jest gorsze.")
            print(f"  Prawdopodobieństwo akceptacji: {prawdopodobienstwo:.3f}")
            print(f"  Wylosowana wartość: {wartosc_losowa:.3f}")
            if wartosc_losowa < prawdopodobienstwo:
                # Akceptujemy gorsze rozwiązanie z pewnym prawdopodobieństwem
                aktualne_x = kandydat_x
                aktualne_f = kandydat_f
                print("  Akceptujemy gorsze rozwiązanie.")
            else:
                print("  Odrzucamy nowe rozwiązanie.")

    # Zmniejszamy temperaturę
    T *= alfa
    print(f"Temperatura zmniejszona do {T:.3f}")

print(f"\nNajlepsze znalezione rozwiązanie:")
print(f"  x = {najlepsze_x:.3f}")
print(f"  f(x) = {najlepsze_f:.3f}")

# Rysujemy wykres funkcji f(x) z zaznaczonym znalezionym punktem
import numpy as np

x_values = np.linspace(min_x, max_x, 500)
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values, label='f(x)')
plt.plot(najlepsze_x, najlepsze_f, 'ro', label='Najlepsze znalezione rozwiązanie')
plt.title('Wykres funkcji f(x) z zaznaczonym najlepszym rozwiązaniem')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()