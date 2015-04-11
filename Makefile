serve:
	@python manage.py runserver 0.0.0.0:8000

test:
	@coverage run --source=pyclub/ --omit=*/wsgi.py manage.py test
	@coverage report
	@coverage html
