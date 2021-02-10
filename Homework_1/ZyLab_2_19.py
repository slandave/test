#Santiago Landaverde
#1856681

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print('')
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar")
print('')

new_servings = float(input("How many servings would you like to make?\n"))
print('')
p = new_servings/servings
new_lemon_juice = lemon_juice * p
new_water = water * p
new_agave_nectar = agave_nectar * p
print('Lemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')
print('{:.2f}'.format(new_lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(new_water), 'cup(s) water')
print('{:.2f}'.format(new_agave_nectar), 'cup(s) agave nectar')
print('')

print('Lemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')
print('{:.2f}'.format(new_lemon_juice/16), 'gallon(s) lemon juice')
print('{:.2f}'.format(new_water/16), 'gallon(s) water')
print('{:.2f}'.format(new_agave_nectar/16), 'gallon(s) agave nectar')

