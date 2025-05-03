
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
            return False
            break
        else:
            print("Opção inválida. Tente novamente.")


#=================================================================
