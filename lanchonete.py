print('Lanches Martins')
print('Cardápio')
print('Combo 01 (x-bacon,refrigerante,batatas')
print('Combo 02 (x-tudo,refrigerante,batatas')
print('Combo 03 (x-cheddar,refrigerante,batatas')

preco= {'combo 01': 20,'combo 02':23,'combo 03': 27
    }

pedido=input('Digite o seu pedido:')
total= 0
itens=pedido.split(',')

if pedido in preco:
  total+=preco[pedido]
  
else:i
    print('Não encontramos no cardápio')

print(total)
