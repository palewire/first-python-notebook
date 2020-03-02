=========================
Chapter 11: Hello groupby
=========================

To take the next step towards ranking the top contributors, we'll need to learn a new trick. It's called `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_.

It's a pandas method that allows you to group a DataFrame by a column and then calculate a sum, or any other statistic, for each unique value. This is necessary when you want to rack up statistics on a long list of values, or about a combination of fields.

*********************
Grouping by one field
*********************

As we've been digging through the data, I'm sure a few questions have popped into mind. One interesting field in the contributions list is the home state of the contributor. A natural question follows: How much of the money came from outside of California?

If you scroll back up and look carefully as the info command we ran after merging out data, you will noticed it includes a column named ``contributor_state``.

That's the field we want to group with here. Here's how you do it.

.. code-block:: python

    merged.groupby("contributor_state")

A nice start. But you'll notice you don't get much back. The data's been grouped by state, but we haven't chosen what to do with it yet. We want totals by state, so we can sum the ``amount`` field the same way we did earlier for the entire DataFrame.

.. code-block:: python

    merged.groupby("contributor_state").amount.sum()

Again our data has come back as an ugly Series. To reformat it as a pretty DataFrame use the reset_index method again.

.. code-block:: python

    merged.groupby("contributor_state").amount.sum().reset_index()

Sorting the biggest totals to the top is as easy as appending the sort_values trick we already know to the end. And voila there's our answer.

.. code-block:: python

    merged.groupby("contributor_state").amount.sum().reset_index().sort_values("amount", ascending=False)


***************************
Grouping by multiple fields
***************************

Finding the top contributors is almost as easy, but since the first and last names are spread between two fields we'll need to submit them to groupby as a list. Copy the last line above, and replace "contributor_state" with a list like the one here:

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)

.. note::

    You should be noticing that several of the top contributors appear to be the same person with their name entered in slightly different ways. This is another important lesson of campaign contributions data. Virtually none of the data is standardized by the campaigns or the government. The onus is on the analyst to show caution and responsibly combine records where the name fields refer to the same person.

To find out if each contributor supported or opposed the measure, you simple add that field to our groupby method.

.. code-block:: python

    merged.groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)

If you wanted just the top supporters or opponents alone, you could run those same commands with the support and oppose datasets we filtered down to earlier. Everything else about the commands would be the same as the first one above.

For the supporters:

.. code-block:: python

    support.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)

For the opponents:

.. code-block:: python

    oppose.groupby(["contributor_firstname", "contributor_lastname"]).amount.sum().reset_index().sort_values("amount", ascending=False)

You've done it. Our brief interview is complete and you've answered the big question that started our inquiry.

Or so you think! Look again at our rankings above. Now compare them against the ranking we looked at earlier in our sorting lesson.

Study it closely and you'll see an important difference. All of the contributors without a first name are dropped from our groupby lists. And some of them gave a lot of money.

This is happening because another pandas quirk. Empty fields are read in by pandas as `null values <https://en.wikipedia.org/wiki/Null_(mathematics)>`_, which is a mathematical representation of nothing. In pandas a null is called a `NaN <https://en.wikipedia.org/wiki/NaN>`_ an abbreviation for "not a number" commonly used in computer programming.

And, guess what, pandas' groupby method will drop any rows with nulls in the grouping fields. So all those records without a first name were silently excluded from our analysis.

Yikes! Whatever our opinion of pandas' default behavior, it's something we need to account for, and a reminder that we should never assume we know computer programming tools are doing under the hood. As with human sources, everything you code tells you should be viewed skeptically and verified.

The solution to this problem is easy. We need to replace those NaN first names with empty strings, which pandas won't drop. We can do that by using pandas' fillna method ahead of the group.

.. code-block:: python

    merged.fillna("").groupby(["contributor_firstname", "contributor_lastname", "committee_position"]).amount.sum().reset_index().sort_values("amount", ascending=False)

Now we've finally got a ranking we can work with. Congratulations, you've finished our analysis.

If you're interested in continuing the interview, see if you can answer a few more questions on your own. Here are some ideas:

- What are the top employers of donors for and against the measure?
- Which committees had the fewest donors?
- What was the average size of donations both for and against?
