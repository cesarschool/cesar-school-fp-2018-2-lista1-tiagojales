## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    cigarro = int(input('Quantos cigarros você fuma por dia?\n'))
    ano = int(input('Por quantos anos você fuma?\n'))
    reducao = (ano * 365 * cigarro * 10) // 1440
    print('Você perdeu {0} dia(s) de vida.'.format(reducao))
    
if __name__ == '__main__':
    main()
