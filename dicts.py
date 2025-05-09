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
        "hp": 10,
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
        "hp": 25,
        "defesa": 10,
        "forca": 7
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
        "hp": 18,
        "defesa": 4,
        "forca": 9
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
        "hp": 16,
        "defesa": 5,
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

inimigos = [
    { "Nome": "Peão amaldiçoado", "hp": 1, "defesa": 1, "forca": 1},
    { "Nome": "Cavalo sem cabeça", "hp": 10, "defesa": 5, "forca": 5},
    { "Nome": "Bispo das trevas", "hp": 50, "defesa": 1, "forca": 20},
    { "Nome": "Torre da perdição", "hp": 10, "defesa": 3, "forca": 2}
]


party = [
    {}
]


