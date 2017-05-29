==========================
Chapter 13: Hello Markdown
==========================

If you looked at notebooks published by others, you've probably noticed that the authors have helpfully summarized and annotated their code by inserting text, links and images between code blocks.

Here's an example from `a recent project by the Los Angeles Times <https://github.com/datadesk/california-electricity-capacity-analysis/blob/master/analysis.ipynb>`_.

.. image:: /_static/markdown_example.png

This is accomplished by adding new cells to your notebook and converting them from the default output, Python code, to an alternative called Markdown. `Markdown <https://en.wikipedia.org/wiki/Markdown>`_ is a markup language that formats text. It's a common, lightweight alternative to HTML.

****************
Writing Markdown
****************

To create and print a new Markdown cell in your notebook, start up your notebook again from the terminal.

.. code-block:: bash

    $ jupyter notebook

Now open your notebook file. At the top, add a new cell by clicking the plus button and hitting the up arrow button to move it to the top slot.

Click on the box and use your mouse to pull down the option menu that current reads "Code" from the toolbar. Replace it with "Markdown."

.. image:: /_static/markdown_pulldown.png

Now click into the cell and type the following:

.. code-block:: text

    # First Python Notebook

    Hello world!

Hit the play button you will see the result. The first line has been turned into a header because that is how Markdown formats ``#`` at the front of lines. To learn more Markdown rules refer to `its documentation <http://daringfireball.net/projects/markdown/basics>`_.

.. image:: /_static/markdown_print.png

Now try adding more cells to your document lower down and annotating individual lines of code before they are run.

After you've finished, save your notebook and return to your terminal so we can commit your work and push it to GitHub. Again, open the terminal and hit the ``CTRL-C`` key combination to halt the notebook.

You can see git has noticed the changes you've made by running the status command.

.. code-block:: bash

    $ git status

Now tell git to log your notebook file changes using add.

.. code-block:: bash

    $ git add *.ipynb

Now log your changes with commit.

.. code-block:: bash

    $ git commit -m "Markdown"
