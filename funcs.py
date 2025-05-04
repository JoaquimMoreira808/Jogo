#=================================================================

from arts import * 
from dicts import *
from lists import *
import random

#=================================================================

def digitar(texto: str):
    def delay(t):
        for i in range(t):
            pass
    tempo = max(1, (99999999 // len(texto)))  
    for letra in texto:
        print(letra, end='', flush=True)
        delay(tempo)
    print()

#=================================================================
#Varíavel global pra controle do menu

starts = 1
#=================================================================

def continuar():
    input("Pressione qualquer tecla para continuar...")

#=================================================================

# Menu, é um menu :I

def menu():
    while True:
        print("\n╔═══════════════════════════════╗")
        print("║         MENU PRINCIPAL        ║")
        print("╠═══════════════════════════════╣")
        print("║ 1. Seguir caminho             ║")
        print("║ 2. Ver mapa                   ║")
        print("║ 3. Gerenciar itens            ║")
        print("║ 4. Gerenciar party            ║")
        print("║ 0. Sair                       ║")
        print("╚═══════════════════════════════╝")


        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            seguir_caminho()
        elif escolha == "2":
            print("Você abre o mapa e observa a região.")
        elif escolha == "3":
            print("Abrindo o inventário de itens...")
        elif escolha == "4":
            mostrar_party()
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
        digitar("Os antigos contam sobre uma coroa de poder arcano infinito,")
        digitar("contam que o objeto habita a última casa do tabuleiro.") 
        digitar("Aqueles corajosos o suficiente mudariam a história,")
        digitar("mas ninguém esperava que o impossível fosse feito por um peão.")
        menu()

#=================================================================

def mostrar_party():
    sprites = ""
    for nome, info in party.items():
        sprites += f"{info['sprite']}" 
    print("\n" + sprites)

    for nome, info in party.items():
        print(f"{nome} | HP: {info['hp']} | Defesa: {info['defesa']} | Força: {info['forca']}")

    continuar() 

#==================================================================

def acampamento_aventureiros():
    digitar("um acampamento. A fogueira bruxuleia, iluminando")
    digitar("os rostos cansados dos aventureiros.")
    digitar('"Um de nós pode ir com você", diz um deles, com olhos sombrios. Quem você escolhe?')
    continuar()

    personagens_aleatorios = random.sample(list(personagens.items()), 3)

    opcoes = {}
    for i, (nome, info) in enumerate(personagens_aleatorios, 1):
        print(f"\n[{i}] {nome}:")
        print(info["sprite"])
        print(f"HP: {info['hp']}")
        print(f"Defesa: {info['defesa']}")
        print(f"Força: {info['forca']}")
        print("-" * 30)
        opcoes[str(i)] = (nome, info)

    escolha = ""
    while escolha not in opcoes:
        escolha = input("\nEscolha com sabedoria (1, 2 ou 3): ").strip()

    escolhido_nome, escolhido_info = opcoes[escolha]
    party[escolhido_nome] = escolhido_info
    digitar(f"{escolhido_nome} agora faz parte do seu grupo.")
    
    continuar()

#==================================================================

def achar_estrutura():
    estrutura_nome, dados = random.choice(list(estruturas.items()))

    print(dados["sprite"])
    digitar(dados["mensagem"])
    continuar()

    while True:
        print("\n╔═══════════════════════════════╗")
        print("║        O que você faz?        ║")
        print("╠═══════════════════════════════╣")
        print("║ 1. Sair dali                  ║")
        print("║ 2. Explorar estrutura         ║")
        print("╚═══════════════════════════════╝")
        escolha = input("Escolha uma opção (1 ou 2): ").strip()

        if escolha == "1":
            digitar("Você decide não se arriscar e parte em silêncio...")
            break
        elif escolha == "2":
            digitar("Você explora os arredores com cautela...")
            break
        else:
            print("Escolha uma opção válida.")

#==================================================================

acoes = [acampamento_aventureiros, achar_estrutura]
pesos = [1, 3]

def seguir_caminho():
    mensagem = random.choice(inicios_caminho)
    digitar(mensagem)
    evento = random.choices(acoes, weights=pesos, k=1)[0]
    evento()

#==================================================================    

