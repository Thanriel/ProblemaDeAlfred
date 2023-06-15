# Autores: Samuel Gonzaga, Symon Breno e Thales Emanoel
# Version 3.0 - 06/14/23

def maximize_profit(k, n, m, dishes):
    # Cria uma matriz para armazenar os resultados intermediários
    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(k + 1)]

    # Percorre os dias
    for day in range(1, k + 1):
        # Percorre os pratos
        for dish in range(1, n + 1):
            cost, profit = dishes[dish - 1]  # Obtem o custo e o lucro do prato atual

            # Percorre o orçamento
            for budget in range(m + 1):
                # Calcula o lucro máximo considerando o prato atual e o orçamento disponível

                # Verifica se é possível escolher o prato atual no dia atual
                if budget >= cost:
                    dp[day][dish][budget] = max(dp[day][dish][budget], dp[day - 1][dish][budget - cost] + profit)

                # Verifica o lucro máximo sem escolher o prato atual
                dp[day][dish][budget] = max(dp[day][dish][budget], dp[day][dish - 1][budget])

    # Verifica se é possível atender aos requisitos do problema
    if dp[k][n][m] == 0:
        return 0, []

    # Reconstrói a sequência de pratos escolhidos
    chosen_dishes = []
    budget = m
    for day in range(k, 0, -1):
        for dish in range(n, 0, -1):
            if dp[day][dish][budget] != dp[day][dish - 1][budget]:
                chosen_dishes.append(dish)
                budget -= dishes[dish - 1][0]
                break

    # Inverte a ordem dos pratos escolhidos
    chosen_dishes.reverse()

    return dp[k][n][m], chosen_dishes


def read_test_case():
    print('Insira os dias, quantidade de pratos e orçamento: ', end=' ')
    k, n, m = map(int, input().split())
    while True:    
        if k == 0 and n == 0 and m == 0:
            return None
        
        if k < 1 or k > 21 or m < 0 or m > 100 or n < 1 or n > 50:
            print('Entradas fora do padrão, insira novamente: ', end=' ')
            k, n, m = map(int, input().split())
            break
        else:
            break
    dishes = []
    for i in range(n):
        print('Insira o custo e lucro do prato '+ str(i) +':', end=' ')
        cost, profit = map(int, input().split())
        while True:
            if cost < 1 or cost > 50 or profit < 1 or profit > 10000:
                print('Entradas fora do padrão, insira novamente: ', end=' ')
                cost, profit = map(int, input().split())
            else:
                break
        dishes.append((cost, profit))
    return k, n, m, dishes


def main():
    while True:
        test_case = read_test_case()
        if test_case is None:
            break
        k, n, m, dishes = test_case
        max_profit, chosen_dishes = maximize_profit(k, n, m, dishes)
        print()
        print('Lucro: R$'f'{max_profit:.1f}')
        if max_profit > 0:
            print('Pratos:', end=' ')
            for dish in chosen_dishes:
                print(dish, end=' ')
        print()


if __name__ == "__main__":
    main()
