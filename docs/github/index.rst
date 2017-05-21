========================
Chapter 14: Hello GitHub
========================

Now visit `GitHub <http://www.github.com>`_ and create a new public repository named ``first-python-notebook``. Don't check "Initialize with README." You want to start with a blank repository.

Then connect your local directory to GitHub's site with the following.

.. code-block:: bash

    $ git remote add origin https://github.com/<yourusername>/first-python-notebook.git

Now, finally, push your commit up to GitHub.

.. code-block:: bash

    $ git push origin master
