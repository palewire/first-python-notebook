# JupyterLab

A [Jupyter](http://jupyter.org/) notebook is a browser-based interface where you can write, run, remix and republish code.

It is free software that anyone can install and run. It is used by [scientists](http://nbviewer.jupyter.org/github/robertodealmeida/notebooks/blob/master/earth_day_data_challenge/Analyzing%20whale%20tracks.ipynb), [scholars](http://nbviewer.jupyter.org/github/nealcaren/workshop_2014/blob/master/notebooks/5_Times_API.ipynb), [investors](https://github.com/rsvp/fecon235/blob/master/nb/fred-debt-pop.ipynb) and corporations to create and share their research.

It is also used by journalists to develop stories and show their work. Examples published by past students and teachers of this class include:

* [“As Opioid Crisis Ramped Up, Pills Flowed Into Vermont by the Millions”](https://github.com/asuozzo/arcos-opioid-analysis-vt) by 
Andrea Suozzo
* [“A frenzy of well drilling is depleting aquifers in California farmland.”](https://github.com/datadesk/groundwater-analysis) by Gabrielle LaMarr LeMee
* [“What it’s like to go to school when dozens have been killed nearby”](https://github.com/datadesk/highschool-homicide-analysis) by Iris Lee
* [“City of Chicago Parking and Camera Ticket Data”](https://github.com/propublica/il-tickets-notebooks) by David Eads
* [“Chicago's Sidewalk Snow Clearance: The North Side Complains, the South Side Gets Fined“](https://github.com/reliablerascal/snow-clearance) by Rob Reid

You can find hundreds of other examples [on GitHub](https://github.com/search?q=language%3A%22Jupyter+Notebook%22&type=Repositories&ref=advsearch&l=Jupyter+Notebook&l=&s=updated&o=desc), including notebooks published by [Buzzfeed](https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis/blob/master/notebooks/tennis-analysis.ipynb), [ProPublica](https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb), [The Economist](https://github.com/theeconomist/big-mac-data/blob/master/Big%20Mac%20data%20generator.ipynb), [POLITICO](https://github.com/The-Politico/politico-2018-district-similarity-maps/blob/master/demographic_similarity.ipynb), [The Markup](https://github.com/the-markup/investigation-isp) and [the Los Angeles Times](https://github.com/datadesk/notebooks).

There are numerous ways to install and configure Jupyter notebooks. Since this tutorial is designed for beginners, it will demonstrate how to use [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop), a self-contained application that provides a ready-to-use Python environment with several popular libraries bundled in. It can be installed on any operating system with a simple point-and-click interface.

```{note}
Advanced users like to have more control over when and where code is installed on their system. Readers interested in the techniques preferred by the pros should consult [our appendix](/appendix/index.md). It requires use of your computer’s command-line interface.
```

## Install JupyterLab Desktop

<div class="responsive-iframe-container">
    <iframe class="responsive-iframe" src="https://www.youtube.com/embed/578B63wZ7rI?si=0G3M2pFHt71J8irv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

The first step is to visit [JupyterLab Desktop’s homepage on GitHub](https://github.com/jupyterlab/jupyterlab-desktop) in your web browser.

![Jupterlab Desktop homepage](/_static/jupyter-desktop-repo.png)

Scroll down to the documentation below the code until you reach the [Installation](https://github.com/jupyterlab/jupyterlab-desktop) section.

![jupyterlab desktop download](/_static/jupyter-desktop-install.png)

Then pick the link appropriate for your operating system. The installation file is large so the download might take a while.

Find the file in your downloads directory and double click it to begin the installation process. Follow the instructions presented by the pop-up windows, sticking to the default options. 

```{warning}
Your computer's operating system might flag the JupyterLab Desktop installer as an unverified or insecure application. Don't worry. The tool has been vetted by Project Jupyter's core developers and it's safe to use.

If your system is blocking you from installing the tool, you'll likely need to work around its barriers. For instance, on MacOS, this might require [visiting your system’s security settings](https://www.wikihow.com/Install-Software-from-Unsigned-Developers-on-a-Mac) to allow the installation. 
```