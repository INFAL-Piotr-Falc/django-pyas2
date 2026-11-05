test:
	@(pytest -q pyas2/tests/)

serve:
	@(ENV=example python manage.py migrate && python manage.py runserver)

release:
	@(python setup.py bdist_wheel register upload -s)
