=====================
Chapter 12: Hello git
=====================

In this act, we will publish your notebook to the Internet using `GitHub <http://www.github.com/>`_, a social network for sharing and collaborating on code. GitHub is a platform frequently used by journalists and others to publish their notebooks. As listed above, examples include:


* `"The Tennis Racket" <https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb>`_ by BuzzFeed and the BBC
* `"Californians are paying billions for power they don't need" <https://github.com/datadesk/california-electricity-capacity-analysis/blob/master/analysis.ipynb>`_ by the Los Angeles Times
* `"Machine bias" <https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb>`_ by ProPublica

GitHub is an online extension of a command-line tool called `git <https://git-scm.com/>`_, a free and open-source version control tool for tracking and managing changes to code.

The first step in working with git is to convert a directory on your computer into a `repository <https://en.wikipedia.org/wiki/Repository_(version_control)>`_ that will have its contents tracked going forward. You do that by returning to your terminal, hitting the ``CTRL-C`` key combination to return the standard command line and entering the following.

.. code-block:: bash

    $ git init .

That will instruct git to initialize a new repository in your current folder.

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
