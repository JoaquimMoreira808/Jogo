import random
from dicts import *

class Item:
    def __init__(self, nome, descricao_curta, descricao_longa, raridade="Comum", dano=0, dano_real=0, defesa=0, hp=0):
        self.nome = nome
        self.descricao_curta = descricao_curta
        self.descricao_longa = descricao_longa
        self.raridade = raridade
        self.dano = dano
        self.dano_real = dano_real
        self.defesa = defesa
        self.hp = hp

    def __repr__(self):
        return f"<Item: {self.nome} (Raridade: {self.raridade})>"
        
#Raridade dos itens
pesos_raridade = (
    ("Comum", 70),
    ("Incomum", 45),
    ("Raro", 25),
    ("Épico", 15),
    ("Lendário", 10)
)

# ==========================
# Itens
# ==========================

#Informações dos Itens
frasco_piche = Item(
    "Frasco de Piche",
    "Reduz temporariamente a velocidade do inimigo. ",
    "Um frasco de piche pegajoso. Durante cercos, óleo fervente ou piche eram usados para atrasar inimigos.",
    raridade="Comum",
    defesa=3
)

unguento_curandeiro = Item(
    "Unguento do Curandeiro",
    "Restaura um pouco de HP. ",
    "Pomada medicinal usada em batalhas medievais. Curandeiros utilizavam ervas naturais para tratar ferimentos.",
    raridade="Comum",
    hp=2
)

polvora_negra = Item(
    "Pólvora Negra",
    "Causa dano leve. " ,
    "Uma pequena carga de pólvora instável. No fim da era medieval, a pólvora começou a ser usada em armas de cerco.",
    raridade="Comum",
    dano=3
)

flechas_incendiarias = Item(
    "Flechas Incendiárias",
    "Causam dano leve. ",
    "Flechas mergulhadas em óleo e incendiadas eram usadas para causar caos em campos e construções inimigas.",
    raridade="Incomum",
    dano=4
)

taca_do_cavaleiro_risonho = Item(
    "Taça do Cavaleiro Risonho",
    "Uma taça de estanho, lascada na borda.",
    "Diz-se que um cavaleiro se recusava a matar, mesmo em batalha. \n" \
    "Ele brindava com os inimigos antes de morrer sorrindo — mais livre que qualquer rei.",
    raridade="Incomum",
    hp=5
)

cordao_maos_atadas = Item(
    "Cordão das Mãos Atadas",
    "Um laço de corda escurecida, cheira a salmoura. ",
    "Usado por servos que juraram nunca mover peças por vontade própria. \n" \
    "Alguns dizem que os ossos de seus pulsos ainda tremem quando o jogo muda.",
    raridade="Incomum",
    dano=6
)

fragmento_peao_corrompido = Item(
    "Fragmento de Peão Corrompido",
    "Pequeno pedaço de estátua negra, derretida por dentro. ",
    "Um peão que alcançou o fim... e recusou transformar-se. Morreu inteiro. \n" \
    "Virou lenda entre os que preferem permanecer menores.",
    raridade="Raro",
    dano=8
)

medalhao_da_abertura = Item(
    "Medalhão da Abertura",
    "Uma moeda achatada, com dois lados idênticos. ",
    "Nas vilas das fileiras iniciais, diz-se que quem carrega esse medalhão pode evitar o primeiro movimento... \n" \
    "só uma vez.",
    raridade="Raro",
    defesa=6
)

lamina_de_seis_casas = Item(
    "A Lâmina de Seis Casas",
    "Espada curta e quebrada, sem guarda. ",
    "Feita para peões — finos de espírito, mas firmes de vontade. Quem a empunha não recua. Quem recua, morre.",
    raridade="Raro",
    dano=7
)

recorte_veu_casamento = Item(
    "Recorte de Véu de Casamento",
    "Trapo branco com fios de ouro, manchado de vinho escuro. ",
    "Era usado nos casamentos dos bispos do Leste. Hoje, é usado para cobrir corpos que caem antes da terceira jogada.",
    raridade="Raro",
    hp=7
)

sineta_ultimo_taberneiro = Item(
    "Sineta do Último Taberneiro",
    "Pequeno sino de ferro, sem som. ",
    "Diz-se que existia uma taverna na coluna H. Quando a guerra alcançou sua porta, o dono tocou esta sineta... "
    "e nenhuma peça jamais passou por lá novamente.",
    raridade="Raro",
    defesa=8
)

carta_nunca_entregue = Item(
    "Carta Nunca Entregue",
    "Papel ressecado, a tinta manchada por lágrimas ou chuva. ",
    "Escrita por um escudeiro ao seu amante, um peão do lado inimigo. \n" \
    "Foi guardada por um corvo que jamais soube a quem levar.",
    raridade="Épico",
    hp=10
)

botao_segundo_lanceiro = Item(
    "Botão de Uniforme do Segundo Lanceiro",
    "Um botão de bronze polido, leve como poeira. ",
    "Não houve Primeiro Lanceiro. \n" \
    "O Segundo existiu por engano, mas virou lenda porque sobreviveu a três promessas quebradas e a um cavalo cego.",
    raridade="Épico",
    dano=12
)

ovo_torre_ociosa = Item(
    "Ovo da Torre Ociosa",
    "Casca vazia, quente ao toque. ",
    "As torres costumavam guardar ovos. Por quê? Ninguém sabe. \n" \
    "Mas toda vez que alguém morre, um ovo se parte ao longe.",
    raridade="Épico",
    hp=11
)


espada_rei_caido = Item(
    "Espada do Rei Caído",
    "Espada lendária que causa 12 de dano e ignora armadura.",
    "A Espada do Rei Caído pertenceu a um antigo monarca que enlouqueceu durante a guerra.\n" \
    "Forjada com aço negro e encantada por um feiticeiro traidor, ela foi selada após destruir um exército inteiro.\n" \
    "Diz-se que 'Sua lâmina carrega o lamento das almas que tombaram diante dela.'",
    raridade="Lendário",
    dano_real=12
)

#Dicionário dos itens
itens_possiveis_encontrar = {
    "frasco_piche": frasco_piche,
    "unguento_curandeiro": unguento_curandeiro,
    "polvora_negra": polvora_negra,
    "flechas_incendiarias": flechas_incendiarias,
    "taca_do_cavaleiro_risonho": taca_do_cavaleiro_risonho,
    "cordao_maos_atadas": cordao_maos_atadas,
    "fragmento_peao_corrompido": fragmento_peao_corrompido,
    "medalhao_da_abertura": medalhao_da_abertura,
    "lamina_de_seis_casas": lamina_de_seis_casas,
    "recorte_veu_casamento": recorte_veu_casamento,
    "sineta_ultimo_taberneiro": sineta_ultimo_taberneiro,
    "carta_nunca_entregue": carta_nunca_entregue,
    "botao_segundo_lanceiro": botao_segundo_lanceiro,
    "ovo_torre_ociosa": ovo_torre_ociosa,
    "espada_rei_caido": espada_rei_caido,

}