def LerCasosDeTeste():
    casos_teste = []
    
    while True:
        k, n, m = map(int, input().split())
        if k == n == m == 0:
            break
        
        pratos = []
        
        for _ in range(n):
            c, v = map(int, input().split())
            pratos.append((c, v))
        
        casos_teste.append((k, n, m, pratos)) 
        
    return casos_teste


def main():
    
    casosTeste = LerCasosDeTeste()
    resultados = []
    
    for caso in casosTeste:
        k, n, m, pratos = caso
        CriarCardapio(pratos, k, m, pesos)

if __name__ == "__main__":
    main()   