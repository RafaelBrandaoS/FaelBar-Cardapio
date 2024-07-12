from python.conexao import criar_conexao, fechar_conexao
from werkzeug.utils import secure_filename
import os


def lista_produtos():
    con = criar_conexao()
    cursor = con.cursor()
    sql = 'SELECT * FROM produtos order by sessao, nome'
    cursor.execute(sql)
    produtos = cursor.fetchall()
    cursor.close()
    con.commit()
    fechar_conexao(con) 
    return produtos


def lista_sessoes():
    produtos = lista_produtos()
    sessao = []
    for produto in produtos:
        if produto[3] not in sessao:
            sessao.append(produto[3])
    return sessao


def salvar_dados(imagem, nome, preco, sessao):
    con = criar_conexao()
    nome_imagem = imagem.filename
    estenssao = nome_imagem.split('.')[1]
    cursor = con.cursor()
    img = os.path.join('imagens', 'produtos', {secure_filename(nome_imagem)})
    sql = "insert into produtos (nome, preco, sessao, img) values (%s, %s, %s, %s)"
    valores = (nome, preco, sessao, img)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)


def salva_imagem(imagem):
        try:
            nome_imagem = imagem.filename
            
            destino_final =  os.path.join('static', 'imagens', 'produtos')
            save = os.path.join(destino_final, secure_filename(nome_imagem))
            imagem.save(save)
        except:
            erro = 'erro'
            return erro


def pegar_dados(produto_id):
    con = criar_conexao()
    cursor = con.cursor()
    sql = f'select * from produtos where id = {produto_id}'
    cursor.execute(sql)
    d = cursor.fetchall()[0]
    cursor.close()
    fechar_conexao(con)
    dados = {'id': d[0], 'nome': d[1], 'preco': d[2], 'sessao': d[3], 'imagem': d[4]}
    return dados


def atualizar_dados(produto_id, imagem, nome, preco, sessao):
    con = criar_conexao()
    cursor = con.cursor()
    sql = f"update produtos set nome = '{nome}', preco = '{preco}', sessao = '{sessao}', img = '{imagem}'  where id = '{produto_id}'"
    cursor.execute(sql)
    cursor.close
    con.commit()
    fechar_conexao(con)


def deletar(produto_id, imagem=''):
    con = criar_conexao()
    cursor = con.cursor()
    sql = f"delete from produtos where id = {produto_id}"
    cursor.execute(sql)
    cursor.close()
    con.commit()
    fechar_conexao(con)
    os.unlink(imagem)
