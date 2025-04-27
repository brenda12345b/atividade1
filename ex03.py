import json
import string

ARQUIVO = 'assentos.json'
LINHAS = 5
COLUNAS = 5

def inicializar_assentos():
    mapa = {}
    for i in range(LINHAS):
        for j in range(1, COLUNAS + 1):
            assento = f"{string.ascii_uppercase[i]}{j}"
            mapa[assento] = "L"  # L = Livre
    salvar_mapa(mapa)

def carregar_mapa():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        inicializar_assentos()
        return carregar_mapa()

def salvar_mapa(mapa):
    with open(ARQUIVO, 'w') as f:
        json.dump(mapa, f, indent=4)

def mostrar_mapa(mapa):
    print("\n🗺️  Mapa de Assentos (L = Livre, R = Reservado):")
    for i in range(LINHAS):
        linha = string.ascii_uppercase[i]
        for j in range(1, COLUNAS + 1):
            assento = f"{linha}{j}"
            status = mapa[assento]
            print(f"{assento}[{status}]", end="  ")
        print()

def reservar_assento(mapa, codigo):
    if codigo not in mapa:
        print("❗Assento inválido.")
    elif mapa[codigo] == "R":
        print("❌ Assento já reservado.")
    else:
        mapa[codigo] = "R"
        salvar_mapa(mapa)
        print("✅ Assento reservado com sucesso.")

def cancelar_reserva(mapa, codigo):
    if codigo not in mapa:
        print("❗Assento inválido.")
    elif mapa[codigo] == "L":
        print("ℹ️ Esse assento já está livre.")
    else:
        mapa[codigo] = "L"
        salvar_mapa(mapa)
        print("✅ Reserva cancelada.")

def menu():
    while True:
        print("\n🎟️ Sistema de Reservas de Evento")
        print("1. Ver mapa de assentos")
        print("2. Reservar um assento")
        print("3. Cancelar uma reserva")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        mapa = carregar_mapa()

        if opcao == '1':
            mostrar_mapa(mapa)
        elif opcao == '2':
            mostrar_mapa(mapa)
            codigo = input("Digite o código do assento (ex: A1): ").upper()
            reservar_assento(mapa, codigo)
        elif opcao == '3':
            mostrar_mapa(mapa)
            codigo = input("Digite o código do assento a liberar: ").upper()
            cancelar_reserva(mapa, codigo)
        elif opcao == '4':
            print("👋 Tchau!")
            break
        else:
            print("❗Opção inválida.")

if __name__ == '__main__':
    menu()

