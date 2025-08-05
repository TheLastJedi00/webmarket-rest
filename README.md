# 🧥 API Brechó – Backend com FastAPI

Este é o backend de uma aplicação web para um **brechó online**. A API está sendo desenvolvida com **FastAPI** e será responsável por gerenciar produtos, categorias, usuários, pedidos e outras funcionalidades essenciais para uma plataforma de **venda de roupas de segunda mão**.

> ⚠️ **Este projeto ainda está em desenvolvimento.** Mais funcionalidades serão adicionadas nas próximas etapas.

---

## 🚀 Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente e iniciar o servidor local usando `uvicorn`.

### 1. Clone o repositório

```bash
git clone https://github.com/TheLastJedi00/webmarket-rest.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual

# Windows:
.venv\Scripts\activate

# Linux/MacOS:
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode o servidor com Uvicorn

```bash
uvicorn main:app --reload
```

> Aqui, `main.py` deve ser o arquivo onde sua instância do FastAPI (`app = FastAPI()`) está definida.  
> O `--reload` faz com que o servidor reinicie automaticamente ao detectar mudanças no código – útil para desenvolvimento.

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
