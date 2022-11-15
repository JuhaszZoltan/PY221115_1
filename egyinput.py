x_y = input('add meg az x és y értékét vesszővel elválasztva: ')
array = x_y.split(',')
x = int(array[0])
y = int(array[1])

print(f'{x} és {y} összege = {x + y}')