const linhas = document.querySelectorAll('.linha');
const detalhes = document.querySelectorAll('.mais')

function clicou(linha) {
    // muda o estilo da linha selecionada
    linhas.forEach(element => {
        element.classList.remove('selecionado');
    });

    let selecionado = document.getElementById(linha);
    let mostrar = document.getElementById('produto-'+linha);

    console.log(mostrar);
    mostrar.classList.add('ativo');
    selecionado.classList.add('selecionado');

    let voltar = document.getElementById('voltar-'+linha);
    voltar.addEventListener('click', () => {
        mostrar.classList.remove('ativo');
        selecionado.classList.remove('selecionado');
    });
};
