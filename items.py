import random
from dicts import *

class item:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def usar(self, usuario, alvo):
        print(f"{player.nome} usou {self.nome} em {alvo.nome}!")
        

# ==========================
# Itens
# ==========================


frasco_piche = item(
    "Frasco de Piche",
    "Um frasco de piche pegajoso. Reduz temporariamente a velocidade do inimigo." \
    "Durante cercos, óleo fervente ou piche eram usados para atrasar inimigos."
)

unguento_curandeiro = item(
    "Unguento do Curandeiro",
    "Pomada medicinal usada em batalhas medievais. Restaura um pouco de HP." \
    "Curandeiros usavam pomadas à base de ervas para tratar ferimentos."
)

polvora_negra = item(
    "Pólvora Negra",
    "Uma pequena carga de pólvora instável. Causa dano leve em todos os inimigos." \
    "No fim da era medieval, a pólvora começou a ser usada em armas de cerco e explosivos."
)