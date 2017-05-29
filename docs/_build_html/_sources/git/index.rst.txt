=====================
Chapter 12: Hello git
=====================



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
