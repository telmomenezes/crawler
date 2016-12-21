Simple web crawler.

# Installation #

## Clone Repository ##

Start by cloning the source code to your current local directory.

    $ git clone https://github.com/telmomenezes/crawler.git

## Create Virtual Environment and Install Python Packages ##

It is advisable to work with virtual environments. To create one in the current directory you can do this:

    $ virtualenv -p /usr/local/bin/python3 venv

The, anytime you want to activate it:

    $ source venv/bin/activate

Finally, after activating the virtual environment above, you can install the crawler and its Python dependencies:

    $ pip install --editable .


# How to use #

You probably want to use the code directly, but this simple command line tool is provided:

    $ crawler <url>