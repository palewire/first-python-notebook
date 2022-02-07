===============================
Appendix: Advanced installation
===============================

Your computer needs the following computer-programming tools to participate. Verify you have them working before you begin.

A command-line interface
------------------------

Whether you know about it or not, there should be a way to open a window and directly issue commands to your operating system. Different operating systems give this tool slightly different names, but they all have some form of it.

On Windows this is called the "command prompt." On MacOS it is called the "terminal."

On Windows 10, we recommend you install the `Windows Subsystem for Linux`_ and select the Ubuntu distribution from the Windows Store. This will give you access to a generic open-source terminal without all the complications and quirks introduced by Windows. On MacOS, the standard terminal app will work fine.

Python 3.6 or higher
--------------------

`Python`_ is a free and open-source computer programming language. It's one of the most popular in the world and praised by its supporters as clear and easy to read.

That makes it ideal for beginners and is partly why it's been adopted by professionals in many fields, ranging from engineering and web development to journalism and music.

You can check if Python is already installed on your computer by visiting your command line and entering the following:

.. code-block:: bash

    python --version

You should see something like this after you hit enter:

.. code-block:: bash

    Python 3.6.10

If not, you'll need to install Python on your system.

If you see a number starting with 2, like say ...

.. code-block:: bash

    Python 2.7.12

...then you have an outdated version of Python and will need to upgrade to a version starting with a three. You can probably complete the class without doing so, but the maintainers of Python are gradually phasing out version two and officially recommend you upgrade.

Instructions for both new installations and upgrades can be found `here`_.


.. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Python: https://www.python.org/
.. _here: https://docs.python-guide.org/starting/installation/


pipenv
------

Before we can start programming, we need to do a little housekeeping on our computer. It's not required, but every organized Python project should have a system for managing two highly technical, but very important, issues. They are:

1. How to install and manage your programming tools
2. How to your keep your code from conflicting with other projects

We will solve these problems with `Pipenv`_. It handles both of the issues outlined above, hence the tool's two-part name, which is a programming portmanteau.

The “pip” package manager
~~~~~~~~~~~~~~~~~~~~~~~~~

Whatever the aim of your project,  you likely will rely on one or more Python packages that extend the language’s standard library. This allows you to import modules written by other trusty Python developers into your own code so that you can focus on the work that matters to you. The JupyterLab development environment, pandas analysis kit and Altair chart library covered in this class are all examples.

These third-party packages are available — for free — via the `Python Package Index <https://pypi.org/>`_, where they are published largely by volunteers. To download and install them on your computer, you need a tool called a package manager.

Python’s default package manager is `pip`_. It allows you to retrieve and unpack PyPi packages from your terminal. It goes something like this:

.. code-block:: bash

    pip install jupyterlab

With pip, you can also document the exact version of each of package your project requires and store in a list that records everything necessary to run your code.

Typically these dependencies are specified in a `requirements.txt`_ file. This document makes it easier to sync your project’s requirements across multiple machines if, for instance, you are collaborating with other developers.

Lucky for us, all the functionality of pip is included in Pipenv, as well as much more.

The “env” environment manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Python's third-party packages are all installed in a shared "global" folder somewhere in the depths of your computer. By default, every Python project on your computer draws from this same set of installed programs.

This approach is fine for your first experiments with Python, but it quickly falls apart when you start to get serious about coding.

For instance, say you develop a web application today with `Flask`_ version 1.1. What if, a year from now, you want to start a new project and use a newer version of Flask? Your old app is still live and requires occasional patches, but you don't have time to re-write all of your old to make it compatible with the latest version of Flask.

Open-source projects are changing every day and such conflicts are common, especially when you factor in the sub-dependencies of your project’s direct dependencies, as well as the sub-dependencies of those sub-dependencies.

Programmers solve this problem by creating a `virtual environment`_ for each project that isolates them into discrete, independent containers that do not rely on code in the global environment.

Strictly speaking, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don’t have to take my word for it, you can read discussions on `StackOverflow`_ and `Reddit`_.

Good thing Pipenv can do this too.

Installing Pipenv
~~~~~~~~~~~~~~~~~

Pipenv and its prerequisites are installed via your computer's `command-line interface`_. You can verify its there by typing the following into your terminal:

.. code-block:: bash

    pipenv --version

If you have it installed, you should see the terminal respond with the version on your machine.

.. code-block:: bash

    pipenv, version 2018.11.26

If you get an error, you will need to install it.

If you are on a Mac, Pipenv’s maintainers `recommend`_ installing via `Homebrew`_:

.. code-block:: bash

    brew install pipenv

If you are on Windows 10 and using the `Windows Subsystem for Linux`_, you can install `Linuxbrew`_ and use it to install Pipenv.

If neither option makes sense for you, Pipenv's `docs`_ recommend a `user install`_ via pip:

.. code-block:: bash

    pip install --user pipenv

Whatever installation route you choose, you can confirm your success by testing for its version again:

.. code-block:: bash

    pipenv --version

If you see that version number now, you know you're okay.

Create a code directory to store all your work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's create a common folder where all you of your projects will be stored starting with this one. This is also where our virtualenv will be configured.

Open your command-line interface, which will start you off in your home directory. Enter the following command and press enter to see all of the folders there now.

.. code-block:: bash

    ls


Next use the `mkdir`_ to create a new directory for your code. In the same style as the Desktop, Documents and Downloads folders included by most operating system, we will name this folder Code.

.. code-block:: bash

    mkdir Code


To verify that worked, you can open in your file explorer and navigate to your home folder.

Create a project directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's make a folder for your work in this class.

.. code-block:: bash

    mkdir Code/first-python-notebook


Next use your terminal to navigate into the new directory with the `cd`_ command:

.. code-block:: bash

    cd Code/first-python-notebook


Install your first package
~~~~~~~~~~~~~~~~~~~~~~~~~~

Now let's install a simple Python package to see Pipenv in action. We'll choose `yolk3k <https://pypi.org/project/yolk3k/>`_, a simple command-line tool that can list all your installed python packages.

We can add it to our project's private virtual environment by typing its name after Pipenv's install command.

.. code-block:: bash

    pipenv install yolk3k


When you invoke Pipenv's ``install`` command, it checks for an existing virtual environment connected to your project's directory. Finding none, it creates one, then installs yolk3k into it.

As a result, two files are added to your project directory: Pipfile and Pipfile.lock. These are Pipenv's `alternative`_ to the requirements.txt file mentioned earlier.

Open these files in a text editor (such as `Sublime Text`_, `Atom`_ or `Visual Studio Code`_), and you'll see how they describe your project's Python requirements.

In the Pipfile, you'll see the name and exact version of any package we directed Pipenv to install. So far, we've only installed yolk3k, and we didn't specify an exact version, so you'll see:

.. code-block:: bash

    [packages]
    yolk3k = "*"

Pipfile.lock has a more complicated, nested structure that specifies the exact version of your project's direct dependencies along with all their sub-dependencies.

Now that yolk is installed, we can execute it inside our environment using Pipenv's run command. Let's use its simple command for listing all of our currently installed tools.

.. code-block:: bash

    pipenv run yolk -l

You should see the computer spit out everything you have installed. You'll notice that yolk3k is on the list. You've completed the setup process for First Python Notebook. Now the real fun begins.


Navigate to project directory
-----------------------------

Now let's check where we are in our computer's file system. For this we'll use a command called `pwd`_, which stands for ``p``\ resent ``w``\ orking ``d``\ irectory.

.. code-block:: bash

    pwd

The output is the full path of your location in the file system, something like ``/Users/palewire/Code/first-python-notebook``. If you aren't currently in the project directory we created in `chapter 1`_, you need to change directories.

First, jump into the code directory:

.. code-block:: bash

    cd Code

Then, jump into project directory:

.. code-block:: bash

    cd first-python-notebook

This is where you'll store a local copy of all the code and files you create for this project.

.. note::

    It isn't necessary to change directories one level at a time. You can also specify the full path of directory you want to change into:

    .. code-block:: bash

        cd Code/first-python-notebook


Install JupyterLab
------------------

Now we will return to Pipenv and use it to install JupyterLab, the web-based interactive development environment for Jupyter notebooks, code and data.

.. code-block:: bash

    pipenv install jupyterlab


Install pandas
--------------

We'll install pandas the same way we installed the JupyterLab:

.. code-block:: python

    pipenv install pandas

Install altair
--------------

Install altair as well.

.. code-block:: python

    pipenv install altair


.. note::

    You can install more than one package at once. For instance, all three of the packages above could be added like so:

    .. code-block:: bash

        pipenv install jupyterlab pandas altair


Create your first notebook
--------------------------

Now we can use pipenv's run command to start JupyterLab from your terminal.

.. code-block:: bash

    pipenv run jupyter lab

That will open up a new tab in your default web browser that looks something like this:

.. image:: /_static/labpreview.png

Click the "Python 3" button in the middle panel and create a new Python 3 notebook. You should now be able to pick up in `chapter two <../notebook>`_ and start work from there.


.. _Pipenv: https://pipenv.kennethreitz.org/en/latest/
.. _Cheese Shop: https://youtu.be/Hz1JWzyvv8A
.. _pip: https://pip.pypa.io/en/latest/
.. _requirements.txt: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Flask: https://palletsprojects.com/p/flask/
.. _virtual environment: https://docs.python.org/3/tutorial/venv.html
.. _venv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _StackOverflow: https://conda.io/docs/index.html
.. _Reddit: https://www.reddit.com/r/Python/comments/2qq1d9/should_i_always_use_virtualenv/
.. _Python Packaging Authority: https://www.pypa.io/en/latest/
.. _command-line interface: https://en.wikipedia.org/wiki/Command-line_interface
.. _recommend: https://pipenv.kennethreitz.org/en/latest/install/#homebrew-installation-of-pipenv
.. _Homebrew: https://brew.sh/
.. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Linuxbrew: https://docs.brew.sh/Homebrew-on-Linux
.. _docs: https://pipenv.kennethreitz.org/en/latest/install/#pragmatic-installation-of-pipenv
.. _user install: https://pip.pypa.io/en/stable/user_guide/#user-installs
.. _chapter 2: ../notebook/
.. _mkdir: https://en.wikipedia.org/wiki/Mkdir
.. _cd: https://en.wikipedia.org/wiki/Cd_(command)
.. _alternative: https://github.com/pypa/pipfile
.. _Sublime Text: https://www.sublimetext.com/
.. _Atom: https://atom.io/
.. _Visual Studio Code: https://code.visualstudio.com/
