print('Lanches Martins')
print('Cardápio:')
print('combo 01, combo 02, combo 03')

preco = {'combo 01': 20, 'combo 02': 23, 'combo 03': 27}

pedido = input('Digite o pedido: ').lower().strip()

total = 0
for item in pedido.split(','):
    item = item.strip()
    if item in preco:
        total += preco[item]
        print(f'✅ {item}: +R${preco[item]}')
    else:
        print(f'❌ {item}: não encontrado')

print(f'Total: R${total}')
