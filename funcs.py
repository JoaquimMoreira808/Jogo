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

boss1_encounter = False

starts = 1

progressao = 0

almas = []

bestiario = []

RESET = "\033[0m"
BRANCO = "\033[97m"
AZUL = "\033[94m"
VERDE = "\033[92m"
ROXO = "\033[95m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
CINZA = "\033[90m"

#=================================================================

def continuar():
    input(f"{CINZA}Pressione Enter para continuar...{RESET}")

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
        print("║ 4. Progressao                  ║")
        print("║ 5. Dropar amuleto              ║")
        print("║ 0. Menu                        ║")
        print("╚════════════════════════════════╝")

        global progressao
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            encontrar_inimigo()
        elif escolha == "0":
            menu()
        elif escolha == "2":
            achar_estrutura()
        elif escolha == "3":
            acampamento_aventureiros()
        elif escolha == "4":
            num = int(input("Número progressão:"))
            progressao += num
        elif escolha == "5":
            tentar_drop_fragmento()
        else:
            print("Opção inválida. Tente novamente.")

#=================================================================

#MENU PRINCIPAL
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
            ver_mapa()
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

def ver_mapa():
    print(f"Você já seguiu por {progressao} casas.")
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

#HELPPER PARA O SISTEMA DE ITENS E AMULETOS
#Informações dos itens
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
        return getattr(item, 'descricao_curta', 'Item não possui Informações')

def get_descricao_longa(item):
    if isinstance(item, dict):
        return item.get('descricao_longa', 'Sem descrição detalhada.')
    else:
        return getattr(item, 'descricao_longa', 'Sem descrição detalhada.')

#Caracteristicas dos itens
def get_dano(item):
    try:
        if isinstance(item, dict):
            return int(item.get('dano', 0) or 0)
        return int(getattr(item, 'dano', 0) or 0)
    except (ValueError, TypeError):
        return 0

def get_dano_real(item):
    try:
        if isinstance(item, dict):
            return int(item.get('dano_real', 0) or 0)
        return int(getattr(item, 'dano_real', 0) or 0)
    except (ValueError, TypeError):
        return 0

def get_hp(item):
    try:
        if isinstance(item, dict):
            return int(item.get('hp', 0) or 0)
        return int(getattr(item, 'hp', 0) or 0)
    except (ValueError, TypeError):
        return 0
    
def get_defesa(item):
    try:
        if isinstance(item, dict):
            return int(item.get('defesa', 0) or 0)
        return int(getattr(item, 'defesa', 0) or 0)
    except (ValueError, TypeError):
        return 0

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

def menu_fogueira(almas):
    while True:
        print("\n====Fogueira====")
        print("1. Reviver aliado")
        print("2. Montar amuleto")
        print("3. Apagar fogueira")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            reviver_aliados(almas)
        elif escolha == '2':
            novo_amu = montar_amuletos()
            if novo_amu:
                inventario.append(novo_amu)
                aplicar_bonus_amuleto([novo_amu], head, player)
                print("Você montou um amuleto e os atributos foram aplicados aos personagens.")
        elif escolha == '3':
            print("Você apaga a fogueira e se retira.")
            break
        else:
            print("Opção inválida tente novamente.")

#==================================================================

#Amuletos
fragmentos_coletados: set[str] = set()
amuletos_coletados: set[str] = set()

def tentar_drop_fragmento(chance=0.5):
    if random.random() >= chance:
        print("Nenhum fragmento desta vez.")
        return
        

    frag = random.choice(list(fragmentos_catalogo))
    if frag in fragmentos_coletados:
        print(f"Você achou outro {frag}, mas já tem esse.")
    else:
        fragmentos_coletados.add(frag)
        atr = fragmentos_catalogo[frag]["atributo"]
        bonus = fragmentos_catalogo[frag]["bonus"]
        print(f"Você obteve um{frag}! (+{bonus} {atr})")
        inventario.append

#==================================================================

#aplicação de atributos adicionais aos personagens ao montar um amuleto
def aplicar_bonus_amuleto(amuletos, head, player):
    atributo_mapeamento = {
        "força": "forca",
        "resistência": "defesa",
        "vida": "hp"
    }

    for amuleto in amuletos:
        for atributo, bonus in amuleto["atributos"].items():
            if atributo == "capacidade":
                global party_capacidade
                party_capacidade += bonus
            elif atributo in atributo_mapeamento:
                atributo_personagem = atributo_mapeamento[atributo]

                # Aplica o bônus ao player
                player[atributo_personagem] += bonus

                # Aplica o bônus à party
                atual = head
                while atual:
                    atual.data[atributo_personagem] += bonus
                    atual = atual.next

pesos_raridade_dict = dict(pesos_raridade)

#==================================================================

def montar_amuletos():
    disponiveis = [
        nome for nome, info in amuletos_catalogo.items()
        if info["requer"].issubset(fragmentos_coletados)
        and nome not in amuletos_coletados
    ]

    if not disponiveis:
        print("\nVocê não possui fragmentos suficientes para forjar um amuleto.")
        return False
    else:
        print("\nAmuletos disponíveis:")
        for idx, nome in enumerate(disponiveis, 1):
            req = ", ".join(sorted(amuletos_catalogo[nome]["requer"]))
            print(f"{idx}. {nome}  (requer: {req})")

        try:
            escolha = int(input("Escolha o número (0 para cancelar): ")) - 1
            if escolha == -1:
                print("Forja cancelada.")
                return False
            if escolha not in range(len(disponiveis)):
                raise ValueError
        except ValueError:
            print("Escolha inválida.")
            return False

        nome_amuleto = disponiveis[escolha]
        dados = amuletos_catalogo[nome_amuleto]

        fragmentos_coletados.difference_update(dados["requer"])
        amuletos_coletados.add(nome_amuleto)

        amuleto_forjado = {
            "nome": nome_amuleto,
            "fragmentos": list(dados["requer"]),
            "atributos": dados["atributos"]
        }

        print(f"\nForjou {AZUL}**{nome_amuleto}**{RESET}!")
        for atributo, bonus in dados["atributos"].items():
            sinal = "+" if bonus >= 0 else ""
            print(f"   • {atributo}: {sinal}{bonus}")
        print("Todos os aliados sentiram o poder de um novo amuleto!\n")

        return amuleto_forjado

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
#Reviver aliados
def reviver_aliados(almas):
    global head, tail
    tail = obter_ultimo_node(head)

    if not almas:
      print("Não há nenhuma alma para ser restaurada.")
      return
    
    count = 0
    atual = head
    while atual:
        count += 1
        atual = atual.next
    
    if count >= party_capacidade + len(almas):
    
        digitar(f"Seu grupo já tem {party_capacidade} membros. "
            "Você precisa de um Amuleto do Arsenal para recrutar mais aventureiros.")
        continuar()
        return

  
    print("\nRevivendo aliados...")
    while almas:
        
        if count >= 4 and not possui_amuletos_capacidade_extra():
            print("A party está cheia. Não é possível reviver mais aliados sem um Amuleto do Arsenal.")
            break

        personagem = almas.pop(0)
        tail = add_node(tail, personagem)
        count +=1
        print(f"{personagem['Nome']} foi revivido.")
   
    print("Todos os aliados foram revividos.")
#==================================================================

def gameover():
    global head, tail, almas, progressao
    limpar_terminal()
    print(gameover_art)
    continuar()
    head = Node(copy.deepcopy(player))
    tail = head
    almas = []
    progressao = 0
    menu1()


#==================================================================


   

#ACAMPAMENTOS DOS AVENTUREIROS
def possui_amuletos_capacidade_extra():
    for item in inventario:
        if isinstance(item, dict) and "capacidade" in item.get("atributos", {}):
            return True
    return False

def acampamento_aventureiros():
    global head, tail, party_capacidade
    tail = obter_ultimo_node(head)

    count = 0
    atual = head

    while atual:
        count += 1
        atual = atual.next

    digitar("um acampamento. A fogueira bruxuleia, iluminando")
    digitar("os rostos cansados dos aventureiros.")
    digitar('"Um de nós pode ir com você", diz um deles, com olhos sombrios. Quem você escolhe?')
    continuar()

    if count >= party_capacidade:
        digitar(f"Seu grupo já tem {party_capacidade} membros. "
                "Você precisa de um Amuleto do Arsenal para recrutar mais aventureiros.")
        continuar()
        return

   

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
party_capacidade = 4
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
        continuar()
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
        return 0, 0

    escolha = int(escolha)
    if escolha == len(opcoes) + 1:
        return 0, 0  # Cancelou

    if 1 <= escolha <= len(opcoes):
        item, _ = opcoes[escolha - 1]
        print(f"\nVocê usou {AZUL}{get_nome(item)}{RESET}!")

        dano_causado = 0
        dano_real = 0

        if item.hp > 0:
            player_node.data['hp'] += item.hp
            print(f"Você recuperou {VERDE}{item.hp} de HP{RESET}!")
        if item.defesa > 0:
            player_node.data['defesa'] += item.defesa
            print(f"Você aumentou sua {AMARELO}defesa em {item.defesa}{RESET}!")
        if item.dano > 0:
            dano_causado = item.dano
            print(f"{get_nome(item)} causa {VERMELHO}{item.dano} de dano{RESET} no oponente!")
        if item.dano_real > 0:
            dano_real = item.dano_real
            print(F"{get_nome(item)} causa {ROXO}{item.dano_real} de dano real (ignorando a defesa){RESET} no oponente")

        # Remover item do inventário se for consumível
        if get_raridade(item) in ["Comum", "Incomum"]:
            inventario.remove(item)
            print(f"O item {get_nome(item)} foi consumido.")
        else:
            print(f"O item {get_nome(item)} não foi consumido por ser de raridade {get_raridade(item)}.")

        input("Pressione Enter para continuar...")
        return dano_causado, dano_real

    else:
        print("Opção inválida. Tente novamente.")
        return 0, 0

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
    print(f"{VERMELHO}        Início do Combate       {RESET}")
    print("=" * 27)
    print()

    while combate_player and combate_inimigos:
        atacante = combate_player
        defensor = combate_inimigos

        print("Sua vez! O que deseja fazer?")
        print("Enter. Atacar")
        print("1. Usar item")
        escolha = input("Escolha: ")


        #Player ataca com itens, restaura hp ou aumenta a defesa
        if escolha == "1":
            dano_causado, dano_real = usar_item(atacante)

            if dano_real > 0:
                defensor.data['hp'] -= dano_real
                print(f"O inimigo recebeu {dano_real} de dano real (ignora a defesa do oponente)!")

            elif dano_causado > 0:
                if defensor.data['defesa'] >= dano_causado:
                    defensor.data['defesa'] -= dano_causado
                    print(f"{VERMELHO}{defensor.data['Nome']} absorveu o dano com a defesa!{RESET}")
                else:
                    restante = dano_causado - defensor.data['defesa']
                    defensor.data['defesa'] = 0
                    defensor.data['hp'] = restante
                    print(f"{VERMELHO}{defensor.data['Nome']} teve a sua defesa quebrada e perdeu {restante} de HP!{RESET}")
            else:
                print("Você não usou nenhum item ou o item não causou dano.")
                input("Pressione Enter para continuar...")

        #Player ataca
        else:
            forca = atacante.data.get("forca", 0)
            defesa = defensor.data.get("defesa", 0)

            print(f"{AMARELO}{atacante.data['Nome']} ataca {defensor.data['Nome']} causando {forca} de dano!{RESET}")

            if defesa > 0:
                if forca <= defesa:
                    defensor.data['defesa'] -= forca
                    print(f"{AZUL}{defensor.data['Nome']} absorveu o dano com a defesa!{RESET}")
                else:
                    dano_restante = forca - defesa
                    defensor.data['defesa'] = 0
                    defensor.data['hp'] -= dano_restante
                    print(f"{AMARELO}{defensor.data['Nome']} teve a defesa quebrada e perdeu {dano_restante} de HP!{RESET}")
            else:
                defensor.data['hp'] -= forca
                print(f"{AMARELO}{defensor.data['Nome']} não tinha defesa e perdeu {forca} de HP!{RESET}")

            input("Pressione Enter para continuar...")

        # Verifica se inimigo morreu
        if defensor.data['hp'] <= 0:
            print(f"{VERDE}{defensor.data['Nome']} foi derrotado!{RESET}")
            head_player = morreu(defensor, head_player)

            inimigo_morto = copy.deepcopy(defensor.data)
            inimigo_morto['hp'] = player['hp']
            bestiario.append(inimigo_morto)

            combate_inimigos = remover_node(combate_inimigos, defensor)

            tentar_drop_fragmento()


            continuar()
            continue

        #Inimigo ataca
        forca = defensor.data.get("forca", 0)
        defesa = atacante.data.get("defesa", 0)

        print(f"{VERMELHO}{defensor.data['Nome']} ataca {atacante.data['Nome']} causando {forca} de dano!{RESET}")

        if defesa > 0:
            if forca <= defesa:
                atacante.data['defesa'] -= forca
                print(f"{AZUL}{atacante.data['Nome']} absorveu o dano com a defesa!{RESET}")
            else:
                dano_restante = forca - defesa
                atacante.data['defesa'] = 0
                atacante.data['hp'] -= dano_restante
                print(f"{AMARELO}{atacante.data['Nome']} teve a defesa quebrada e perdeu {dano_restante} de HP!{RESET}")
        else:
            atacante.data['hp'] -= forca
            print(f"{VERMELHO}{atacante.data['Nome']} não tinha defesa e perdeu {forca} de HP!{RESET}")

        continuar() 
        
        if atacante.data['hp'] <= 0:
            print(f"{VERMELHO}{atacante.data['Nome']} foi derrotado!{RESET}")
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
        print(f"{header_p:<35}  {header_e}")
        print(f"{'-'*len(header_p):<35}  {'-'*len(header_e)}")

        # Impressão em colunas
        comprimento = max(len(players), len(enemies))
        for i in range(comprimento):
            p = players[i] if i < len(players) else {}
            e = enemies[i] if i < len(enemies) else {}

            #Status player
            nome_p = p.get('Nome', '')
            hp_p   = f"HP: {p.get('hp','')}" if p else ''
            defesa_p    = f"DEF: {p.get('defesa', '')}" if p else ''

            #Status inimigo
            nome_e = e.get('Nome', '')
            hp_e   = f"HP: {e.get('hp','')}" if e else ''
            defesa_e    = f"DEF: {e.get('defesa', '')}" if e else ''

            print(f"{nome_p:<15} {hp_p:<8} {defesa_p:<8}    {nome_e:<20} {hp_e:<8} {defesa_e}")
        # === Fim do novo bloco ===f

        continuar()

    limpar_terminal()
    if not combate_player:
        gameover()
        return

    print("="*30)
    print(f"{VERDE}Você venceu o combate!{RESET}")
    print("="*30) 

    continuar()

#==================================================================

#ESTRUTURA
def achar_estrutura():
    estrutura_nome, dados = random.choice(list(estruturas.items()))
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
                pesos = [pesos_raridade_dict.get(get_raridade(item), 1) for item in itens]
                item_encontrado = random.choices(itens, weights=pesos, k=1)[0]
                
                if item_encontrado.raridade in ["Raro", "Lendário"] and item_encontrado in inventario:
                    digitar(f"Você percebe que ja possui {item_encontrado.nome}, então você decide apenas continuar seu caminho.")
                else:
                    inventario.append(item_encontrado)
                    digitar(f"Você encontrou um item: {item_encontrado.nome}!")
                    digitar(f"{item_encontrado.descricao_curta}")

                    defesa_item = get_defesa(item_encontrado)
                    if get_defesa(item_encontrado) > 0:
                        player["defesa"] += get_defesa(item_encontrado)
                        item_equipado =  item_encontrado
                        digitar(f"A defesa do personagem aumentou em {get_defesa(item_encontrado)} pontos!")

                    else:
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
            menu_fogueira(almas)
            
            
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

def encontrar_inimigo_definido(party_dict):
    if not isinstance(party_dict, list) or not party_dict:
        print("Party inválida.")
        return

    head_inimigos = Node(party_dict[0])
    tail_inimigos = head_inimigos

    print(f"{party_dict[0]['Nome']}")
    print(f"  HP    : {party_dict[0]['hp']}")
    print(f"  Força : {party_dict[0]['forca']}")
    print(f"  Defesa: {party_dict[0]['defesa']}\n")

    for inimigo in party_dict[1:]:
        tail_inimigos = add_node(tail_inimigos, inimigo)
        print(f"{inimigo['Nome']}")
        print(f"  HP    : {inimigo['hp']}")
        print(f"  Força : {inimigo['forca']}")
        print(f"  Defesa: {inimigo['defesa']}\n")

    input("\nIniciar o combate...\n")
    limpar_terminal()
    combate(head, head_inimigos, almas, bestiario)

#==================================================================

#CHANCES DE ENCONTRAR AVENTUREIRO, ESTRUTURAS OU INIMIGOS
acoes = [acampamento_aventureiros, achar_estrutura, encontrar_inimigo]
pesos = [1, 1, 1]

def seguir_caminho():
    mensagem = random.choice(inicios_caminho)
    global progressao
    progressao += 1
    if progressao == 1:
        print("""
=================================
    O Refúgio Dos Esquecidos              
=================================
              """)
        digitar(mensagem)
        acampamento_aventureiros()
    elif progressao == 8:
        boss1()
    elif progressao == 16:
        print("Teste")
    elif progressao == 24:
        print("Teste")
    else:
        digitar(mensagem)
        evento = random.choices(acoes, weights=pesos, k=1)[0]
        evento()

#==================================================================    

#INVENTÁRIO
inventario = []

def abrir_inventario():
    if not inventario and not fragmentos_coletados:
        print("\nSeu inventário está vazio.")
        continuar()
        return

    categorias = {
        "Amuletos": [],
        "Fragmentos Amuletos": [],
        "Consumiveis": [],
        "Equipados": [],
        "Itens de Combate": []
    }

    for item in inventario:
        if isinstance(item, dict):
            categorias["Amuletos"].append(item)
        else:
            hp = get_hp(item)
            defesa = get_defesa(item)
            raridade = get_raridade(item)

            if defesa > 0:
                categorias["Equipados"].append(item)
            elif hp > 0 or raridade in ["Comum", "Incomum"]:
                categorias["Consumiveis"].append(item)
            else:
                categorias["Itens de Combate"].append(item)

    for frag in fragmentos_coletados:
        categorias["Fragmentos Amuletos"].append({
            "nome": f"Fragmento de {frag}",
            "descricao_longa": f"Um fragmento que contém o poder de {frag}. Junte-o a outro para montar um amuleto.",
            "raridade": "Comum"     
        })

    while True:
        print("\n--- Inventário: ---")
        nomes_categorias = list(categorias.keys())
        for idx, nome_cat in enumerate(nomes_categorias, start=1):
            print(f"{idx}. {nome_cat} ({len(categorias[nome_cat])} itens)")
        print("0. Voltar")

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

                print(f"{AZUL}\nNome:{RESET} {get_nome(item_escolhido)}")
                print(f"{AZUL}Descrição:{RESET} {get_descricao_longa(item_escolhido)}")
                print(f"{AZUL}Raridade:{RESET} {get_raridade(item_escolhido)}")

                # Exibir apenas atributos que o item possui
                dano = get_dano(item_escolhido)
                if dano:
                    print(f"{AZUL}Dano:{RESET} {dano}")

                dano_real = get_dano_real(item_escolhido)
                if dano_real:
                    print(f"{AZUL}Dano Real:{RESET} {dano_real}")

                hp = get_hp(item_escolhido)
                if hp:
                    print(f"{AZUL}HP:{RESET} {hp}")

                defesa = get_defesa(item_escolhido)
                if defesa:
                    print(f"{AZUL}Defesa:{RESET} {defesa}")
                continuar()

        except ValueError:
            print("Opção inválida. Tente novamente.")
            continuar()

#================================================================== 

def boss1():
    global boss1_encounter
    if boss1_encounter == True:
        digitar(f"{CINZA}Maegra ergue-se por completo. Sua voz soa como uma catedral desabando:{RESET}")
        digitar(f"{BRANCO}“Tu não passas. É nosso dever não deixar que a história se repita, agora morras, peão.”{RESET}")
        encontrar_inimigo_definido(boss1_party)
    else:
        digitar(f"{CINZA}O chão range como se estivesse suspirando. Três figuras estão imóveis diante dos portões negros.{RESET}\n")
        digitar(f"{CINZA}O jogador se aproxima, revelando duas silhuetas baixas em armaduras partidas, um ao lado do outro.{RESET}\n") 
        digitar(f"{CINZA}Entre eles, uma estrutura colosal de pedra e carne, imóvel como o tempo.{RESET}\n")
        
        digitar(f"{CINZA}O vento sopra. Um sino distante toca. Um sussurro ecoa pela névoa, vindo da Rainha Branca:{RESET}")
        digitar(f"{BRANCO}“Aeli e Tharn, peões, como tu. Maegra, um bastião. Eles não guardam o caminho por ódio,{RESET}") 
        digitar(f"{BRANCO}querido peão... mas por amor a uma velha promessa.”{RESET}\n")
        
        digitar(f"{CINZA}Aeli dá um passo à frente. Seu elmo, partido ao meio, revela um olho ainda aceso.{RESET}")
        digitar(f"{BRANCO}“Entendo sua vontade, peão. A bruxa diz coisas pra você.”{RESET}\n")
        
        digitar(f"{CINZA}Tharn resmunga, sem tirar os olhos do jogador:{RESET}")
        digitar(f"{BRANCO}“Além daqui, apenas ruína, não deixaremos outro experimentá-la.”{RESET}\n")
        
        digitar(f"{CINZA}Maegra ergue-se por completo. Sua voz soa como uma catedral desabando:{RESET}")
        digitar(f"{BRANCO}“Tu não passas. É nosso dever não deixar que a história se repita, agora morras, peão.”{RESET}")

        digitar("Prepare-se para enfrentar:")
        print(boss1_art)
        boss1_encounter = True
        encontrar_inimigo_definido(boss1_party)


#================================================================== 
