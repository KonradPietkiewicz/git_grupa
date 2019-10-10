import requests
import os

URL_FILE = 'https://s3.zylowski.net/public/input/2aa1.txt'

def download_txt():
    r = requests.get(URL_FILE)
    if r.status_code == 200:
        with open('file.txt', 'wb') as f:
            f.write(r.content)
        return 'Sukces! Pomyślnie pobrano plik.'
    else:
        return 'Nie ma plik .txt w takim URL: {}'.format(URL_FILE)

def count_punctuation():

    with open('file.txt', 'r') as f:
        counter = 0
        for letter in f.read():
            if letter in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
                counter += 1
    return counter


def count_sentences():
    with open('file.txt', 'r') as f:
        counter = 0
        for sentence in f.read():
            if sentence in '.?!':
                counter += 1
    return counter


def count_letters():
    with open('file.txt', 'r') as f:
        counter = 0
        for letter in f.read():
            if letter.isalpha():
                counter += 1
    return counter


def generate_raport():
    with open('statystyki.txt', 'w') as file:
        lines = [
            'Liczba liter: {}'.format(count_letters()),
            'Liczba wyrazów: {}'.format(count_words()),
            'Liczba znaków interpunkcyjnych: {}'.format(count_punctuation()),
            'Liczba zdań: {}'.format(count_sentences()),
            ]
        file.write('===STATYSTYKI===\n' + '\n'.join(lines))


def count_words():
    with open('file.txt', 'r') as f:
        counter = 0
        for word in f.read().split():
            counter += 1
    return counter

def exit():

    if os.path.exists("file.txt"):
        os.remove("file.txt")
    if os.path.exists("statystyki.txt"):
        os.remove("statystyki.txt")


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
        print(download_txt())
    elif prompt == '2':
        print('2. Zlicz liczbę liter w pobranym pliku')
    elif prompt == '3':
        print('3. Zlicz liczbę wyrazów w pliku')
        count_words()
    elif prompt == '4':
        print('4. Zlicz liczbę znaków interpunkcyjnych w pliku')
        print(count_punctuation())
    elif prompt == '5':
        print('5. Zlicz liczbę zdań w pliku')
        print(count_sentences())
    elif prompt == '6':
        print('6. Wygeneruj raport o użyciu liter (A-Z)')
        generate_raport()
    elif prompt == '7':
        print('7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt')
    elif prompt == '8':
        exit()
        break
    else:
        print('Niepoprawna wartość. Wybierz opcje 1-8.')
