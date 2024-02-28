# target:
#    some command for this tareget

ACTIVATE = source venv/bin/activate &&

venv:
	python3.12 -m venv venv
	$(ACTIVATE) \
		pip install -U pip && \
		pip install -r requirements.txt

clean:
	rm -rf venv

run: ## run Django app locally
	$(ACTIVATE) python3 manage.py runserver

heroku-logs:
	heroku logs --tail --app job-app-cli


.PHONY:
	venv \
	clean