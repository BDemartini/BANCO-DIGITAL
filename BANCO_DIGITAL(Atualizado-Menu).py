import time
lista = ['D', 'S', 'E', 'Q']
banco = "\033[1;33mBANCO DIGITAL\033[m"
palavra = "="
print("\033[1;33m-=\033[m"*13)
print(' ')
print(banco.center(30, " "))
print(' ')
print("\033[1;33m-=\033[m"*13)
print('')
print('\033[1;36m• [R] Registro\033[m')
print('\033[1;32m• [L] Loguin\033[m')
print('')
print("-="*13)
CPF = name = 0
acabast = 1
while acabast == 1:
	reg_log = input('Registro ou Loguin ? ').upper()[0]
	if reg_log == 'L':
		info_conta = {CPF:name}
		CPF = int(input('Digite seu CPF: '))
		info_conta = {CPF:name}
		while CPF != name:
			if CPF != name:
				print('Esta conta não foi encontrada, tente novamente ou crie uma conta: ')
				break
			elif CPF == name:
				print(f'Olá {nome}.')
				while reg_log == 'R':
					CPF = str(input('Digite seu CPF: '))
					name = str(input('Digite seu nome: '))
					confirm = str(input('As informações estão corretas?[s/n] ')).strip().upper()[0]
					break
					if confirm == 'N':
						print('Aguarde um instante...')
						time.sleep(1)
					if confirm == 'S':
						print('\033[4;35mAgradeçemos o registro!!\033[m')
						break
	elif reg_log == 'R':
		CPF = str(input('Digite seu CPF: '))
		name = str(input('Digite seu nome: '))
		confirm = str(input('As informações estão corretas?[s/n] ')).strip().upper()[0]
		if confirm == 'N':
			print('Aguarde um instante...')
			time.sleep(1)
		if confirm == 'S':
			print('\033[4;35mAgradeçemos o registro!!\033[m')
			while 'L':
					info_conta = {CPF:name}
					info_conta_certo = CPF
					ksdt = info_conta[CPF]
					print(ksdt)
					reconh = str(input('Digite seu CPF: '))
					if reconh == info_conta_certo:
						print(f'Olá, {name}')
						acabast = acabast - 1
						break
					else:
						print('Conta não encontrada')
						break
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
print('')
print('-='*7)
print('[D] Depositar')
print('[S] Sacar')
print('[E] Extrato')
print('[Q] Sair')
print('-='*7)
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