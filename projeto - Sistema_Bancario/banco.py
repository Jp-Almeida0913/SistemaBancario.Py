import os, time

#### Funções ####
def timer(mensagem):
    global titulo
    i=1
    for x in range(1,4):
        print(titulo.center(51, "_"))
        print(f"{mensagem}Voltando ao inicio: " , i)
        time.sleep(3)
        os.system('cls')
        i-=1


def deposito(quantia_depositar):
    global extrato
    if quantia_depositar <= 0:
        msg = "Operação inválida, valor negativo. "
        timer(msg)
    else:
        extrato += quantia_depositar
        valores_depositados.append(quantia_depositada)
        msg = "Deposito realizado com sucesso."
        timer(msg)


def saque(quantia_sacada, titulo):
    global extrato, x, valores_saques, numero_saque
    print(titulo.center(51, "_"))
    if extrato <=0:
        msg = "Operação inválida, saldo insuficiente. "
        timer(msg)   
    elif quantia_sacada >500 or quantia_sacada <=0:
        msg = "Operação inválida, valor fora dos limites.\nLimites: Minímo R$1,00 e Máximo R$500,00\n"
        timer(msg)
    else:
        numero_saque +=1
        os.system('cls')
        extrato -= quantia_sacada
        valores_saques.append(quantia_sacada)
        msg = "Saque realizado com sucesso. "
        timer(msg)


def verificar_extrato():
    global  extrato, numero_saque, numero_deposito, valores_saques, valores_depositados
    print (f"Salto da conta: R${extrato:.2f}")
    if numero_deposito <=0 and numero_saque <= 0:
        print("\n\nNão foram realizadas movimentações.")
    else:
        print("Transações realizadas:")
        for x in range (0, numero_saque):
            print(f"Saque: R${valores_saques[x]:.2f}")
            x+=1
        for  x in range (0, numero_deposito):
            print(f"Deposito: R${valores_depositados[x]:.2f}")


#### Código Estruturado ####

## Váriaveis ##
extrato = 1500.00
numero_saque = 0
numero_deposito = 0
valores_saques = []
valores_depositados = []


## Laço de repetição principal ##
while True:
    titulo ="BOAS VINDAS"
    print(titulo.center(51, "_"))
    mensagem = f"""
Selecione uma operação para prosseguir: 
1) Verificar Extrato
2) Realizar Depósito
3) Realizar Saque ({numero_saque}/3)
4) Sair do Sistema

"""

    flag = input(f"{mensagem}-->")
    os.system('cls')
    try: 
        flag = int(flag)
    except:
        print("Digite apenas números...")
        time.sleep(3)
        os.system('cls')
    
    
    # Opções #
    match flag:
        case 1:
            titulo = "Extrato"
            print(titulo.center(51, "_"))
            verificar_extrato()
            flag = input("\n\n\nDigite qualquer coisa para continuar ")
            os.system('cls')
            
        case 2:
            numero_deposito +=1
            titulo = "DEPOSITO"
            print(titulo.center(51, "_"))
            quantia_depositada = float(input("Insira o valor que deseja depositar:\n\n-->"))
            os.system('cls')
            deposito(quantia_depositada)
            
        case 3:
            titulo = "SAQUE"
            if numero_saque > 2:
                msg="Máximo de saques realizados"
                timer(msg)
            else:
                print(titulo.center(51, "_"))
                quantia_sacada = float(input("Insira o valor que deseja sacar:\n\n-->"))
                saque(quantia_sacada, titulo)
                os.system('cls')

        case 4:
            os.system('cls')
            i=3
            for x in range(1,4):
                print("Encerrando... em: " , i)
                time.sleep(1)
                os.system('cls')
                i-=1
            break ##Realiza Break no While
        
        case _:
            print("Opção Inválida")
            time.sleep(1)
            os.system('cls')

## Finalização ##
print("Encerrado")