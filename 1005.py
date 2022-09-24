'''
Para a resolução do problema '1005 - Average 1' vale a mesma explicação dada no problema '1003 - Simple Sum'.
A noção de média aritmética de dois números é um pré-requisito para resolver esse problema.
Acompanhe o raciocínio:
Média aritmética remete ao termo média, mediano, no meio. Note que, muito didaticamente, a média aritmética de dois números é a soma desses números dividida por dois.
media_aritmetica_A_B = (A + B) / 2
Mas, a questão fala que as notas possuem pesos. Nesse caso em específico a média aritmética simples não será utilizada.
Nesse caso, a média aritmética ponderada, que nada mais é do que a soma das notas multiplicadas pelos seus pesos dividido pela soma dos pesos deve ser utilizada.
media_aritmetica_ponderada_A_B = (A * peso_A + B * peso_B) / (peso_A + peso_B)
'''

A = float(input())
B = float(input())
peso_A = 3.5
soma_A = A * peso_A
peso_B = 7.5
soma_B = B * peso_B
SOMA = soma_A + soma_B
SOMA_PESOS = peso_A + peso_B
media_aritmetica_A_B = SOMA / SOMA_PESOS 
print('MEDIA = {:.5f}'.format(media_aritmetica_A_B))
