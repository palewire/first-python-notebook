=================================
Chapter 2: Hello Jupyter Notebook
=================================

A `Jupyter Notebook <http://jupyter.org/>`_ is a browser application where you can write, run, remix and republish code.

It is free software you can install and run like any other open-source library. It is used by `scientists <http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb>`_, `scholars <http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb>`_, `investors <https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb>`_ and corporations to create and share their research.

It is also used by journalists to develop stories and show their work. Examples include:

* `"The Tennis Racket" <https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb>`_ by BuzzFeed and the BBC
* `"Fire officials were concerned about Westlake building where 5 died in a blaze" <https://github.com/datadesk/la-vacant-building-complaints-analysis/blob/master/la-vacant-building-complaints-analysis.ipynb>`_ by the Los Angeles Times
* `"Machine bias" <https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb>`_ by ProPublica

Learn how to install Jupyter and create your first notebook by following this video or the written instructions below.

.. youtube:: kjrXSvX2JTk

*********************************
Activate your virtual environment
*********************************

To start off, open up your :doc:`command-line interface </prerequisites/cli>` and activate the :doc:`virtual environment </virtualenv/cli>` created for this project.

After the terminal is open, navigate to the code directory.

.. code-block:: bash

    cd Code

Jump into virtual environment directory.

.. code-block:: bash

    cd first-python-notebook

Activate the virtual environment, as we've done before.

.. code-block:: bash

    # In Mac OSX ...
    source bin/activate
    # In Windows ...
    cd Scripts
    . .\activate
    cd ..

*********************************
Install Jupyter Notebook with pip
*********************************

Now that we're in the virtual environment, we will use the :doc:`pip </prerequisites/pip>` command line tool to install the Jupyter Notebook software.

.. code-block:: bash

    pip install jupyter

You can verify it's been installed by running pip's freeze command, which will list all of the installed Python libraries.

.. code-block:: bash

    pip freeze

**************************
Create your first notebook
**************************

Now that Jupyter is installed, you can start its browser interface from your terminal.

.. code-block:: bash

    jupyter notebook

That will open up a new tab in your default web browser that looks something like this:

.. image:: /_static/notebook.png

Click the "New" button in the upper right and create a new Python 2 notebook.

****************************
Write Python in the notebook
****************************

Now you are all setup and ready to start writing Python code.

Do not stress. There is nothing too fancy about it. You can start by just doing a little simple math.

Type the following into the first box, then hit the play button in the toolbar above the notebook (or hit SHIFT+ENTER on your keyboard).

.. code-block:: python

    2+2

.. image:: /_static/2_plus_2.png

There. You have just written your first Python code. You have entered two integers and added them together using the plus sign operator.

Not so bad, right?

.. note::

    If you get an error after you run a cell, look carefully at your code and see that it exactly matches what's been written in the example. Don't worry.

    Code crashes are a normal part of life for computer programmers. They're usually caused by small typos that can be quickly corrected.

This to-and-fro of writing Python code in a notebook cell and then running it with the play button is the rhythm of working in a notebook. Over time you will gradually stack cells to organize an analysis that runs from top to bottom.

The cells can contain variables, functions and other Python tools.

A simple example would be storing your number in a variable in one cell ...

.. code-block:: python

    number = 2

... then adding it to another number in the next.

.. code-block:: python

    number + 3

Run those two cells in succession and the notebook should output the number five. Change the number value to 3 and run both cells again and it should output six.

.. note::

    The video at the top of this page introduces more of these Python fundamentals by writing and running cells of code in the notebook. If you've never written Python before, be sure to watch the clip before you advance to the next chapter.


Once you've got the hang of making the notebook run, you're ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.
