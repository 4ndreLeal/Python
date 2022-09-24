'''
As principais operações matemáticas estão presentes na sintaxe do Python de forma muito intuitiva.
Veja:
A + B (Soma dos valores da classe int ou float armazenados nas variáveis A e B. Se A e B forem Strings, o sinal de soma é utilizado para concatená-las em uma só String).
A - B (Subtração dos valores da classe int ou float armazenados nas variáveis A e B).
A * B (Multiplicação dos valores da classe int ou float armazenados nas variáveis A e B. Se, por exemplo, A for String e B for número, a string A é repetida B vezes).
A / B (Divisão real dos valores da classe int ou float armazenados nas variáveis A e B. Se A e B forem inteiros, a divisão real se equivale à divisão inteira).
A // B (Divisão inteira dos valores da classe int ou float armazenados nas variáveis A e B. O resultado será inteiro mesmo que pelo menos um deles seja real).
A ** B (Exponenciação dos valores da classe int ou float armazenados nas variáveis A e B).
A % B (Resto da divisão dos valores da classe int ou float armazenados nas variáveis A e B).
É importante referir que algumas das operações também podem ser realizadas com o aproveitamento de métodos presentes em bibliotecas importáveis do Python.
Exemplo:
from math import pow
exponenciacao = pow(A, B)
As linhas 12 e 13 equivalem a A ** B.

=> Conclusão:
Para solucionar o problema '1003 - Simple Sum' basta utilizar o operador matemático de soma '+'.
'''

A = int(input())
B = int(input())
SOMA = A + B
print('SOMA = {}'.format(SOMA))
