=========================
Chapter 1: Hello notebook
=========================

A `Jupyter Notebook <http://jupyter.org/>`_ is a browser application where you can write, run, remix and republish code. It is free software you can install and run like any other open-source library. It is used by `scientists <http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb>`_, `scholars <http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb>`_, `investors <https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb>`_ and corporations to create and share their work.

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
    . .\activate
    cd ..

Use ``pip`` on the command line to install Jupyter Notebook.

.. code-block:: bash

    pip install jupyter


Start up the notebook from your terminal.

.. code-block:: bash

    jupyter notebook

That will open up a new tab in your default web browser that looks something like this:

.. image:: /_static/notebook.png


Click the "New" button in the upper right and create a new Python 2 notebook. Now you are all setup and ready to start writing code.

Do not stress. There is nothing too fancy about it. You can start by just doing a little simple math.

Type the following into the first box, then hit the play button in the toolbar above the notebook (or hit SHIFT+ENTER on your keyboard).

.. code-block:: python

    2+2

.. image:: /_static/2_plus_2.png

There. You have just written your first Python code. You have entered two integers and added them together using the plus sign operator. Not so bad, right?

Now it is the time for us to get our hands on some real data and get some real work done. To do that, we need some real tools.
