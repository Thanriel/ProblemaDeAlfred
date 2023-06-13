def maximize_profit(pratos, orçamento):
    pratos_ordenados = sorted(pratos, key=lambda x: x[1], reverse=True)  # Ordena os pratos por lucro em ordem decrescente
    cardapio = []
    lucro_total = 0

    for prato in pratos_ordenados:
        preco = prato[0]
        lucro = prato[1]

        # Verifica se o prato pode ser adicionado ao cardápio sem exceder o orçamento
        if preco <= orçamento:
            cardapio.append(prato)
            orçamento -= preco
            lucro_total += lucro

    return cardapio, lucro_total


# Função para ler os casos de teste da entrada
def ler_casos_teste():
    casos_teste = []
    
    while True:
        k, n, m = map(int, input().split())
        if k == n == m == 0:
            break
        
        pratos = []
        for _ in range(n):
            c, ν = map(int, input().split())
            pratos.append((c, ν))
        
        casos_teste.append((k, m, pratos))
    
    return casos_teste


# Função para imprimir os resultados
def imprimir_resultados(resultados):
    for cardapio, lucro in resultados:
        print("Cardápio:")
        for prato in cardapio:
            print("Preço:", prato[0], "Lucro:", prato[1])

        print("Lucro total:", lucro)
        print()


# Processa os casos de teste
casos_teste = ler_casos_teste()
resultados = []
for caso in casos_teste:
    k, m, pratos = caso
    cardapio_final, lucro_final = maximize_profit(pratos, m)
    resultados.append((cardapio_final, lucro_final))

# Imprime os resultados
imprimir_resultados(resultados)