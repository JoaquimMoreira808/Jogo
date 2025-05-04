#=================================================================

from arts import * 

#=================================================================

# Delay pra textos: Recomendação usar de 1 a 15 sendo 1 o mais rápido.
# Exemplo: digitar(10, "Olá, mundo!")

def digitar(tempo: int, texto: str):
    def delay(t):
        for i in range(t):
            pass
    for letra in texto:
        print(letra, end='', flush=True)
        delay(tempo * 999999)
    print()

#=================================================================
#Varíavel global pra controle do menu

starts = 0  

#=================================================================

# Menu, é um menu :I

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Seguir caminho")
        print("2. Ver mapa")
        print("3. Gerenciar itens")
        print("4. Gerenciar party")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Você segue pelo caminho misterioso...")
        elif escolha == "2":
            print("Você abre o mapa e observa a região.")
        elif escolha == "3":
            print("Abrindo o inventário de itens...")
        elif escolha == "4":
            print("Gerenciando os membros da party...")
        elif escolha == "0":
            print("Até a próxima, aventureiro!")
            menu1()
        else:
            print("Opção inválida. Tente novamente.")

#=================================================================

def menu1():
    print(menu_art)
    input("")
    if input:
        start()

#=================================================================

def start(): 
    global starts 
    if starts >= 1:
        menu()
    else:
        starts += 1
        print("""\n""")
        digitar(4, "Os antigos contam sobre uma coroa de poder arcano infinito,")
        digitar(4, "contam que o objeto habita a última casa do tabuleiro.") 
        digitar(6, "Aqueles corajosos o suficiente mudariam a história,")
        digitar(6, "mas ninguém esperava que o impossível fosse feito por um peão.")
        menu()

#=================================================================
