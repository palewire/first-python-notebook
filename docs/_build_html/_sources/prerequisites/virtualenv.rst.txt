==========
virtualenv
==========

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the Python tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools for different projects on one computer.

By developing your applications inside separate virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict.

You can also more easily recreate your project on another machine, handy when you want to copy your code to a server that publishes pages on the Internet.

#######
Windows
#######

Here's a walkthrough of how to do it on Windows:

.. youtube:: f-mYxXbPehI

1. Verify pip and python are already installed as we did in the previous installers.
2. Verify if virtualenv is not already installed.

.. code-block:: bash

    virtualenv --version

3. Install virtualenv with pip.

.. code-block:: bash

    pip install virtualenv

4. Verify that virtualenv has been installed.

.. code-block:: bash

    virtualenv --version

#######
Mac OSX
#######

Here's how to do it on Mac OSX:

.. youtube:: uL5QYHbVXE0

1. Verify pip and python are already installed as we did in the previous installers.
2. Verify if virtualenv is not already installed.

.. code-block:: bash

    virtualenv --version

3. Install virtualenv with pip. We'll need to use ``sudo`` to install it in the system folders.

.. code-block:: bash

    sudo pip install virtualenv

4. Verify that virtualenv has been installed.

.. code-block:: bash

    virtualenv --version
