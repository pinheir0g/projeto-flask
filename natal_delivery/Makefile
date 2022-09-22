rundev:
	poetry shell
	FLASK_DEBUG=True
	FLASK_APP=natal_delivery/app.py flask run

install:
	poetry install

test:
	pytest tests/ -v


installp:
	pip install --upgrade pip
	pip install --upgrade poetry


init_db:
	poetry shell FLASK_APP=natal_delivery/app.py flask create db
	poetry shell FLASK_APP=natal_delivery/app.py flask db upgrade