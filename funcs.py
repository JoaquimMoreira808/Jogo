#=================================================================

from arts import * 
from dicts import *
from lists import *
from items import *

import random
import os
import time

#=================================================================

def digitar(texto: str, delay: float = 0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
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
        print("║ 5. Mostrar almas perdidas     ║")
        print("║ 6. Visualizar Bestiario       ║")
        print("║ 0. Sair                       ║")
        print("╚═══════════════════════════════╝")


        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            seguir_caminho()
        elif escolha == "2":
            print("Você abre o mapa e observa a região.")
        elif escolha == "3":
            abrir_inventario()  
        elif escolha == "4":
            mostrar_party()
        elif escolha == "5":
            mostrar_almas()
        elif escolha == "6":
            visualizar_bestiario()
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
    for personagem in party: 
        sprites += f"{personagem['sprite']}"  
    print("\n" + sprites)

    for personagem in party:
        print(f"{personagem['Nome']} | HP: {personagem['hp']} | Defesa: {personagem['defesa']} | Força: {personagem['forca']}")

    continuar()


#==================================================================

def mostrar_almas():
    if not almas:
        print("\nNão há nenhuma alma perdida.")
        continuar()
        return
    sprites = ""
    for personagem in almas: 
        sprites += f"{personagem['sprite']}"  
    print("\n" + sprites)

    for personagem in almas:
        print(f"{personagem['Nome']} | HP: {personagem['hp']} | Defesa: {personagem['defesa']} | Força: {personagem['forca']}")

    continuar()


#==================================================================
def visualizar_bestiario():
    if not bestiario:
        print("\nVocê ainda não derrotou nenhum inimigo.")
        continuar()
        return
    
    sprites = ""
    for inimigo in bestiario: 
        sprites += f"{inimigo['sprite']}"  
    print("\n" + sprites)

    for inimigo in bestiario:
        print(f"{inimigo['Nome']} | HP: {inimigo['hp']} | Defesa: {inimigo['defesa']} | Força: {inimigo['forca']}")
    
    continuar()

#==================================================================

import random

def acampamento_aventureiros():
    digitar("um acampamento. A fogueira bruxuleia, iluminando")
    digitar("os rostos cansados dos aventureiros.")
    digitar('"Um de nós pode ir com você", diz um deles, com olhos sombrios. Quem você escolhe?')
    continuar()

    personagens_aleatorios = random.sample(personagens, 3)

    opcoes = {}
    for i, personagem in enumerate(personagens_aleatorios, 1):
        nome = personagem["Nome"]
        print(f"\n[{i}] {nome}:")
        print(personagem["sprite"])
        print(f"HP: {personagem['hp']}")
        print(f"Defesa: {personagem['defesa']}")
        print(f"Força: {personagem['forca']}")
        print("-" * 30)
        opcoes[str(i)] = personagem

    escolha = ""
    while escolha not in opcoes:
        escolha = input("\nEscolha com sabedoria (1, 2 ou 3): ").strip()

    escolhido = opcoes[escolha]
    party.append(escolhido)
    digitar(f"{escolhido['Nome']} agora faz parte do seu grupo.")
    
    continuar()


#==================================================================

#  _____                 _           _       
# /  __ \               | |         | |      
# | /  \/ ___  _ __ ___ | |__   __ _| |_ ___ 
# | |    / _ \| '_ ` _ \| '_ \ / _` | __/ _ \
# | \__/\ (_) | | | | | | |_) | (_| | ||  __/
#  \____/\___/|_| |_| |_|_.__/ \__,_|\__\___|
                                           

# ---------- Funções de batalha ----------
def calcular_dano(forca, defesa):
    dano = forca - defesa
    return max(1, dano)

def batalha(personagem, inimigo):
    fila_turnos = ["jogador", "inimigo"]
    turno_atual = 0

    hp_personagem = personagem["hp"]
    hp_inimigo = inimigo["hp"]

    while hp_personagem > 0 and hp_inimigo > 0:
        if fila_turnos[turno_atual] == "jogador":
            digitar(f"\nVez de {personagem['Nome']} atacar!")
            dano = calcular_dano(personagem["forca"], inimigo["defesa"])
            hp_inimigo -= dano
            digitar(f"{personagem['Nome']} causou {dano} de dano. HP do inimigo: {max(hp_inimigo, 0)}")
        else:
            digitar(f"\n--- TURNO DO INIMIGO ---")
            dano = calcular_dano(inimigo["forca"], personagem["defesa"])
            hp_personagem -= dano
            digitar(f"{inimigo['Nome']} causou {dano} de dano. Seu HP: {max(hp_personagem, 0)}")

        turno_atual = (turno_atual + 1) % len(fila_turnos)
        input("\nPressione Enter para continuar...")

    if hp_personagem > 0:
        digitar(f"\nVocê derrotou {inimigo['Nome']}!")
        personagem["hp"] = hp_personagem 
        return True
    else:
        digitar(f"\n{personagem['Nome']} foi derrotado pelo {inimigo['Nome']}...")
        return False

# ---------- Estrutura de lista encadeada ----------
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        novo_nodo = Nodo(valor)
        if self.fim:
            self.fim.proximo = novo_nodo
        else:
            self.inicio = novo_nodo
        self.fim = novo_nodo

    def remover(self):
        if self.inicio is None:
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return valor

    def vazia(self):
        return self.inicio is None

# ---------- Função de combate geral ----------
def combate(party, inimigos):
    fila_inimigos = ListaEncadeada()
    for inimigo in inimigos:
        fila_inimigos.adicionar(inimigo)

    fila_personagens = ListaEncadeada()
    for personagem in party[::-1]:
        fila_personagens.adicionar(personagem)

    almas = []

    # ---------- Introdução ao combate ----------
    digitar("\nVocê encontrou um grupo de inimigos!")
    digitar("\nSua party:")
    for personagem in party:
        digitar(f"- {personagem['Nome']}")
        if "sprite" in personagem:
            print(personagem["sprite"])

    digitar("\nInimigos:")
    for inimigo in inimigos:
        digitar(f"- {inimigo['Nome']}")
        if "sprite" in inimigo:
            print(inimigo["sprite"])

    input("\nPressione Enter para começar a batalha...")

    # ---------- Loop de combate ----------
    while not fila_inimigos.vazia() and not fila_personagens.vazia():
        personagem_atual = fila_personagens.remover()
        inimigo_atual = fila_inimigos.remover()

        if batalha(personagem_atual, inimigo_atual):
            # Personagem venceu: volta pra fila
            fila_personagens.adicionar(personagem_atual)

            if inimigo_atual not in bestiario:
                bestiario.append(inimigo_atual)
        else:
            # Personagem perdeu: vai pra lista de almas
            digitar(f"\n{personagem_atual['Nome']} foi derrotado. Próximo personagem entra em combate.")
            if personagem_atual in party:
                party.remove(personagem_atual)
            almas.append(personagem_atual)
            
            # Inimigo venceu: volta pra fila
            fila_inimigos.adicionar(inimigo_atual)

    # ---------- Resultado final ----------
    if fila_inimigos.vazia():
        digitar("\nTodos os inimigos foram derrotados! Vitória!")
    elif fila_personagens.vazia():
        os.system('cls' if os.name == 'nt' else 'clear')
        digitar("\nTodos os seus personagens foram derrotados. Derrota!")
        digitar("Acabou pro beta")
                    
#  _____                 _           _       
# /  __ \               | |         | |      
# | /  \/ ___  _ __ ___ | |__   __ _| |_ ___ 
# | |    / _ \| '_ ` _ \| '_ \ / _` | __/ _ \
# | \__/\ (_) | | | | | | |_) | (_| | ||  __/
#  \____/\___/|_| |_| |_|_.__/ \__,_|\__\___|
                                           
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
            
            chance = random.choices(["item", "nada"], weights=[70, 30], k=1)[0]
            
            if chance == "item":
                item_encontrado = random.choice(itens_possiveis)
                inventario.append(item_encontrado)
                digitar(f"Você encontrou um item: {item_encontrado.nome}!")
                digitar(f"{item_encontrado.descricao}")

            else:
                digitar("Você vasculha tudo, mais não encontra nada de útil.")

        else:
            print("Escolha uma opção válida.")


#==================================================================

def encontrar_inimigo():
    party_inimiga = []
    inimigos_disponiveis = inimigos.copy()
    for _ in range(len(party)):
        inimigo_aleatorio = random.choice(inimigos_disponiveis)
        party_inimiga.append(inimigo_aleatorio)
        inimigos_disponiveis.remove(inimigo_aleatorio)
    combate(party, party_inimiga)

#==================================================================

acoes = [acampamento_aventureiros, achar_estrutura, encontrar_inimigo]
pesos = [1, 2, 3]


def seguir_caminho():
    mensagem = random.choice(inicios_caminho)
    digitar(mensagem)
    evento = random.choices(acoes, weights=pesos, k=1)[0]
    evento()

#==================================================================    

inventario = []

itens_possiveis = [
    item("Unguento do Curandeiro", "Cura 15 de HP."),
    item("Frasco de Piche", "Reduz a velocidade do inimigo."),
    item("Pólvora Negra", "Causa 5 de dano ao inimigo."),
    item("Flechas Incendiárias", "Causa dano contínuo leve."),
    item("Mapa Roubado", "Mostra a localização de um acampamento.")
]

def abrir_inventario():
    if not inventario:
        print("\nSeu inventário está vazio.")
        continuar()
        return

    print("\nInventário:")
    for i, item in enumerate(inventario, 1):
        print(f"{i}. {item.nome} — {item.descricao}")

    continuar()

    #================================================================== 