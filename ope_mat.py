# Vamos solicitar como entrada dois numeros e depois vamos realizar uma opreração simples entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"
if isinstance(resultado, (int,float)):
    resultado = abs(resultado)

print("Resultado: ", resultado)
