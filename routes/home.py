from flask import Blueprint, render_template, url_for
import os
from python.produtos import lista_produtos, lista_sessoes

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    sessao = lista_sessoes()
    produtos = lista_produtos()
    return render_template('index.html', produtos=produtos, sessao=sessao)
