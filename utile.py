def controllo_orientamento(orientamento):
    if orientamento == 'orizzontale' or orientamento == 'verticale':
        return True
    else:
        return False


def controlla_punto_partenza(righe, colonne, riga_partenza, colonna_partenza):
    if riga_partenza <= righe and colonna_partenza <= colonne:
        return True
    else:
        return False


def crea_nave_tipo_lista(portaerei, corazzata, sottomarino, cacciatorpediniere, sommergibile):
    tipo_lista = []
    contatore = 0
    while contatore < portaerei:
        nuovo = 5
        tipo_lista.append(nuovo)
        contatore += 1
    while contatore < portaerei + corazzata:
        nuovo = 4
        tipo_lista.append(nuovo)
        contatore += 1
    while contatore < portaerei + corazzata + sottomarino:
        nuovo = 3
        tipo_lista.append(nuovo)
        contatore += 1
    while contatore < portaerei + corazzata + sottomarino + cacciatorpediniere:
        nuovo = 2
        tipo_lista.append(nuovo)
        contatore += 1
    while contatore < portaerei + corazzata + sottomarino + cacciatorpediniere + sommergibile:
        nuovo = 1
        tipo_lista.append(nuovo)
        contatore += 1
    return tipo_lista


def scegli_controlla_punto_sparo(righe, colonne, campo_battaglia):
    error = True
    while error:
        try:
            riga_sparo = int(input("sparo_riga:\n"))
            colonna_sparo = int(input("sparo_colonna:\n"))
            if not (controlla_punto_partenza(righe, colonne, riga_sparo, colonna_sparo)):
                print("\u001b[31mIl punto non è dentro il campo, riprova!\033[0m")
            elif not (campo_battaglia[riga_sparo - 1][colonna_sparo - 1] == '-'):
                print("\u001b[31mHai già sparato in questo punto, riprova!\033[0m")
            else:
                error = False
        except ValueError:
            print("\u001b[31mInserimento non valido, per favore riprova!\033[0m")
    return riga_sparo, colonna_sparo


def messaggio_utente(i):
    if i == 5:
        print(f'\nFornisci coordinate ed orientamento della nave portaerei che è lunga 5!')
    elif i == 4:
        print(f'\nFornisci coordinate ed orientamento della nave corazzata che è lunga 4!')
    elif i == 3:
        print(f'\nFornisci coordinate ed orientamento della nave sottomarino che è lunga 3!')
    elif i == 2:
        print(f'\nFornisci coordinate ed orientamento della nave cacciatorpediniere che è lunga 2!')
    elif i == 1:
        print(f'\nFornisci coordinate ed orientamento della nave sommergibile che è lunga 1!')
