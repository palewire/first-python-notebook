===
Git
===

`Git <http://git-scm.com/>`_ is a version control program for saving the changes
you make to files over time. It is useful when you're working on your own,
but quickly becomes essential with large software projects, especially when you work with others.

For this class you will need to have git installed and working from your command-line interface.

You can verify it's working from your terminal by typing in the follow code and hitting the enter key:

.. code-block:: bash

    git --version

If git is installed and working, you should see something like this:

.. code-block:: bash

    git version 2.11.0

If you don't have it installed, you'll need to follow the instructions below.

*******
Windows
*******

Here's how to install git on Windows.

.. youtube:: F_CjRyoa45A

1. Verify the git is not already installed on the command prompt.
2. Download the installer from `git-for-windows.github.io <https://git-for-windows.github.io/>`_.
3. Run the installer, accepting all of the default options.
4. Return to the command prompt and verify git is now installed.
5. Configure git with your identity with these two commands:

.. code-block:: bash

    git config --global user.email "your@email.com"
    git config --global user.name "your name"

*******
Mac OSX
*******

.. youtube:: quEyv0vd6K8

If you've followed the previous installation instructions for :doc:`a code compiler </prerequisites/compiler>`, git should be already installed and ready to go. You can test it out by opening up the command prompt or cygwin and typing in the command above. Here it is again:

.. code-block:: bash

    git --version

If it's not, visit `git-scm.com <http://www.git-scm.com>`_ and download the installer. Run it.

Either way, configure git with your identity using these two commands:

.. code-block:: bash

    git config --global user.email "your@email.com"
    git config --global user.name "your name"
