from random import choice
def polynomial(k):   
  with open ('poly2.txt', 'a', encoding='utf-8') as my_f:      
    for i in range(k, 1, -1):
      n = choice(range(0,10))
      z = choice(range(0, 2))
      if n == 0:
        my_f.write(f'')
      else: 
        if z == 0:          
          my_f.write(f'{n}*x^{i} + ')
        else:
          my_f.write(f'{n}*x^{i} - ')    
    if n == 0:
      my_f.write(f'') 
    else:  
      my_f.write(f'{n}') 
    my_f.write(f' = 0\n')