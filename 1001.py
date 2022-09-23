'''
Python é uma linguagem fortemente tipada e com tipagem dinâmica. O que significa isso?
Ser fortemente tipada é uma característica das linguagens que não permitem que um tipo de dado seja tratado como outro tipo. 
Exemplo: 
Concatenar 3 (Inteiro) com '3' (String) é um erro de tipagem (TypeError) em Python.
Tipagem dinâmica é uma característica das linguagens que, na declaração de dados, não recebem nenhuma especificação do tipo, realizando tal assimilação dinamicamente.
Exemplo: 
Na linguagem C, você pode e deve declarar variáveis especificando o tipo (int inteiro, float ponto_flutuante, char letra). 
Em Python seria: (inteiro = 3, ponto_flutuante = 3.5, nome = 'André').

=> Conclusão:
Para fins de robustez da linguagem, o "ideal" seria uma tipagem estática e forte, mas não existe o ideal quando você pode obter o mesmo resultado de incontáveis formas.
A linguagem Python, muito utilizada na atualidade, realiza múltiplas tarefas a partir de uma tipagem forte e dinâmica.
No problema 1001, quase tudo é solucionado a partir dessa lógica. 
Outro conhecimento necessário é a noção do método cast(), responsável por garantir que o dado será do tipo que precisamos.
Exemplo & Desafio:
O que será impresso na tela?
variavel = '3'
cast_variavel = int(variavel)
print(cast_variavel)
Por fim, introduzo o método .format(), responsável por formatar a String adicionando o conteúdo da variável desejada. Essa é apenas uma das formas de formatação.
'''

A = int(input())
B = int(input())
X = A + B
print('X = {}'.format(X))
