from math import hypot
cat_op = float(input('Digite o valor do cateto oposto: '))
cat_ad = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(cat_op, cat_ad)
print('Sendo o cateto oposto {} e o cateto adjacente {}, então a hipotenusa é {:.2f}'.format(cat_op, cat_ad, hip))

