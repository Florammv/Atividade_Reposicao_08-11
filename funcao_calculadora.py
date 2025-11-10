#definindo as variáveis
numero1_txt = input("Digite um número: ")
numero2_txt = input("Digite outro número: ")
operacao_txt = input("Digite 1 para adição; 2 para subtração; 3 para multiplicação; e 4 para divisão: ")

#convertendo as variáveis de texto para número
numero1 = int(numero1_txt)
numero2 = int(numero2_txt)
operacao = int(operacao_txt)

#criando o comando if para realizar as quatro operações básicas e retornar seu resultado
If(operacao = 1): #para adição
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")

else If(operacao = 2): #para subtração
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")

else If(operacao = 3): #para multiplicação
    resultado = numero1 * numero2
    print(f"{numero1} x {numero2} = {resultado}")

else If(operacao = 4): #para divisão
    resultado = numero1 / numero2
    print(f"{numero1} : {numero2} = {resultado}")