=====
Remix
=====

Now here's where things get fun. Your entire analysis is scripted top to bottom, which means it can be rerun and reproduced. It also be remixed.

Remember this line earlier?

.. code-block:: python

    my_prop = 'PROPOSITION 064- MARIJUANA LEGALIZATION. INITIATIVE STATUTE.'

That's where we set which proposition we wanted to filter on. It was a key fork in the road, which shaped all the analysis that followed.

That means that if we substituted a different proposition name from the ``value_counts`` list just above it we could rerun our notebook and conduct an identical analysis of another proposition, without writing another line of code.

Let's try it. I picked the death penalty ban that was on the same ballot and changed that cell of code to this:

.. code-block:: python

    my_prop = 'PROPOSITION 062- DEATH PENALTY. INITIATIVE STATUTE.'

Now I go to the Run menu at the top of the notebook and selected "Run All Cells." Wait a few seconds and, boom, you'll have a whole new group of donors plotted out.
