import json
from datetime import datetime

ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(descricao, prazo):
    tarefas = carregar_tarefas()
    nova = {
        'descricao': descricao,
        'prazo': prazo,
        'concluida': False
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso.")

def listar_tarefas():
    tarefas = carregar_tarefas()
    tarefas_ordenadas = sorted(tarefas, key=lambda x: datetime.strptime(x['prazo'], '%Y-%m-%d'))
    for i, t in enumerate(tarefas_ordenadas):
        status = "✔️" if t['concluida'] else "❌"
        print(f"{i + 1}. [{status}] {t['descricao']} (Prazo: {t['prazo']})")

def marcar_concluida(indice):
    tarefas = carregar_tarefas()
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        salvar_tarefas(tarefas)
        print("✅ Tarefa marcada como concluída.")
    else:
        print("❗Índice inválido.")

def menu():
    while True:
        print("\n📋 Gerenciador de Tarefas")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Descrição: ")
            prazo = input("Prazo (YYYY-MM-DD): ")
            adicionar_tarefa(descricao, prazo)

        elif escolha == '2':
            listar_tarefas()

        elif escolha == '3':
            listar_tarefas()
            try:
                indice = int(input("Número da tarefa para marcar como concluída: ")) - 1
                marcar_concluida(indice)
            except ValueError:
                print("❗Digite um número válido.")

        elif escolha == '4':
            print("👋 Até logo!")
            break

        else:
            print("❗Opção inválida.")

if __name__ == '__main__':
    menu()
