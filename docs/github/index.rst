========================
Chapter 14: Hello GitHub
========================

In this section, we will publish your notebook to the Internet using `GitHub <http://www.github.com/>`_, a social network for sharing and collaborating on code. GitHub is a platform frequently used by journalists and others to publish their notebooks. Examples include:

* `"The Tennis Racket" <https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb>`_ by BuzzFeed and the BBC
* `"California H-2A visas analysis" <https://github.com/datadesk/california-h2a-visas-analysis/blob/master/04_analysis.ipynb>`_ by the Los Angeles Times
* `"Machine bias" <https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb>`_ by ProPublica

.. youtube:: XPdr5bCv-T4

GitHub is an online extension of the git command-line tool we installed in :doc:`a previous chapter </git/index>`. In may help to think of GitHub as a social network that publishes and connects git code repositories.

GitHub also offers free hosting to open-source software projects. It is where many of the world's largest are developed, including `pandas <https://github.com/pandas-dev/pandas>`_, `the Jupyter Notebook <https://github.com/jupyter/notebook>`_ and the `flavor of Python <https://github.com/ipython/ipython>`_ they favor.

.. warning::

    If you've set up your GitHub account with two-factor authentication, you will need to take the extra step of generating an SSH key that allows you to publish your work.

    If you've just made a GitHub account for the first time, do not worry about this. If you have turned on two-factor authentication, but don't have SSH keys, read more how to set it up in `GitHub's documentation <https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/>`_.

****************************
Creating a GitHub repository
****************************

Visit `GitHub <http://www.github.com>`_ and create a new public repository named ``first-python-notebook``. Don't check "Initialize with README." You want to start with a blank repository.

This will create a new repository page. It needs to be synchronized with the local repository we've already created.

You can connect your local directory to GitHub's site by returning to the terminal and using git's "remote add" command to connect it with GitHub.

.. code-block:: bash

    $ git remote add origin https://github.com/<yourusername>/first-python-notebook.git

.. note::

    The tradition among developers is to label your default remote repository as the "origin", which is why you see it included in the command above. You could substitute a different nickname for GitHub there if you wanted, but it's probably best to stick with the standard terminology.

Next we'll try "pushing" the latest commit from your repository up to GitHub. Assuming all of your work has been properly logged to your local repository, here's what it takes.

.. code-block:: bash

    $ git push origin master

.. note::

    That might seem like a long weird command (it is!) but it's one you'll need to memorize to continue working with GitHub.

    If you pick it apart, it's not that complicated. The first two terms, git push, tell git you'd like to copy your code from your local directory to a remote repository. The third, origin, indicates the destination you'd like to update. Remember, we gave our GitHub repository the alias origin. The fourth tells it which branch of your code you'd like to synchronize. We haven't covered it yet in this class, but the standard branch of code in any new git repository is called the master branch. If you're interested, you can read more about branches `in the git user manual <https://git-scm.com/book/id/v2/Git-Branching-Branches-in-a-Nutshell>`_.

Now reload the GitHub page in your browser and you should see your code online. Congratulations, you've published you work.

To see how your notebook appears on the web, click on the ipynb file in the browser and it should render much like it does in the live notebook on your localhost server. This URL can now be used to share your work with the entire world.

As a parting challenge, try saving a change to your local notebook. Then add and commit it to your repository with git. Finally push it back up to GitHub to see your published the change arrive online.
