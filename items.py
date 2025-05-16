import random
from dicts import *

class Item:
    def __init__(self, nome, descricao_curta, descricao_longa, raridade="Comum"):
        self.nome = nome
        self.descricao_curta = descricao_curta
        self.descricao_longa = descricao_longa
        self.raridade = raridade

    def __repr__(self):
        return f"<Item: {self.nome} (Raridade: {self.raridade})>"
        

# ==========================
# Itens
# ==========================

#Descrição dos Itens
frasco_piche = Item(
    "Frasco de Piche",
    "Reduz temporariamente a velocidade do inimigo. ",
    "Um frasco de piche pegajoso. Durante cercos, óleo fervente ou piche eram usados para atrasar inimigos.",
    raridade="Comum"
)

unguento_curandeiro = Item(
    "Unguento do Curandeiro",
    "Restaura um pouco de HP. ",
    "Pomada medicinal usada em batalhas medievais. Curandeiros utilizavam ervas naturais para tratar ferimentos.",
    raridade="Incomum"
)

polvora_negra = Item(
    "Pólvora Negra",
    "Causa dano leve em todos os inimigos. " ,
    "Uma pequena carga de pólvora instável. No fim da era medieval, a pólvora começou a ser usada em armas de cerco.",
    raridade="Incomum"
)

flechas_incendiarias = Item(
    "Flechas Incendiárias",
    "Causam dano contínuo leve. ",
    "Flechas mergulhadas em óleo e incendiadas eram usadas para causar caos em campos e construções inimigas.",
    raridade="Raro"
)

espada_rei_caido = Item(
    "Espada do Rei Caído",
    "Espada lendária que causa 30 de dano e ignora armadura.",
    "A Espada do Rei Caído pertenceu a um antigo monarca que enlouqueceu durante a guerra.\n"
    "Forjada com aço negro e encantada por um feiticeiro traidor, ela foi selada após destruir um exército inteiro.\n"
    "Diz-se que 'Sua lâmina carrega o lamento das almas que tombaram diante dela.'",
    raridade="Lendário"
)

#raridade dos itens

pesos_raridade = {
    "Comum": 60,
    "Incomum": 30,
    "Raro": 7,
    "Lendário": 3
}

# Dicionário dos itens
itens_possiveis_encontrar = {
    "frasco_piche": frasco_piche,
    "unguento_curandeiro": unguento_curandeiro,
    "polvora_negra": polvora_negra,
    "flechas_incendiarias": flechas_incendiarias,
    "espada_rei_caido": espada_rei_caido,
}