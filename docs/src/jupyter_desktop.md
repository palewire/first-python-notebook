# JupyterLab

A [Jupyter](http://jupyter.org/) notebook is a browser-based interface where you can write, run, remix and republish code.

It is free software you can install and run like any other open-source library. It is used by [scientists](http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb), [scholars](http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb), [investors](https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb) and corporations to create and share their research.

It is also used by journalists to develop stories and show their work. Examples published by past teachers of this class include:

* [“As Opioid Crisis Ramped Up, Pills Flowed Into Vermont by the Millions”](https://github.com/asuozzo/arcos-opioid-analysis-vt) by 
Andrea Suozzo
* [“A frenzy of well drilling is depleting aquifers in California farmland.”](https://github.com/datadesk/groundwater-analysis) by Gabrielle LaMarr LeMee
* [“What it’s like to go to school when dozens have been killed nearby”](https://github.com/datadesk/highschool-homicide-analysis) by Iris Lee
* [“City of Chicago Parking and Camera Ticket Data”](https://github.com/propublica/il-tickets-notebooks) by David Eads

You can find hundreds of other examples [on GitHub](https://github.com/search?q=language%3A%22Jupyter+Notebook%22&type=Repositories&ref=advsearch&l=Jupyter+Notebook&l=&s=updated&o=desc), including work by [Buzzfeed](https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb), [ProPublica](https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb), [The Economist](https://github.com/theeconomist/big-mac-data/blob/master/Big%20Mac%20data%20generator.ipynb), [POLITICO](https://github.com/The-Politico/politico-2018-district-similarity-maps/blob/master/demographic_similarity.ipynb), [The Markup](https://github.com/the-markup/investigation-isp) and [the Los Angeles Times](https://github.com/datadesk/notebooks).

There are numerous ways to install and configure Jupyter notebooks. Since this tutorial is designed for beginners, it will demonstrate how to use [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop), a self-contained application that provides a ready-to-use Python environment with several popular libraries bundled in. It can be installed on any operating system with a simple point-and-click interface.

```{note}
Advanced users like to take advantage of Python’s power tools to have more control over when and where code is installed on their system. Readers interested in the techniques preferred by the pros should consult [our appendix](/appendix/index.md). It requires use of your computer’s command-line interface.
```

## Install JupyterLab Desktop

The first step is to visit [JupyterLab Desktop’s homepage on GitHub](https://github.com/jupyterlab/jupyterlab-desktop#download) in your web browser.

![jupterlab desktop homepage](/_static/jupyterlabdesktop-homepage.png)

Scroll down to the documentation below the code until you reach the [Download](https://github.com/jupyterlab/jupyterlab-desktop#download) section.

![jupyterlab desktop download](/_static/jupyterlabdesktop-download.png)

Then pick the link appropriate for your operating system. The installation file is large so the download might take a while.

Find the file in your downloads directory and double click it to begin the installation process. Follow the instructions presented by the pop-up windows, sticking to the default options. 

```{warning}
Your computer's operating system might flag the JupyterLab Desktop installer as an unverified or insecure application. Don't worry. The tool has been vetted by Project Jupyter's core developers and it's safe to use.

If your system is blocking you from installing the tool, you'll likely need to work around its barriers. For instance, on MacOS, this might require [visiting your system’s security settings](https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac) to allow the installation. 
```

## Open a Python 3 notebook

Once the program is installed, you can accept the installation wizard's offer to immediately open the program, or you can search for "Jupyter Lab" in your operating system’s application finder.

That will open up a new window that looks something like this:

![jupyterlab desktop](/_static/jupyterlabdesktop.png)

Hit the "Python 3" button in the launcher panel on the right and you're ready to move on to our next chapter.
