import PySimpleGUI as sg
import sqlite3

sg.theme('Reddit')

# Conexão com o banco de dados

conexao = sqlite3.connect('produtos.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        categoria TEXT NOT NULL
    )
''')

conexao.commit()

# Categorias de produtos

product_categories = ["Eletrônicos", "Móveis", "Roupas", "Brinquedos", "Comida", "Bebidas", 
                      "Cosméticos", "Livros", "Esportes", "Jardinagem"]

# NOVO

def salvar_produto(cliente, produto, quantidade, categoria):
    # Salvar os dados no banco de dados
    
    cursor.execute('''
            INSERT INTO produtos (cliente, produto, quantidade, categoria)
            VALUES (?, ?, ?, ?)
        ''', (cliente, produto, quantidade, categoria))

    conexao.commit()

    sg.popup('Produto cadastrado com sucesso!')
    
def mostrar_produtos():

    cursor.execute('SELECT * FROM produtos')

    produtos = cursor.fetchall()

    layout_produtos = [
        [sg.Table(
            values=produtos,
            headings=['ID', 'Cliente', 'Produto', 'Quantidade', 'Categoria'],
            auto_size_columns=True,
            num_rows=10
        )],
        [sg.Button('Fechar')]
    ]

    janela_produtos = sg.Window('Produtos Cadastrados', layout_produtos)

    while True:
        evento, valores = janela_produtos.read()

        if evento == sg.WIN_CLOSED or evento == 'Fechar':
            break

    janela_produtos.close()


# Interface do usuário
layout = [
    [sg.Text('Cliente',size=(6,0)),sg.Input(key='1',size=(20,0))],
    [sg.Text('Produto',size=(6,0)),sg.Input(size=(20,0),key='2')],
    [sg.Text('Quantidade'),sg.Input(key='3',size=(3,0))],
    [sg.Text('Categoria do Produto'), sg.Combo(product_categories, key='4')],
    [sg.Button('Salvar')],

    # NOVO
    [sg.Button('Ver Produtos')]

]

window = sg.Window('Cadastro de Produtos',layout)

# Loop de eventos

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        if values['1'] == '' or values['2'] == '' or values['3'] == '' or values['4'] == '':
            sg.popup('Por favor, preencha todos os campos.')
        else:
            salvar_produto(values['1'], values['2'], values['3'], values['4'])
            window['1'].update('')
            window['2'].update('')
            window['3'].update('')
            window['4'].update('')

# NOVO
    elif event == 'Ver Produtos':
        mostrar_produtos()

# Fecha o banco de dados

conexao.close()
window.close()

# colocar botão de delete para apagar registro no banco de dados, e colocar botão de editar para editar registro no banco de dados
# colocar mais informações "cpf, endereço, telefone" no cadastro de produtos
# acrescentar uma caixa onde possa selecionar se o cliente é pessoa física ou jurídica, e se for pessoa jurídica, acrescentar o campo "CNPJ" no cadastro de produtos
# acrescentar uma caixa de pesquisa para pesquisar produtos cadastrados no banco de dados
# acrescentar uma caixa para selecionar  a forma de pagamento (dinheiro, cartão, pix, boleto) no cadastro de produtos
# acrescentar uma caixa onde selecione se já foi pago ou não.
