# TP2 - Travail collaboratif avec GitLab

Application web REST developpee avec **FastAPI** (Python 3.10+). Elle sert de
software de reference pour la mise en place de la chaine CI/CD.

## Description

L'application expose des endpoints REST qui renvoient du JSON :

| Methode | Endpoint                 | Auteur | Description                                      |
|---------|--------------------------|--------|--------------------------------------------------|
| GET     | `/`                      | Leader | Verifie que l'application tourne                  |
| GET     | `/addition?a=1&b=2`      | Dev1   | Retourne la somme de `a` et `b`                   |
| GET     | `/greeting?name=X`       | Dev2   | Salue `X` et renvoie hostname + IP du serveur     |

### Exemples de reponses

`GET http://localhost:8008/`

```json
{"message": "it works !"}
```

`GET http://localhost:8008/addition?a=1&b=2`

```json
{"result a+b=": 3, "developer": "Dev1"}
```

`GET http://localhost:8008/greeting?name=X`

```json
{"message": "Hello X", "developer": "Dev2", "hostname": "pc-name", "IP": "192.168.0.x"}
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows  (source venv/bin/activate sous Linux/Mac)
pip install -r requirements.txt
```

## Lancer l'application

```bash
uvicorn main:app --reload --port 8008
```

L'application est alors disponible sur http://localhost:8008
La documentation interactive (Swagger) est sur http://localhost:8008/docs

## Lancer les tests

```bash
pytest -v
```
