# Secure Django REST Graph QL API and template

A Django project with 4 models and a GraphQL API (Graphene-Django).

## Tech stack

- Python 3
- Django
- Graphene-Django (GraphQL)
- Graphene
- psycopg2 (PostgreSQL)
- Database: PostgreSQL

## Project structure

- `research_publications_mgt/`: project settings and root URLs
- `api/`: Django app
- `publications/`: Django app
- `reviews/`: Django app
- `users/`: Django app
- Tests: `api/tests.py`, `publications/tests.py`, `reviews/tests.py`, `users/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Publication` | `publications` | title, abstract, pub_date, authors, summary |
| `Author` | `publications` | name, email, affeliation, orcId |
| `UserManager` | `users` | — |
| `User` | `users` | name, email, role |

## URL routes

Declared in `urls.py`:

- `/token/`
- `/token/refresh/`
- `/blog/`
- `/users/`
- `/login/`
- `/logout/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
