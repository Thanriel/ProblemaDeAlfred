def LerCasosDeTeste():
    casos_teste = []
    
    while True:
        k, n, m = map(int, input().split())
        if k == n == m == 0:
            break
        #Teste
        pratos = []
        
        for _ in range(n):
            c, v = map(int, input().split())
            pratos.append((c, v))
        
        casos_teste.append((k, n, m, pratos)) 
        
    return casos_teste

def CriaPesosPratos(pratos):
    pesos = []
    
    for i in range(len(pratos)):
        subvetor = pratos[i]
        pesos.append(subvetor[1]/subvetor[0])
    
    return pesos

def CriarCardapio(pratos, k, m, pesos):
    cont = 0
    cardapio = []
    lucro = 0
    pesosOrdenados = sorted(pesos, reverse=True)
    quantidadeRepeticao = 0
    
    for i in range(k):
        repetindo = False
        
        while True:
            
            index = pesos.index(pesosOrdenados[cont])
            pratoEspecifico = pratos[index]
            
            if repetindo:
                if quantidadeRepeticao < 1:
                    if pratoEspecifico[0] <= m:
                        cardapio.append(index + 1)
                        m -= pratoEspecifico[0]
                        lucro += pratoEspecifico[1]/2
                        cont = 0
                        repetindo = False
                        quantidadeRepeticao = 1
                        break
                else:
                    return 0, 0
                    
            if pratoEspecifico[0] <= m:
                
                if len(cardapio) != 0:
                    
                    if cardapio[i-1] != pratos.index(pratoEspecifico) + 1:
                        
                        cardapio.append(index + 1)
                        m -= pratoEspecifico[0]
                        lucro += pratoEspecifico[1]
                        cont = 0
                        quantidadeRepeticao = 0
                        break
                    
                    else:
                        cont += 1
                
                elif len(cardapio) == 0:
                    
                    cardapio.append(index + 1)
                    m -= pratoEspecifico[0] 
                    lucro += pratoEspecifico[1]
                    cont = 0
                    break
            else:
                cont += 1
            
            if cont >= len(pesosOrdenados) and repetindo:
                return 0, 0
            
            else:
                repetindo = True
                cont = 0
                
    return cardapio, lucro
                
                
        
          


def main():
    
    casosTeste = LerCasosDeTeste()
    resultados = []
    
    for caso in casosTeste:
        k, n, m, pratos = caso
        pesos = CriaPesosPratos(pratos)
        
        CriarCardapio(pratos, k, m, pesos)

if __name__ == "__main__":
    main()   