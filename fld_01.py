irsz = input('irányítószám: ')
varos = input('település: ')
ktn = input('közterület neve: ')
ktj = input('közterület jellege: ')
hsz = input('házszám: ')

cim = irsz + " " + varos +", " + ktn + " " + ktj + " " + hsz + "."
print(cim)
print(f"{irsz} {varos}, {ktn} {ktj} {hsz}.")