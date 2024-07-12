from flask import Blueprint, render_template, url_for
import os
from python.produtos import lista_produtos, lista_sessoes

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    sessao = lista_sessoes()
    produtos = lista_produtos()
    imagem = produtos[4]
    imagem.split('/')
    imagem = imagem.split('/')
    imagem = os.path.join(imagem[0], imagem[1], imagem[2])
    return render_template('index.html', produtos=produtos, sessao=sessao, caminho_imagem=imagem)
