const imagem = document.getElementById('img');
const previw = document.getElementById('previw');


if(imagem) {
    imagem.addEventListener("change", () => {
        if(imagem.files) {
            const img = imagem.files[0];
            console.log(img);
            if(img['size'] < 2097152) {
                const leitor = new FileReader();

                console.log(img['size']);

                leitor.onload = () => {
                    previw.src = leitor.result;
                }
                
                leitor.readAsDataURL(img);
            } else {
                alert('Erro! \nArquivo muito grande. Maximo suportado 2MB.');
            }
        }
    });

    previw.addEventListener('click', () => {
        imagem.click();
    });
}

const nova_imagem = document.querySelector('#nova-img');
const novo_previw = document.querySelector('#edit-previw');

if(nova_imagem) {
    nova_imagem.addEventListener("change", () => {
        if(nova_imagem.files) {
            const n_img = nova_imagem.files[0];
            console.log(n_img);
            if(n_img['size'] < 2097152) {
                const n_leitor = new FileReader();

                console.log(n_img['size']);

                n_leitor.onload = () => {
                    novo_previw.src = n_leitor.result;
                }
                
                n_leitor.readAsDataURL(n_img);
            } else {
                alert('Erro! \nArquivo muito grande. Maximo suportado 2MB.');
            }
        }
    });

    novo_previw.addEventListener('click', () => {
        console.log({'status': 'clicou'});
        nova_imagem.click();
    });
}
