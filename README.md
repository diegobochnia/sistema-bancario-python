# Sistema Bancário em Python

Projeto de um sistema bancário desenvolvido em **Python**, criado com o objetivo de praticar lógica de programação, estruturas de dados, funções, CRUD e persistência de dados.

O projeto está atualmente **em desenvolvimento** e será construído de forma progressiva em três versões, aumentando a complexidade conforme novos conceitos forem aplicados.

## Funcionalidades planejadas

O sistema permitirá:

- Criar contas
- Listar contas
- Consultar uma conta
- Editar dados da conta
- Excluir contas
- Realizar depósitos
- Realizar saques
- Transferir valores entre contas
- Consultar extrato
- Validar saldo e operações

## Versões do projeto

### Versão 1 — Dados em memória

A primeira versão utilizará apenas Python.

Os dados das contas serão armazenados temporariamente em estruturas como listas e dicionários.

Objetivos:

- Praticar lógica de programação
- Trabalhar com funções
- Utilizar listas e dicionários
- Implementar operações CRUD
- Criar regras básicas de um sistema bancário

> Os dados serão perdidos quando o programa for encerrado.

---

### Versão 2 — Persistência com JSON

Na segunda versão, os dados passarão a ser armazenados em arquivos JSON.

Objetivos:

- Trabalhar com leitura e escrita de arquivos
- Implementar persistência de dados
- Manter contas e movimentações salvas após o encerramento do programa
- Organizar melhor a estrutura do sistema

---

### Versão 3 — Banco de dados

Na terceira versão, o armazenamento em JSON será substituído por um banco de dados.

Objetivos:

- Trabalhar com banco de dados
- Criar e consultar registros
- Atualizar e excluir informações
- Armazenar contas e transações de forma estruturada
- Aplicar conceitos de persistência de dados em uma aplicação real

## Tecnologias

- Python
- JSON
- Banco de dados *(planejado para a versão 3)*
- Git
- GitHub

## Estrutura planejada

```text
sistema-bancario-python/
│
├── versao-1/
│   └── main.py
│
├── versao-2/
│   └── main.py
│
├── versao-3/
│   └── main.py
│
└── README.md
