frase = input()

while frase != "*":
    frase = frase.upper()

    palavras = frase.split(" ")

    letra = palavras[0][0]

    poema = True

    for palavra in palavras:
        if palavra[0] != letra:
            print("N")
            poema = False
            break;

    if poema:
        print("Y")

    frase = input()