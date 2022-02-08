===================================
Chapter 1: Hello JupyterLab Desktop
===================================

A `Jupyter notebook`_ is a browser-based interface where you can write, run, remix and republish code.

It is free software you can install and run like any other open-source library. It is used by `scientists`_, `scholars`_, `investors`_ and corporations to create and share their research.

It is also used by journalists to develop stories and show their work. Examples include:

* `"The Tennis Racket"`_ by BuzzFeed and the BBC
* `"Machine bias"`_ by ProPublica
* `More than 35 different notebooks`_ published by the Los Angeles Times

There are numerous ways to install and configure Jupyter notebooks. Since this tutorial is designed for beginners, it will demonstrate how to use `JupyterLab Desktop <https://github.com/jupyterlab/jupyterlab-desktop>`_, a self-contained application that provides a ready-to-use Python environment with several popular libraries already bundled in. It can be installed on any operating system with a simple point-and-click interface.

.. note::

    Advanced users like to take advantage of Python’s power tools to have more control over when and where code is installed on their system. Readers interested in the techniques preferred by the pros should consult `our appendix <../appendix/>`_. It requires use of your computer’s command-line interface.


Install JupyterLab Desktop
==========================

The first step is to visit `JupyterLab Desktop’s homepage on GitHub <https://github.com/jupyterlab/jupyterlab-desktop#download>`_ in your web browser.

.. image:: /_static/jupyterlabdesktop-homepage.png

Scroll down to the documentation below the code until you reach the `Download <https://github.com/jupyterlab/jupyterlab-desktop#download>`_ section.

.. image:: /_static/jupyterlabdesktop-download.png

Then pick the link appropriate for your operating system. The installation file is large so the download might take a while.

Find the file in your downloads directory and double click it to begin the installation process. Follow the instructions presented by the pop-up windows, sticking to the default options. 

.. warning::

    Your computer's operating system might flag the JupyterLab Desktop installer as an unverified or insecure application. Don't worry. The tool has been vetted by Project Jupyter's core developers and it's safe to use.
    
    If your system is blocking you from installing the tool, you'll likely need to work around its barriers. For instance, on MacOS, this might require `visiting your system’s security settings <https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac>`_ to allow the installation. 

Once the program is installed, you can accept the installation wizard's offer to immediately open the program, or you can search for "Jupyter Lab" in your operating system’s application finder.

That will open up a new window that looks something like this:

.. image:: /_static/jupyterlabdesktop.png

Hit the "Python 3" button in the launcher panel on the right and you're ready to move on to our next chapter.

.. _scientists: http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb
.. _scholars: http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb
.. _investors: https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb
.. _"The Tennis Racket": https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb
.. _More than 35 different notebooks: https://github.com/datadesk/notebooks
.. _"Machine bias": https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb
.. _Jupyter Notebook: http://jupyter.org/
