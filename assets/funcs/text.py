def digitar(tempo: int, texto: str):
    def delay(t):
        for i in range(t):
            pass
    for letra in texto:
        print(letra, end='', flush=True)
        delay(tempo * 999999)
    print()


