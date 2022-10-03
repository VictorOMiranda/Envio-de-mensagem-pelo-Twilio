import pandas as pd
from twilio.rest import Client

#abrindo os arquivos por mês

lista_meses= ['janeiro', 'fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas= pd.read_excel(f'{mes}.xlsx')
    if(tabela_vendas['Vendas']>55000).any():
        vendedor =tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendedor'].values[0]
        vendas=tabela_vendas.loc[tabela_vendas['Vendas']>55000,'Vendas'].values[0]
        print (f'No mês de {mes} o Vendedor:{vendedor}, bateu a meta e vendeu o total de: {vendas}' )

# Your Account SID from twilio.com/console
account_sid = "AC839c528e8dcfafabb208d7663b336a69"
# Your Auth Token from twilio.com/console
auth_token  = "df405034f950980f66ddc2fdd1ce8fed"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5511numero de celular",
    from_="+19893941609",
    body='f'No mês de {mes} o Vendedor:{vendedor}, bateu a meta e vendeu o total de: {vendas}' ' )

print(message.sid)