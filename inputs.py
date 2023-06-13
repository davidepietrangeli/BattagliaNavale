import argparse
import sys


# Metodo che crea l'oggetto 'ArgumentParser' per gestire gli argomenti della riga di comando
def inizializza_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--righe",
                        help="Numero delle righe del campo",
                        type=int,
                        default=9)

    parser.add_argument("-c", "--colonne",
                        help="Numero delle colonne del campo",
                        type=int,
                        default=9)

    parser.add_argument("-s1", "--portaerei",
                        help="Numero della nave Portaerei della flotta, se non specificato, uguale a 1. La lunghezza "
                             "Portaerei è 5.",
                        type=int,
                        default=1)

    parser.add_argument("-s2", "--corazzata",
                        help="Numero della nave Corazzata della flotta, se non specificato, uguale a 1. La lunghezza "
                             "Corazzata è 4.",
                        type=int,
                        default=1)

    parser.add_argument("-s3", "--sottomarino",
                        help="Numero della nave Sottomarino della flotta, se non specificato, uguale a 1. La lunghezza "
                             "Sottomarino è 3.",
                        type=int,
                        default=1)

    parser.add_argument("-s4", "--cacciatorpediniere",
                        help="Numero della nave Cacciatorpediniere della flotta, se non specificato, uguale a 1. La lunghezza "
                             "Cacciatorpediniere è 2.",
                        type=int,
                        default=1)

    parser.add_argument("-s5", "--sommergibile",
                        help="Numero della nave Sommergibile della flotta, se non specificato, uguale a 1. La lunghezza "
                             "Sommergibile è 1.",
                        type=int,
                        default=1)

    parser.add_argument("-o", "--opzioni",
                        help="La variante del gioco che vuoi giocare: 0 se dopo un colpo puoi sparare di nuovo, "
                             "1 altrimenti",
                        type=int,
                        default=0)

    return parser.parse_args()


# Metodo che controlla la validità degli argomenti
def controllo_parser(args):
    try:
        controllo_arguments(args)
    # Se viene sollevata un'eccezione 'ValueError' il programma viene interrotto
    except ValueError:
        sys.exit()


# Metodo che controlla la validità degli argomenti passati, verificando che rientrino in dei range o soddisfino determinate condizioni
def controllo_arguments(args):
    if not 0 < args.righe < 100:
        print('\u001b[31mNumero non valido diInvalid number of rows\033[0m')
        raise ValueError
    if not 0 < args.colonne < 100:
        print('\u001b[31mNumero non valido di colonne\033[0m')
        raise ValueError
    if not 0 <= args.portaerei <= 2:
        print('\u001b[31mNumero non valido di portaerei\033[0m')
        raise ValueError
    if not 0 <= args.corazzata <= 3:
        print('\u001b[31mNumero non valido di corazzata\033[0m')
        raise ValueError
    if not 0 <= args.sottomarino <= 4:
        print('\u001b[31mNumero non valido di sottomarino\033[0m')
        raise ValueError
    if not 0 <= args.cacciatorpediniere <= 5:
        print('\u001b[31mNumero non valido di cacciatorpediniere\033[0m')
        raise ValueError
    if not 0 <= args.sommergibile <= 6:
        print('\u001b[31mNumero non valido di sommergibile\033[0m')
        raise ValueError
    if not (args.opzioni == 0 or args.opzioni == 1):
        print('\u001b[31mInput "opzioni" non valido. Deve essere o 0 o 1\033[0m')
        raise ValueError
