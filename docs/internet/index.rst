=========================
Chapter 5: Hello Internet
=========================

In this act, we will publish your notebook to the Internet using `GitHub <http://www.github.com/>`_, a social network for sharing and collaborating on code. GitHub is a platform frequently used by journalists and others to publish their notebooks. As listed above, examples include:


* `"The Tennis Racket" <https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb>`_ by BuzzFeed and the BBC
* `"Californians are paying billions for power they don't need" <https://github.com/datadesk/california-electricity-capacity-analysis/blob/master/analysis.ipynb>`_ by the Los Angeles Times
* `"Machine bias" <https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb>`_ by ProPublica

GitHub is an online extension of a command-line tool called `git <https://git-scm.com/>`_, a free and open-source version control tool for tracking and managing changes to code.

The first step in working with git is to convert a directory on your computer into a `repository <https://en.wikipedia.org/wiki/Repository_(version_control)>`_ that will have its contents tracked going forward. You do that by returning to your terminal, hitting the ``CTRL-C`` key combination to return the standard command line and entering the following.

.. code-block:: bash

    $ git init .

That will instruct git to initialize a new repository in your current folder.

Now visit `GitHub <http://www.github.com>`_ and create a new public repository named ``first-python-notebook``. Don't check "Initialize with README." You want to start with a blank repository.

Then connect your local directory to GitHub's site with the following.

.. code-block:: bash

    $ git remote add origin https://github.com/<yourusername>/first-python-notebook.git

Then officially add your notebook file to your repository for tracking with git's ``add`` command.

.. code-block:: bash

    # Using the '*' will add all files that end with ipynb, the notebook's standard file extension.
    $ git add *.ipynb

Log its addition with Git's ``commit`` command. You can include a personalized message after the ``-m`` flag.

.. code-block:: bash

    $ git commit -m "First commit"

If this is your first time using Git, you may be prompted to configure you name and email. If so, take the time now. Then run the ``commit`` command above again.

.. code-block:: bash

    $ git config --global user.email "your@email.com"
    $ git config --global user.name "your name"

Now, finally, push your commit up to GitHub.

.. code-block:: bash

    $ git push origin master

Reload your repository on GitHub and see your handiwork.

If looked at the example above, you've probably noticed that other notebook authors have helpfully summarized and annotated their code by inserting text, links and images between code blocks.

.. image:: /_static/markdown_example.png

This is accomplished by adding new cells to your notebook and converting them from the default output, python code, to an alternative called Markdown. `Markdown <https://en.wikipedia.org/wiki/Markdown>`_ is a markup language that formats text. It's a common lightweight alternative to HTML.

To create and print a new Markdown cell in your notebook, start up your notebook again from the terminal.

.. code-block:: bash

    $ jupyter notebook

Now open your notebook file. At the top, add a new cell by clicking the plus button and hitting the up arrow button to move it to the top slot.

Click on the box and use your mouse to pull down the option menu that current reads "Code" from the toolbar. Replace it with "Markdown."

.. image:: /_static/markdown_pulldown.png

Now click into the cell and type the following:

.. code-block:: markdown

    # First Python Notebook

    Hello world!

Now hit the play button you will see the result. The first line has been turned into a header because that is how Markdown formats ``#`` at the front of lines. To learn more Markdown rules refer to `its documentation <http://daringfireball.net/projects/markdown/basics>`_.

.. image:: /_static/markdown_print.png

Now try adding more cells to your document lower down and annotating individual lines of code before they are run.

After you've finished, save your notebook and return to your terminal so we can commit your work and push it to GitHub. Again, open the terminal and hit the ``CTRL-C`` key combination to halt the notebook.

Again you'll want to tell git to log your notebook file changes using ``add``.

.. code-block:: bash

    $ git add *.ipynb

Now log your changes with ``commit``.

.. code-block:: bash

    $ git commit -m "Markdown"

Push your commit up to GitHub.

.. code-block:: bash

    $ git push origin master

Soon after your Markdown edits should appear on the GitHub site alongside your code.
