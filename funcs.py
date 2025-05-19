#=================================================================

from arts import * 
from dicts import *
from lists import *
from items import *
import copy
import random
import os
import time

#=================================================================

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#=================================================================

def digitar(texto: str, delay: float = 0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

#=================================================================
#Varíaveis globais

starts = 1

almas = []

bestiario = []

#=================================================================

def continuar():
    input("...")

#=================================================================

def debug():
    while True:
        print("╔════════════════════════════════╗")
        print("║         MENU PRINCIPAL         ║")
        print("╠════════════════════════════════╣")
        print("║ 1. Combate                     ║")
        print("║ 2. Encontrar estrutura         ║")
        print("║ 3. Acampamento                 ║")
        print("║ 0. Menu                        ║")
        print("╚════════════════════════════════╝")


        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            encontrar_inimigo()
        elif escolha == "0":
            menu()
        elif escolha == "2":
            achar_estrutura()
        elif escolha == "3":
            acampamento_aventureiros()  
        else:
            print("Opção inválida. Tente novamente.")

#=================================================================

# Menu, é um menu :I
def menu():
    while True:
        print("\n╔═══════════════════════════════╗")
        print("║         MENU PRINCIPAL        ║")
        print("╠═══════════════════════════════╣")
        print("║ 1. ➤ Seguir o caminho         ║")
        print("║ 2. ➤ Mapa do tabuleiro        ║")
        print("║ 3. ➤ Ver bolsa de itens       ║")
        print("║ 4. ➤ Sua guilda               ║")
        print("║ 5. ➤ Frasco de almas          ║")
        print("║ 6. ➤ Visualizar Bestiario     ║")
        print("║ 0. ➤ Sair                     ║")
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
        elif escolha == "ze":
            debug()
        elif escolha == "0":
            print("Até a próxima, aventureiro!")
            menu1()
        else:
            print("Opção inválida. Tente novamente.")
            continuar()

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
        print("\n")

        digitar("Ahh... meu querido peão.")
        digitar("Ainda moves teus passos na penumbra do início.")
        digitar("A coroa, forjada no silêncio da última casa, espera.")
        digitar("Outros tombaram tentando alcançá-la...")
        digitar("Mas tu, pequeno e esquecido... és a peça que o próprio jogo teme.")
        menu()

#=================================================================

def mostrar_party():
    sprites = ""
    current = head
    while current:
        sprites += current.data['sprite']
        current = current.next
    print("\n" + sprites)

    current = head
    while current:
        p = current.data
        print(f"{p['Nome']} | HP: {p['hp']} | Defesa: {p['defesa']} | Força: {p['forca']}")
        current = current.next

    continuar()


#==================================================================


def mostrar_almas():
    if not almas:
        print("O frasco de almas pulsa... nenhum dos teus caiu no frias garras da escuridão.")
    else:
        sprites = ""
        for personagem in almas:
            sprites += f"{personagem['sprite']}\n"
        print("\n" + sprites)

        for personagem in almas:
            print(f"{personagem['Nome']} | HP: {personagem['hp']} | Defesa: {personagem['defesa']} | Força: {personagem['forca']}")

        continuar()


#==================================================================
def visualizar_bestiario():
       if not bestiario:
        print("Você ainda não derrotou nenhum inimigo.")
       else:
            for inimigos in bestiario:
                print(f"{inimigos['Nome']} | HP: {inimigos['hp']} | Defesa: {inimigos['defesa']} | Força: {inimigos['forca']}")

            continuar()
       

    
    
   

#==================================================================

def gameover():
    global head, tail, almas
    limpar_terminal()
    print(gameover_art)
    continuar()
    head = Node(copy.deepcopy(player))
    tail = head
    almas = []
    menu1()

#==================================================================

import random

def gerar_amuletos():
    atributos_possiveis = ['força', 'resistência', 'vida', 'capacidade']
    escolhidos = random.sample(atributos_possiveis, 2)

    amuleto = {
        'nome': 'Amuleto Misterioso',
        'descricao_curta': f"+{escolhidos[0]} / +{escolhidos[1]}",
        'descricao_longa': f"Este amuleto confere bônus em {escolhidos[0]} e {escolhidos[1]}. Suas origens são incertas, mas emana uma energia ancestral.",
        'atributos': {escolhidos[0]: random.randint(1, 5), escolhidos[1]: random.randint(1, 5)}
    }

    return amuleto

    
#==================================================================

def acampamento_aventureiros():
    global head, tail
    # Recalcula o tail para garantir que aponta ao último nó válido
    tail = obter_ultimo_node(head)

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

    escolhido_original = opcoes[escolha]
    escolhido = copy.deepcopy(escolhido_original)

    tail = add_node(tail, escolhido)

    digitar(f"{escolhido['Nome']} agora faz parte do seu grupo.")
    continuar()


#==================================================================

#Lista encadeada e afins

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

def add_node(tail, personagem):
    novo_node = Node(personagem)
    tail.next = novo_node
    novo_node.prev = tail
    return novo_node

def remover_node(head, node):
    if node.prev:
        node.prev.next = node.next
    else:
        head = node.next
    if node.next:
        node.next.prev = node.prev
    node.prev = None
    node.next = None
    return head


def obter_ultimo_node(head):
    current = head
    while current.next:
        current = current.next
    return current

def tamanho_lista(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def remover_tail(head):
    if head is None:
        return None 
    
    if head.next is None:
        return None
    
    atual = head
    while atual.next:
        atual = atual.next
    
    if atual.prev:
        atual.prev.next = None
    
    return head

#==================================================================

#Definição de party

head = Node(copy.deepcopy(player))
tail = head
#==================================================================

def atacar(atacante, defensor):
    dano = max(atacante.data['forca'] - defensor.data['defesa'], 1)  
    defensor.data['hp'] -= dano
    print(f"{atacante.data['Nome']} ataca {defensor.data['Nome']} e causa {dano} de dano!")

def adicionar_alma(head_almas, node):
    node.next = head_almas
    return node  


def adicionar_bestiario(head_bestiario, node):
    node.next = head_bestiario
    return node  

count = tamanho_lista(head)

def combate(head_player, head_inimigos, almas, bestiario):
    def copiar_lista(head, invertida=False):
        nova_head = None
        atual_original = head
        while atual_original:
            copia_data = dict(atual_original.data)
            novo_node = Node(copia_data)
            if invertida:
                novo_node.next = nova_head
                nova_head = novo_node
            else:
                if nova_head is None:
                    nova_head = novo_node
                    ultimo = novo_node
                else:
                    ultimo.next = novo_node
                    ultimo = novo_node
            atual_original = atual_original.next
        return nova_head

    def morreu(personagem, lista_original):
        if personagem.data.get('amigo', False):
            lista_original = remover_tail(lista_original)
        return lista_original

    combate_player   = copiar_lista(head_player, invertida=True)
    combate_inimigos = copiar_lista(head_inimigos)

    limpar_terminal()
    print("=" * 27)
    print("        Início do Combate       ")
    print("=" * 27)
    print()

    while combate_player and combate_inimigos:
        atacante = combate_player
        defensor = combate_inimigos

        atacar(atacante, defensor)
        if defensor.data['hp'] <= 0:
            print(f"{defensor.data['Nome']} foi derrotado!")
            head_player = morreu(defensor, head_player)

            inimigo_morto = copy.deepcopy(defensor.data)
            inimigo_morto['hp'] = player['hp']
            bestiario.append(inimigo_morto)
            
            combate_inimigos = remover_node(combate_inimigos, defensor)
            continue

        continuar()

        atacar(defensor, atacante)
        continuar()

        if atacante.data['hp'] <= 0:
            print(f"{atacante.data['Nome']} foi derrotado!")
            head_player = morreu(atacante, head_player)

            morto = copy.deepcopy(atacante.data)
            morto['hp'] = player['hp']
            almas.append(morto)

            combate_player = remover_node(combate_player, atacante)
            continue

        limpar_terminal()

        # === Novo bloco de status lado a lado ===
        print("\n--- Status do Combate ---\n")
        players = []
        current = combate_player
        while current:
            players.append(current.data)
            current = current.next

        enemies = []
        current = combate_inimigos
        while current:
            enemies.append(current.data)
            current = current.next

        # Cabeçalhos
        header_p = "Seu grupo"
        header_e = "Inimigos"
        print(f"{header_p:<25}  {header_e}")
        print(f"{'-'*len(header_p):<25}  {'-'*len(header_e)}")

        # Impressão em colunas
        comprimento = max(len(players), len(enemies))
        for i in range(comprimento):
            p = players[i] if i < len(players) else {}
            e = enemies[i] if i < len(enemies) else {}
            nome_p = p.get('Nome', '')
            hp_p   = f"HP: {p.get('hp','')}" if p else ''
            nome_e = e.get('Nome', '')
            hp_e   = f"HP: {e.get('hp','')}" if e else ''
            print(f"{nome_p:<15} {hp_p:<8}    {nome_e:<20} {hp_e}")
        # === Fim do novo bloco ===

        continuar()

    limpar_terminal()
    if not combate_player:
        gameover()
        return

    print("Todos os inimigos foram derrotados. Você venceu o combate!")  
    for _ in range(random.randint(1, 3)):
        inventario.append(gerar_amuletos())

    continuar()

#==================================================================

def achar_estrutura():
    mensagem = random.choice(inicios_caminho)
    estrutura_nome, dados = random.choice(list(estruturas.items()))
    digitar(mensagem)
    digitar(dados["mensagem"])
    print(dados["sprite"])
    continuar()

    while True:
        print("\n╔═══════════════════════════════╗")
        print("║        O que você faz?        ║")
        print("╠═══════════════════════════════╣")
        print("║ 1. Sair dali                  ║")
        print("║ 2. Explorar estrutura         ║")
        print("║ 3. Montar uma fogueira        ║")
        print("╚═══════════════════════════════╝")
        escolha = input("Escolha uma opção (1 ou 2): ").strip()

        #player sai da estrutura
        if escolha == "1":
            digitar("Você decide não se arriscar e parte em silêncio...")
            break

        #player decide explorar a estrutura
        elif escolha == "2":
            digitar("Você explora os arredores com cautela...")
            
            chance = random.choices(["item", "nada"], weights=[70, 30], k=1)[0]
            
            if chance == "item":
                itens = list(itens_possiveis_encontrar.values())
                pesos = [pesos_raridade.get(item.raridade, 1) for item in itens]
                item_encontrado = random.choices(itens, weights=pesos, k=1)[0]
                
                inventario.append(item_encontrado)
                digitar(f"Você encontrou um item: {item_encontrado.nome}!")
                digitar(f"{item_encontrado.descricao_curta}")

                digitar("Você guarda o item com cuidado antes de seguir seu caminho.")
                return

            else:
                digitar("Você vasculha tudo, mas não encontra nada de útil.")
                break

        #player decide monter uma fogueira
        elif escolha == "3":
            digitar ("Você monta uma pequena fogueira com galhos secos ao redor...")
            digitar("O calor do fogo traz um alívio momentâneo do frio da noite.")
            print(fogueira_art)
            break

        else:
            print("Essa opção não parece válida. Tente novamente.")


#==================================================================

def encontrar_inimigo():
    digitar("um sentimento estranho. Algo está vindo.")
    mensagem = random.choice(inimigos_frases)
    digitar(f"\n{mensagem}\n")

    inimigos_disponiveis = inimigos.copy()
    count = tamanho_lista(head)

    primeiro_inimigo = random.choice(inimigos_disponiveis)
    inimigos_disponiveis.remove(primeiro_inimigo)
    head_inimigos = Node(primeiro_inimigo)
    tail_inimigos = head_inimigos

    print(f"{primeiro_inimigo['Nome']}")
    print(f"  HP    : {primeiro_inimigo['hp']}")
    print(f"  Força : {primeiro_inimigo['forca']}")
    print(f"  Defesa: {primeiro_inimigo['defesa']}\n")

    for _ in range(count - 1):
        inimigo_aleatorio = random.choice(inimigos_disponiveis)
        inimigos_disponiveis.remove(inimigo_aleatorio)
        tail_inimigos = add_node(tail_inimigos, inimigo_aleatorio)

        print(f"{inimigo_aleatorio['Nome']}")
        print(f"  HP    : {inimigo_aleatorio['hp']}")
        print(f"  Força : {inimigo_aleatorio['forca']}")
        print(f"  Defesa: {inimigo_aleatorio['defesa']}\n")

    input("\Iniciar o combate...\n")
    limpar_terminal()
    combate(head, head_inimigos, almas, bestiario)


#==================================================================

acoes = [acampamento_aventureiros, achar_estrutura, encontrar_inimigo]
pesos = [1, 1, 1]

def seguir_caminho():
    mensagem = random.choice(inicios_caminho)
    digitar(mensagem)
    evento = random.choices(acoes, weights=pesos, k=1)[0]
    evento()

#==================================================================    
inventario = []

def abrir_inventario():
    if not inventario:
        print("\nSeu inventário está vazio.")
        continuar()
        return

    while True:
        print("\nInventário:")
        for i, item in enumerate(inventario, 1):
            print(f"{i}. {item['nome']} — {item['descricao_curta']}")

        print(f"{len(inventario) + 1}. Voltar")

        escolha = input("\nEscolha um item para ver mais detalhes ou voltar: ")

        if not escolha.isdigit():
            print("Escolha um item válido.")
            continue

        escolha = int(escolha)

        if escolha == len(inventario) + 1:
            break
        elif 1 <= escolha <= len(inventario):
            item_selecionado = inventario[escolha - 1]
            print(f"\n{item_selecionado['nome']} - {item_selecionado['descricao_longa']}")
            input("\nPressione Enter para continuar...")
        else:
            print("Escolha inválida.")

    continuar()

#================================================================== 