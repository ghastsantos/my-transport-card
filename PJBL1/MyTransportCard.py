adminPassword = "senhadoadm"
myCredits = 0
ticketValue = 5

while True:
    entry = input("Bem-Vindo ao MyTransportCard. Você é usuário ou administrador?: ").lower()
    if entry == "administrador" or entry == "admin":
        print("Você está tentando entrar como administrador.")
        incorrectAttempts = 0
        remainingAttempts = 3
        while True:
            password = input("Digite a senha ou 1 para ir à tela inicial:")
            if password == adminPassword:
                print("Bem-vindo administrador!")
                break
            elif password == "1":
                break
            else:
                incorrectAttempts += 1
                remainingAttempts -= 1
                if incorrectAttempts >= 3:
                    print("Você excedeu o número máximo de tentativas. Encerrando o sistema por motivos de segurança, tente novamente mais tarde.")
                    exit()
                print(f"Sua senha é inválida. Você possui mais {remainingAttempts} tentativas, digite a senha correta ou 1 para ir à tela inicial: ")

        if password == adminPassword:
            while True:
                print("Escolha algumas das opções abaixo:")
                print("1 - Visualizar número de créditos")
                print("2 - Adicionar mais créditos")
                print("3 - Atualizar valor da passagem")
                print("4 - Pagar uma passagem")
                print("5 - Trocar de login")
                print("6 - Encerrar o programa")
                optionsMenu = input("Digite a opção desejada: ")

                if optionsMenu == "1":
                    print(f"Você possui {myCredits} créditos.")
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "2":
                    addCredits = input("Digite quantos créditos você deseja adicionar:")
                    myCredits += int(addCredits)
                    print('Créditos adicionados com sucesso!')
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "3":
                    ticketValue = input("Digite o novo valor da passagem:")
                    print('Valor da passagem alterado com sucesso!')
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "4":
                    if myCredits < int(ticketValue):
                        print("Você não possui créditos suficientes para pagar a passagem.")
                        seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    else:
                        myCredits -= int(ticketValue)
                        print("Passagem paga com sucesso!")
                        seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "5":
                    break
                elif optionsMenu == "6":
                    print("Encerrando o programa. Volte sempre!")
                    exit()
                else: 
                    print("Opção inválida. Tente novamente.")
                    continue

    elif entry == "usuario" or entry == "usuário":
        while True:
            userName = input("Digite o seu nome ou 1 para ir à tela inicial: ")
            if userName.isalpha():
                print(f"Bem-vindo {userName}!")
                break
            elif userName == "1":
                break
            else:
                print("Digite um nome com apenas letras ou 1 para ir à tela inicial.")

        if userName.isalpha():
            while True:
                print("Escolha algumas das opções abaixo:")
                print("1 - Adicionar mais créditos")
                print("2 - Pagar uma passagem")
                print("3 - Trocar de login")
                print("4 - Encerrar o programa")
                optionsMenu = input("Digite a opção desejada: ")

                if optionsMenu == "1":
                    addCredits = input("Digite quantos créditos você deseja adicionar:")
                    myCredits += int(addCredits)
                    print('Créditos adicionados com sucesso!')
                    seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "2":
                    if myCredits < int(ticketValue):
                        print("Você não possui créditos suficientes para pagar a passagem.")
                        seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    else:
                        myCredits -= int(ticketValue)
                        print("Passagem paga com sucesso!")
                        seeMenu= input('Pressione qualquer tecla para ver o menu novamente: ')
                    if seeMenu == '':
                        continue
                elif optionsMenu == "3":
                    break
                elif optionsMenu == "4":
                    print("Encerrando o programa. Volte sempre!")
                    exit()
                else: 
                    print("Opção inválida. Tente novamente.")
                    continue
    else:
        print("Entrada inválida. Tente novamente.")