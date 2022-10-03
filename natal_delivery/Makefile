rundev:
	FLASK_DEBUG=True
	poetry shell
	FLASK_APP=natal_delivery/app.py flask run
shdev:
	FLASK_APP=natal_delivery/app.py
	poetry shell

install:
	poetry install

test:
	pytest tests/ -v


installp:
	pip install --upgrade pip
	pip install --upgrade poetry


init_db:
	FLASK_APP=natal_delivery/app.py flask create db
	FLASK_APP=natal_delivery/app.py flask db upgrade