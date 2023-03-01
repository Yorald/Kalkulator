import logging
logging.basicConfig(level=logging.DEBUG)
def kalkulator(number_1, number_2):
    if calculation_text == "1":
        result = number_1 + number_2
        logging.info(f"Dodaję {number_1} i {number_2}")
        return result
    elif calculation_text == "2":
        result = number_1 - number_2
        logging.info(f"Odejmuję {number_1} i {number_2}")
        return result
    elif calculation_text == "3":
        result = number_1*number_2
        logging.info(f"Mnożę {number_1} i {number_2}")
        return result
    elif calculation_text == "4":
        result = number_1/number_2  
        logging.info(f"Dzielę {number_1} i {number_2}")
        return result    
               
if __name__ == "__main__":
    calculation_text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    number_1_text = input("Podaj pierwszy składnik: ")
    number_2_text = input("Podaj drugi składnik: ")
    numero_uno = int(number_1_text)
    numero_dos = int(number_2_text)
    logging.info(f"Dodaję {number_1_text} i {number_2_text}")

    wynik = kalkulator(numero_uno, numero_dos)
    logging.info(f"Wynik to {wynik}")
    

    