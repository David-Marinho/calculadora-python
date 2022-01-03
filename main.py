from func import calculadora

num1 = ''

print('Bem vindo a calculadora V3.0')
escolha = input('deseja calcular com a raiz quadrada? ').upper()

if escolha[:1] == 'S':
    num1 = float(input('digite o numero: '))
    num2 = float(input('digite o indice da raiz: '))
    op = 'r'

else:
    conta = input('digite a conta: ').replace(' ', '')
    
    for i in conta:
        if i.isnumeric():
            num1 += i
        
        else:
            break
    
    op = conta[len(num1)]
    num2 = conta[len(num1) + 1:]
    num2 = float(num2)
    num1 = float(num1)

result = calculadora(num1, num2, op)
print('=-=' * 30)
print(f'o resultado é igual a \033[36m{result}\033[m')
print('=-=' * 30)