"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

Quantas_notas = (input ("Digite o numero de notas: "))

Nota_1 = float(input ("Digite a nota 1: "))
Nota_2 = float(input ("Digite a nota 2: "))
Nota_3 = float(input ("Digite a nota 3: "))

Media = (Nota_1 + Nota_2 + Nota_3) / Quantas_notas

print(f"A média é: {Media:.2f}")
