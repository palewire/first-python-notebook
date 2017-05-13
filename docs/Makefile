# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = FirstPythonNotebook
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

livehtml:
	sphinx-autobuild -b html ./ ./_build_html

pdf:
	sphinx-build -b pdf ./ build/pdf
	pdftk build/pdf/prologue-01-cli.pdf cat 5-end output build/pdf/prologue-01-cli-trimmed.pdf
	pdftk build/pdf/prologue-02-python.pdf cat 5-end output build/pdf/prologue-02-python-trimmed.pdf
	pdftk build/pdf/prologue-03-pip.pdf cat 5-end output build/pdf/prologue-03-pip-trimmed.pdf
	pdftk build/pdf/prologue-04-virtualenv.pdf cat 5-end output build/pdf/prologue-04-virtualenv-trimmed.pdf
	pdftk build/pdf/prologue-05-compiler.pdf cat 5-end output build/pdf/prologue-05-compiler-trimmed.pdf
	pdftk build/pdf/prologue-06-git.pdf cat 5-end output build/pdf/prologue-06-git-trimmed.pdf

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
