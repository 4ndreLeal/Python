'''
A função print() é embutida no Python e recebe argumentos predefinidos em sua estrutura que, na maioria dos casos, não são modificados pelo usuário.
O estado inicial dos métodos da função print() se adequam ao que a maioria dos usuários necessitam e, portanto, raramente são modificados.
No entanto, para fins de aprofundamento na sintaxe e lógica em Python, note:
O estado inicial da função print() é print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False).
Para resolução do problema '1000 - Hello World!' é necessário focar apenas nos métodos objects, sep e end.
De forma didática, objects (objetos) representa a(s) String(s) que queremos imprimir. No problema 1000 temos apenas um objeto, representado por: 'Hello World!'.
Note que a String 'Hello World!' é equivalente à concatenação das Strings 'Hello' e 'World!'. Entendeu o porquê da chave se chamar objects?
O método sep é uma abreviação para separator (separador). Este método define como os objectos serão separados na String inteira que aparece na tela.
Por fim, o método end (fim) define como a String inteira será encerrada.
Note que, por padrão, a String inteira é separada com um espaço em branco e, ao percorrer todo o tamanho da String, finaliza com uma quebra de linha.

=> Conclusão:
O método completo da função print() para imprimir 'Hello World!' seria: print('Hello', 'World!', sep=' ', end='\n', file=sys.stdout, flush=False).
Como todos os métodos já estão embutidos, poderiamos apenas utilizar: print('Hello World!').
'''

print('Hello World!')
