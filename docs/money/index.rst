======================
Chapter 4: Hello money
======================

In November 2016, California voters had a lot of decisions to make.

Millions of votes `were cast <http://graphics.latimes.com/la-na-pol-2016-election-results-california/>`_ across the state to choose who should be America's next president, to send more than 50 members off to Congress, to select a new U.S. senator and to refill most of the seats in the Sacramento statehouse.

On top of all that, every ballot in the state included a list of propostions, yes or no questions that give voters the power to directly change the law.

They vary every election, and this time 17 different proposals were put to voters.

.. figure:: /_static/voter_guide.jpg
    :align: right
    :width: 350px

    The state's record setting voter guide

Should the state take out $9 billion in bonds to fund education? Should the cost of prescription drugs be limited? Should the cigarette tax be increased? Should recreational marijuana use be legalized? Should actors in pornographic films be required to wear condoms? Should the state stop administering the death penalty? Or should it instead speed up administering the death penalty?

And that's just the start. The election guide the state sends to every registered voter `set a new record <http://www.latimes.com/politics/la-pol-ca-california-voter-guide-november-ballot-20160909-snap-story.html>`_ for length at 224 pages long.

***************
Meet CAL-ACCESS
***************

By election day, nearly $500 million dollars was spent by political campaigns that sought to influence voters to vote yes or no on those 17 propositions.

We know that because every dollar that is raised or spent by political campaigns in the state of California has to be disclosed. That's thanks to the `Political Reform Act of 1974 <http://www.fppc.ca.gov/about-fppc/about-the-political-reform-act.html>`_, which was itself enacted by voters via a proposition.

Groups that support or oppose propositions, known as "committees," must register with the secretary of state and file periodic reports. Those reports list the names, occupations and employers of donors, as well as how campaign funds are spent.

.. figure:: /_static/hello_calaccess.png
    :align: right
    :width: 350px

    The CAL-ACCESS website at `cal-access.sos.ca.gov <http://cal-access.sos.ca.gov/>`_

Those reports are stored in a public database maintained by the government. Almost every state has one like it. In California, the database is called `CAL-ACCESS <http://cal-access.sos.ca.gov/>`_.

The CAL-ACCESS website offers tools to inspect recent filings, and `a bulk download <http://www.sos.ca.gov/campaign-lobbying/cal-access-resources/raw-data-campaign-finance-and-lobbying-activity/>`_ where you can access the raw data.

Unfortunately, the downloadable files are so jumbled, dirty and difficult that they are rarely used.

Even the secretary of state himself, Alex Padilla, has condemned CAL-ACCESS as a `Frankenstein monster of code <http://www.sacbee.com/news/politics-government/capitol-alert/article49257065.html>`_.

****************************************
Meet the California Civic Data Coalition
****************************************

In 2014, a team of journalists, academics and developers formed to solve the problem. They call themselves the `California Civic Data Coalition <http://www.californiacivicdata.org/about/>`_.

Their project, which is still in development, aims to create an open-source pipeline that converts the raw data published by CAL-ACCESS into refined data files that a beginner, like yourself, can easily pick up and analyze.

The coalition's effort has drawn hundreds of contributions from developers and journalists at dozens of news organizations and was named a winner of the `Knight News Challenge <http://www.californiacivicdata.org/2015/07/22/knight-news-challenge/>`_.

.. figure:: /_static/hello_ccdc.png
    :align: right
    :width: 350px

    Downloads `now offered <http://calaccess.californiacivicdata.org/downloads/latest/>`_ at the coalition's website

Experimental versions of the coalition's data files enabled `the Los Angeles Times <http://www.latimes.com/politics/la-pol-ca-road-map-california-2018-campaign-spending-20170219-story.html?foo=bar>`_ to calculate the $500 million figure quoted earlier in this chapter. It has also powered `interactive graphics <http://www.latimes.com/projects/la-pol-ca-california-governor-2018-money/>`_ and `several <http://www.latimes.com/local/politics/la-me-pol-brown-money-20141031-story.html>`_ `other <http://www.latimes.com/politics/la-pol-ca-newsom-waterfront-governor-20170519-story.html>`_ investigations into the role of money in state politics.

You can review, install and contribute to the coalition's open-source codebase `on GitHub <www.github.com/california-civic-data-coalition>`_.

Currently, the coalition's `website <http://www.californiacivicdata.org/>`_ archives the data published each day by the state and offers more complete documentation and easier access to the original files.

In the near future, the site will offer simplified data files free to the public that make it signficantly easier to understand and investigate. Until they reach that goal we will be working with experimental early versions created for this class.

In the next chapter, we will show how to import that data into pandas and your notebook to start an analysis.
