:tocdepth: 2

=====================
First Python Notebook
=====================

A step-by-step guide to analyzing data with Python and the Jupyter Notebook.

It was developed by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ for a `Oct. 2, 2016, "watchdog workshop" organized by Investigative Reporters and Editors <http://ire.org/events-and-training/event/2819/2841/>`_ at San Diego State University's school of journalism. It is scheduled to be taught to students at Stanford's Journalism School and at the annual conference of the National Institute for Computer-Assisted Reporting in early 2017.


What you will learn
-------------------

This three-hour tutuorial will guide you through an investigation of money in politics using data from the `California Civic Data Coalition <http://www.californiacivicdata.org/>`_.

You will learn just enough Python to do damage with the powerful `pandas <http://pandas.pydata.org/>`_  data analysis library, the most popular open-source tool for working with large data files. You will also learn how to record, remix and republish your analysis using the `Jupyter Notebook <http://jupyter.org/>`_, a browser-based app for writing code that is emerging as the standard for sharing reproducible research in the sciences.

And most important: you will see how these tools can increase the speed and veracity of your journalism.


Prelude: Prequisites
--------------------

Before you can begin, your computer needs the following tools installed and working to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. Version 2.7 of the `Python <http://python.org/download/releases/2.7.6/>`_ programming language
3. The `pip <https://pip.pypa.io/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python
4. A code compiler that can install our heavy-duty analysis tools

.. warning::

    Stop and make sure you have all these tools installed and working properly. Otherwise, you're not gonna have a good time.

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to open a window that lets you type in commands. Different operating systems give this tool slightly different names, but they all have some form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the "command prompt." Here are instructions for `Windows 10 <http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/) and for [Windows 8](http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8) and [earlier versions](http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_. On Apple computers, you open the `"Terminal" application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_. Ubuntu Linux comes with a program of the `same name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`_.


Python
~~~~~~

For Apples
^^^^^^^^^^

If you are using Mac OSX, Python version 2.7 is probably already installed and you can test to see what version, if any, is already available by typing the following into your terminal.

.. code-block:: bash

    python -V

You should see something like this after you hit enter:

.. code-block:: bash

    $ python -V
    Python 2.7.12

If you get an error instead, Mac users should install Python by following `these instructions <http://docs.python-guide.org/en/latest/starting/install/osx/>`_ offered by The Hitchhikers Guide to Python.

For Windows
^^^^^^^^^^^

Just like Apple users, Windows people should open their command prompt and investigate whether Python is already installed.

.. code-block:: bash

    python -V

You should see something like this after you hit enter:

.. code-block:: bash

    python -V
    Python 2.7.12


If not Windows users can find a similar installation guide `here <http://docs.python-guide.org/en/latest/starting/install/win/>`_ which will have you try downloading and installing Python from `here <https://www.python.org/downloads/release/python-2712/>`_. After that's done, ensure Python is installed by reopening the command prompt and running the command above again.

pip and virtualenv
~~~~~~~~~~~~~~~~~~

The `pip package manager <https://pip.pypa.io/en/latest/>`_ makes it easy to install open-source libraries that expand what you're able to do with Python. Later, we will use it to install everything needed to create a working web application.

Verify pip is installed with the following.

.. code-block:: bash

    pip -V

If you don't have it already, you can get pip by following `these instructions <https://https://pip.pypa.io/en/latest/ip.pypa.io/en/latest/installing.html>`_.

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the different tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools for different projects on one computer. By developing your applications inside separate virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict. You can also more easily recreate your project on another machine, handy when you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    virtualenv --version

If you don't have it, install it with pip.

.. code-block:: bash

    pip install virtualenv
    # If you're on a Mac or Linux and get an error saying you lack permissions,
    # try again as a superuser.
    sudo pip install virtualenv


If that doesn't work, `try following this advice <http://virtualenv.readthedocs.org/en/latest/installation.html>`_.


Code compiler
~~~~~~~~~~~~~

A `code compiler <https://en.wikipedia.org/wiki/Compiler>`_ is a tool that lets your computer installed more advanced software. It is required to take advantage of the pandas data analysis library.

For Apples
^^^^^^^^^^

If you are using Mac OSX, you need to have XCode, Apple's developer kit that includes a tool for compiling heavy-duty software.

You can make sure you've got it by running this on your command prompt.

.. code-block:: bash

    xcode-select --install

For Windows
^^^^^^^^^^^

Windows users will need to download and install `this Microsoft package <https://www.microsoft.com/en-us/download/details.aspx?id=44266>`_, a compiler that will allow us to install other Python tools later.


Act 1: Hello Jupyter Notebook
-----------------------------

A `Jupyter Notebook <http://jupyter.org/>`_ is a browser application where you can write, run, remix and republish code. It is free software you can install and run like any other open-source library. It is used by scientists, scholars, investors and corporations to create and share their work.

It is also used by journalists to develop stories and show their work. Examples include:

* `"The Tennis Racket" <https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb>`_ by BuzzFeed and the BBC
* `"Californians are paying billions for power they don't need" <https://github.com/datadesk/california-electricity-capacity-analysis/blob/master/analysis.ipynb>`_ by the Los Angeles Times
* `"Machine bias" <https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb>`_ by ProPublica


The first step in our lesson is to get Jupyter's software installed. We're going to start that process by creating a new development environment with virtualenv in your terminal. Name it after our application.

.. code-block:: bash

    virtualenv first-python-notebook

Jump into the directory it created.

.. code-block:: bash

    cd first-python-notebook

Turn on the new virtualenv, which will instruct your terminal to only use those libraries installed inside its sealed space. You only need to create the virtual environment once, but you will need to repeat these "activation" steps each time you return to working on this project.

.. code-block:: bash

    # In Linux or Mac OSX try this...
    . bin/activate
    # In Windows it might take something more like...
    cd Scripts
    activate
    cd ..

Use ``pip`` on the command line to install Jupyter Notebook.

.. code-block:: bash

    pip install jupyter


Start up the notebook from your terminal.

.. code-block:: base

    jupyter notebook

That will open up a new tab in your default web browser that looks something like this:

.. image:: /_static/notebook.png


Click the "New" button in the upper right and create a new Python 2 notebook. Now you are all setup and ready to start writing code.

Do not stress. There is nothing too fancy about it. You can start by just doing a little simple math.

Type the following into the first box, then hit the play button in the toolbox (or hit SHIFT+ENTER on your keyboard).

.. code-block:: python

    2+2

There. You have just written your first Python code. You have entered two integers and added them together using the plus sign operator. Not so bad, right?

Now it is the time for us to get our hands on some real data and get some real work done. To do that, we need some real tools.


Act 2: Hello pandas
-------------------

Lucky for us, Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: navigate the web, parse data, interact with a database, run fancy statistics, build a pretty website and so much more.

Some of those tools are included a toolbox that comes with the language, known as the standard library. Others have been built by members of Python's developer community and need to be downloaded and installed from the web.

For this exercise, we're going to install and use [pandas](http://pandas.pydata.org/), a tool developed at a financial investment firm that has become the leading open-source tool for accessing and analyzing data.

We'll install pandas the same way we installed the Jupyter Notebook earlier: Our friend ``pip``. Save your notebook, switch to your window/command prompt and hit ``CTRL-C``. That will kill your notebook and return you to the command line. There we'll install pandas.

.. code-block:: python

    pip install pandas

Now let's restart our notebook and get back to work.

.. code-block:: python

    jupyter notebook

Use the next open box to import pandas into our script, so we can use all its fancy methods here in our script.

.. code-block:: python

    import pandas


Act 3: Hello analysis
---------------------

Until last November, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved
Proposition 64, which appeared, which asked voters if it ought to be legalized. A "yes" vote supported legalization. A "no" vote opposed it. In the final tally, 57% voted yes.

According to California's Secretary of State, approximately $23 million was raised to campaign in support of Prop. 64. Almost 2 million was been raised to oppose it.

Your mission, should you choose to accept it, is to download a list of campaign committees and contributors to figure out the biggest donors both for and against the measure.

Click here to download the file as a list of comma-separated values. This is known as a CSV file. It is the most common way you will find data published online. Save the file with the name first-python-notebook.csv in the same directory where you made this notebook.

Download a list of committees that supported and opposed one or more of the 17 measures on last November's ballot.
