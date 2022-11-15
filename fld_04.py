arfolyam = float(input('€ árfolyama: '))
forint = int(input('ennyi HUF-ot szeretnénk átváltani: '))

print(f'ez {round(forint/arfolyam, 2)} €-t ér')