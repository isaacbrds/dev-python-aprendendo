frase = 'Olá, bem vindo a este treinamento!'

print(frase.split())

hashtag = 'music #guitar #gamer #coder #python'

print(hashtag.split())
print(hashtag.split('#'))
print(hashtag.split('#', 3))

hashtag_separadas_por_espaco = hashtag.split(' ')
print(','.join(hashtag_separadas_por_espaco))
print('.'.join(hashtag_separadas_por_espaco))
print(' '.join(hashtag_separadas_por_espaco))