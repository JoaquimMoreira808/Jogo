
from dicts import *  
from funcs import *  

# ---------- Funções de combate ----------
def calcular_dano(forca, defesa):
    dano = forca - defesa
    return max(1, dano)

def batalha(personagem, inimigo):
    fila_turnos = ["jogador", "inimigo"]
    turno_atual = 0

    hp_personagem = personagem["hp"]
    hp_inimigo = inimigo["hp"]

    print(f"\n{personagem['Nome']} encontrou: {inimigo['Nome']}!")
    print(personagem["sprite"])

    while hp_personagem > 0 and hp_inimigo > 0:
        print("\n--- TURNO ---")
        if fila_turnos[turno_atual] == "jogador":
            print(f"\n Vez de {personagem['Nome']} atacar!")
            dano = calcular_dano(personagem["forca"], inimigo["defesa"])
            hp_inimigo -= dano
            print(f"{personagem['Nome']} causou {dano} de dano. HP do inimigo: {max(hp_inimigo, 0)}")
        else:
            print("Turno do Inimigo!")
            dano = calcular_dano(inimigo["forca"], personagem["defesa"])
            hp_personagem -= dano
            print(f"{inimigo['Nome']} causou {dano} de dano. Seu HP: {max(hp_personagem, 0)}")

        turno_atual = (turno_atual + 1) % len(fila_turnos)

    if hp_personagem > 0:
        print(f"\nVocê derrotou  {inimigo['Nome']}!")
        personagem["hp"] = hp_personagem  # Atualiza HP restante
        return True
    else:
        print(f"\n {personagem['Nome']} foi derrotado pelo {inimigo['Nome']}...")
        return False

#filas encadeada para revezamento de personagens e inimigos
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

# ---------- fila de personagens e inimigos puxando a lista encadeada ----------
fila_inimigos = ListaEncadeada()
for inimigo in inimigos:
    fila_inimigos.adicionar(inimigo)

fila_personagens = ListaEncadeada()
for personagem in personagens:  
    fila_personagens.adicionar(personagem)

# ---------- Loop principal ----------
# ---------- Loop principal ----------

personagem_atual = fila_personagens.remover()
inimigo_atual = fila_inimigos.remover()  

while personagem_atual and inimigo_atual:
    venceu = batalha(personagem_atual, inimigo_atual)

    if venceu:
        print("Avançando para o próximo inimigo...\n")
        inimigo_atual = fila_inimigos.remover()  
    else:
        personagem_atual = fila_personagens.remover() 
        if personagem_atual:
            print(f"\n{personagem_atual['Nome']} entrou na luta!")  


# ---------- Resultado final ----------
if fila_inimigos.vazia():
    print("\nTodos os inimigos foram derrotados! Vitória!")
else:
    print("\nTodos os seus personagens foram derrotados. Derrota!")
