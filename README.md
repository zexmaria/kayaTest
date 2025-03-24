# Projeto Kaya Doc (teste para backend jr)
***

## 💻 Sobre o Projeto
***

Este é um projeto feito com Python, Django e Tailwindcss. O projeto é um teste da empresa Kaya onde precisei replicar a página https://kayadoc.com/medicos/ e a página de perfil de algum dos médicos (ex: https://kayadoc.com/medicos/23/perfil/) usando Tailwindcss e Templates do Django para servir essas páginas no localhost.

Aqui você encontra um passo a passo para **clonar**, **instalar** e **rodar** o projeto no seu computador.
***
## Observações iniciais:
* O site foi desenvolvido baseado na versão **<u>Desktop</u>** e para rodar perfeitamente apenas nesta resolução(1024px). Não é garantido que funcionará bem em resolução diferente (tablet ou mobile).

* O site foi feito de forma dinâmica onde o banco de dados precisará ser populado para que seja apresentado de forma correta.

* O tutorial a seguir foi pensado para sistemas Linux, não testado para Windows ou macOS.

***
## Pré-requisitos


* Python 3.10+
* PIP
* Django 5+
* Node.js 22.14+
* NPM
* Tailwindcss 3.4.17
***

## 🛠️  Instalações necessárias:

### 🐍Python 3.10 ou superior
Verifique se o Python está instalado.


No Linux, abra o terminal e digite: 

``` python3 --version```

Se aparecer Python 3.10 ou maior, você já tem! Se não, siga os passos abaixo.

1. Atualize o sistema:

``` sudo apt update && sudo apt upgrade -y ```

2. Instale o Python 3.10:

``` sudo apt install python3.10 -y```

3. Verifique se o PIP está instalado:

``` pip --version```

Se não estiver instalado, siga os passos abaixo:

``` sudo apt install python3-pip -y```


### 🧩Git

1. Verifique se o Git está instalado.

No terminal digite: 

````git --version````

* Caso não apareça nenhuma versão instalada, digite:

````sudo apt install git -y````

### ⚙️Node.js
1. Verifique se o Node.js e o NPM está instalado.

````node -v````

````npm -v````


* Caso não apareça nenhuma versão instalada, siga os passos abaixo: 


2. Baixe o instalador Node.js 20.x LTS (atual estável em 2025)

No terminal digite:

````curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -````


3. Instale o Node.js:

No terminal digite:

````sudo apt install -y nodejs````


4. Verifique se o Node.js e o npm foram instalados:

````node -v````

````npm -v````
***
## 🛠️ Instalando Aplicação Localmente

### 1. Clone o repositório
No terminal, clone o repositório usando um dos métodos abaixo:

Clone com HTTPS:

````git clone https://github.com/zexmaria/kayaTest.git````

Clone com SSH:

````git@github.com:zexmaria/kayaTest.git````

### 2. Acesse a Pasta do Projeto
Navegue até a pasta do projeto:

````cd KayaTest````

### 3. Crie um ambiente virtual com VENV
Instale um ambente virtual com  o nome de sua preferência. Como exemplo estarei usando o nome ".meuvenv"

````python3 -m venv .meuvenv````

Ative o ambiente virtual:

````source .meuvenv/bin/activate````


### 4. Instale as dependências
Com ambiente virtual ativo, instale as dependências do projeto com o comando abaixo:

````pip install -r requirements.txt````

### 5. Instale o Tailwindcss v3
1. Use o comando abaixo para instalar o Tailwind.:

```` npm install -D tailwindcss@3 ````


2. Para ativar o Tailwind, use o comando abaixo:


````npx tailwindcss -i ./core/static/css/input.css -o ./core/static/css/output.css --watch````

***
## ⚙️Rodando o Projeto
1. Execute os seguintes comandos para aplicar as migrações e iniciar o servidor:

````python manage.py migrate````

```python manage.py runserver```

2. Acesse o localhost pelo browser com o seguinte endereço:

http://127.0.0.1:8000/

3. Para acessar o painel administrativo do Django, crie um superusuário em outro terminal e com o venv ativado, usando o comando:

````python manage.py createsuperuser````

O terminal irá solicitar que você insira um nome de usuário, endereço de e-mail e senha para o superusuário. Preencha as informações conforme solicitado.

4. Acesse o painel administrativo do Django com o seguinte endereço:

http://127.0.0.1:8000/admin/

5. Após fazer login como superusuario, cadastre alguns médicos para usar a aplicação com todas suas funcionalidades 
***



