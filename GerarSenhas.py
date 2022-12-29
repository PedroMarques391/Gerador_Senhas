import string
from random import random, choice

valores = string.ascii_letters
valores += string.digits
valores += string.punctuation

tamanho = int(input(f"Digite o tamanho da senha que você quer:"))

senha = ''

for i in range(tamanho):
    senha += choice(valores)
print("Sua senha ideal é: " + senha)
