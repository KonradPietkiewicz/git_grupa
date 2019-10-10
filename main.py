while True:
    print("""
    1. Pobierz plik z internetu
    2. Zlicz liczbę liter w pobranym pliku
    3. Zlicz liczbę wyrazów w pliku
    4. Zlicz liczbę znaków interpunkcyjnych w pliku
    5. Zlicz liczbę zdań w pliku
    6. Wygeneruj raport o użyciu liter (A-Z)
    7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt
    8. Wyjście z programu
    """)

    prompt = input('Wybierz opcje: ')

    if prompt == '1':
        print("1. Pobierz plik z internetu")
    elif prompt == '2':
        print('2. Zlicz liczbę liter w pobranym pliku')
    elif prompt == '3':
        print('3. Zlicz liczbę wyrazów w pliku')
    elif prompt == '4':
        print('4. Zlicz liczbę znaków interpunkcyjnych w pliku')
    elif prompt == '5':
        print('5. Zlicz liczbę zdań w pliku')
    elif prompt == '6':
        print('6. Wygeneruj raport o użyciu liter (A-Z)')
    elif prompt == '7':
        print('7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt')
    elif prompt == '8':
        break
    else:
        print('Niepoprawna wartość. Wybierz opcje 1-8.')
