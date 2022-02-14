.PHONY: serve

serve:
	rm -rf docs/jupyter_execute
	cd docs && pipenv run make livehtml
