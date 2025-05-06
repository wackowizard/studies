'''import math
angulo = float(input('Digite um ângulo qualquer: '))
angulo_radiano = math.radians(angulo)
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)
print('O ângulo de {:.0f} tem o seno de {:.2f}'. format(angulo, seno))
print('O ângulo de {:.0f} tem o cosseno de {:.2f}'. format (angulo, cosseno))
print('O ângulo de {:.0f} tem a tangente de {:.2f}'. format(angulo, tangente))'''
#acima como eu fiz de primeira, abaixo uma forma mais prática
from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))



