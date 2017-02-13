.PHONY: serve

serve:
	cd docs && sphinx-autobuild . _build_html
