from PIL import Image
import pyautogui
import time
from datetime import datetime, timedelta


def znajdz_obraz(obraz_szukany):
    obraz_screenshot = pyautogui.screenshot()
    obraz_wzorcowy = Image.open(obraz_szukany)
    wynik = pyautogui.locate(obraz_wzorcowy, obraz_screenshot, grayscale=True)
    if wynik is not None:
        return 1
    else:
        return 0


stawka = 20
saldo = 0  # Inicjalizacja salda
placebet_x = 1419  # Współrzędna X przycisku "placebet"
placebet_y = 538  # Współrzędna Y przycisku "placebet"
wager_x = 700  # Współrzędna X przycisku "wager"
wager_y = 331  # Współrzędna Y przycisku "wager"
wpisz_wartosc = 1000  # Wartość do wpisania

licznik_czerwonych = 0
ostatnie_odswiezenie = datetime.now()

while True:
    print("Kliknięto w przycisk 'placebet'")
    pyautogui.click(placebet_x, placebet_y)  # Kliknięcie w przycisk "placebet"
    time.sleep(1)  # Opóźnienie 1 sekundy po kliknięciu
    print(licznik_czerwonych)
    czerwony_obecny = znajdz_obraz('czerwony.png')
    zielony_obecny = znajdz_obraz('zielony.png')

    if czerwony_obecny:
        licznik_czerwonych += 1
        saldo -= stawka
        if licznik_czerwonych == 5:
            wpisz_wartosc5 = 2000
            saldo -= wpisz_wartosc5
            pyautogui.click(wager_x, wager_y)
            pyautogui.click(wager_x, wager_y)
            pyautogui.typewrite(str(wpisz_wartosc5))
            pyautogui.press('enter')
            print("Zmieniono wartość wpisywaną na", wpisz_wartosc5)
        elif licznik_czerwonych == 6:
            licznik_czerwonych = 0
            stawka = 20
            saldo += stawka * 2
            pyautogui.click(wager_x, wager_y)
            pyautogui.click(wager_x, wager_y)
            pyautogui.typewrite(str(stawka))
            pyautogui.press('enter')
            print("Przegrana - Zresetowano stawkę na", stawka)


    elif zielony_obecny:
        licznik_czerwonych = 0
        stawka = 20
        saldo += stawka*2
        pyautogui.click(wager_x, wager_y)
        pyautogui.click(wager_x, wager_y)
        pyautogui.typewrite(str(stawka))
        pyautogui.press('enter')
        print("Zielony - Zresetowano stawkę na", stawka)
        czas_teraz = datetime.now()
        if czas_teraz - ostatnie_odswiezenie >= timedelta(hours=2):
            pyautogui.press('f5')  # Odświeżanie strony
            print("Odświeżono stronę")
            ostatnie_odswiezenie = czas_teraz

    print("Saldo:", saldo)  # Wyświetlanie aktualnego salda
