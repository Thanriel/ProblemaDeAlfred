# Problema de Alfred

O problema de Alfred se resume a um restaurante que quer maximizar o lucro com um número determinado de pratos levando em consideração uma quantidade de k dias. É importante que pratos repetidos em dias consecutivos tenham seu valor de lucro reduzido em 50% na primeira repetição e a 0 nas seguintes.

# Como pode ser modelado com o paradigma guloso?

Todo algoritmo se resume a uma função, que verifica os pratos com maiores pesos primeiro(peso = lucro/custo), levando em conta a não repetição dos pratos em dias consecutivos, já que em maioria, seu valor será menor que em dias intercalados.

# O algoritmo apresenta sempre a solução ótima?

Quanto a local sim, já que é uma solução para o problema em questão, mas quanto a global não é possível cravar com certeza, já que ele usa uma métrica de sempre olhar o maior peso e não dar prioridade para as repetições, fazendo com que talvez não tenha as melhores soluções em certos tipos de casos de usos.

# Como pode ser modelado com o paradigma dinâmico?

É baseado na descoberta dos valores anteriores e a comparação com os atuais, levando em conta os dias e o lucro cedido pelos pratos, procurando o maior valor entre as duas comparações, mas existe um problema. O grupo teve dificuldades em levar em conta a repetição dos pratos com redução nos preços, devido ao tamanho da matriz e a complexidade exigida.

# Subestrutura ótima e sobreposição de problemas

O algoritmo subdivide os pratos com valores mais significativos conforme os custos, memorizando o maior valor possível, o que garante que comparações com valores menores e custos elevados demais, ou repetições de combinações não precisem ser checadas futuramente.

# É baseado em algum algoritmo clássico?

Para entendimento e como exemplo para resultados, foram adaptadas algumas partes do algoritmo para resolução do problema da mochila.
