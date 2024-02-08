from datetime import datetime

extensions = [
    "myst_nb",
    "sphinx_multitoc_numbering",
]
source_suffix = ".md"
master_doc = "index"

project = 'First Python Notebook'
year = datetime.now().year
copyright = f'{year} palewi.re'

exclude_patterns = ["_build"]

html_theme = "palewire"
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}
html_theme_options = {
    "canonical_url": f"https://palewi.re/docs/first-python-notebook/",
}

html_static_path = ['_static']

pygments_style = 'sphinx'

# jupyter_execute_notebooks = "off"
