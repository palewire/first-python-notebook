=========================
Chapter 3: Hello analysis
=========================

Until last November, the use and sale of marijuana for recreational purposes was illegal in California. That changed when voters approved Proposition 64, which asked voters if the practice ought to be legalized. A yes vote supported legalization. A no vote opposed it. `In the final tally <http://elections.cdn.sos.ca.gov/sov/2016-general/sov/65-ballot-measures-formatted.pdf>`_, 57% of voters said yes.

Your mission, `should you choose to accept it <https://www.youtube.com/watch?v=0TiqXFssKMY>`_, is to analyze lists of campaign committees and contributors to figure out the biggest donors both for and against the measure.

To start `click here <http://first-python-notebook.readthedocs.io/en/latest/_static/prop-committees.csv>`_ to download a list of last November's 17 ballot measures and their affiliated fundraising committees.

The data are structured in rows of comma-separated values. This is known as a CSV file. It is the most common way you will find data published online. Save the file with the name ``prop-committees.csv`` in the same directory where you made your notebook.

Open the file in your notebook using the `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>`_ function in ``pandas``.

.. code-block:: python

    pandas.read_csv("prop-committees.csv")

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

Our next job is to filter down this list, which includes all disclosed contributions to all proposition campaigns, to just those linked to Proposition 64.

We could try to do this with a filter, as we did above with the committees. But look carefully at the columns listed above in the contribution file's ``info`` output. You will notice that this file contains a field called ``calaccess_committee_id`` that is identical to the one found in the committee CSV.

That's because these two files are drawn from a `"relational database" <https://en.wikipedia.org/wiki/Relational_database>`_ that tracks a variety of information about campaigns using an array of tables linked by common identifiers. In this case, the unique identifying codes of committees in one table can be expected to match those found in another.

We can therefore safely join the two files using the ``pandas`` `merge <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html>`_ method. By default this method will return only those rows with ids found in both tables. That means that if we join the full contributions file to our filtered list of Proposition 64 committees, only the contributions to the Proposition 64 committees will remain.

Here's how to do it. It's as simple as passing both variables to ``merge`` and specifying which field we'd like to join with. We will save the result into another new variable.

.. code-block:: python

    merged = pandas.merge(prop, contribs, on="calaccess_committee_id")

That new ``DataFrame`` variable can inspected just as the ones above.

.. code-block:: python

    merged.head()

.. image:: /_static/merged_head.png

After all that we have created a new dataset that includes only contributions supporting and opposing Proposition 64. We're ready to move on from preparing our data to interviewing it.


==========================

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

Now sum up the total disclosed contributions to each for comparison. First the opposition.

.. code-block:: python

    oppose.amount.sum()

.. image:: /_static/oppose_amount_sum.png

Then the supporters.

.. code-block:: python

    support.amount.sum()

.. image:: /_static/support_amount_sum.png

The support is clearly larger. But what percent is it of the overall disclosed total? We can find out by combined two ``sum`` calculations using the division operator.

.. code-block:: python

    support.amount.sum() / merged.amount.sum()

.. image:: /_static/support_amount_percent.png

We've encountered a lot of different committees as we've explored the data. A natural question follows: Which ones have raised the most money?

To figure that out, we'll need to group the data by that column and then sum up the ``amount`` for each. We can do that be using the ``pandas`` `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_ method and the ``sum`` trick we've already learned.

If you scroll back up and look carefully as the ``info`` command we ran after merging out data, you will noticed it includes a column named ``committee_name_x`` and ``commitee_name_y``. That is because the field was present on both our committee list and our contributions list prior to joining them together. Rather than drop one of them, ``pandas`` is trained to keep them both and to append suffixes to the end.

That's the field we want to group by here. Since they are identical, it doesn't matter which one we pick. Let's go with x.

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
