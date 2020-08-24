from datetime import datetime, timedelta

data_atual = datetime.now()
print(data_atual)
print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
print(data_atual.strftime('%c'))
print(data_atual.weekday)

tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
print(tupla[data_atual.weekday()])

nova_data = datetime.now() - timedelta(days = 365)
print(nova_data)
