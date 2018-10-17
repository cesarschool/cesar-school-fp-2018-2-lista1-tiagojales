## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    import math
    raio = float(input('Digite o raio da circunferência (m):\n'))
    area = math.pi * math.pow(raio,2)
    diametro = raio * 2
    comprimento = 2 * math.pi * raio
    print('A circunferência tem: {0} m² de área, {1} m de diâmetro e {2} m de comprimento.'.format(area, diametro, comprimento))
    
if __name__ == '__main__':
    main()
