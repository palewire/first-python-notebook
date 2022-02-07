.PHONY: serve

serve:
	cd docs && pipenv run make livehtml
