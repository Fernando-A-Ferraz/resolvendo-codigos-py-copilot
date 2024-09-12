#Vamos testar se uma palavra é um palíndromo?! 

def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida

# Solicitar ao usuário que insira uma palavra
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')

