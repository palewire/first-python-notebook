:tocdepth: 2

=====================
First Python Notebook
=====================

A step-by-step guide to analyzing data with Python and the Jupyter Notebook.

It was developed by `Ben Welsh <http://palewi.re/who-is-ben-welsh/>`_ for a `Oct. 2, 2016, "watchdog workshop" organized by Investigative Reporters and Editors <http://ire.org/events-and-training/event/2819/2841/>`_
at San Diego State University's school of journalism. It is scheduled to be taught to students at Stanford's Journalism School
and at the annual conference of the National Institute for Computer-Assisted Reporting in early 2017.


What you will learn
-------------------

This three-hour tutuorial will guide you through an investigation of money in politics using data from the `California Civic Data Coalition <http://www.californiacivicdata.org/>`_.

You will learn just enough Python to do damage with the powerful `pandas <http://pandas.pydata.org/>`_  data analysis library, the most popular open-source
library for working with large data files. You will also learn how to record, remix and republish your analysis
using the `Jupyter Notebook <http://jupyter.org/>`_, a browser-based tool for writing code
that is emerging as the standard for sharing reproducible research in the sciences.

And most important: you will see how these tools can increase the speed and veracity of your journalism.


Prelude: Prequisites
--------------------

Before you can begin, your computer needs the following tools installed and working to participate.

1. A `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_ to interact with your computer
2. Version 2.7 of the `Python <http://python.org/download/releases/2.7.6/>`_ programming language
3. The `pip <https://pip.pypa.io/en/latest/installing.html>`_ package manager and `virtualenv <http://www.virtualenv.org/en/latest/>`_ environment manager for Python


Command-line interface
~~~~~~~~~~~~~~~~~~~~~~

Unless something is wrong with your computer, there should be a way to open a window that lets you type in commands. Different operating systems give this tool slightly different names, but they all have some form of it, and there are alternative programs you can install as well.

On Windows you can find the command-line interface by opening the "command prompt." Here are instructions for `Windows 10 <http://www.howtogeek.com/235101/10-ways-to-open-the-command-prompt-in-windows-10/) and for [Windows 8](http://windows.microsoft.com/en-us/windows/command-prompt-faq#1TC=windows-8) and [earlier versions](http://windows.microsoft.com/en-us/windows-vista/open-a-command-prompt-window>`_.
On Apple computers, you open the `"Terminal" application <http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line>`_.
Ubuntu Linux comes with a program of the `same name <http://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it>`_.


Python
~~~~~~

If you are using Mac OSX or a common flavor of Linux, Python version 2.7 is probably already installed and you can test to see what version,
if any, is already available by typing the following into your terminal.

.. code-block:: bash

    python -V

Even if you find it already on your machine, Mac users should install it separately by following
`these instructions <http://docs.python-guide.org/en/latest/starting/install/osx/>`_ offered by The Hitchhikers Guide to Python.

Windows people can find a similar guide `here <http://docs.python-guide.org/en/latest/starting/install/win/>`_ which will have them try
downloading and installing Python from `here <https://www.python.org/downloads/release/python-2712/>`_.
