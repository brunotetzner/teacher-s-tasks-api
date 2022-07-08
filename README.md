# Teacher-s-tasks - Bruno Tetzner :boom:

API desenvolvida para funcionar como uma lista de tarefas. Visando ajudar professores a gerenciarem sua rotina acadêmica.

## :hammer: Tecnologias utilizadas :wrench:

- Python
- Flask
- PostgreSQL
- Psycopg-2 binary
- SQLAlchemy



# Rodando o projeto

> Para rodar essa aplicação é necessário ter o python na versão 3.8 ou acima. Também é necessário ter o PostgreSQL instalado na sua maquina.

Após clonar o repositório, crie e inicie o ambiente virtual:
```
python -m venv venv
```

```
source venv/bin/activate
```

Após iniciado, o prefixo '(venv)' deverá aparecer no inicio do caminho das pastas no terminal.

Após isso instale as dependências do arquivo requirements.txt
```
pip install -r requirements.txt
```
Crie um arquivo `.env` tendo como base o arquivo `.env.example`. Crie um banco de dados e preencha a variável de ambiente `SQLALCHEMY_DATABASE_URI` com as informações do seu banco.

exemplo:
```
SQLALCHEMY_DATABASE_URI=postgresql://jonDoe:1234@localhost:5432/teacher_db
```
Depois basta rodar as migrations do projeto:
```
flask db upgrade
```

Por fim basta rodar o projeto com o comando:

```
flask run
```

Caso prefira, você também pode usar o link do deploy:

- [Deploy](https://teacher-s-tasks.herokuapp.com)


## Documentação das rotas

Essa aplicação tem quatro rotas, sendo elas:
- Postagem de uma tarefa
- Edição de uma tarefa
- Exclusão de uma tarefa
- Listagem de tarefas

### Criação de tarefa:
`[POST] BASEURL/api/tasks`

```
{
 "title":"finish work",
"description":"finish work to students",
"finish_date":"25/12/2022"
}
```

Se tudo correr bem o retorno será:
Status: `201`
```
{
  "id":1
   "title":"Reunião de professores",
  "description":"Reunião semestral de professores no colégio municipal",
   "finish_date":"25/12/2022"
}
```

### Edição de tarefas de tarefa:
`[PATCH] BASEURL/api/tasks/1`

> Não se esqueça de passar o id da tarefa!

```
{
   "title":"Palestra para os professores",
}
```

Se tudo correr bem o retorno será:
Status: `200`
```
{
  "id":1
  "title":"Palestra para os professores",
  "description":"Reunião semestral de professores no colégio municipal",
  "finish_date":"25/12/2022"
}
```

### Listagem de tarefas:
`[GET] BASEURL/api/tasks`

```
no body
```


Se tudo correr bem o retorno será:
Status: `200`
```
[
  {
    "id":1
     "title":"Palestra para os professores",
    "description":"Reunião semestral de professores no colégio municipal",
    "finish_date":"25/12/2022"
  }
]
```

### Apagando uma tarefa:
`[DELETE] BASEURL/api/tasks/1`

> Não se esqueça de passar o id da tarefa!

```
no body
```


Se tudo correr bem o retorno será:

Status:`204`
```
no body
```
