def calculate_profit(k, dia, orçamento, last_prato, memo, pratos):
    # Verificar se a solução já foi calculada anteriormente
    if memo[dia][orçamento][last_prato] != -1:
        return memo[dia][orçamento][last_prato]

    # Caso base: não há mais dias ou orçamento é zero
    if dia == k or orçamento == 0:
        return 0

    # Caso contrário, para cada prato disponível
    max_profit = 0
    for i in range(len(pratos)):
        custo, lucro = pratos[i]

        # Verificar se é possível cozinhar o prato no dia atual
        if custo <= orçamento:
            # Verificar se o prato é diferente do último prato escolhido
            if last_prato != i:
                # Calcular o lucro do prato
                profit = lucro + calculate_profit(dia + 1, orçamento - custo, i)
            else:
                # Calcular o lucro do prato com redução
                profit = lucro / 2 + calculate_profit(dia + 1, orçamento - custo, i)

            # Verificar se o lucro é maior que o máximo atual
            if profit > max_profit:
                max_profit = profit

    # Atualizar a matriz de memoização
    memo[dia][orçamento][last_prato] = max_profit

    return max_profit


def main():
    while True:
        # Ler os valores de k, n e m
        k, n, m = map(int, input().split())

        # Verificar condição de parada
        if k == n == m == 0:
            break

        # Ler os pratos disponíveis
        pratos = []
        for _ in range(n):
            custo, lucro = map(int, input().split())
            pratos.append((custo, lucro))

        # Inicializar a matriz de memoização
        memo = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]

        # Chamar a função para maximizar o lucro
        max_profit = calculate_profit(k, 0, m, -1, memo, pratos)

        # Imprimir o lucro máximo com 1 dígito após o ponto decimal
        print(f'{max_profit:.1f}')


if __name__ == '__main__':
    main()
