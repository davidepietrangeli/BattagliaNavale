# Funzione che controlla se la stringa 'orientamento' specificata è valida
def controllo_orientamento(orientamento):
    if orientamento == 'o' or orientamento == 'v':
        return True
    else:
        return False


# Funzione che verifica se un punto di partenza specificato è valido all'interno di una griglia di dimensioni date
def controlla_punto_partenza(righe, colonne, riga_partenza, colonna_partenza):
    if riga_partenza <= righe and colonna_partenza <= colonne:
        return True
    else:
        return False


# Parametri: il numero di navi desiderato per ogni tipologia
# Funzione che sfrutta un ciclo while per aggiungere i tipi di nave alla lista 'tipo_lista'
# Restituisco la lista 'tipo_lista' contenente i tipi di nave corrispondenti alle quantità specificate
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


# Funzione che permette all'utente di inserire la riga e la colonna dove si desidera sparare all'interno del campo di battaglia
# Funzione che mi restituisce una tupla contenente le coordinate di sparo
def scegli_controlla_punto_sparo(righe, colonne, campo_battaglia):
    error = True
    while error:
        try:
            # Inserimento di riga e colonna che associo all'attributo 'input_val'
            input_val = input(f'\nInserisci riga e colonna dove sparare (es: 3 1): ')
            # Funzione 'map' che mi separa i due valori di 'input_val' e me li salva nell'attributo 'riga_partenza' e 'colonna_partenza'
            riga_sparo, colonna_sparo = map(int, input_val.split())
            # Verifico che il punto di sparo è interno al campo di gioco chiamando la funzione 'controlla_punto_partenza'
            if not (controlla_punto_partenza(righe, colonne, riga_sparo, colonna_sparo)):
                print("\u001b[31mIl punto non è dentro il campo, riprova!\033[0m")
            # Controllo se il carattere in quel punto del campo è diverso da '-'
            elif not (campo_battaglia[riga_sparo - 1][colonna_sparo - 1] == '-'):
                print("\u001b[31mHai già sparato in questo punto, riprova!\033[0m")
            else:
                error = False
        except ValueError:
            print("\u001b[31mInserimento non valido, per favore riprova!\033[0m")
    return riga_sparo, colonna_sparo


# Funzione che stampa un messaggio specifico in base al valore dell'argomento 'i'
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
