# Ausuario inserer as notas de 2 provas, 1 trabalho e o programa calcula a média

def main():
    nota1 = float(input("Digite a nota da primeira prova (máximo 35 pontos): "))
    while nota1 > 35:
        print("Nota inválida. A nota máxima para a primeira prova é 35.")
        nota1 = float(input("Digite a nota da primeira prova (máximo 35 pontos): "))
    
    nota2 = float(input("Digite a nota da segunda prova (máximo 35 pontos): "))
    while nota2 > 35:
        print("Nota inválida. A nota máxima para a segunda prova é 35.")
        nota2 = float(input("Digite a nota da segunda prova (máximo 35 pontos): "))
    
    nota_trabalho = float(input("Digite a nota do trabalho (máximo 30 pontos): "))
    while nota_trabalho > 30:
        print("Nota inválida. A nota máxima para o trabalho é 30.")
        nota_trabalho = float(input("Digite a nota do trabalho (máximo 30 pontos): "))

    def calcular_media(nota1, nota2, nota_trabalho):
        return (nota1 + nota2 + nota_trabalho) / 3
    
    media = calcular_media(nota1, nota2, nota_trabalho)
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    main()