player = {
    "sprite": """
    _    
   (0)    
  (___)   
  _|_|_   
 (__8__)  
 /__0__\  
""",
    "hp": 10,
    "defesa": 3,
    "forca": 5
}

personagens = {
    "peao": {
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
    "torre": {
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
    "cavalo": {
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
    "bispo": {
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
}

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

party = {
    "jogador": player
}




