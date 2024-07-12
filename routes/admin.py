from flask import Blueprint, render_template, url_for, request, jsonify
from python.produtos import lista_produtos, salva_imagem, salvar_dados, pegar_dados, atualizar_dados, deletar

admin_route = Blueprint('admin', __name__)

@admin_route.route('/')
def admin():
    " html que mostra a lista de produtos e os butões adicionar, editar e deletar produtos "
    produtos = lista_produtos()
    return render_template('admin.html', produtos=produtos)


@admin_route.route('/adicionar')
def add_produto():
    " formulário para adicionar novo produto "
    return render_template('admin_add.html')


@admin_route.route('/adicionar/update', methods=['POST'])
def add_update():
    " adiconar novo produto ao banco de dados "
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    sessao = request.form.get('sessao')
    
    imagem = request.files['img']
    salva_imagem(imagem, nome)
    salvar_dados(imagem, nome, preco, sessao)
    
    return render_template('add_sucess.html', nome=nome)


@admin_route.route('/<int:produto_id>/editar')
def edit_produto(produto_id):
    " formulário para atualizar um produto selecionado "
    
    dados = pegar_dados(produto_id)
    
    return render_template('admin_edit.html', dados=dados)


@admin_route.route('/<int:produto_id>/update', methods=['POST'])
def edit_update(produto_id):
    " atualizar o produto selecionado "
    nome = request.form.get('novo-nome')
    preco = request.form.get('novo-preco')
    sessao = request.form.get('nova-sessao')
    img = request.files['nova-img']
    
    imagem = pegar_dados(produto_id)['imagem']
    
    if img:
        salva = salva_imagem(img, nome)
        if salva == 'erro':
            return 'ERRO AO SALVAR A IMAGEM'
        else:
            salva_imagem(img, nome)
    atualizar_dados(produto_id, imagem, nome, preco, sessao)
    
    return render_template('edit_sucess.html', nome=nome, func='Editado')


@admin_route.route('/<int:produto_id>/deletar')
def delet_produto(produto_id):
    " deletar um produto selecionado "
    imagem = pegar_dados(produto_id)['imagem']
    nome = pegar_dados(produto_id)['nome']
    img = f'./static/{imagem}'
    
    deletar(produto_id, img)
    
    return render_template('edit_sucess.html', nome=nome, func='Deletado')
