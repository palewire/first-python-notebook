=========================
Chapter 2: Hello notebook
=========================

A `Jupyter notebook`_ is a browser application where you can write, run, remix and republish code.

It is free software you can install and run like any other open-source library. It is used by `scientists`_, `scholars`_, `investors`_ and corporations to create and share their research.

It is also used by journalists to develop stories and show their work. Examples include:

* `"The Tennis Racket"`_ by BuzzFeed and the BBC
* `"Machine bias"`_ by ProPublica
* `More than 30 different notebooks published`_ by the Los Angeles Times


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

    If you've never written Python before, we recommend `An Informal Introduction to Python`_ and subsequent sections of python.org's tutorial.


Once you've got the hang of making the notebook run, you're ready to introduce pandas, the powerful Python analysis library that can do a whole lot more than add a few numbers together.


.. _scientists: http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb
.. _scholars: http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb
.. _investors: https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb
.. _"The Tennis Racket": https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb
.. _More than 30 different notebooks published: https://github.com/datadesk/notebooks
.. _"Machine bias": https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb
.. _Jupyter Notebook: http://jupyter.org/
.. _chapter 1: ../pipenv/
.. _pwd: https://en.wikipedia.org/wiki/Pwd
.. _An Informal Introduction to Python: https://docs.python.org/3/tutorial/introduction.html
