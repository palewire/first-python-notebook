==========
virtualenv
==========

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the Python tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools for different projects on one computer.

By developing your applications inside separate virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict.

You can also more easily recreate your project on another machine, handy when you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    virtualenv --version

If you don't have it, you can install it with pip.

.. code-block:: bash

    pip install virtualenv
    # If you're on a Mac or Linux and get an error saying you lack permissions,
    # try again as a superuser.
    sudo pip install virtualenv

#######
Windows
#######

Here's a walkthrough of how to do it on Windows:

.. youtube:: f-mYxXbPehI

#######
Mac OSX
#######

Here's how to do it on Mac OSX:

.. youtube:: uL5QYHbVXE0
