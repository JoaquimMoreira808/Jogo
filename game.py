from arts import *
from dicts import *
from funcs import *

print(menu_art)

press_to_start = input("")

if press_to_start:
    print("""\n""")
    digitar(4, "Os antigos contam sobre uma coroa de poder arcano infinito,")
    digitar(4, "contam que o objeto habita a última casa do tabuleiro.") 
    digitar(6, "Aqueles corajosos o suficiente mudariam a história,")
    digitar(6, "mas ninguém esperava que o impossível fosse feito por um peão.")

menu_time = True
if menu_time == False:
    menu()

while menu_time:
    menu_time = menu()

    