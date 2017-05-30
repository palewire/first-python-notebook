===========================
Chapter 1: Hello virtualenv
===========================

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the Python tools you use to build an application are sealed off.

Why do you need this?

By developing each of your Python projects inside a separate virtual environment, you can:You can:

* Juggle different versions of the same Python libraries without a conflict.
* Easily install your project on another machine, as can your colleagues
* Quickly copy your code to a server that publishes pages on the Internet.

For those reasons, virtualenv has become one of the most popular ways to manage Python projects. Alternatives include its more complex cousins `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_ and `conda <https://conda.io/docs/index.html>`_.

.. note::

    All that said, working within a virtual environment is not required. At first, it might even feel like a hassle. But in the long run, you will be glad you did it. And you don't have to take my word for it, you can read discussions on `StackOverflow <https://conda.io/docs/index.html>`_ and `Reddit <https://www.reddit.com/r/Python/comments/2qq1d9/should_i_always_use_virtualenv/>`_.

Learn how to create your first virtualenv by following this video or the written instructions below.

.. youtube:: t1vJzFbmfv8

**********************************************
Create a code directory to store all your work
**********************************************

Before we create your first virtualenv, the first step is to create a common folder where all you of your projects will be stored starting with this one.

Open your :doc:`command-line interface </prerequisites/cli>`, which will start you off in your home directory. Enter the following command and press enter to see all of the folders there now.

.. code-block:: bash

    ls

Next use the `mkdir <https://en.wikipedia.org/wiki/Mkdir>`_ to create a new directory for your code. In the same style as the Desktop, Documents and Downloads folders included by most operating system, we will name this folder Code.

.. code-block:: bash

    mkdir Code

To verify it's worked, you can open in your file explorer and navigate to your home folder.

*****************************************
Create a virtualenv to store this project
*****************************************

Next use your terminal to navigate into the new directory with the `cd <https://en.wikipedia.org/wiki/Cd_(command)>`_ command.

.. code-block:: bash

    cd Code

Now use the virtualenv command to create a new virtual environment. This is a one time thing necessary to initialize a new environment.

.. code-block:: bash

    virtualenv first-python-notebook

If you inspect the new directory this command created in your file explorer, you will see that it has generated a set of folders inside. They are the basic tools that make the virtual environment work and include a complete copy of the Python programming language just for this project.

***********************
Activate the virtualenv
***********************

Now use cd jump into the directory that was created created.

.. code-block:: bash

    cd first-python-notebook

Now the trickiest part. Each time you want to begin working on a virtualenv project, you need to start off by "activating" it inside your terminal.

The activation program is called activate. It was created inside the new folders in this directory. You will need to run it each and every time you start work in this environment.

On Mac OSX the program is inside a folder called bin. You can easily run it from your terminal by using the `source <https://en.wikipedia.org/wiki/Source_(command)>`_ command.

.. code-block:: bash

    source bin/activate

Fun fact: The source command has a shorter nickname if you don't want to type as much. It is simply a period.

.. code-block:: bash

    . bin/activate

On Windows the activate script is inside a folder called Scripts. You will need to move into that folder, run the script, and then back out to the folder we are in now.

.. code-block:: bash

    cd Scripts
    . .\activate
    cd ..

You can verify that your virtualenv is running by using the `which <https://en.wikipedia.org/wiki/Which_(Unix)>`_ command to ask your computer what installation of Python it is currently using.

.. code-block:: bash

    which python

If you are in your virtualenv, it should return a path leading to the same folder inside your virtualenv as activate. My looks like this:

.. code-block:: bash

    /home/ben/Code/first-python-notebook/bin/python

*************************
Reactivate the virtualenv
*************************

You will need to remember to activate your virtualenv environment every time you log on to your computer and start work on this project. Before we move on, let's take a moment to practice this routine.

Quit out of your command-line interface. Reopen it.

This new terminal will not be activated and working inside your virtual environment. You can verify this by using the which command again.

.. code-block:: bash

    which python

This time, you are likely to see a path to your computer system's global installation of Python, which we do not want to use on this project. Here's what mine looks like (yours will be slightly different):

.. code-block:: bash

    /usr/bin/python

We need to repeat the steps above to enter your new virtual environment and activate it.

First navigate into your code folder.

.. code-block:: bash

    cd Code

Then into your virtualenv folder

.. code-block:: bash

    cd first-python-notebook

Now activate your virtual environment with the source command. In you're on Mac OSX, let's use the shorter version this time.

.. code-block:: bash

    . bin/activate

If you're on Windows, here's the routine again.

.. code-block:: bash

    cd Scripts
    . .\activate
    cd ..

Finally, verify the process has succeeded using the which command. It should now return a path leading to your virtual environment.

.. code-block:: bash

    which python

That's it for this chapter. You've successfully created your first virtual environment. Now let's put it to use.
