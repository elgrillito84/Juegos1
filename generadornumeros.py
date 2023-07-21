import random
numero1= float(input("¿Cuál es el afortunado?"))
numero2= random.randint (1,432823)
if numero1%2==0:
    numero1=numero1*numero2
    numero1=numero2-numero1
    numero1=numero1%numero2
    print (numero1)
