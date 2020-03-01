=======================
Chapter 1: Hello pipenv
=======================

`Pipenv`_ is a package manager and virtual environment manager combined into one handy command-line tool. In this chapter, we will explain why it is crucial to establishing a sturdy development space before you begin to code.

*************************
The “pip” package manager
*************************

Python is a versatile language. You can use it analyze and visualize data, as you will learn in this course. You can also use Python to automate tasks, scrape websites, launch web applications and so much more.

Whatever the aim of your project, likely you will rely on one or more Python packages that extend the language’s standard library. This allows you to import modules written by other trusty Python developers into your own code so that you can focus on the work that matters to you. The Jupyter notebook, pandas analysis kit and Altair chart library covered in this class are all examples.

These third-party packages are available — for free — via the Python Package Index. To install these packages on your own computer, you need a tool called a package manager.

Python’s default package manager is `pip`_. With pip, you can also document the exact version of each of package your project requires. Typically these dependencies are specified in a `requirements.txt`_ file. This document makes it easier to sync your project’s requirements across multiple machines if, for instance, you are collaborating with other developers.

*****************************
The “env” environment manager
*****************************

By default, Python's third-party packages are all installed in a shared "global" environment. By default, every project on your computer draws from the same set of installed programs. While is a simple and straightforward way to configure a computer, it quickly falls apart when you start to get serious about coding.

What if you start a new, separate Python project that requires a *different* version of a previously installed package? Open-source projects are changing every day and such conflicts are common, especially when you factor in the sub-dependencies of your project’s direct dependencies, as well as the sub-dependencies of those sub-dependencies.

For instance, say you develop an web application today with `Flask`_ version 1.1. A year later, you want to start a new project and use a newer version of Flask. However, your old app is still live and requires occasional patches. Flask has changed enough in the past year that code cannot be compatible with both versions.

Programmers solve this problem by creating a `virtual environment`_ for each project in order to isolate its packages from other projects on our computer as well as the global Python environment.

Strictly speaking, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don’t have to take my word for it, you can read discussions on `StackOverflow`_ and `Reddit`_.

********************
The convenient combo
********************

By this point, you can see the appeal of a single tool that can:

# Install and document your project’s dependencies
# Isolate these dependencies from your other Python projects

With Pipenv, that’s exactly what you get. This added convenience has earned pipenv broad support in the Python community. Like it’s predecessor pip, pipenv now is maintained by the `Python Packaging Authority`_.

Enough exposition. Let's start setting up your workspace.

*****************
Installing pipenv
*****************

Pipenv and its prerequisites are installed via your computer's `command-line interface`_. You can verify its there by typing the following into your terminal:

.. bash-code:: bash

    pipenv --version

If you have it installed, you should see a print out with the version on your machine. If you get an error, you will need to install pipenv. Instructions for that can be found `here <https://pipenv.readthedocs.io/en/latest/install/>`_

**If you are on a Mac**, Pipenv’s docs `recommend`_ installing via `Homebrew`_:

.. code-block:: bash

    brew install pipenv


**If you are on Windows 10**, consider installing both `Windows Subsystem for Linux`_ and selecting a Linux distribution from the Windows Store. We recommend choosing Ubuntu. Once you've set up your Linux-based terminal, you can install `Linuxbrew`_ and use it to install Pipenv.

**If neither option makes sense for you**, Pipenv's `docs`_ recommend a `user install`_ via pip:

.. code-block:: bash

    pip install --user pipenv


Whatever installation route you choose, you can confirm your success by calling up Pipenv's help text:

.. code-block:: bash

    pipenv --version

If you see that version number now, you know you're okay.

**********************************************
Create a code directory to store all your work
**********************************************

Now let's create a common folder where all you of your projects will be stored starting with this one.

Open your command-line interface, which will start you off in your home directory. Enter the following command and press enter to see all of the folders there now.

.. code-block:: bash

    ls


Next use the `mkdir`_ to create a new directory for your code. In the same style as the Desktop, Documents and Downloads folders included by most operating system, we will name this folder Code.

.. code-block:: bash

    mkdir Code


To verify it's worked, you can open in your file explorer and navigate to your home folder.


***************************
Create a project directory
***************************

Now let's make a folder for your first python notebook.

.. code-block:: bash

    mkdir Code/first-python-notebook


Next use your terminal to navigate into the new directory with the `cd`_ command:

.. code-block:: bash

    cd Code/first-python-notebook


****************************
Install your first package
****************************

Now let's install a simple Python package to see pipenv in action. We'll choose `yolk3k <https://pypi.org/project/yolk3k/>`_, a simple command-line tool that can list all your installed python packages.

We can add it to our project's private virtual environment by typing its name after pipenv's install command.

.. code-block:: bash

    pipenv install yolk3k


When you invoke Pipenv's ``install`` command, it checks for an existing virtual environment connected to your project's directory. Finding none, it creates one, then installs Jupyter into it.

As a result, two files are added to your project directory: Pipfile and Pipfile.lock. These are an `alternative`_ to the standard requirements.txt file mentioned earlier.

Open these files in a text editor (such as `Sublime Text`_, `Atom`_ or `Visual Studio Code`_), and you'll see how they describe your project's Python requirements.

In Pipfile, you'll see the name and exact version of any package we directed Pipenv to install. So far, we've only installed Jupyter, and we didn't specify an exact version of Jupyter, so you'll see:

.. code-block:: bash

    [packages]
    yolk3k = "*"

Pipfile.lock has a much more complicated, nested structure that specifies the exact version of your project's direct dependencies along with all their sub-dependencies.

Now that yolk is installed, we can excecute it inside our environment using pipenv's run command. Let's use its simple command for listing all of our currently installed tools.

.. code-block:: bash

    pipenv run yolk -l

You should see the computer spit out everything you have installed. You'll notice that yolk3k is on the list. You've completed the setup process for First Python Notebook. Now the real fun begins.

.. _Pipenv: https://pipenv.kennethreitz.org/en/latest/
.. _Cheese Shop: https://youtu.be/Hz1JWzyvv8A
.. _pip: https://pip.pypa.io/en/latest/
.. _requirements.txt: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Flask: https://palletsprojects.com/p/flask/
.. _virtual environments: https://docs.python.org/3/tutorial/venv.html
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
