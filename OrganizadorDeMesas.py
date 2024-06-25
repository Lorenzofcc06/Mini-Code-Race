def menu():
    print("Knirsch Culinárias")
    print('''
    1 - Reservar mesa
    2 - Remover reserva
    3 - Removar todas reservas
    4 - Modificar a reserva
    5 - Mostrar as mesas reservadas
    6 - Mostrar mesas disponíveis
    7 - Sair
    
    ''')
    opcao = int(input("Digite uma opção: "))
    return opcao


def reservaMesa(mesasP,mesasM,mesasG):
    nome_reserva = input("Digite o nome e sobrenome para sua reserva: ").upper()
    quantidade = int(input("Digite a quantidade de pessoas: "))
    soma = len(mesasP) + len(mesasM) + len(mesasG)
    if soma >= 8:
        print("Atingimos o total de reservas")
    if quantidade <= 0:
        print("Erro")
    elif quantidade <= 2:
        mesasP.append(nome_reserva)
        print("Uma mesa pequena foi reservada!")
    elif quantidade > 2 and quantidade <= 4:
        mesasM.append(nome_reserva)
        print("Uma mesa média foi reservada!")   
    elif quantidade > 4:
        mesasG.append(nome_reserva)
        print("Uma mesa grande foi reservada!")
    return mesasP, mesasM, mesasG

def removerReserva(mesasP, mesasM, mesasG,mesasUsadas):
    print(f"Mesas Pequenas reservadas = {mesasP}")
    print(f'Mesas médias reservadas: {mesasM}')
    print(f'Mesas grandes reservadas: {mesasG}')
    remova = input("Digite o nome e sobrenome da sua reserva:").upper()
    if remova in mesasP:
        mesasP.remove(remova)
        mesasUsadas += 1
    elif remova in mesasM:
        mesasM.remove(remova)
        mesasUsadas += 1
    elif remova in mesasG:
        mesasG.remove(remova)
        mesasUsadas += 1
    else:
        print("A reserva não existe")
    return mesasP,mesasM,mesasG,mesasUsadas

def removerTudo(mesasP,mesasM,mesasG,mesasUsadas):
    mesasUsadas +=  len(mesasP) + len(mesasM) + len(mesasG)
    mesasP = []
    mesasM = []
    mesasG = []
    print("Todas reservas foram removidas!")
    return mesasP,mesasM, mesasG, mesasUsadas

def modifiarReserva(mesasP,mesasM,mesasG):
    print(f"Mesas Pequenas reservadas = {mesasP}")
    print(f'Mesas médias reservadas: {mesasM}')
    print(f'Mesas grandes reservadas: {mesasG}')
    modifica = input("Digite o nome e sobrenome da reserva que deseja modificar: ").upper()
    if modifica in mesasP:
        mudar = int(input("Digite quantas pessoas a mesa tera agora: "))
        if mudar > 0 and mudar <= 2:
            print(f"Agora sua mesa sera reservada para {mudar}")
        elif mudar > 2 and mudar <= 4:
            mesasP.remove(modifica)
            mesasM.append(modifica)
            print(f"Sua reserva foi movida para uma mesa média de {mudar}")
        elif mudar > 4:
            mesasP.remove(modifica)
            mesasG.append(modifica)
            print(f"Sua reserva foi movida para uma mesa grande de {mudar}")
        else:
            print("Erro numero invalido")
    elif modifica in mesasM:
        mudar = int(input("Digite quantas pessoas a mesa tera agora: "))
        if mudar > 0 and mudar <= 2:
            mesasM.remove(modifica)
            mesasP.append(modifica)
            print(f"Sua reserva foi movida para uma mesa pequena de {mudar}")
        elif mudar > 2 and mudar <= 4:
            print(f"Agora sua mesa sera reservada para {mudar}")
        elif mudar > 4:
            mesasM.remove(modifica)
            mesasG.append(modifica)
            print(f"Sua reserva foi movida para uma mesa grande de {mudar}")
        else:
            print("Erro numero invalido")
    elif modifica in mesasG:
        mudar = int(input("Digite quantas pessoas a mesa tera agora: "))
        if mudar > 0 and mudar <= 2:
            mesasG.remove(modifica)
            mesasP.append(modifica)
            print(f"Sua reserva foi movida para uma mesa pequena de {mudar}")
        elif mudar > 2 and mudar <= 4:
            mesasG.remove(modifica)
            mesasM.append(modifica)
            print(f"Sua reserva foi movida para uma mesa média de {mudar}")
        elif mudar > 4:
            print(f"Agora sua mesa sera reservada para {mudar}")
        else:
            print("Erro numero invalido")
    return mesasP,mesasM,mesasG
def mostrarReservadas(mesasP,mesasM,mesasG):
    print(f"Mesas Pequenas reservadas = {mesasP}")
    print(f'Mesas médias reservadas: {mesasM}')
    print(f'Mesas grandes reservadas: {mesasG}')

def mostrarQuantas(mesasP,mesasM,mesasG):
    dispo = 8
    soma = len(mesasP) + len(mesasM) + len(mesasG)
    total = dispo - soma
    print(f"O total de mesas disponíveis é de {total} mesas!")
    return total

def main():
    mesasP = []
    mesasM = []
    mesasG = []
    quantidade = 0
    opcao = 0
    mesasUsadas = 0
    while True:
        opcao  = menu()
        if opcao == 1:
            mesasP,mesasM,mesasG = reservaMesa(mesasP,mesasM,mesasG)
        elif opcao == 2:
            mesasP,mesasM,mesasG,mesasUsadas = removerReserva(mesasP,mesasM,mesasG,mesasUsadas)
        elif opcao == 3:
            mesasP,mesasM,mesasG,mesasUsadas = removerTudo(mesasP,mesasM,mesasG,mesasUsadas)
        elif opcao == 4:
            mesasP,mesasM,mesasG = modifiarReserva(mesasP,mesasM,mesasG)
        elif opcao == 5:
            mostrarReservadas(mesasP,mesasM,mesasG)
        elif opcao == 6:
            quantidade = mostrarQuantas(mesasP,mesasM,mesasG)
        elif opcao == 7:
            print(f"O total de mesas usadas foi de {mesasUsadas} mesas")
            break
main()
