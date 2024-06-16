from flask import Flask, render_template
import openpyxl
import matplotlib as plt
import webbrowser

app = Flask(__name__)

@app.route('/')
#Coletando dados
def index():
#     class Produto:
#         def __init__(self, nome, descricao,preco, imagens):
#             self.nome = nome
#             self.preco = preco
#             self.link = descricao
#             self.imagens = imagens

    
#     MeusProdutos = []
#     workbook = openpyxl.load_workbook('dados.xlsx')
#     sheet = workbook['Disponíveis']
#     nomes = []
#     links = []
#     categoria = []

#     for contador in range(6,30):
#         conteudoA = sheet['A' + str(contador)].value
#         conteudoB = sheet['B' + str(contador)].value
#         conteudoC = sheet['C' + str(contador)].value
#         conteudoD = sheet['D' + str(contador)].value
# #
#         nomes.append(Produto(conteudoA, conteudoB,conteudoC,conteudoD))
    class Produto:
            def __init__(self, nome, descricao,preco, imagens):
                self.nome = nome
                self.preco = preco
                self.link = descricao
                self.imagens = imagens
            def __str__(self):
                return f'{self.nome} / {self.preco} / {self.link} / {self.imagens}'

    workbook = openpyxl.load_workbook('dados.xlsx')
    sheet = workbook['Disponíveis']
    nomes = []
    links = []
    base = []
    contador = 4

    #coleta de dados
    while(1):
        nome = sheet['A' + str(contador)].value
        if nome == ':':
            break
        preço = sheet['B' + str(contador)].value
        descricao = sheet['C' + str(contador)].value
        imagens = sheet['D' + str(contador)].value
        #print(conteudo)
        conteudo = Produto(nome,preço, descricao,imagens)
        base.append(conteudo)
        contador += 1
    for i in base:
        print(i)


    # Crie uma nova lista contendo apenas os elementos não nulos
    base_filtrada = [produto for produto in base if produto.nome is not None]

    # Agora base_filtrada contém apenas os elementos com nome não nulo
    for produto in base_filtrada:
        print(produto)
    base = base_filtrada

    categoria = {}  # Crie um dicionário vazio
    cont = len(base)
    memoria = 0
    NomeMemoria = base[memoria].nome
    NomeCategoria = [NomeMemoria]
    # Inicialize o contador
    for i in range(cont):
        #print(NomeMemoria)
        if base[i].nome == ";":
            # Use a fatia de base para criar uma nova lista de produtos
            categoria[NomeMemoria] = base[memoria+1:i]
            if i + 1 < len(base):
                memoria = i + 1  # Atualize a posição de memória
                NomeMemoria = base[memoria].nome  
                NomeCategoria.append(NomeMemoria)
            else:
                break



    return render_template('index.html', nome = categoria, categorias =  NomeCategoria)


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
