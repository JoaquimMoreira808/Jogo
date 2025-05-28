# :chess_pawn: Dark Crow: Sistema de RPG Tático em Python

**Dark Crow** é um sistema de RPG de combate tático baseado em guerra medieval e fantasia sombria, inspirado em jogos como _Dark Souls_ e _Fire Emblem_. Utiliza estruturas de dados estudadas em disciplinas de algoritmos e estrutura de dados, com foco em modularidade, reutilização e clareza.

---

> [!IMPORTANT]
> :scroll: Licença:
> 
> Projeto desenvolvido para fins educacionais na disciplina de Estrutura de Dados. Livre para modificar e evoluir.
>
> **Obs:** Todas as informações sobre os colaboradores e a Universidade se encontram no fim deste README.

## Link do [Fluxograma do SIstema](https://excalidraw.com/#json=YHlOT2jcWS6ZVSMGZVmxv,4MjIXevlfRjiZ4ClaedPbw)

---

## :open_file_folder: Estrutura do Projeto

- `funcs.py`: Loop principal do jogo e sistema de combate.
- `items.py`: Itens históricos com descrições curtas e longas.
- `dicts.py`: Lista duplamente encadeada de aliados e Gerador de estruturas.
- `arts.py`: Artes ASCII dos objetivos.
- `list.py`: Frases geradas para o sistema.

---

## :crossed_swords: Funcionalidades

- Combate por turnos entre personagens e inimigos.
- Inventário dividido por categorias (consumíveis, amuletos, armas, etc.).
- Sistema de estruturas com eventos e recompensas.
- Uso de itens com atributos (dano, defesa, HP).
- Histórico de eventos e inimigos derrotados.
- Gerenciamento de grupo com lista duplamente encadeada.

---

## :bulb: Principais Conceitos Aplicados

### Programação

- Modularização de arquivos e funções.
- Orientação a objetos.
- Funções puras e reuso de código.

### Estruturas de Dados

- Listas, tuplas, sets, dicionários.
- Listas encadeadas duplas personalizadas.
- Controle de fluxo baseado em estruturas.

---

## :brain: Justificativa das Estruturas de Dados

O sistema **Dark Crow** foi planejado com base nos principais tipos de estruturas de dados vistas na disciplina. Abaixo estão os detalhes do uso e justificativa de cada estrutura:

---

### 1. **Listas (`list`) – incluindo Pilhas e Filas**

- **Onde é usada:**
  - Inventário de itens (como lista de objetos `Item`).
  - Lista de almas obtidas (fila).
  - Histórico de eventos e bestiário.

- **Justificativa:**
  - Listas permitem inserção, remoção e iteração simples.
  - A estrutura de **fila** é usada na lista de almas: o jogador coleta almas de inimigos e as últimas adicionadas vão para o final da fila.
  - A lógica de **pilha** pode ser usada ao montar estratégias (último item usado, último aliado morto, etc.).
  - A ordenação preservada permite exibir os itens ou eventos na ordem que ocorreram.

---

### 2. **Tuplas (`tuple`)**

- **Onde é usada:**
  - Coordenadas ou emparelhamento fixo de informações (ex: `("Espada Rúnica", 25)`).
  - Retornos de funções com múltiplos dados imutáveis.

- **Justificativa:**
  - São ideais quando os dados não devem ser modificados após definidos.
  - Úteis para representar pares fixos ou retornos que não exigem mutabilidade.
  - Garantem integridade dos dados e melhor desempenho do que listas.

---

### 3. **Conjuntos (`set`)**

- **Onde é usada:**
  - Controle de amuletos únicos já obtidos pelo jogador no RPG.

- **Justificativa:**
  - Como os amuletos são gerados aleatoriamente pela função gerar_amuletos() e possuem combinações únicas de atributos, é importante evitar que o jogador obtenha duplicatas exatas.
  - O uso de set permite armazenar assinaturas ou identificadores desses amuletos e garantir que **cada amuleto especial seja único no inventário.**
  - Muito útil para lógica de verificação ("se este evento já aconteceu").

---

### 4. **Dicionários (`dict`)**

- **Onde é usada:**
  - Definição de personagens (`player`, `inimigo`).
  - Armazenamento de dados dos itens, estruturas, eventos.
  - Uso de `defaultdict(int)` para agrupamento de consumíveis.

- **Justificativa:**
  - Proporcionam acesso direto por chave, com tempo constante (`O(1)`).
  - Tornam o código mais legível e organizado para entidades com múltiplos atributos.
  - O `defaultdict` facilita o controle automático de quantidades, sem precisar inicializar valores manualmente.

---

### 5. **Listas Encadeadas (Duplamente Encadeadas)**

- **Onde é usada:**
  - Controle do grupo de aliados em combate.

- **Justificativa:**
  - A estrutura de lista **duplamente encadeada** permite:
    - Inserção e remoção eficiente em qualquer ponto (`O(1)`), ideal para combate dinâmico.
    - Navegação nos dois sentidos: alguns eventos ou habilidades podem afetar o aliado anterior ou o próximo.
  - Evita os custos de realocação de memória presentes nas listas convencionais.
  - Boa aplicação prática de estrutura dinâmica, mostrando domínio do conteúdo da disciplina.

```python
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
```

---

## :pushpin: Resumo das Estruturas

| Estrutura          | Aplicação principal                          | Por que foi usada                                                                 |
|--------------------|----------------------------------------------|-----------------------------------------------------------------------------------|
| **Lista**          | Inventário, almas, bestiário                 | Estrutura sequencial, ordenada, versátil para múltiplos usos                     |
| **Pilha**          | Histórico de aliados, eventos recentes       | Último a entrar, primeiro a sair (LIFO)                                          |
| **Fila**           | Lista de almas                               | Primeiro a entrar, primeiro a sair (FIFO)                                        |
| **Tupla**          | Raridades e pesos de drop (ex: ("Épico", 15))| Imutabilidade, clareza e desempenho                                              |
| **Set**            | Controle de eventos únicos                   | Não permite duplicatas, busca eficiente                                          |
| **Dicionário**     | Player, inimigos, dados dos itens            | Acesso direto por chave, ideal para atributos nomeados                           |                                          |
| **Lista encadeada**| Gestão do grupo de aliados em combate        | Inserção/remoção dinâmica, navegação dupla, baixo custo computacional            |

---

## :repeat: Fluxo de Jogo

- `menu()` é o hub principal.
- `combate()` realiza batalhas com cópias temporárias da party.
- `menu_fogueira()` permite reviver aliados e montar amuletos.
- Eventos aleatórios (estrutura, acampamento, combate) controlam a progressão.
- `gameover()` reseta o jogo ao estado inicial com segurança.

---

## :gear: Tecnologias e Requisitos

- Python 3.10+.
- Estrutura modular de arquivos.
- Rodar com `python game.py`.

---

## :chart_with_upwards_trend: Futuras Expansões

- Sistema rodando fora do terminar do VS Code.
- Habilidades e magias.
- Sistema de escolha de caminhos ramificados.

---
## Informacões Adicionais
### :busts_in_silhouette: Integrantes

- **Nome:** André Luis da Silva Reis | **RA:** 1987363  :man_technologist:
- **Nome:** Joaquim Fernando Santana Moreira | **RA:** 1993917 :man_technologist:
- **Nome:** José Vitor de Almida Lima | **RA:** 1994104 :man_technologist:

### Informações Acadêmicas
- **Universidade:** UNIMAR - Universidade de Marília :school:
- **Curso:** Analise e Desenvolvimento de Sistemas :mortar_board:
- **Disciplina:** Estrutura de Dados :computer:
- **Docente:** Gustavo Marttos Caceres Pereira :man_teacher:
