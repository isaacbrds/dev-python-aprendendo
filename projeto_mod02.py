from datetime import datetime
import random
usuario = input('Digite o nome do usuário: ')
idade = input('Digite a idade do usuário: ')
data_aniversario = datetime.strptime(input('Digite sua data de aniversário: '), '%d/%m/%Y')
data_cadastro = datetime.now()
data_cadastro_ptbr = datetime.strftime((data_cadastro), '%d/%m/%Y')
cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']

cartao_usuario = random.choice(cartoes)


print(f'''Olá {usuario}, seu registro foi concluído com sucesso no dia {data_cadastro_ptbr}.
Parabéns, houve um sorteio e você ganhou um cartao no valor de {cartao_usuario}''')