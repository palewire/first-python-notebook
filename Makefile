.PHONY: docs

docs:
	rm -rf docs/_build
	rm -rf docs/jupyter_execute
	cd docs && pipenv run make livehtml
