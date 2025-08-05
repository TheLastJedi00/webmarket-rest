# 🧥 API Brechó – Backend com FastAPI

Este é o backend de uma aplicação web para um **brechó online**. A API está sendo desenvolvida com **FastAPI** e será responsável por gerenciar produtos, categorias, usuários, pedidos e outras funcionalidades essenciais para uma plataforma de **venda de roupas de segunda mão**.

> ⚠️ **Este projeto ainda está em desenvolvimento.** Mais funcionalidades serão adicionadas nas próximas etapas.

---

## 🚀 Como rodar o projeto localmente

Você pode rodar o projeto de duas formas:

- [x] Usando ambiente virtual (`.venv`) + Uvicorn  
- [x] Usando Docker Compose

---

### 🐍 Opção 1 – Usando ambiente virtual e Uvicorn

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

#### 2. Crie e ative um ambiente virtual

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/MacOS:
source .venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Rode o servidor com Uvicorn

```bash
uvicorn app.main:app --reload
```

> Certifique-se de que o `app = FastAPI()` está no arquivo `main.py` dentro da pasta `app`.

---

### 🐳 Opção 2 – Usando Docker Compose

Certifique-se de ter o **Docker** e o **Docker Compose** instalados.  
Para subir o projeto com Docker, basta rodar:

```bash
docker compose up --build
```

Isso irá:

- Criar a imagem da aplicação com base no `Dockerfile`,
- Subir o container com a API rodando no ambiente correto,
- Expor a API (geralmente na porta `8008`).

---

## 🔮 Sobre o Projeto

O objetivo deste projeto é criar uma **API RESTful completa** que será usada por um site de brechó. As principais funcionalidades planejadas incluem:

- Cadastro e gerenciamento de produtos (roupas, acessórios, etc.);
- Cadastro de categorias (ex: camisetas, calças, vestidos...);
- Controle de estoque;
- Carrinho de compras;
- Processamento de pedidos;
- Autenticação e gerenciamento de usuários;
- Integração com um frontend para exibição e compra dos produtos.

---

## 📌 Requisitos

- Python 3.10 ou superior
- pip
- virtualenv (opcional, mas recomendado)
- uvicorn
- FastAPI

---

## 📂 Estrutura Inicial do Projeto

```
webmarket-rest/
│
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── users.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

Em construção 🪚.

---
