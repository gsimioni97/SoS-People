from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Ajuda:
    def __init__(self, id, nome, icon, tipo, descricao):
        self.id = id
        self.nome = nome
        self.icon = icon
        self.tipo = tipo
        self.descricao = descricao

#ajuda1 = Ajuda(0,'Roger Felix Lombo','glyphicon-usd','Ajuda com dinheiro','Preciso de ajuda para comprar meus remédios')
#ajuda2 = Ajuda('Zilda Pereira Lima','glyphicon-cutlery','Ajuda com alimentação','Necessito de 10KG de alimento')
#ajuda3 = Ajuda('Marcos Pedro de Souza','glyphicon-home','Ajuda com moradia','Preciso de um lugar para morar com a minha família')
#ajuda4 = Ajuda('Rodrigo Leme','glyphicon-map-marker','Ajuda com transporte','Gostaria de voltar para minha família')
#ajuda5 = Ajuda('Maria Santana','glyphicon-tint','Ajuda com água','Estamos sem agua limpa para beber')
#ajuda6 = Ajuda('ONG Boa Ajuda','glyphicon-usd','Ajuda com dinheiro','Precisamos de recursos financeiros para a ONG')

#lista2 = [ajuda1, ajuda2, ajuda3, ajuda4, ajuda5, ajuda6]
lista = []






@app.route('/')
def inicio():
    return render_template('index.html',  conteudos=lista)



@app.route('/form')
def form():
    return  render_template('form.html')



@app.route('/criar', methods=['POST',])
def criar():
    id = len(lista)
    nome = request.form['InputNome']
    tipo = request.form['inputAjuda']
    if tipo == 'Ajuda com alimentação':
        icon = 'glyphicon-cutlery'
    elif tipo == 'Ajuda com dinheiro':
        icon = 'glyphicon-usd'
    elif tipo == 'Ajuda com moradia':
        icon = 'glyphicon-home'
    elif tipo == 'Ajuda com transporte':
        icon = 'glyphicon-map-marker'
    else:
        icon = 'glyphicon-tint'
    descricao = request.form['InputDescricao']
    ajuda = Ajuda(id, nome, icon, tipo, descricao)
    lista.append(ajuda)
    return redirect('/')

app.run(debug=True)