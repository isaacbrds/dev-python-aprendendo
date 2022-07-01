frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan, rafael, carol, camila'

palavras1 = frase1.split()
palavras2 = frase2.split(',')

print(palavras1, palavras2)

print(','.join(palavras1))
print(' &'.join(palavras2))