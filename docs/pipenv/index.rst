===========================
Chapter 1: Hello pipenv
===========================

`Pipenv`_ is a package manager and virtual environment manager combined in one handy command-line tool. In this chapter, we will explain what that means and show you how to use Pipenv to get First Python Notebook running on your own computer.

***********************
The “pip” part
***********************

Python is a versatile language. You can use it analyze and visualize data, as you will learn in this course. You can also use Python to automate tasks, scrape websites, launch web applications and so much more.

Whatever the aim of your project, likely you will rely on one or more Python packages that extend the language’s standard library. This allows you to import modules written by other trusty Python developers into your own code so that you can focus on the work that matters to you.

These third-party packages are available—for free—via the Python Package Index (aka, the `Cheese Shop`_). To install these packages on your own computer, you need a tool called a package manager.

Python’s default package manager is `pip`_. With pip, you can also document the exact version of each of package your project requires. Typically these dependencies are specified in a `requirements.txt`_ file. This document makes it easier to sync your project’s requirements across multiple machines if, for instance, you are collaborating with other developers.

***********************
The “env” part
***********************

But here we bump into another set of problems: What if your colleague is working on another Python project that requires a *different* version of a package required by your project? Such conflicts are common, especially when you factor in the sub-dependencies of your project’s direct dependencies, as well as the sub-dependencies of those sub-dependencies.

Dependency conflicts also occur when you have multiple Python projects on your own computer. Say you develop a web app today with `Flask`_ version 1.1. A year later, you want to start a new web app with Flask 2.3. However, your old app is still live and requires occasional patches. Now you’re in a bind: Will you refactor your old code to be compatible with the latest version of Flask, or give up maintaining your legacy web app?

These issues arise because, by default, Python third-party packages are all installed in a shared "global" environment. Instead, we create a `virtual environment`_ for each project in order to isolate its packages from other projects on our computer as well as the global Python environment.

Strictly speaking, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don’t have to take my word for it, you can read discussions on `StackOverflow`_ and `Reddit`_.

***********************
The convenient combo
***********************

By this point, you can see the appeal of a single tool that can 1) install and document your project’s dependencies; and, 2) isolate these dependencies from your other Python projects.

With Pipenv, that’s exactly what you get. This added convenience has earned Pipenv broad support in the Python community. Like it’s predecessor pip, Pipenv now is maintained by the `Python Packaging Authority`_.

Enough exposition. Let's start setting up your workspace.

***********************
Installing Pipenv
***********************

Pipenv and it's prerequisites are installed via your computer's `command-line interface`_.

**If you are on a Mac**, Pipenv’s docs `recommend`_ installing via `Homebrew`_:

.. code-block:: bash

    brew install pipenv 


**If you are on Windows 10**, consider installing both `Windows Subsystem for Linux`_ and selecting a Linux distribution from the Windows Store (we recommend Ubuntu). Once you've set up your Linux-based terminal, you can install `Linuxbrew`_ and use it to install Pipenv. 

**If neither option makes sense for you**, Pipenv's `docs`_ recommend a `user install`_ via pip:

.. code-block:: bash

    pip install --user pipenv


Whatever installation route you choose, you can confirm your success by calling up Pipenv's help text:

.. code-block:: bash

    pipenv --help


Your output should look like this:

.. code-block:: bash

    Usage: pipenv [OPTIONS] COMMAND [ARGS]...

    Options:
      --where             Output project home information.
      --venv              Output virtualenv information.
      --py                Output Python interpreter information.
      --envs              Output Environment Variable options.
      --rm                Remove the virtualenv.
      --bare              Minimal output.
      --completion        Output completion (to be eval'd).
      --man               Display manpage.
      --support           Output diagnostic information for use in GitHub issues.
      --site-packages     Enable site-packages for the virtualenv.  [env var:
                          PIPENV_SITE_PACKAGES]
      --python TEXT       Specify which version of Python virtualenv should use.
      --three / --two     Use Python 3/2 when creating virtualenv.
      --clear             Clears caches (pipenv, pip, and pip-tools).  [env var:
                          PIPENV_CLEAR]
      -v, --verbose       Verbose mode.
      --pypi-mirror TEXT  Specify a PyPI mirror.
      --version           Show the version and exit.
      -h, --help          Show this message and exit.


    Usage Examples:
       Create a new project using Python 3.7, specifically:
       $ pipenv --python 3.7

       Remove project virtualenv (inferred from current directory):
       $ pipenv --rm

       Install all dependencies for a project (including dev):
       $ pipenv install --dev

       Create a lockfile containing pre-releases:
       $ pipenv lock --pre

       Show a graph of your installed dependencies:
       $ pipenv graph

       Check your installed dependencies for security vulnerabilities:
       $ pipenv check

       Install a local setup.py into your virtual environment/Pipfile:
       $ pipenv install -e .

       Use a lower-level pip command:
       $ pipenv run pip freeze

    Commands:
      check      Checks for security vulnerabilities and against PEP 508 markers
                 provided in Pipfile.
      clean      Uninstalls all packages not specified in Pipfile.lock.
      graph      Displays currently-installed dependency graph information.
      install    Installs provided packages and adds them to Pipfile, or (if no
                 packages are given), installs all packages from Pipfile.
      lock       Generates Pipfile.lock.
      open       View a given module in your editor.
      run        Spawns a command installed into the virtualenv.
      shell      Spawns a shell within the virtualenv.
      sync       Installs all packages specified in Pipfile.lock.
      uninstall  Un-installs a provided package and removes it from Pipfile.
      update     Runs lock, then sync.


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

Now let's install one of the essential third-party packages for this course: Jupyter Notebook, which we will discuss in more depth in `chapter 2`_.

.. code-block:: bash

    pipenv install jupyter


When you invoke Pipenv's ``install`` command, it checks for an existing virtual environment connected to your project's directory. Finding none, it creates one, then installs Jupyter into it.

As a result, two files are added to your project directory: Pipfile and Pipfile.lock. These are an `alternative`_ to the standard requirements.txt file mentioned earlier.

Open these files in a text editor (such as `Sublime Text`_, `Atom`_ or `Visual Studio Code`_), and you'll see how they describe your project's Python requirements.

In Pipfile, you'll see the name and exact version of any package we directed Pipenv to install. So far, we've only installed Jupyter, and we didn't specify an exact version of Jupyter, so you'll see: 

.. code-block:: bash

    [packages]
    jupyter = "*"

Pipfile.lock has a much more complicated, nested structure that specifies the exact version of your project's direct dependencies along with all their sub-dependencies.
  
You've completed the setup process for First Python Notebook. Now the real fun begins.

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
