# API Playlist

API REST para gerenciamento de playlists, construída com **Django 6.1** e **Django REST Framework**.
Permite cadastrar álbuns e músicas, relacionar músicas a um álbum e marcar faixas como favoritas.

## Tecnologias

- Python 3
- Django 6.1
- Django REST Framework 3.18
- djangorestframework-simplejwt 5.5
- SQLite (banco padrão de desenvolvimento)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/fabianossilvasantos/API-Playlist.git
cd API-Playlist
```

Crie e ative um ambiente virtual:

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Aplique as migrations:

```bash
python manage.py migrate
```

Crie um superusuário para acessar o admin (opcional):

```bash
python manage.py createsuperuser
```

Rode o servidor:

```bash
python manage.py runserver
```

A API fica disponível em `http://127.0.0.1:8000/api/` e o admin em `http://127.0.0.1:8000/admin/`.

## Modelos

### Album

| Campo            | Tipo         | Descrição                        |
| ---------------- | ------------ | -------------------------------- |
| `id`             | integer      | Identificador (somente leitura)  |
| `titulo`         | string (200) | Título do álbum                  |
| `ano_lancamento` | integer      | Ano de lançamento                |
| `musicas`        | lista        | Músicas do álbum (somente leitura) |

### Musica

| Campo              | Tipo         | Descrição                                 |
| ------------------ | ------------ | ----------------------------------------- |
| `id`               | integer      | Identificador (somente leitura)           |
| `titulo`           | string (200) | Título da música                          |
| `artista`          | string (150) | Nome do artista                           |
| `duracao_segundos` | integer      | Duração em segundos                       |
| `favorita`         | boolean      | Marca a faixa como favorita (padrão `false`) |
| `album`            | integer      | ID do álbum relacionado (opcional)        |

Uma música pode existir sem álbum. Ao excluir um álbum, suas músicas são excluídas junto (`on_delete=CASCADE`).

## Endpoints

Todas as rotas ficam sob o prefixo `/api/`.

### Músicas

| Método   | Rota                  | Descrição                     |
| -------- | --------------------- | ----------------------------- |
| `GET`    | `/api/musicas/`       | Lista todas as músicas        |
| `POST`   | `/api/musicas/`       | Cria uma música               |
| `GET`    | `/api/musicas/{id}/`  | Detalha uma música            |
| `PUT`    | `/api/musicas/{id}/`  | Atualiza uma música por completo |
| `PATCH`  | `/api/musicas/{id}/`  | Atualiza campos específicos   |
| `DELETE` | `/api/musicas/{id}/`  | Remove uma música             |

### Álbuns

| Método   | Rota                 | Descrição                        |
| -------- | -------------------- | -------------------------------- |
| `GET`    | `/api/albuns/`       | Lista todos os álbuns            |
| `POST`   | `/api/albuns/`       | Cria um álbum                    |
| `GET`    | `/api/albuns/{id}/`  | Detalha um álbum e suas músicas  |
| `PUT`    | `/api/albuns/{id}/`  | Atualiza um álbum por completo   |
| `PATCH`  | `/api/albuns/{id}/`  | Atualiza campos específicos      |
| `DELETE` | `/api/albuns/{id}/`  | Remove um álbum e suas músicas   |

## Exemplos de uso

Criar um álbum:

```bash
curl -X POST http://127.0.0.1:8000/api/albuns/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Acabou Chorare", "ano_lancamento": 1972}'
```

```json
{
  "id": 1,
  "titulo": "Acabou Chorare",
  "ano_lancamento": 1972,
  "musicas": []
}
```

Criar uma música vinculada ao álbum:

```bash
curl -X POST http://127.0.0.1:8000/api/musicas/ \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Tirando de Letra", "artista": "Novos Baianos", "duracao_segundos": 195, "favorita": true, "album": 1}'
```

```json
{
  "id": 1,
  "titulo": "Tirando de Letra",
  "artista": "Novos Baianos",
  "duracao_segundos": 195,
  "favorita": true,
  "album": 1
}
```

Consultar o álbum com as músicas aninhadas:

```bash
curl http://127.0.0.1:8000/api/albuns/1/
```

```json
{
  "id": 1,
  "titulo": "Acabou Chorare",
  "ano_lancamento": 1972,
  "musicas": [
    {
      "id": 1,
      "titulo": "Tirando de Letra",
      "artista": "Novos Baianos",
      "duracao_segundos": 195,
      "favorita": true,
      "album": 1
    }
  ]
}
```

Marcar uma música como favorita:

```bash
curl -X PATCH http://127.0.0.1:8000/api/musicas/1/ \
  -H "Content-Type: application/json" \
  -d '{"favorita": true}'
```

## Estrutura do projeto

```
API-Playlist/
├── config/              # Configuração do projeto Django
│   ├── settings.py
│   ├── urls.py          # Rotas raiz (admin + /api/)
│   ├── asgi.py
│   └── wsgi.py
├── playlist/            # App principal
│   ├── models.py        # Album e Musica
│   ├── serializers.py   # AlbumSerializer e MusicaSerializer
│   ├── views.py         # ViewSets com CRUD completo
│   ├── urls.py          # DefaultRouter da API
│   ├── admin.py
│   └── migrations/
├── manage.py
└── requirements.txt
```

## Estado atual

Projeto em desenvolvimento. Pontos ainda em aberto:

- **Autenticação**: o `simplejwt` já está configurado como classe de autenticação padrão, mas as rotas de obtenção e refresh de token ainda não foram registradas, e nenhuma permissão foi definida — hoje os endpoints estão abertos.
- **Testes**: `playlist/tests.py` ainda está vazio.
- **Configuração**: `SECRET_KEY` e `DEBUG` estão fixos no `settings.py`, adequado apenas para desenvolvimento local.
