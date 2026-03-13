# Calculadora simples

print("=== Calculadora ===")

# pedir números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# pedir operação
operacao = input("Escolha a operação (+, -, *, /): ")

# cálculo
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")
    exit()

# mostrar resultado
print("Resultado:", resultado)