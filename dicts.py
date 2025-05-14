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
        "hp": 15,
        "defesa": 3,
        "forca": 5
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
        "forca": 3
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
        "hp": 12,
        "defesa": 2,
        "forca": 7
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
        "hp": 10,
        "defesa": 2,
        "forca": 4
    }
]


# ==========================
# Inimigos
# ==========================

inimigos = [
    {
        "Nome": "Peão das Sombras",
        "sprite": "\033[1;31m    _\n   (_)    \n  (___)   \n  _|_|_   \n (_____)  \n /_____\\\033[0m",
        "hp": 12,
        "defesa": 2,
        "forca": 4
    },
    {
        "Nome": "Torre Espectral",
        "sprite": "\033[1;30m  _  _  _   \n | || || |  \n |_______| \n \\__ ___ / \n  |_|___|  \n  |___|_| \n (_______) \n /_______\\\033[0m",
        "hp": 18,
        "defesa": 5,
        "forca": 3
    },
    {
        "Nome": "Cavalo Maldito",
        "sprite": "\033[1;31m  ^^__    \n /  - \\_  \n<|    __< \n<|    \\   \n<|     \\  \n<|______\\ \n _|____|_ \n(________)\n/________\\\033[0m",
        "hp": 14,
        "defesa": 3,
        "forca": 6
    },
    {
        "Nome": "Bispo Corrupto",
        "sprite": "\033[1;30m   _O_    \n  / //\\   \n {     }  \n  \\___/   \n  (___)   \n   |_|    \n  /   \\   \n (_____)  \n(_______) \n/_______\\\033[0m",
        "hp": 10,
        "defesa": 2,
        "forca": 5
    },
    {
        "Nome": "Peão Infernal",
        "sprite": "\033[0;31m    _\n   (_)    \n  (___)   \n  _|_|_   \n (_____)  \n /_____\\\033[0m",
        "hp": 13,
        "defesa": 3,
        "forca": 5
    },
    {
        "Nome": "Torre Sombria",
        "sprite": "\033[0;30m  _  _  _   \n | || || |  \n |_______| \n \\__ ___ / \n  |_|___|  \n  |___|_| \n (_______) \n /_______\\\033[0m",
        "hp": 22,
        "defesa": 6,
        "forca": 4
    },
    {
        "Nome": "Cavalo do Abismo",
        "sprite": "\033[0;31m  ^^__    \n /  - \\_  \n<|    __< \n<|    \\   \n<|     \\  \n<|______\\ \n _|____|_ \n(________)\n/________\\\033[0m",
        "hp": 16,
        "defesa": 4,
        "forca": 7
    },
    {
        "Nome": "Bispo do Caos",
        "sprite": "\033[1;31m   _O_    \n  / //\\   \n {     }  \n  \\___/   \n  (___)   \n   |_|    \n  /   \\   \n (_____)  \n(_______) \n/_______\\\033[0m",
        "hp": 11,
        "defesa": 3,
        "forca": 6
    },
    {
        "Nome": "Cavaleiro das Trevas",
        "sprite": "\033[1;30m    _    \n   ( )   \n  <_I_>  \n  _|V|_  \n \\__I__/ \n /__I__\\\033[0m",
        "hp": 22,
        "defesa": 5,
        "forca": 8
    },
    {
        "Nome": "Guardião Abissal",
        "sprite": "\033[0;31m   _____  \n  /     \\ \n | () () |\n  \\  ^  / \n   |||||  \n   ||||| \033[0m",
        "hp": 35,
        "defesa": 6,
        "forca": 8
    }
]



# ==========================
# Estruturas
# ==========================


estruturas = {
    "fortaleza": {
        "sprite": """
                uuu       uuu
               uuu|=====uuu |
               | |======| |'|
^-/^-/^-/^-/^-/| | .==. | | |-^~/-^
^-/^-/^-/^- ^~ |___|##|___|/ ^~ ^ ^
""",
        "mensagem": "Uma fortaleza antiga, suas muralhas sussurram segredos de guerras passadas."
    },
    "ponte": {
        "sprite": """
 `
           |xx|             |x|
  ============|===============|===--
  ejm ~~~~~|xx|~~~~~~~~~~~~~|x|~~~ ~~  ~   ~

""",
        "mensagem": "Uma ponte de pedra sobre um rio sereno. Algo parece observar por baixo dela..."
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
        "mensagem": "Uma torre mística ergue-se solitária, irradiando energia arcana do topo."
    },
    "cabana": {
        "sprite": """
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
        "mensagem": "Uma cabana isolada, fumaça escapa pela chaminé. Alguém ainda vive aqui?"
    }
}

# ==========================
# Party (Grupo do Jogador)
# ==========================


#boss e inimigos 



party = [
    {
        "Nome": "Player",
        "sprite": """
    _    
   ( )    
  <_I_>   
  _|V|_   
 \__I__/ 
 /__I__\  
""",
        "hp": 10,
        "defesa": 3,
        "forca": 1000000
    }
]

almas = []