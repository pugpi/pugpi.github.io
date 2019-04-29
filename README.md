# Python User Group - Piauí

Este repositório hospeda o código para o  site do [Python User Group - Piauí](https://pugpi.github.io/). Estamos aqui porque gostaríamos que você também contribuísse conosco.

![Um pug com um chapéu nordestino apontando o dedo para cima, com a sigla PUG-PI](https://avatars2.githubusercontent.com/u/5644128?s=400&v=4)

O site é feito com  [Pelican](http://getpelican.com/) - um gerador de site estático escrito em Python - e usa um tema chamado [Alchemy](https://github.com/nairobilug/pelican-alchemy).

## Executando

A maneira mais fácil de fazer isso é usando um [ambiente virtual](http://docs.python-guide.org/en/latest/dev/virtualenvs/) Python. Nós recomendamos usar [`pyenv`](https://github.com/yyuu/pyenv) with [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) para configurá-lo. Felizmente `pyenv` tem um instalador automático, [pyenv-installer](https://github.com/yyuu/pyenv-installer).

### Ambiente virtual

Uma vez que você tem `pyenv` instalado, crie um ambiente virtual para conter o Pelican e suas dependências:

    $ pyenv virtualenv pugpi
    $ pyenv activate pugpi

Isso cria um ambiente virtual e então ativa-o.

### Forkar / Clonar o repositório

Se você não o tem localmente ainda, clone este repositório.

    $ git clone https://github.com/pugpi/pugpi.github.io.git

### Instalar os requisitos

Use `pip` para instalar a lista de dependências (incluindo o Pelican) em seu ambiente virtual:

    $ pip install -r requirements.txt

### Gerar o site

Agora que as dependências existem, nós podemos dar build:

    $ make html

Isso pega os arquivos markdown do diretório `content/` e gera páginas HTML estáticas dentro do diretório `output/`.

### Visualizar o site

Você pode servir o site gerado previamente em seu navegador:

    $ make serve

Você o acessará em: [http://localhost:8000](http://localhost:8000).

## Contribuindo com o Blog

Se você tem interesse em escrever um post para o Blog do PUG-PI, você precisa:

- [Fork](https://github.com/pugpi/pugpi.github.io/fork) o repositório do **PUG-PI**.
- Escreva um post usando markdown no diretório `content`. Observe o padrão do markdown em outros posts já criados. Tente segui-lo.
- Dê push das mudanças para uma branch, como `why-i-love-python`, em *seu* fork do repositório.
- Abra um [pull request](https://help.github.com/articles/using-pull-requests/) para a branch `master`.

Nós apreciamos a sua contribuição!

## Contato / Ajuda

Se você tiver problemas com sua configuração, você pode obter ajuda criando uma [issue](https://github.com/pugpi/pugpi.github.io/issues/new).
