alfabeto = input() + " "
crypto = input() + " "
frase = input()

descrypto = [alfabeto[crypto.index(letra)] if letra in crypto else letra for letra in frase]

print("".join(descrypto))
