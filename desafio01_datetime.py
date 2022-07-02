from datetime import datetime

data_aniversario = datetime.strptime(input('Digite a data do seu aniversário: '), '%d/%m/%Y')

data_atual = datetime.now()  
meu_niver = data_aniversario - data_atual
print(meu_niver.days)