import json

ARQUIVO = 'estoque.json'

def carregar_estoque():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, 'w') as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto(nome, quantidade, preco):
    estoque = carregar_estoque()
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.append(produto)
    salvar_estoque(estoque)
    print("✅ Produto adicionado com sucesso.")

def listar_produtos():
    estoque = carregar_estoque()
    if not estoque:
        print("📦 Estoque vazio.")
        return

    total = 0
    for i, p in enumerate(estoque):
        subtotal = p['quantidade'] * p['preco']
        total += subtotal
        print(f"{i + 1}. {p['nome']} - Qtd: {p['quantidade']}, Preço: R${p['preco']:.2f}, Subtotal: R${subtotal:.2f}")
    
    print(f"\n💰 Valor total do estoque: R${total:.2f}")

def menu():
    while True:
        print("\n📦 Controle de Estoque")
        print("1. Adicionar produto")
        print("2. Listar produtos e valor total")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))
                adicionar_produto(nome, quantidade, preco)
            except ValueError:
                print("❗Erro: Digite valores válidos para quantidade e preço.")

        elif opcao == '2':
            listar_produtos()

        elif opcao == '3':
            print("👋 Até mais!")
            break

        else:
            print("❗Opção inválida.")

if __name__ == '__main__':
    menu()
