========================
Chapter 4: Hello science
========================

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
