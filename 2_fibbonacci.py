# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def calcularFibonnaci():
    print('=================================== Iniciando ===============================================')
    print('==> Digite um número para verificar se ele pertence à sequência de fibonnaci:  ')
    numero = int(input('==> '))

    n1 = 1
    n2 = 1
    valoresFibonnaci = [0, 1, 1]

    #calcula os valores de fibonnaci até que ultrapassem o numero informado, preenchendo o array
    while numero > n2:
        numAux = n1
        n1 = n2
        n2 = numAux + n1
        valoresFibonnaci.append(n2)

    if numero in valoresFibonnaci:
        print('Pertence!')
        print('=================================== Fim ===============================================')
    else:
        print('NÃO Pertence!')
        print('=================================== Fim ===============================================')

calcularFibonnaci()    
            

