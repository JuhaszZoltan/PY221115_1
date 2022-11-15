fogy = float(input('ennyit eszik az autó 100-on: '))
b_ar = int(input('ennyibe kerül egy liter benzin (HUF): '))
ut = float(input('ennyi Km-t szeretnénk megtenni: '))

koltseg = ut * ar * fogy / 100

print(f'útiköltség: {round(koltseg)} HUF')