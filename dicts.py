player = {
    "Nome": "Player",
    "sprite": """
    _    
   ( )    
  <_I_>   
  _|V|_   
 \__I__/ 
 /__I__\  
""",
    "hp": 14,
    "defesa": 4,
    "forca": 5,
    "amigo": True,
}


personagens = [
    {
        "Nome": "Peao",
        "sprite": """
    _    
   (_)    
  (___)   
  _|_|_   
 (_____)  
 /_____\  
""",
        "hp": 16,
        "defesa": 4,
        "forca": 5,
        "amigo": True
    },
    {
        "Nome": "Torre",
        "sprite": """
  _  _  _   
 | || || |  
 |_______| 
 \__ ___ / 
  |_|___|  
  |___|_| 
 (_______) 
 /_______\ 
""",
        "hp": 20,
        "defesa": 6,
        "forca": 4,
        "amigo": True
    },
    {
        "Nome": "Cavalo",
        "sprite": r"""
  ^^__    
 /  - \_  
<|    __<    
<|    \
<|     \    
<|______\   
 _|____|_   
(________)
 /________\ 
""",
        "hp": 13,
        "defesa": 2,
        "forca": 7,
        "amigo": True
    },
    {
        "Nome": "Bispo",
        "sprite": """
   _O_    
  / //\   
 {     }   
  \___/   
  (___)    
   |_|      
  /   \     
 (_____)   
(_______) 
/_______\  
""",
        "hp": 11,
        "defesa": 2,
        "forca": 5,
        "amigo": True
    }
]


inimigos = [
    {
        "Nome": "Peão das Sombras",
        "hp": 10,
        "defesa": 1,
        "forca": 4
    },
    {
        "Nome": "Torre Espectral",
        "hp": 15,
        "defesa": 4,
        "forca": 3
    },
    {
        "Nome": "Cavalo Maldito",
        "hp": 12,
        "defesa": 2,
        "forca": 6
    },
    {
        "Nome": "Bispo Corrupto",
        "hp": 9,
        "defesa": 2,
        "forca": 5
    },
    {
        "Nome": "Peão Infernal",
        "hp": 11,
        "defesa": 2,
        "forca": 5
    },
    {
        "Nome": "Torre Sombria",
        "hp": 18,
        "defesa": 5,
        "forca": 4
    },
    {
        "Nome": "Cavalo do Abismo",
        "hp": 14,
        "defesa": 3,
        "forca": 7
    },
    {
        "Nome": "Bispo do Caos",
        "hp": 10,
        "defesa": 3,
        "forca": 6
    },
    # {
    #     "Nome": "Cavaleiro das Trevas",
    #     "hp": 22,
    #     "defesa": 5,
    #     "forca": 5
    # }
]


# ==========================
# Estruturas
# ==========================


estruturas = {
    "fortaleza": {
        "sprite": r"""
                uuu       uuu
               uuu|=====uuu |
               | |======| |'|
^-/^-/^-/^-/^-/| | .==. | | |-^~/-^
^-/^-/^-/^- ^~ |___|##|___|/ ^~ ^ ^
""",
        "mensagem": "uma fortaleza antiga, suas muralhas sussurram segredos de guerras passadas."
    },
    "lapide": {
        "sprite": r"""
             ______________   
           /                \
          /  _     ___   _   \
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \.  _|_. | .  ||
          |                  ||
          |   Ana'be Atrix   ||
          |                  ||
/.,\))/.,(//,,..,,\||(,,.,\\,.((//(,,.\||(

""",
        "mensagem": "uma lápide sob uma árvore que nunca floresce. Ainda pulsa o eco suave de um nome sussurrado por alguém que jamais a esqueceu."
    },
    "ponte": {
        "sprite": """
 `
           |xx|             |x|
  ============|===============|===--
  ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~

""",
        "mensagem": "uma ponte de pedra sobre um rio sereno. Algo parece observar por baixo dela..."
    },
    "torre_mistica": {
        "sprite": """
                          ._
                          |~
                        uuuuu
                        |_#-|
                        | _#|
                        |_ -|
   ________ .$$. ______ | - | _____________
           .#$$$. __    |-  | ....__
     _.--' $$$$$$    ` -[__N]        `--a:f-
           $$$$$$    -.
      -.    `:/'    _.))        .--.
             ||   .'.-'     _..-.. _.-.
""",
        "mensagem": "uma torre mística que se ergue solitária, irradiando energia arcana no topo."
    },
    "cabana": {
        "sprite": r"""
                   )
                 _(
             ___|_|_________
            /___|_|_________\
       ()  /_________________\
   `'.()))/___________________\'-.'`'.
  .,'(())()   ____     ____  |,.'     '-.
     )(()))  |)~~(|   |)~~(| |. '-. ()`'.
    ()()(()) ||__||   ||__|| | `'.,(())
   ())()(()))________________|___ ()))()
   ()((())()))| | | | | | | | | | (()()))
  ()))(()()())|_|_|_|_|_|_|_|_|_|)(()(()
  (()((())(()-------------------|(())(())
  ~^~ ^" ^"  ^~^   ^"   ~^~    ^~^~(()(()
  ^"     ^~^   ~^~   ^"    ^~^   ~~^~""^
""",
        "mensagem": "uma cabana isolada, fumaça escapa pela chaminé. Alguém ainda vive aqui?"
    }
}

# ==========================
# Party (Grupo do Jogador)
# ==========================


boss1_party = [
    {
        "Nome": "Aeli, um peão.",
        "hp": 18,          
        "defesa": 5,       
        "forca": 6         
    },
    {
        "Nome": "Tharn, um peão.",
        "hp": 22,          
        "defesa": 6,       
        "forca": 6         
    },
    {
        "Nome": "Maegra, a torre",
        "hp": 35,          
        "defesa": 9,       
        "forca": 10        
    }
]

boss2_party = [
    {
    "Nome": "O Rei Branco, Coroa Partida",
    "hp": 48, 
    "defesa": 10,
    "forca": 12     
    }
]

boss3_party = [
    {
        "Nome": "Selene, a Rainha Branca",
        "hp": 20,
        "defesa": 10,
        "forca": 4
    }
]

final_boss_party = [
    {
        "Nome": "Gustav O'Martoz, o Último Lorde da Coroa",
        "hp": 60,          
        "defesa": 10,      
        "forca": 15    
    }
]