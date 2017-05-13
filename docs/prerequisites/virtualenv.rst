==========
virtualenv
==========

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ creates an isolated corner of your computer where all the Python tools you use to build an application are sealed off. We will use it to store all of the tools needed for the analysis in this class.

#######
Windows
#######

Here's how to install it on Windows:

.. youtube:: f-mYxXbPehI

1. Verify pip and python are already installed as we did in the previous installers.
2. Check virtualenv is not already installed.

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

Here's how to install it on Mac OSX:

.. youtube:: uL5QYHbVXE0

1. Verify pip and python are already installed as we did in the previous installers.
2. Check virtualenv is not already installed.

.. code-block:: bash

    virtualenv --version

3. Install virtualenv with pip. We'll need to use ``sudo`` to install it in the system folders.

.. code-block:: bash

    sudo pip install virtualenv

4. Verify that virtualenv has been installed.

.. code-block:: bash

    virtualenv --version
