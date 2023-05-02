lista = ['D', 'S', 'E', 'Q']
banco = "BANCO DIGITAL"
palavra = "="
print("-="*15)
print(' ')
print(banco.center(41, " "))
print(' ')
print("-="*15)
print(' ')
sald = 0
saldp = 0
saldn = 0
saldf = 0
dep = 0
saq = 0
contando = 0
gru = 0
limiti = 500
saldon = 0
listadep = []
listasaq = []
print('[D] Depositar')
print('[S] Sacar')
print('[E] Extrato')
print('[Q] Sair')
print(' ')
while True:
	saldon = dep + limiti - saq
	saldf = saldp - saldn
	a = str(input('O que deseja fazer? ')).strip().upper()[0]
	if a == 'D':
		dep = float(input('Informe o valor do depósito: '))
		listadep.append(dep)
		listadep
		saldp = saldp + dep
	if gru < 3:
		if a == 'S':
			gru = gru + 1
			saq = float(input('Informe o valor do saque: '))
			if saq < saldon:
				saldn = saldn + saq
				listasaq.append(saq)
				listasaq
			else:
				print('Operação falhou ! Você não tem saldo suficiente. ')
				gru = gru - 1
				saq = saq - saq
	if a == 'E':
		for c in enumerate(listadep):
			print(f'Deposito: {c[1]:.2f}')
		for d in enumerate(listasaq):
				print(f'Saque: {d[1]:.2f}')
	if a == 'Q':
		break