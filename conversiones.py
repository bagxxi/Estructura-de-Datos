#Ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar mediante sys.argv
# en el siguiente orden: Sol, Peso Argentino, Dólar Americano

import sys

pen = float(sys.argv[1])
usd = float(sys.argv[2])
ars = float(sys.argv[3])
clp = float(sys.argv[4])




clp_a_pen = clp * pen #0.0046

clp_a_ars = clp * ars #0.093

clp_a_usd = clp * usd #0.00013

print(f''.center(100, "="))
print(f'CONVERSION DE DIVISAS'.center(100, "="), end='\n\n')
print(f'Los $ {clp:.0f} pesos chilenos equivalen a: '.center(100, " "), end='\n\n')
print(f'{clp_a_pen:.1f} Soles Peruanos (/s, PEN)'.center(100, " "))
print(f'{clp_a_ars:.1f} Pesos Argentinos ($, ARS)'.center(100, " "))
print(f'{clp_a_usd:.1f} Dólares Estadounidenses ($, USD)'.center(100, " "), end='\n\n')
print(f''.center(100, "="))
print(f''.center(100, "="))
