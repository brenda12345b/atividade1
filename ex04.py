import json
from datetime import datetime
import getpass

ARQUIVO = 'usuarios.json'

def carregar_usuarios():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO, 'w') as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(usuarios):
    usuario = input("Nome de usuário: ")
    if usuario in usuarios:
        print("❗Usuário já existe.")
        return
    senha = getpass.getpass("Senha: ")
    usuarios[usuario] = {
        'senha': senha,
        'saldo': 0.0,
        'transacoes': []
    }
    salvar_usuarios(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

def login(usuarios):
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ")
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        print(f"🔐 Login bem-sucedido! Bem-vindo(a), {usuario}.")
        menu_bancario(usuario, usuarios)
    else:
        print("❌ Usuário ou senha incorretos.")

def registrar_transacao(usuario, usuarios, tipo, valor):
    transacao = {
        'tipo': tipo,
        'valor': valor,
        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    usuarios[usuario]['transacoes'].append(transacao)

def menu_bancario(usuario, usuarios):
    while True:
        print("\n🏦 Menu Bancário")
        print("1. Ver saldo")
        print("2. Depósito")
        print("3. Saque")
        print("4. Extrato")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            saldo = usuarios[usuario]['saldo']
            print(f"💰 Saldo atual: R${saldo:.2f}")

        elif opcao == '2':
            valor = float(input("Valor do depósito: "))
            if valor > 0:
                usuarios[usuario]['saldo'] += valor
                registrar_transacao(usuario, usuarios, 'Depósito', valor)
                salvar_usuarios(usuarios)
                print("✅ Depósito realizado.")
            else:
                print("❗Valor inválido.")

        elif opcao == '3':
            valor = float(input("Valor do saque: "))
            if 0 < valor <= usuarios[usuario]['saldo']:
                usuarios[usuario]['saldo'] -= valor
                registrar_transacao(usuario, usuarios, 'Saque', valor)
                salvar_usuarios(usuarios)
                print("✅ Saque realizado.")
            else:
                print("❗Saldo insuficiente ou valor inválido.")

        elif opcao == '4':
            print("📄 Extrato de Transações:")
            for t in usuarios[usuario]['transacoes']:
                print(f"{t['data']} - {t['tipo']}: R${t['valor']:.2f}")

        elif opcao == '5':
            print("👋 Saindo da conta...")
            break
        else:
            print("❗Opção inválida.")

def menu():
    usuarios = carregar_usuarios()
    while True:
        print("\n🔐 Sistema Bancário")
        print("1. Cadastrar usuário")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            login(usuarios)
        elif opcao == '3':
            print("👋 Até logo!")
            break
        else:
            print("❗Opção inválida.")

if __name__ == '__main__':
    menu()
