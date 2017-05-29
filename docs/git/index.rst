=====================
Chapter 12: Hello git
=====================


*****************************
Creating a new git repository
*****************************

The first step in working with git is to convert a directory on your computer into a `repository <https://en.wikipedia.org/wiki/Repository_(version_control)>`_ that will have its contents tracked going forward.

You do that by returning to your terminal. If your notebook server is running, hit the ``CTRL-C`` key combination to return the standard command line. Then entering the following:

.. code-block:: bash

    $ git init .

That will instruct git to initialize a new repository in your current folder, which is represented by the period.

If this is your first time using git, you should configure git with your name and email. This will ensure that your work is properly logged by the respository's history file. Like the init a command above, this is something that only needs to be done once.

.. code-block:: bash

    $ git config --global user.email "your@email.com"
    $ git config --global user.name "your name"

********************
Committing your work
********************

Now you're ready to start logging your work. Changes to you code are logged by git in batches known as "commits."

.. note::

    There's no rule about when to you commit your work, but disciplined developers get in the habit of doing it as frequently. Whenever you've reached a small milestone or a breaking point in your work, it's a good idea to make a commit.

It is not required by a good first step before committing any work is run git's status command, which will output the current state of your repository.

.. code-block:: bash

    git status

Since your repository is brand new, all of the files will be listed as "untracked." That means that while git sees that these files exist it is not monitoring them for changes.

The first step in logging your work is to ask git to start tracking your files using the `add command <https://git-scm.com/docs/git-add>`_.

In this repository, the only file we need to track are your notebooks. You can add all of them by running the command below, which uses the "wildcard" asterisk to start tracking all files with the notebook extension.

.. code-block:: bash

    $ git add *.ipynb

Run the status command again and you'll see something different. That's git telling you that the notebooks in your repository have been staged and are ready to commit.

.. code-block:: bash

    git status

Log its addition with git's `commit command <https://git-scm.com/docs/git-commit>`_. You must include a personalized message, which can you provided along with the command by adding on the ``-m`` flag along with a description of the work you've done.

.. code-block:: bash

    $ git commit -m "First commit"

That's it. You've made your first git commit.

To get some practice, save a change to your notebook and try to log another.

It might seen a little burdonsome at first, but it is correct to follow the status to add to commit cycle each time. Take it slowly and carefully and you'll quickly get the hang of it.
