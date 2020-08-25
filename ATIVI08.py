print("calcule a quantidade ds numeros impares e pares")
PAR=0
IMPAR=0
for i in range(5):
    numero = int(input(" informe um numero: "))
    if(numero%2==0):
          PAR=PAR+1
    else:
        IMPAR=IMPAR+1
print("Números pares {}".format(PAR))
print("Números impares {}".format(IMPAR))
