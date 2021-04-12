from func import calculadora

print('Bem vindo a calculadora V2.0')

num1 = float(input('digite um numero: '))

op = input('[+] para somar \n[-] subtrair \n[*] para multiplicar \n[/] dividir \n[%] para resto de divisao '
           '\n[r] raiz \ndigite o simbolo da operaçao desejada: ')

if op == 'r':
    num2 = int(input('digite o indice da raiz: '))

else:
    num2 = float(input('digite o segundo numero: '))

result = calculadora(num1, num2, op)
print('=-=' * 30)
print(f'o resultado é igual a \033[36m{result}\033[m')
print('=-=' * 30)