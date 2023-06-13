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

def maximize_profit(k, n, m, pratos):
    # Inicializando a matriz de memoização
    memo = [[[-1, []] for _ in range(m+1)] for _ in range(k+1)]
    
    # Função auxiliar para calcular o lucro máximo
    def calculate_profit(dia, orçamento):
        # Verificar se a solução já foi calculada anteriormente
        if memo[dia][orçamento][0] != -1:
            return memo[dia][orçamento]

        # Caso base: não há mais dias ou orçamento é zero
        if dia == k or orçamento == 0:
            return [0, []]

        # Caso contrário, para cada prato disponível
        max_profit = [0, []]
        for i in range(n):
            custo, lucro = pratos[i]

            # Verificar se é possível cozinhar o prato no dia atual
            if custo <= orçamento:
                # Calcular o lucro do prato
                profit = lucro + calculate_profit(dia + 1, orçamento - custo)[0]

                # Verificar se o lucro é maior que o máximo atual
                if profit > max_profit[0]:
                    max_profit = [profit, [i+1]]  # Atualizar o máximo

        # Se houver um prato no dia atual, verificar se é possível repeti-lo
        if max_profit[1] and dia + 2 <= k:
            # Calcular o lucro se repetir o prato no dia seguinte
            repeat_profit = calculate_profit(dia + 2, orçamento)[0] + (max_profit[0] / 2)

            # Verificar se o lucro repetindo o prato é maior que o máximo atual
            if repeat_profit > max_profit[0]:
                max_profit = [repeat_profit, max_profit[1] + max_profit[1]]

        # Atualizar a matriz de memoização
        memo[dia][orçamento] = max_profit

        return max_profit

    # Chamar a função auxiliar para calcular o lucro máximo
    max_profit = calculate_profit(0, m)

    return max_profit


def main():
    
    casosTeste = LerCasosDeTeste()
    resultados = []
    
    for caso in casosTeste:
        k, n, m, pratos = caso
        max_profit, pratos_escolhidos = maximize_profit(k, n, m, pratos)
        print(f'{max_profit:.1f}')
        for prato in pratos_escolhidos:
            print(prato, end=' ')
        print()

if __name__ == "__main__":
    main()   