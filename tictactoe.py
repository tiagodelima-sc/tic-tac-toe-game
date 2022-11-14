from os import system

def main():
	print('\n1) Novo Jogo\n2) Instruções\n3) Sair\n')
	
	while True:
		try:
			opcao = int(input('Opção: '))
			if opcao < 1 or opcao > 3:
				raise ValueError				
			break

		except ValueError:
			print('Digite uma das opções acima')

	if opcao == 1:
		novo_jogo()
	elif opcao == 2:
		instrucoes()
	else:
		exit()
	
def novo_jogo():
	players = [input('\nNome do Primeiro Jogador (X): '),input('Nome do Segundo Jogador (O): ')]
	posicoes = [' ' for i in range(9)]
	vez = 1

	tabuleiro(posicoes)
	
	while not verifica_ganhou(posicoes):

		if ' ' not in posicoes:
			print('Vix, deu Velha! O jogo empatou.\n')
			jogar_novamente()

		print('Rodada do Player %s'% players[0])
		while True:
			try:
				jogada = int(input('posição -> '))

				if jogada < 1 or jogada > 9:
					raise ValueError
				elif posicoes[jogada-1] != ' ':
					print('ERRO! Essa posição ja foi usada')
					continue

				break	
			except ValueError:
				print('POSIÇÃO INVALIDA!. Digite uma posição entre 1 e 9')

		players.reverse()
		if vez == 1:
			posicoes[jogada-1] = 'X'
			vez = 2
		else:
			posicoes[jogada-1] = 'O'
			vez = 1

		tabuleiro(posicoes)
	
	print('Vencedor: %s\n'%players[1])
	jogar_novamente()

def instrucoes():
	system('cls')
	print('\nPara escolher a posição, utilize os numeros a seguir:\n')
	tabuleiro([1,2,3,4,5,6,7,8,9])
	print('\nA cada rodada, o jogador deverá escolher uma posição para jogar com seu sinal X ou O.')
	main()

def tabuleiro(pos):
	print("\n")
	print(' %s | %s | %s'%(pos[0],pos[1],pos[2]))
	print(' ----------- ')
	print(' %s | %s | %s'%(pos[3],pos[4],pos[5]))
	print(' ----------- ')
	print(' %s | %s | %s'%(pos[6],pos[7],pos[8]))
 
	print("\n")
	print(' 1 | 2 | 3')
	print(' ----------- ')
	print(' 4 | 5 | 6')
	print(' ----------- ')
	print(' 7 | 8 | 9')
	print()

def verifica_ganhou(elem):
	if elem[0] == elem[1] == elem[2] and elem[0] != ' ':
		ganhar = True
	elif elem[3] == elem[4] == elem[5] and elem[3] != ' ':
		ganhar = True
	elif elem[6] == elem[7] == elem[8] and elem[6] != ' ':
		ganhar = True
	elif elem[0] == elem[3] == elem[6] and elem[0] != ' ':
		ganhar = True
	elif elem[1] == elem[4] == elem[7] and elem[1] != ' ':
		ganhar = True
	elif elem[2] == elem[5] == elem[8] and elem[2] != ' ':
		ganhar = True	
	elif elem[0] == elem[4] == elem[8] and elem[0] != ' ':
		ganhar = True
	elif elem[2] == elem[4] == elem[6] and elem[2] != ' ':
		ganhar = True 
	else:
		ganhar = False

	return ganhar

def jogar_novamente():
	while True:
		jogar = input('Deseja Jogar Novamente? \n1) Sim\n2) Não\n')
		if jogar == '2':
			print('\nSaindo do Jogo')
			exit()

		elif jogar == '1':
			novo_jogo()
		else:
			print('Opção Inválida, digite novamente.')


if __name__=='__main__':
	main()