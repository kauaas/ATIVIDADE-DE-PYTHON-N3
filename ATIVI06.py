N1=int(input("digite um número: "))
N2=int(input("digite outro número: "))
while N2<N1:
	N1=int(input("digite um número: "))
	N2=int(input("digite outro número: "))
else:
	for i in range(N1,N2,1):
		print(i)
