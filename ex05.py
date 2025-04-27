import json

ARQUIVO = 'contatos.json'

def carregar_contatos():
    try:
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_contatos(contatos):
    with open(ARQUIVO, 'w') as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(contato)
    salvar_contatos(contatos)
    print("✅ Contato adicionado com sucesso!")

def buscar_contato(nome_busca):
    contatos = carregar_contatos()
    resultados = [c for c in contatos if nome_busca.lower()_
