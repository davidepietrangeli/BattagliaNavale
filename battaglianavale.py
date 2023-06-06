# @author PIETRANGELI DAVIDE:
import os
import campo
import inputs
import giocatore
import utile


args = inputs.inizializza_parser()
inputs.controllo_parser(args)

tipo_lista = utile.crea_nave_tipo_lista(args.portaerei, args.corazzata, args.sottomarino, args.cacciatorpediniere, args.sommergibile)

campo_giocatore1, lista_navi1 = campo.crea_campo(args.righe, args.colonne, tipo_lista)
input('\n\nPremi INVIO e passa il computer al prossimo giocatore:')
os.system('cls' if os.name == 'nt' else 'clear')

campo_giocatore2, lista_navi2 = campo.crea_campo(args.righe, args.colonne, tipo_lista)
input('\n\nPremi INVIO e passa il computer al prossimo giocatore per iniziare il gioco:')
os.system('cls' if os.name == 'nt' else 'clear')

campo_battaglia1 = [['-'] * args.colonne for x in range(args.righe)]
campo_battaglia2 = [['-'] * args.colonne for x in range(args.righe)]
giocatore.inizio_gioco(lista_navi1, lista_navi2, args.righe, args.colonne, args.opzioni, campo_battaglia1, campo_battaglia2)
