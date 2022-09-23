'''
Para a resolução do problema '1002 - Area of a Circle' deduzirei a fórmula da área do círculo (A = π * R²), onde π ≅ 3.14159.
Inicialmente, desenhe um círculo.
Note que um círculo pode ser dividido em vários triângulos iguais. Utilizarei como notação que o círculo pode ser dividido em n triângulos iguais.
Perceba que, em uma aproximação grosseira, a área do círculo é n vezes a área do triángulo desenhado.
No entanto, os triângulos não comportam todo o espaço do círculo. É visível que colado à base de cada triângulo existe um espaço não comportado.
Desenhe um triângulo com base menor. Teste desenhar círculos divididos em triângulos com bases cada vez menores.
Consegue visualizar que quanto menor a base do triângulo desenhado, maior é a sua altura, maior é o número de triângulos e menor o espaço não comportado?
Sendo assim, o que aconteceria se o círculo fosse dividido em n triângulos com base muito pequena?
Utilizando a lógica de limites, é possível perceber que n tenderia ao infinito, então:
A = lim  (n * b * h / 2)
      n -> ∞
Note que, ao dividir o círculo em infinitos triângulos de base muito pequena, a soma das bases é aproximadamente igual ao comprimento da circunferência.
Por definição, π = C / D. C é o comprimento da circunferência e D é o diâmetro da circunferência.
Por definição, R = D / 2. R é o raio da circunferência
Rearranjando as variáveis, temos: C = 2 * π * R.
Então, n * b ≅ 2 * π * R.
Note que, ao dividir o círculo em infinitos triângulos de base muito pequena, a altura de cada triângulo é aproximadamente igual ao raio da circunferência.
Então, h ≅ R.
Juntando as duas expressões, temos: A = C * R / 2, ou A = 2 * π * R * R / 2, ou ainda A = π * R².

=> Conclusão:
Deduzimos que a Área do Círculo é dada pela fórmula A = π * R².
Introduzi o uso de bibliotecas com a função pow da biblioteca math. Esta função é equivalente à potenciação habitual.
'''

from math import pow
R = float(input())
π = 3.14159
A = π * pow(R, 2)
print('A={:.4f}'.format(A))
