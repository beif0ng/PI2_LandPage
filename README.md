# PI2_LandPage
Projeto desenvolvido pelo alunos da UNIVESP, para o projeto integrador 2.
Membros:
- Adriano Moreira de Lucena, RA: 2010805
- Danilo Camilo Stivalletti, RA: 2006442
- Gilvan Alves Barros, RA: 1823108
- Lucas Fernandes Sardão, RA: 2007614
- Patric Oberdan dos Santos, RA: 2003595
- Ricardo Henrique Leoni Medeiros, RA: 2002411
- Veridiana de Lima Carneiro, RA: 1819810
- Vinicius Samuel De Oliveira, RA: 2001417

O objetivo do nosso grupo é ampliar a visibilidade do polo na internet, e por isso desenvolvemos uma pagina web.


# Orientações(para rodar o projeto em localhost) 

## 1- Criar ambiente virtual
 - abrir a pasta do projeto no terminal
 - criar ambiente virtual (powershell - terminal VsCode)
     - python -m venv venv
 - Ativar o venv
    - venv\Scripts\activate
    obs: funciona pelo windonws usando o vscode
    obs2: caso não execute o script de ativação fazer:
        - abrir o powershell do windonws como administrador e digitar o codigo abaixo
        - Set-ExecutionPolicy Unrestricted
        - digitar 'A' e enter.
        - reiniciar o VsCode
        - ativar o venv
        (tutorial: https://cursos.alura.com.br/forum/topico-venv-nao-monta-no-visual-studio-code-145318)

## 2- Instalar pacotes requeridos
 - Instalar requeriments (https://jtemporal.com/requirements-txt/)
    - pip install -r requirements.txt

## Para rodar aplicação flask(para não ter que resetar o flask run toda hora)
 - $env:FLASK_ENV = "development"
 - $env:FLASK_APP = "main.py"
 - flask run
    - Abrir navegador no endereço "Running on http://xxx.x.x.x:5000/" que aparecer
 - Ctrl + C para finalizar a aplicação
