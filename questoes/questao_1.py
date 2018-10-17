## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    salario = float(input('Digite o seu salário:\n'))
    porcent = float(input('Digite o aumento recebido (%):\n'))
    aumento = salario * porcent / 100
    novo_salario = aumento + salario
    print('O aumento foi de R$ {0}, e o novo salário é de R$ {1}'.format (aumento, novo_salario))  


if __name__ == '__main__':
    main()
