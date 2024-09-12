# Agora vamos solicitar uma string e um número inteiro como entrada. Depois termos que retornar a string repetida o número de vezes indicado pelo número informado.

string_input = input("Digite uma string: ")
numero_input = int(input("Digite um número inteiro: "))

resultado = ', '.join([string_input] * numero_input)
resultado += '.'

print(resultado)



