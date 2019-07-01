inventory = {'gold' : 500,'backpack' : ['dagger', 'bedroll','bread']}

inventory['pocket'] = ['coin', 'map', 'shell']
del inventory['backpack'][0]
inventory['gold'] += 50
print(inventory)

# dodaj do slownika klucz "pocket"
# pod klucz "pocket" wpisz liste zawierajaca "coin", "map", "shell"
# usun 'dagger' z 'backpack'
# dodaj 50 do numeru pod 'gold'
