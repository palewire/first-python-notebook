=======================
Chapter 9: Hello totals
=======================

In some ways, your database is no different from a human source. Getting a good story requires careful, thorough questioning. In this section we will move ahead by conducting an interview with pandas to pursue our quest of finding out the biggest donors to Proposition 64.

.. youtube:: -xjprU5jlO0

Using tricks we learned as far back as :doc:`chapter three <pandas/index>`, we can start off by answering a simple question: What is the total sum of Proposition 64 contributions that have been reported?

****************
Summing a column
****************

To answer that let's start by getting our hands on amount, the column from the contributions DataFrame with the numbers in it. We can do that just as we did with other columns above.

.. code-block:: python

    merged.amount

Now we can add up the column's total using the pandas method `sum <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.sum.html>`_, just as we did when we were first getting started with pandas.

.. code-block:: python

    merged.amount.sum()

And printed out below your cell, there's our answer.

We've completed our first piece of analysis and discovered the total amount spent on this proposition.

Time to run off to Twitter and publish our results to the world, right?

Wrong.

*******************
How not to be wrong
*******************

The total we generated is not the overall total raised in the campaign, and is guaranteed to be lower than the totals reported in the media and by the campaigns.

Why?

In California, campaigns are `only required <http://www.documentcloud.org/documents/2781363-460-2016-01.html#document/p10>`_ to disclose the names of donors who give over $100, so our data is missing all of the donors who gave less than that amount.

The cutoff varies, and there are some exceptions, but the same thing is true in other states and also at the federal level in races for Congress and the White House.

The overall totals are instead reported on cover sheets included with disclosure reports that lump together all the smaller contributions as part of a grand total. Those are the records most commonly cited to total up a campaign's fundraising.

The result is that an itemized list of contributions, like the one we have, cannot be used to calculate a grand total. That's true in California and virtually anywhere else you work with campaign data. Overlooking that limitation is a rookie mistake routinely made by analysts new to this field.

But that doesn't mean our data is worthless. We just have to use it responsibly. In many cases, professional campaign reporters will refer to an analysis drawn from a list like ours as applying only to "large donors."

Since large donors typically account for most of the money, the results are still significant. And the high level of detail included in each record — like the donor's name, employer and occupation — makes the limitations worth working through.

************************************
Which side got more large donations?
************************************

Adding up a big total is all well and good. But we're aiming for something more nuanced.

We want to separate the money spent supporting the proposition from the money opposing it. Then we want to find out who raised more.

To answer that question, lets return to the filtering technique we learned in :doc:`chapter seven <filters/index>`.

First let's look at the column we're going to filter by, committee_position.

.. code-block:: python

    merged.committee_position.value_counts()

Now let's filter our merged table down using that column and the pandas filtering method that combines a column, an operator and the value we want to filter by. Let's stick the result in a variable.

.. code-block:: python

    support = merged[merged.committee_position == 'SUPPORT']

Now let's repeat all that for opposing contributions. First the filter into a new variable.

.. code-block:: python

    oppose = merged[merged.committee_position == 'OPPOSE']

Now sum up the total disclosed contributions to each for comparison. First the opposition.

.. code-block:: python

    oppose.amount.sum()

Then the supporters.

.. code-block:: python

    support.amount.sum()

The support is clearly larger. But what percent is it of the overall disclosed total? We can find out by combined two ``sum`` calculations using the division operator.

.. code-block:: python

    support.amount.sum() / merged.amount.sum()
