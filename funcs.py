#=================================================================

from arts import * 
from dicts import *
from lists import *
from items import *
import copy
import random
import os
import time
from collections import defaultdict

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
#MENU DE DEBUG
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

# MENU PRINCIPAL
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

#HELPER PARA O SISTEMA DE ITENS E AMULETOS
def get_nome(item):
    if isinstance(item, dict):
        return item.get('nome', 'Item Desconhecido')
    else:
        return getattr(item, 'nome', 'Item Desconhecido')
    
def get_raridade(item):
    if isinstance(item, dict):
        return item.get('raridade', 'Comum')
    else:
        return getattr(item, 'raridade', 'Comum')
    
def get_descricao_curta(item):
    if isinstance(item, dict):
        return item.get('descricao_curta', 'Item não possui Informações')
    else:
        return getattr(item, 'nome', 'Item não possui Informações')

def get_descricao_longa(item):
    if isinstance(item, dict):
        return item.get('descricao_longa', 'Sem descrição detalhada.')
    else:
        return getattr(item, 'descricao_longa', 'Sem descrição detalhada.')

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

#BESTÁRIO
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

#GERADOR DE AMULETOS
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

#ACAMPAMENTOS DOS AVENTUREIROS
def acampamento_aventureiros():
    global head, tail
    tail = obter_ultimo_node(head)

    digitar("um acampamento. A fogueira bruxuleia, iluminando")
    digitar("os rostos cansados dos aventureiros.")
    digitar('"Um de nós pode ir com você", diz um deles, com olhos sombrios. Quem você escolhe?')
    continuar()

    personagens_aleatorios = random.sample(personagens, 3)
    opcoes = {}

    nomes_linha = [f"[{i+1}] {p['Nome']}".ljust(25) for i, p in enumerate(personagens_aleatorios)]
    print("\n" + "   ".join(nomes_linha))

    sprites_linhas = [p["sprite"].split("\n") for p in personagens_aleatorios]
    max_linhas_sprite = max(len(sprite) for sprite in sprites_linhas)

    for i in range(max_linhas_sprite):
        linha = []
        for sprite in sprites_linhas:
            if i < len(sprite):
                linha.append(sprite[i].ljust(25))
            else:
                linha.append(" " * 25)
        print("   ".join(linha))

    atributos = ["hp", "defesa", "forca"]
    for atributo in atributos:
        linha = []
        for p in personagens_aleatorios:
            valor = f"{atributo.capitalize()}: {p[atributo]}"
            linha.append(valor.ljust(25))
        print("   ".join(linha))

    print("-" * 80)

    for i, personagem in enumerate(personagens_aleatorios, 1):
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

#AÇÕES DO GAME
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


def usar_item(player_node):
    if not inventario:
        print("Você não tem itens no inventário para usar.")
        input("Pressione Enter para continuar...")
        return 0

    print("\nItens no inventário:")

    # Organiza os consumíveis por nome e conta
    contagem_consumiveis = defaultdict(int)
    itens_por_nome = {}
    for item in inventario:
        if get_raridade(item) in ["Comum", "Incomum"]:
            contagem_consumiveis[get_nome(item)] += 1
            itens_por_nome[get_nome(item)] = item  # Armazena um exemplo do item
        elif get_raridade(item) in ["Lendário"]:
            continue
        else:
            Exception("Erro Desconhecido")
            
    # Lista de itens únicos para seleção
    opcoes = []

    # Adiciona consumíveis agrupados
    for nome, qtd in contagem_consumiveis.items():
        item = itens_por_nome[nome]
        opcoes.append((item, qtd))

    # Adiciona itens não consumíveis individualmente
    for item in inventario:
        if get_raridade(item) not in ["Comum", "Incomum"]:
            opcoes.append((item, 1))
        elif get_raridade(item) in ["Lendário"]:
            continue
        else:
            Exception("Erro Desconhecido")

    # Exibe itens com quantidade
    for i, (item, qtd) in enumerate(opcoes, 1):
        qtd_str = f" ({qtd}x)" if qtd > 1 else ""
        print(f"{i}. {get_nome(item)}{qtd_str} (Raridade: {get_raridade(item)}) - {get_descricao_curta(item)}")

    print(f"{len(opcoes)+1}. Cancelar")
    escolha = input("Escolha um item para usar: ")

    if not escolha.isdigit():
        print("Opção inválida. Tente novamente.")
        return 0

    escolha = int(escolha)
    if escolha == len(opcoes) + 1:
        return 0  # Cancelou

    if 1 <= escolha <= len(opcoes):
        item, _ = opcoes[escolha - 1]
        print(f"\nVocê usou {get_nome(item)}!")

        dano_causado = 0

        if item.hp > 0:
            player_node.data['hp'] += item.hp
            print(f"Você recuperou {item.hp} de HP!")
        if item.defesa > 0:
            player_node.data['defesa'] += item.defesa
            print(f"Sua defesa aumentou em {item.defesa}!")
        if item.dano > 0:
            dano_causado = item.dano
            print(f"{get_nome(item)} causa {item.dano} de dano no inimigo!")

        # Remover item do inventário se for consumível
        if get_raridade(item) in ["Comum", "Incomum"]:
            inventario.remove(item)
            print(f"O item {get_nome(item)} foi consumido.")
        else:
            print(f"O item {get_nome(item)} não foi consumido por ser de raridade {get_raridade(item)}.")

        input("Pressione Enter para continuar...")
        return dano_causado

    else:
        print("Opção inválida. Tente novamente.")
        return 0

count = tamanho_lista(head)

#COMBATE
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

        print("Sua vez! O que deseja fazer?")
        print("1. Atacar")
        print("2. Usar item")
        escolha = input("Escolha: ")

        if escolha == "1":
            atacar(atacante, defensor)

        elif escolha == "2":
            dano_extra = usar_item(atacante)
            if dano_extra > 0:
                defensor.data['hp'] -= dano_extra
                print(f"O inimigo recebeu {dano_extra} de dano pelo item!")
            else:
                print("Você não usou nenhum item ou o item não causou dano.")
                input("Pressione Enter para continuar...")

        else:
            print("Opção inválida, você perde o turno.")
            input("Pressione Enter para continuar...")

        # Verifica se inimigo morreu
        if defensor.data['hp'] <= 0:
            print(f"{defensor.data['Nome']} foi derrotado!")
            head_player = morreu(defensor, head_player)

            inimigo_morto = copy.deepcopy(defensor.data)
            inimigo_morto['hp'] = player['hp']
            bestiario.append(inimigo_morto)

            combate_inimigos = remover_node(combate_inimigos, defensor)
            continuar()
        

        continuar()

        atacar(defensor, atacante)
        if atacante.data['hp'] <= 0:
            print(f"{atacante.data['Nome']} foi derrotado!")
            head_player = morreu(atacante, head_player)

            morto = copy.deepcopy(atacante.data)
            morto['hp'] = player['hp']
            almas.append(morto)

            combate_player = remover_node(combate_player, atacante)
            continuar()


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

#ESTRUTURA
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
        escolha = input("Escolha uma opção (1, 2 ou 3): ").strip()

        #player sai da estrutura
        if escolha == "1":
            digitar("Você decide não se arriscar e parte em silêncio...")
            break

        #player decide explorar a estrutura
        elif escolha == "2":
            digitar("Você explora os arredores com cautela...")
            
            chance = random.choices(["item", "nada"], weights=[80, 20], k=1)[0]
            
            if chance == "item":
                itens = list(itens_possiveis_encontrar.values())
                pesos = [pesos_raridade.get(get_raridade(item), 1) for item in itens]
                item_encontrado = random.choices(itens, weights=pesos, k=1)[0]
                
                if item_encontrado.raridade in ["Raro", "Lendário"] and item_encontrado in inventario:
                    digitar(f"Você percebe que ja possui {item_encontrado.nome}, então você decide apenas continuar seu caminho.")
                else:
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
            print("Opção inválida. Tente novamente.")


#==================================================================

#INIMIGOS
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

#CHANCES DE ENCONTRAR AVENTUREIRO, ESTRUTURAS OU INIMIGOS
acoes = [acampamento_aventureiros, achar_estrutura, encontrar_inimigo]
pesos = [1, 1, 1]

def seguir_caminho():
    mensagem = random.choice(inicios_caminho)
    digitar(mensagem)
    evento = random.choices(acoes, weights=pesos, k=1)[0]
    evento()

#==================================================================    

#INVENTÁRIO
inventario = []

def abrir_inventario():
    if not inventario:
        print("\nSeu inventário está vazio.")
        continuar()
        return

    categorias = {
        "Amuletos": [],
        "Consumiveis": [],
        "Itens de Combate": []
    }

    for item in inventario:
        if isinstance(item, dict):
            categorias["Amuletos"].append(item)
        else:
            raridade = get_raridade(item)
            if raridade in ["Comum", "Incomum"]:
                categorias["Consumiveis"].append(item)
            else:
                categorias["Itens de Combate"].append(item)

    while True:
        print("\n--- Inventário: ---")
        nomes_categorias = list(categorias.keys())
        for idx, nome_cat in enumerate(nomes_categorias, start=1):
            print(f"{idx}. {nome_cat} ({len(categorias[nome_cat])} itens)")

        try:
            escolha_cat = int(input("\nEscolha uma categoria para ver os itens (0 para voltar): "))
            if escolha_cat == 0:
                continuar()
                return
            if not (1 <= escolha_cat <= len(nomes_categorias)):
                print("Categoria inválida.")
                continuar()
                return

            categoria_escolhida = nomes_categorias[escolha_cat - 1]
            itens = categorias[categoria_escolhida]

            if not itens:
                print("Essa categoria está vazia.")
                continuar()
                return

            contagem = {}
            lista_itens = []
            for item in itens:
                chave = item['nome'] if isinstance(item, dict) else item.nome
                if chave not in contagem:
                    contagem[chave] = {"quantidade": 1, "item": item}
                    lista_itens.append(item)
                else:
                    contagem[chave]["quantidade"] += 1

            while True:
                print(f"\n--- {categoria_escolhida} ---")
                for i, item in enumerate(lista_itens, start=1):
                    nome = get_nome(item)
                    print(f"{i}. {nome} x{contagem[nome]['quantidade']}")

                escolha_item = int(input("\nEscolha um item para inspecionar (0 para voltar): "))
                if escolha_item == 0:
                    break
                if not (1 <= escolha_item <= len(lista_itens)):
                    print("Item inválido.")
                    continuar()
                    break

                item_escolhido = lista_itens[escolha_item - 1]

                print(f"\nNome: {get_nome(item_escolhido)}")
                print(f"Descrição: {get_descricao_longa(item_escolhido)}")
                print(f"Raridade: {get_raridade(item_escolhido)}")
                input("\nPressione Enter para voltar à lista de itens.")

        except ValueError:
            print("Opção inválida. Tente novamente.")
            continuar()

#================================================================== 