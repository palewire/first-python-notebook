:tocdepth: 2

=====================
First Python Notebook
=====================

A step-by-step guide to analyzing data with Python and the Jupyter Notebook.


What you will learn
-------------------

This three-hour tutorial will guide you through an investigation of money in politics using data from the `California Civic Data Coalition <http://www.californiacivicdata.org/>`_.

You will learn just enough Python to work with the powerful `pandas <http://pandas.pydata.org/>`_  data analysis library, a popular open-source tool for working with large data files. The course will teach you how to use pandas to read, filter, join, rank, group and aggregate structured data.

You will learn how to record, remix and republish your analysis using the `Jupyter Notebook <http://jupyter.org/>`_, a browser-based app for writing code that is emerging as the standard for sharing reproducible research in the sciences.

And most important: you will see how these tools can increase the speed and veracity of your journalism.


About the data
--------------

The course is based on data provided by the `California Civic Data Coalition <http://www.californiacivicdata.org/>`_, an open-source network of journalists and computer programmers working to ease access to the state's jumbled, dirty and difficult database tracking money in politics.

The state's campaign and lobbying data has been used to develop insightful journalism like:

*  `Campaign cash gives Nunez rich travel style <http://articles.latimes.com/print/2007/oct/05/local/me-nunez5>`_, `Los Angeles Times`, Oct. 5, 2007
* `California speaker gives Assembly's juiciest jobs to biggest fundraiser <http://cironline.org/reports/california-speaker-gives-assemblys-juiciest-jobs-biggest-fundraisers-4501>`_, `Center for Investigative Reporting`, May 15, 2013
* `Prop. 47 puts state at center of a national push for sentencing reform <http://www.latimes.com/local/politics/la-me-ff-pol-1101-proposition47-20141101-story.html>`_, `Los Angeles Times`, Nov. 1, 2014
* `Connecting the donor dots in California outside spending campaigns <http://www.sacbee.com/news/politics-government/capitol-alert/article80197182.html>`_, `Sacramento Bee`, May 26, 2016
* `Sacramento's new 'slush funds': Ballot-measure committees <http://www.mercurynews.com/2016/08/20/sacramentos-new-slush-funds-ballot-measure-committees/>`_, `San Jose Mercury News`, Aug. 20, 2016

The goal of the coalition's work is to make the data those reporters used easier to access, understand and analyze. Learn more about the status of the project and the data you can download `here <http://www.californiacivicdata.org/2016/09/15/website-launch/>`_.

About the authors
-----------------

This course was first developed by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ for a Oct. 2, 2016, `"watchdog workshop" <http://www.californiacivicdata.org/2016/10/08/first-python-notebook/>`_ organized by Investigative Reporters and Editors at San Diego State University's school of journalism. It was revised for a Feb. 14-16, 2017, hands-on training of students at Stanford's journalism school. It will be expanded for `a six-hour class <https://www.ire.org/events-and-training/event/2702/2879/>`_ at the annual conference of the National Institute for Computer-Assisted Reporting in March 2017.

Ben is the editor of the Data Desk, a team of reporters and programmers in the Los Angeles Times newsroom. He is also a co-founder of the California Civic Data Coalition.

Prelude: Prequisites
--------------------

Before you can begin, your computer needs the following tools installed and working to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. Version 2.7 of the `Python <http://python.org/download/releases/2.7.6/>`_ programming language
3. The `pip <https://pip.pypa.io/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python
4. A code compiler that can install our heavy-duty analysis tools

.. warning::

    Stop and make sure you have all these tools installed and working properly. Otherwise, you're not gonna have a good time.

Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to open a window that lets you type in commands. Different operating systems give this tool slightly different names, but they all have some form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the "command prompt." Here are instructions for `Windows 10 <http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/) and for [Windows 8](http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8) and [earlier versions](http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_. On Apple computers, you open the `"Terminal" application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_. Ubuntu Linux comes with a program of the `same name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`_.


Python
~~~~~~

For Apples
^^^^^^^^^^

If you are using Mac OSX, Python version 2.7 is probably already installed and you can test to see what version, if any, is already available by typing the following into your terminal.

.. code-block:: bash

    python -V

You should see something like this after you hit enter:

.. code-block:: bash

    $ python -V
    Python 2.7.12

If you get an error instead, Mac users should install Python by following `these instructions <http://docs.python-guide.org/en/latest/starting/install/osx/>`_ offered by The Hitchhikers Guide to Python.

For Windows
^^^^^^^^^^^

Just like Apple users, Windows people should open their command prompt and investigate whether Python is already installed.

.. code-block:: bash

    python -V

You should see something like this after you hit enter:

.. code-block:: bash

    python -V
    Python 2.7.12


If not Windows users can find a similar installation guide `here <http://docs.python-guide.org/en/latest/starting/install/win/>`_ which will have you try downloading and installing Python from `here <https://www.python.org/downloads/release/python-2712/>`_. After that's done, ensure Python is installed by reopening the command prompt and running the command above again.

pip and virtualenv
~~~~~~~~~~~~~~~~~~

The `pip package manager <https://pip.pypa.io/en/latest/>`_ makes it easy to install open-source libraries that expand what you're able to do with Python. Later, we will use it to install everything needed to create a working web application.

Verify pip is installed with the following.

.. code-block:: bash

    pip -V

If you don't have it already, you can get pip by following `these instructions <https://https://pip.pypa.io/en/latest/ip.pypa.io/en/latest/installing.html>`_.

The `virtualenv environment manager <http://www.virtualenv.org/en/latest/>`_ makes it possible to create an isolated corner of your computer where all the different tools you use to build an application are sealed off.

It might not be obvious why you need this, but it quickly becomes important when you need to juggle different tools for different projects on one computer. By developing your applications inside separate virtualenv environments, you can use different versions of the same third-party Python libraries without a conflict. You can also more easily recreate your project on another machine, handy when you want to copy your code to a server that publishes pages on the Internet.

You can check if virtualenv is installed with the following.

.. code-block:: bash

    virtualenv --version

If you don't have it, install it with pip.

.. code-block:: bash

    pip install virtualenv
    # If you're on a Mac or Linux and get an error saying you lack permissions,
    # try again as a superuser.
    sudo pip install virtualenv


If that doesn't work, `try following this advice <http://virtualenv.readthedocs.org/en/latest/installation.html>`_.


Code compiler
~~~~~~~~~~~~~

A `code compiler <https://en.wikipedia.org/wiki/Compiler>`_ is a tool that lets your computer installed more advanced software. It is required to take advantage of the pandas data analysis library.

For Apples
^^^^^^^^^^

If you are using Mac OSX, you need to have XCode, Apple's developer kit that includes a tool for compiling heavy-duty software.

You can make sure you've got it by running this on your command prompt.

.. code-block:: bash

    xcode-select --install

For Windows
^^^^^^^^^^^

Windows users will need to download and install `this Microsoft package <https://www.microsoft.com/en-us/download/details.aspx?id=44266>`_, a compiler that will allow us to install other Python tools later.


Act 1: Hello notebook
---------------------

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
    activate
    cd ..

Use ``pip`` on the command line to install Jupyter Notebook.

.. code-block:: bash

    pip install jupyter


Start up the notebook from your terminal.

.. code-block:: base

    jupyter notebook

That will open up a new tab in your default web browser that looks something like this:

.. image:: /_static/notebook.png


Click the "New" button in the upper right and create a new Python 2 notebook. Now you are all setup and ready to start writing code.

Do not stress. There is nothing too fancy about it. You can start by just doing a little simple math.

Type the following into the first box, then hit the play button in the toolbox (or hit SHIFT+ENTER on your keyboard).

.. code-block:: python

    2+2

There. You have just written your first Python code. You have entered two integers and added them together using the plus sign operator. Not so bad, right?

Now it is the time for us to get our hands on some real data and get some real work done. To do that, we need some real tools.


Act 2: Hello pandas
-------------------

Lucky for us, Python is filled with functions to do pretty much anything you’d ever want to do with a programming language: `navigate the web <http://docs.python-requests.org/>`_, `parse data <https://docs.python.org/2/library/csv.html>`_, `interact with a database <http://www.sqlalchemy.org/>`_, `run fancy statistics <https://www.scipy.org/>`_, `build a pretty website <https://www.djangoproject.com/>`_ and `so <https://www.crummy.com/software/BeautifulSoup/>`_ `much <http://www.nltk.org/>`_ `more <http://pillow.readthedocs.io/en/3.4.x/index.html>`_. Creative people have put these tools to work to get `a wide range of things done <https://www.python.org/about/success/>`_ in the arts, technology and even outer space.

Some of those tools are included a toolbox that comes with the language, known as the standard library. Others have been built by members of Python's developer community and need to be downloaded and installed from the web.

For this exercise, we're going to install and use `pandas <http://pandas.pydata.org/>`_, a tool developed at a financial investment firm that has become the leading open-source tool for accessing and analyzing data.

We'll install pandas the same way we installed the Jupyter Notebook earlier: Our friend ``pip``. Save your notebook, switch to your window/command prompt and hit ``CTRL-C``. That will kill your notebook and return you to the command line. There we'll install pandas.

.. code-block:: python

    pip install pandas

Now let's restart our notebook and get back to work.

.. code-block:: python

    jupyter notebook

Use the next open box to import pandas into our script, so we can use all its fancy methods here in our script.

.. code-block:: python

    import pandas

Run the notebook cell. If nothing happens, that's good. It means you have pandas installed and ready to work.

If you get an error message, return to the prequisites section above and make sure you have everything installed properly. If you do and it still doesn't work, copy and paste the tail end of your error message into Google. Among the results there will almost certainly be others working through the same problem.


Act 3: Hello data
-----------------

Until last November, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved Proposition 64, which asked voters if the practice ought to be legalized. A "yes" vote supported legalization. A "no" vote opposed it. `In the final tally <http://elections.cdn.sos.ca.gov/sov/2016-general/sov/65-ballot-measures-formatted.pdf>`_, 57% of voters said yes.

Your mission, should you choose to accept it, is to analyze lists of campaign committees and contributors to figure out the biggest donors both for and against the measure.

To start `click here <http://first-python-notebook.readthedocs.io/en/latest/_static/prop-committees.csv>`_ to download a list of last November's 17 ballot measures and their affiliated fundraising committees.

The data are structured in rows of comma-separated values. This is known as a CSV file. It is the most common way you will find data published online. Save the file with the name ``prop-committees.csv`` in the same directory where you made your notebook.

Open the file in your notebook using the `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>`_ function in ``pandas``.

.. code-block:: python

    pandas.read_csv("prop-committees.csv")

After you run the cell, you should see something like this.

.. image:: /_static/read_csv.png


It is a ``DataFrame`` where ``pandas`` has structured the CSV data into rows in columns, just like Excel or another spreadsheet software might. The advantage offered here is that rather than manipulating the data through a haphazard series of clicks and keypunches, we will be gradually grinding down the data using a computer programming script that is 100% transparent and reproducible.

In order to do that, we need to store our ``DataFrame`` so it can be reused in subsequent cells. We can do this by saving in a `"variable" <https://en.wikipedia.org/wiki/Variable_(computer_science)>`_, which is a fancy computer programming word for a named shortcut where we save our work as we go.

Go back to your initial cell and change it to this. Then rerun it.

.. code-block:: python

    props = pandas.read_csv("./docs/_static/prop-committees.csv")

After you run it, you shouldn't see anything. That's a good thing. It means our ``DataFrame`` has been saved under the name ``props``, which we can now begin interacting with in the cells that follow. We can do this by calling `"methods" <https://en.wikipedia.org/wiki/Method_(computer_programming)>`_ that ``pandas`` has made available to all ``DataFrames``. There are dozens of these that can do all sorts of interesting things. Let's start with some easy ones that analysts
use all the time.

First, to preview the first few rows of the dataset, try the `head <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html>`_ method.

.. code-block:: python

    props.head()

.. image:: /_static/head.png

To get a look at all of the columns and what type of data they store, try `info <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html>`_.

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

Now that we've seen all the propositions in the dataset, we're ready to take a crucial step towards our goal by filtering the list down to just those committees that supported or opposed Proposition 64.

We can do that by copying the full name of the proposition that appears in the dataset and inserting it into the following statement, which follows the ``pandas`` system for filtering a ``DataFrame``.

You start with the variable you want to filter, and then create an evaluation by combining a column with an `"operator" <https://en.wikipedia.org/wiki/Operator_(computer_programming)>`_ like ``==`` or ``>`` or ``<`` with a value to compare the field against.

.. code-block:: python

    props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

.. image:: /_static/prop_filter.png

Now that we've seen what it outputs, we should save the results of that filter into new variable separate from the full list we imported from the CSV file.

.. code-block:: python

    prop = props[props.prop_name == 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.']

The find out how many records are left after the filter, we can use Python's built-in `len <https://docs.python.org/2/library/functions.html#len>`_ function to inspect our new variable.

.. code-block:: python

    len(prop)

.. image:: /_static/prop_len.png

With that we're ready to move on to a related, similar task: Importing all of the individual contributions reported to last year's 17 ballot measures and filtering them down to just those supporting and opposing Proposition 64.

We're start by downloading `this second CSV file <http://first-python-notebook.readthedocs.io/en/latest/_static/contributions.csv>`_ and saving it to the same directory as this notebook with the name ``contributions.csv``. We'll then open it with ``read_csv`` and save it as a new variable just as we did above.

.. warning::

    The contributions file you're downloading is an experimental early release from `the California Civic Data Coalition's effort <www.californiacivicdata.org>`_ to streamline the state's jumbled, dirty and disorganized official database. It has not yet been fully verified as accurate by our team and any conclusions you draw from it should be considered as provisional.

    If you want to base a news report off the analysis you do here, you should take the additional step of comparing the numbers you produce against the official data `released by the Secretary of State <http://cal-access.sos.ca.gov/>`_.

.. code-block:: python

    contribs = pandas.read_csv("contributions.csv")

Just as we did earlier, you can inspect the contents of this new file with the ``head`` method.

.. code-block:: python

    contribs.head()

.. image:: /_static/contribs_head.png

You should also inspect the columns using the ``info`` method. Running these two tricks whenever you open a new file is a good habit to develop so that you can carefully examine the data you're about to work with.

.. code-block:: python

    contribs.info()

.. image:: /_static/contribs_info.png

Our next job is to filter down this list, which include all disclosed contributions to all proposition campaigns, to just those linked to Proposition 64.

We could try to do this with a filter, as we did above with the committees. But look carefully at the columns listed above in the contribution file's ``info`` output. You will notice that this file contains a field called ``calaccess_committee_id`` that identical to the one found in the committee CSV.

That's because these two files are drawn from a `"relational database" <https://en.wikipedia.org/wiki/Relational_database>`_ that tracks a variety of information about campaigns using an array of tables linked by common identifiers. In this case, the unique identifying codes of committees in one table can be expected to match those found in another.

We can therefore safely join the two files using the `pandas` `merge <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html>`_ method. By default this method will return only those rows that have matching ids. That means that if we join the full contributions file to our filtered list of Proposition 64 committees, only the contributions to those committees will remain.

Here's how to do it. It's as simple as passing both variables to ``merge`` and specifying which field we'd like to join. We will save the result into another new variable.

.. code-block:: python

    merged = pandas.merge(prop, contribs, on="calaccess_committee_id")

That new ``DataFrame`` variable can inspected just as the ones above.

.. code-block:: python

    merged.head()

.. image:: /_static/merged_head.png

After all that we have created a new dataset that includes only contributions supporting and opposing Proposition 64. We're ready to move on from preparing our data and to interviewing it.

Act 4: Hello analysis
---------------------

In some ways, your database is no different from a human source. Getting a good story requires careful, thorough questioning. In this section we will move ahead by conducting an interview with ``pandas`` to pursue our quest of finding out the biggest donors to Proposition 64.

Let's start with something easy. What were the ten biggest contributions? We can find the answer by using the `sort_values <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html>`_ method to rearrange our list using the ``amount`` field.

.. code-block:: python

    merged.sort_values("amount")

.. image:: /_static/merged_sort.png

Note that returns the ``DataFrame`` resorted in ascending order from lowest to highest. To answer our question you'll need to reverse it. Here's how:

.. code-block:: python

    merged.sort_values("amount", ascending=False)

.. image:: /_static/merged_sort_desc.png

You can limit the result to the top five by returning to the ``head`` method and passing in the number of results we'd like.

.. code-block:: python

    merged.sort_values("amount", ascending=False).head(5)

.. image:: /_static/merged_sort_head.png

Question one answered. Here's number two: What is the total sum of contributions that have been reported?

To answer that let's start by getting our hands on ``amount``, the column with the numbers in it. We can do that just as we did with other columns above.

.. code-block:: python

    merged.amount

.. image:: /_static/merged_amount.png

Now add up the column's total using the ``pandas`` method `sum <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sum.html>`_.

.. code-block:: python

    merged.amount.sum()

.. image:: /_static/merged_amount_sum.png

There's our big total. Fun fact: This number is guaranteed to be lower than the totals reported by the campaigns. Why? Campaigns are only required to report the names of donors over $200, so our data is missing all of the donors who gave smaller amounts of money.

The overall totals are reported elsewhere in lump sums and cannot be replicated by adding up the individual contributions. Understanding this is crucial to understanding not just this data, but all campaign finance data.

Adding up a big total is all well and good. But we're aiming for something more nuanced. We want to separate the money spent for the proposition from the money spent against it. To do that, we'll need to return to the filtering trick we learned above.

First let's look at the column we're going to filter by, ``committee_position``.

.. code-block:: python

    merged.committee_position

.. image:: /_static/merged_position.png

Now let's filter our merged table down using that column and the ``pandas`` filtering method that combines a column, an operator and the value we want to filter by.

.. code-block:: python

    merged[merged.committee_position == 'SUPPORT']

.. image:: /_static/support_filter.png

Let's stick the result in a variable.

.. code-block:: python

    support = merged[merged.committee_position == 'SUPPORT']

And count how many contributions are in this new, more limited set.

.. code-block:: python

    len(support)

.. image:: /_static/support_len.png

We can now use this new variable to rank the five biggest supporting contributions by using ``sort_values`` again.

.. code-block:: python

    support.sort_values("amount", ascending=False).head(5)

.. image:: /_static/support_sort.png

Now let's repeat all that for opposing contributions. First the filter into a new variable.

.. code-block:: python

    oppose = merged[merged.committee_position == 'OPPOSE']

Then a count.

.. code-block:: python

    len(oppose)

.. image:: /_static/oppose_len.png

Then a ranking.

.. code-block:: python

    oppose.sort_values("amount", ascending=False).head(10)

.. image:: /_static/oppose_sort.png

Now lets sum up the total disclosed contributions to each for comparison. First the opposition.

.. code-block:: python

    oppose.amount.sum()

.. image:: /_static/oppose_amount_sum.png

The the proponents.

.. code-block:: python

    support.amount.sum()

.. image:: /_static/support_amount_sum.png

The support is clearly larger. But what percent is it over the overall disclosed total? We can find out by combined two sum calculations using the division operator. By dividing the support sum into the merged table's overall sum, we get its percentage of the whole.

.. code-block:: python

    support.amount.sum() / merged.amount.sum()

.. image:: /_static/support_amount_percent.png

We've encountered a lot of different committees as we've explored the data. A natural question follows: Which ones have raised the most money?

To figure that out, we'll need to group the data by that column and then sum up the ``amount`` for each. We can do that be using the ``pandas`` `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_ method and the `sum` trick we've already learned.

If you scroll back up and look carefully as the ``info`` command we ran after merging out data, you will noticed it includes a column named ``committee_name_x`` and ``commitee_name_y``. That is because the field was present on both our committee list and our contributions list prior to joining them together. Rather than drop one of them, ``pandas`` is trained to keep them both and to append a suffix to the end.

That's the field we want to group by here. Since they are identical, it doesn't matter which one we pick.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum()

.. image:: /_static/committee_group.png

Again our data has come back as an ugly ``Series``. To reformat it as a pretty ``DataFrame`` use the ``reset_index`` method again.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum().reset_index()

.. image:: /_static/committee_group_df.png

Sorting the biggest totals to the top is as easy as appending the ``sort_values`` trick we already know to the end. And voila there's our answer.

.. code-block:: python

    merged.groupby("committee_name_x").amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/committee_group_sort.png

Finding the top contributors is just as easy. We only need to substitute the name fields into the ``groupby`` method.

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/name_group.png

.. note::

    You should be noticing that several of the top contributors appear to be the same person with their name entered in slightly different ways. This is another important lesson of campaign contributions data. Virtually none of the data is standardized by the campaigns or the government. The onus is on the analyst to show caution and responsibly combine records where the name fields refer to the same person.

To find out if each contributor supported or opposed the measure, you simple add that field to our ``groupby`` method.

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)

.. image:: /_static/name_position_group.png

You've done it. Our brief interview is complete and you've answered the big question that started our inquiry. If you're interested in continuing the interview, see if you can answer a few more questions on your own. Here are some ideas:

- What percentage of donations came from people who live outside of California?
- What are the top employers of donors who gave for and against the measure?
- Which committees had the fewest donors?

Act 5: Hello science
--------------------

After all this, you might be thinking "Computer programming sounds great, but couldn't I have done it more efficiently in Excel?"

Depending on how slick you are with a spreadsheet, the answer might be yes. With the exception of the ``pandas`` trick that merged the two files most of what we did could be achieved with filters and pivot tables taught in spreadsheet classes.

However, for all their flexibility, one of the great weaknesses of working with spreadsheets is that the numerous steps that go into conducting a complex analysis have to be repeated each time, by hand, whenever you want to replicate your work.

For this reason, some scientific projects that aim for transparency and reproducibility are now requiring that each step in a data analysis be documented in a Jupyter Notebook.

That's good for its own sake and will help catch errors during pre-publication review, but it has a huge added benefit. At any time you can slightly modify your code and rerun the entire thing from the start.

In this case it means we could instantly reproduce our analysis for each of the 17 ballot measures and conduct a similar data interview in a matter of seconds.

To give it a try, scroll back up to the stop of the notebook and reexamine the list of unique propositions we output with the ``value_counts`` method. You can pick any of them. For this example I am going to pick Proposition 66, which sought (and failed) to end California's death penalty.

Copy the proposition's full name and replace Proposition 64's name in the nearby cell where we created the ``prop`` variable.

.. code-block:: python

    prop = props[props.prop_name == 'PROPOSITION 066- DEATH PENALTY. PROCEDURES. INITIATIVE STATUTE.']

Now pull down the ``Cell`` menu at the top of the notebook and select the ``Run all`` option.

.. image:: /_static/run_all.png

Moments later, the notebook will repopulate with the answers to all of questions. This time it will be analyzing Prop 66 instead. Try doing that with Excel.

That's the end of our lesson for now. We'll be working to expand it in the coming weeks as we prepare a longer version for the National Insitute of Computer-Assisted Reporting conference in Jacksonville. If you have any thoughts about how it could be improved or expanded, please email me at `ben.welsh@gmail.com <mailto:ben.welsh@gmail.com>`_. You can learn more about our open-source effort to fix California's cryptic campaign-finance database at `californiacivicdata.org <http://www.californiacivicdata.org/>`_.
