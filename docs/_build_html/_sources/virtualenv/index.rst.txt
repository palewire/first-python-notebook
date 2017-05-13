===========================
Chapter 1: Hello virtualenv
===========================

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the Python tools you use to build an application are sealed off.

Why do you need this?

By developing each project you work on inside a separate virtual environment, you can easily juggle them all on one machine. You can:

* Use different versions of the same Python libraries without a conflict.
* Easily install your project on another machine.
* As can your colleagues.
* Quickly copy your code to a server that publishes pages on the Internet.

For those reasons, virtualenv has become one of the most popular ways to manage Python projects. Alternatives include its more complex cousins `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_ and `conda <https://conda.io/docs/index.html>`_.

.. note::

    All that said, working within a virtual environment is not required. At first, it might even feel like a little bit of a hassle. But in the long run, you will be glad you did it. And you don't have to take my word for it, you can read extended discussions on `StackOverflow <https://conda.io/docs/index.html>`_ and `Reddit <https://www.reddit.com/r/Python/comments/2qq1d9/should_i_always_use_virtualenv/>`_.

**********************************************
Create a code directory to store all your work
**********************************************

.. code-block:: bash

    mkdir Code


*****************************************
Create a virtualenv to store this project
*****************************************

.. code-block:: bash

    cd Code

.. code-block:: bash

    virtualenv first-python-notebook

***********************
Activate the virtualenv
***********************

Jump into the directory it created.

.. code-block:: bash

    cd first-python-notebook

Turn on the new virtualenv, which will instruct your terminal to only use those libraries installed inside its sealed space. You only need to create the virtual environment once, but you will need to repeat these "activation" steps each time you return to working on this project.

.. code-block:: bash

    # In Linux or Mac OSX try this...
    . bin/activate
    # In Windows it might take something more like...
    cd Scripts
    . .\activate
    cd ..

***********************
Reactive the virtualenv
***********************

Jump into the directory it created.

.. code-block:: bash

    cd Code
    cd first-python-notebook

Turn on the new virtualenv, which will instruct your terminal to only use those libraries installed inside its sealed space. You only need to create the virtual environment once, but you will need to repeat these "activation" steps each time you return to working on this project.

.. code-block:: bash

    # In Linux or Mac OSX try this...
    . bin/activate
    # In Windows it might take something more like...
    cd Scripts
    . .\activate
    cd ..
