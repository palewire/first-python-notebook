==========================
Chapter 5: Hello DataFrame
==========================

Now it's time to get real. It's time to start working on our analysis.

Our data source will be the `California Civic Data Coalition <http://www.californiacivicdata.org/>`_, an open-source network of journalists and developers that maintains an archive of data tracking money in California politics.

The coalition has created simplified data files containing the disclosure forms that committees campaigning either for against one of the 17 propositions on the ballot in November 2016 filed with the state of California.

They are:

================================================= ===========
Name                                              Description
================================================= ===========
`committees.csv </_static/committees.csv>`_       Committees active in the election linked to propositions supported or opposed
`contributions.csv </_static/contributions.csv>`_ Donors reported by each of the committees
================================================= ===========

The data are structured in rows of comma-separated values. This is known as a `CSV file <https://en.wikipedia.org/wiki/Comma-separated_values>`_. It is the most common way you will find data published online.

**************************
Importing CSVs with pandas
**************************

The pandas library is able to read in files from a variety formats, including CSV.

If it's not currently running start up your Jupyter Notebook as described in :doc:`chapter two </notebook>`.

Scroll down to the first open cell. There we will import the first CSV file listed above using the `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>`_ function included with ``pandas``.

.. code-block:: python

    pandas.read_csv("http://www.firstpythonotebook/_static/committees.csv")

.. warning::

    You will need to precisely type in the URL to the file. Feel free to copy and paste it from the example above into your notebook.

After you run the cell, you should see something like this.

.. image:: /_static/read_csv.png

It is a ``DataFrame`` where ``pandas`` has structured the CSV data into rows and columns, just like Excel or other spreadsheet software might. The advantage offered here is that rather than manipulating the data through a haphazard series of clicks and keypunches we will be gradually grinding down the data using a computer programming script that is 100% transparent and reproducible.

In order to do that, we need to store our ``DataFrame`` so it can be reused in subsequent cells. We can do this by saving in a `"variable" <https://en.wikipedia.org/wiki/Variable_(computer_science)>`_, which is a fancy computer programming word for a named shortcut where we save our work as we go.

Go back to your initial cell and change it to this. Then rerun it.

.. code-block:: python

    props = pandas.read_csv("./docs/_static/prop-committees.csv")

After you run it, you shouldn't see anything. That's a good thing. It means our ``DataFrame`` has been saved under the name ``props``, which we can now begin interacting with in the cells that follow. We can do this by calling `"methods" <https://en.wikipedia.org/wiki/Method_(computer_programming)>`_ that ``pandas`` has made available to all ``DataFrames``. There are dozens of these that can do all sorts of interesting things. Let's start with some easy ones that analysts
use all the time.

First, to preview the first few rows of the dataset, try the `head <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html>`_ method. Hit the ``+`` button in the toolbar to add a new cell below the first one. Type this in it and hit the run button again.

.. code-block:: python

    props.head()

.. image:: /_static/head.png

To get a look at all of the columns and what type of data they store, add another cell and try `info <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html>`_.

.. code-block:: python

    props.info()

.. image:: /_static/info.png

Look carefully at those results and you see we have more than 100 links between committees and propositions. That's interesting on its own, but our goal is to focus in on just one: Prop 64.

Quick studies will have already noted the ``prop_name`` column where each committee's affiliation is stored. Let's use pandas to drill down on it. To see its contents separate from the rest of the ``DataFrame``, add its name to the variable following a period. That should list out the whole thing.

.. code-block:: python

    props.prop_name

.. image:: /_static/column.png

One of the many cool tricks built in to ``pandas`` is the ability to total up the frequency of values in a column with the `value_counts <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html>`_ method. We can use it here to total up how many committees were active for each proposition.

.. code-block:: python

    props.prop_name.value_counts()

.. image:: /_static/value_counts.png

You may have noticed that both of the previous methods did not return a clean looking table in the same way as ``head``. It's often hard to anticipate, but in these cases and many others ``pandas`` will sometimes return an ugly `Series <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html>`_ rather than more aesthetically pleasing (and powerful) ``DataFrame``.

If that sounds like a bunch of mumbo jumbo, that's because it is! Like most computer programming tools, ``pandas`` has its own odd quirks that you have to pick up as you go. The difference between a ``Series`` and a ``DataFrame`` is one of those. The key is to not worry about it too much and keep hacking.

In most instances, if you have an ugly series generated by a method like ``value_counts`` and you want to convert it into a ``DataFrame`` you can do so by tacking on the `reset_index <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.reset_index.html>`_ method onto the tail end. Why? Again the answer is "because ``pandas`` says so." So let's play along.

.. code-block:: python

    props.prop_name.value_counts().reset_index()

.. image:: /_static/value_counts_df.png

With that we're ready to move on to a related, similar task: Importing all of the individual contributions reported to last year's 17 ballot measures and filtering them down to just those supporting and opposing Proposition 64.

We'll start by downloading `this second CSV file <http://first-python-notebook.readthedocs.io/en/latest/_static/contributions.csv>`_ and saving it to the same directory as this notebook with the name ``contributions.csv``. We'll then open it with ``read_csv`` and save it as a new variable just as we did above.

.. code-block:: python

    contribs = pandas.read_csv("contributions.csv")

.. warning::

    The contributions file you're downloading is an experimental early release from `the California Civic Data Coalition's effort <www.californiacivicdata.org>`_ to streamline the state's jumbled, dirty and disorganized official database. It has not yet been fully verified as accurate by our team and any conclusions you draw from it should be considered as provisional.

    If you want to base a news report off the analysis you do here, you should take the additional step of comparing the numbers you produce against the official data `released by the Secretary of State <http://cal-access.sos.ca.gov/>`_.

Just as we did earlier, you can inspect the contents of this new file with the ``head`` method.

.. code-block:: python

    contribs.head()

.. image:: /_static/contribs_head.png

You should also inspect the columns using the ``info`` method. Running these two tricks whenever you open a new file is a good habit to develop so that you can carefully examine the data you're about to work with.

.. code-block:: python

    contribs.info()

.. image:: /_static/contribs_info.png
