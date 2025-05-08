import random
from dicts import *


# ---------- Lista Encadeada para pular o inimigo conforme ser derretado ----------
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

# ---------- Funções de combate ----------
def calcular_dano(forca, defesa):
    dano = forca - defesa
    return max(1, dano)

def batalha(personagem, inimigo):
    fila_turnos = ["jogador", "inimigo"]
    turno_atual = 0

    hp_personagem = personagem["hp"]
    hp_inimigo = inimigo["hp"]

    print(f"\nVocê encontrou: {inimigo['Nome']}!")
    print(personagem["sprite"])

    while hp_personagem > 0 and hp_inimigo > 0:
        print("\n--- TURNO ---")
        if fila_turnos[turno_atual] == "jogador":
            print("🛡️ Sua vez de atacar!")
            dano = calcular_dano(personagem["forca"], inimigo["defesa"])
            hp_inimigo -= dano
            print(f"Você causou {dano} de dano. HP do inimigo: {max(hp_inimigo, 0)}")
        else:
            print("⚔️ Turno do Inimigo!")
            dano = calcular_dano(inimigo["forca"], personagem["defesa"])
            hp_personagem -= dano
            print(f"{inimigo['Nome']} causou {dano} de dano. Seu HP: {max(hp_personagem, 0)}")

        turno_atual = (turno_atual + 1) % len(fila_turnos)

    if hp_personagem > 0:
        print(f"\n✅ Você derrotou o {inimigo['Nome']}!")
        personagem["hp"] = hp_personagem  # Atualiza o HP restante
        return True
    else:
        print(f"\n💀 Você foi derrotado pelo {inimigo['Nome']}...")
        return False

# ---------- Criando filas ----------
fila_inimigos = ListaEncadeada()
for inimigo in inimigos:
    fila_inimigos.adicionar(inimigo)

fila_personagens = ListaEncadeada()
for chave in personagens:
    fila_personagens.adicionar(personagens[chave])

# ---------- Loop principal ----------
personagem_atual = fila_personagens.remover()

while not fila_inimigos.vazia() and personagem_atual:
    inimigo_atual = fila_inimigos.remover()
    venceu = batalha(personagem_atual, inimigo_atual)

    if venceu:
        print("⚔️ Avançando para o próximo inimigo...")
    else:
        personagem_atual = fila_personagens.remover()
        if personagem_atual:
            print("🧍 Próximo aliado entrou na luta!")

# ---------- Resultado final ----------
if fila_inimigos.vazia():
    print("\n🎉 Todos os inimigos foram derrotados! Vitória!")
else:
    print("\n💀 Todos os seus personagens foram derrotados. Derrota!")
