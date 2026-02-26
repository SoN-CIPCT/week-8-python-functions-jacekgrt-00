def sandwich_maker(ingrs):
  print(f'\nEdit your ingredients by modifying the list below. Here is your sandwich:')
  for ingr in ingrs:
    print(f'*{ingr}')

sandwich1 = ['italian bread', 'bacon', 'lettuce', 'tomato', 'cheddar', 'honey mustard']
sandwich2 = ['sourdough bread', 'ham', 'lettuce', 'tomato', 'pickles','gouda', 'ranch']
print(sandwich_maker(sandwich1))
print(sandwich_maker(sandwich2))