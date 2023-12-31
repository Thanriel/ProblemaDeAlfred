# Autores: Weuler Daniel, João Vitor Rosado e Thales Emanoel
# Version 3.0 - 06/14/23 

def LerCasosDeTeste():
    casos_teste = []
    
    # Lê todos os casos de testes inseridos pelo usuário, critério de parada quando todos forem 0
    while True:
        print('Insira os dias, quantidade de pratos e orçamento:', end=' ')
        k, n, m = map(int, input().split())
        if k == n == m == 0:
            break
        while True:
            if k < 1 or k > 21 or m < 0 or m > 100 or n < 1 or n > 50:
                print('Insira os valores novamente:', end=' ')
                k, n, m = map(int, input().split())
            else:
                break
        
        
        pratos = []
        # Preenche o vetor da descrição dos pratos, com custo e lucro total
        for i in range(n):
            print('Insira o custo e lucro do prato '+ str(i) +':', end=' ')
            c, v = map(int, input().split())
            while True:
                if c < 1 or c > 50 or v < 1 or v > 10000:
                    print('Entradas fora do padrão, insira novamente: ', end=' ')
                    c, v = map(int, input().split())
                else:
                    break
            pratos.append((c, v))
        
        casos_teste.append((k, n, m, pratos)) 
        
    return casos_teste

# Função para criar os pesos relativos dos pratos (Lucro/Custo)
def CriaPesosPratos(pratos):
    pesos = []
    
    for i in range(len(pratos)):
        subvetor = pratos[i]
        pesos.append(subvetor[1]/subvetor[0])
    
    return pesos

# Função para criação do cardapio
def CriarCardapio(pratos, k, m, pesos):
    
    # Variável auxiliar de contagem para o index dos pratos
    cont = 0
    cardapio = []
    lucro = 0
    # Clone ordenado dos pesos para facilitar a busca de valores
    pesosOrdenados = sorted(pesos, reverse=True)
    # Variável para o controle de repetição
    quantidadeRepeticao = 0
    
    # Repetição baseda nos dias 
    for i in range(k):
        
        # Variável que controla se ocorreu uma repetição na leitura dos pratos
        repetindo = False
        
        while True:
            
            # Recuperação do index correspondente ao peso ordenado no vetor original
            index = pesos.index(pesosOrdenados[cont])
            
            # Recupera o prato verificado
            pratoEspecifico = pratos[index]
            
            # Verifica se é uma reptição na leitura do vetor de pratos
            if repetindo:
                
                # Verifica se é a primeira repetição consecutiva de um prato
                if quantidadeRepeticao < 1:
                    
                    # Verifica se o prato pode ser custeado pelo orçamento 
                    if pratoEspecifico[0] <= m:
                        
                        # O index do prato é adicionado em um vetor com a adição de 1, 
                        # O custo é deduzido do orçamento 
                        # O lucro total recebe a adição do lucro do prato
                        # O contador é zerado
                        # Variável de repetição é marcada como falsa
                        # Quantidade de repetição começa a valer 1
                        cardapio.append(index + 1)
                        m -= pratoEspecifico[0]
                        lucro += pratoEspecifico[1]/2
                        cont = 0
                        repetindo = False
                        quantidadeRepeticao = 1
                        break
                else:
                    # Caso o caminho encontrado tenha que repetir novamente o prato, ele retorna 0
                    return 0, 0
            
            # Verifica se o prato cabe no orçamento
            if pratoEspecifico[0] <= m:
                
                # Verifica se o cardapio está vazio
                if len(cardapio) != 0:
                    
                    # Verifica se o prato é diferente do anterior
                    if cardapio[i-1] != pratos.index(pratoEspecifico) + 1:
                        
                        # O index do prato é adicionado em um vetor com a adição de 1, 
                        # O custo é deduzido do orçamento 
                        # O lucro total recebe a adição do lucro do prato
                        # O contador é zerado
                        # Quantidade de repetição começa a valer 0
                        
                        cardapio.append(index + 1)
                        m -= pratoEspecifico[0]
                        lucro += pratoEspecifico[1]
                        cont = 0
                        quantidadeRepeticao = 0
                        break
                    
                    else:
                        cont += 1
                
                # Condição para quando for a primeira entrada no cardápio
                elif len(cardapio) == 0:
                    
                    # O index do prato é adicionado em um vetor com a adição de 1, 
                    # O custo é deduzido do orçamento 
                    # O lucro total recebe a adição do lucro do prato
                    # O contador é zerado
                        
                    cardapio.append(index + 1)
                    m -= pratoEspecifico[0] 
                    lucro += pratoEspecifico[1]
                    cont = 0
                    break
            else:
                cont += 1
            
            # Verifica se todos os valores foram checados duas vezes
            if cont >= len(pesosOrdenados) and repetindo:
                return 0, []
            
            elif cont >= len(pesosOrdenados):
                repetindo = True
                cont = 0
                
    return cardapio, lucro

def main():
    
    casosTeste = LerCasosDeTeste()
    
    for caso in casosTeste:
        k, n, m, pratos = caso
        pesos = CriaPesosPratos(pratos)
        cardapio = []
        
        cardapio, lucro = CriarCardapio(pratos, k, m, pesos)
        print('Resultados: ')
        
        if cardapio != 0:
            print("Lucro: R$"+'{:.1f}'.format(lucro))
            print('Pratos', end=' ')
            for prato in cardapio:
                print(prato, end=' ')
            print()
            
        else:
            print(0.0)
        
if __name__ == "__main__":
    main()   