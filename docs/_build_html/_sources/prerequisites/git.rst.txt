===
Git
===

`Git <http://git-scm.com/>`_ is a version control program for saving the changes
you make to files over time. This is useful when you're working on your own,
but quickly becomes essential with large software projects, especially if you work with other developers.

For this class you will need to have git installed and working from your command prompt.

You can verify it's working on terminal by entering the follow code and hitting the enter key:

.. code-block:: bash

    git --version

If git is installed and working, you should see something like this:

.. code-block:: bash

    git version 2.9.3

If you don't have it installed, here's how to do it on Windows.

.. youtube:: F_CjRyoa45A

1. Verify the git is not already installed on the command prompt.
2. Download the installer from `git-for-windows.github.io <https://git-for-windows.github.io/>`_.
3. Run the installer, accepting all of the default options.
4. Return to the command prompt and verify git is now installed.
5. Configure git with your identity with these two commands: 

.. code-block:: bash

    git config --global user.email "your@email.com"
    git config --global user.name "your name"

And here's how on Mac OSX:
