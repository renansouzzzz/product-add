produtos = {1: ''}

def add_produto(codigo, nome):
    produtos.update({codigo : nome})


print('Deseja adicionar ou apagar algum produto?')



resposta = input("(1) Adicionar - (2) Apagar : ")

if resposta == '1':
    print('Digite o código e o número do produto que deseja adicionar: ')
    codigo = input()
    nome = input()
    add_produto(codigo, nome)


if resposta == '2':
    print('Digite o código e o número do produto que deseja apagar: ')
    codigo = input()
    nome = input()
    del(codigo, nome)

print(produtos)