# 100 - Installation

Based on "Flask Installation" at https://flask.palletsprojects.com/en/3.0.x/installation/

## Python Version

We recommend using the latest version of Python. Flask supports Python 3.8 and newer. (GitPod supports version 3.12.6 at the time of this writing).

## Dependencies

These distributions will be installed automatically when installing Flask.

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) implements WSGI, the standard Python interface between applications and servers.

- [Jinja](https://palletsprojects.com/p/jinja/) is a template language that renders the pages your application serves.

- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

- [Click](https://palletsprojects.com/p/click/) is a framework for writing command line applications. It provides the ```flask``` command and allows adding custom management commands.

- [Blinker](https://blinker.readthedocs.io/) provides support for [Signals](https://flask.palletsprojects.com/en/3.0.x/signals/).

### Optional dependencies

These distributions will not be installed automatically. Flask will detect and use them if you install them.

- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) enables support for [Environment Variables From dotenv](https://flask.palletsprojects.com/en/3.0.x/cli/#dotenv) when running ```flask``` commands.

- [Watchdog](https://pythonhosted.org/watchdog/) provides a faster, more efficient reloader for the development server.

### Greenlet

You may choose to use gevent or eventlet with your application. In this case, greenlet>=1.0 is required. When using PyPy, PyPy>=7.3.7 is required.

These are not minimum supported versions, they only indicate the first versions that added necessary features. You should use the latest versions of each

## Virtual environments

Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the **[venv](https://docs.python.org/3/library/venv.html#module-venv)** module to create virtual environments.

### Create an environment

Create a project folder and a ```.venv``` folder within:

macOS/Linux:

```
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

Windows:

```
> mkdir myproject
> cd myproject
> py -3 -m venv .venv
```

### Activate the environment

Before you work on your project, activate the corresponding environment:

macOS/Linux:

```
$ . .venv/bin/activate
```

Windows:

```
> .venv\Scripts\activate
```

Your shell prompt will change to show the name of the activated environment.

## Install Flask

Within the activated environment, use the following command to install Flask:

```
$ pip install Flask
```

Flask is now installed. Check out the [Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/) or go to the [Documentation Overview](https://flask.palletsprojects.com/en/3.0.x/).


======= UPDATE BELOW ==========

From the root of the repository (opened in GitPod) run the following command which will install all the required packages):

```
$ pip install -r requirements.txt
```

**WARNING**: You may encounter the following: 

```
AttributeError: module 'configparser' has no attribute 'SafeConfigParser'. Did you mean: 'RawConfigParser'?
```

We do **not** have a solution for above error as of yet. :(

If no error, continue:

Install setuptools and wheel:

```
$ pip install -U pip setuptools wheel
```

Install spacy:

```
$ pip install -U spacy
```

Run the following command which will download the [spacy](https://spacy.io/usage/models) NLP language model.

```
$ python -m spacy download en_core_web_md
```

**WARNING**: You may encounter the following:

```
/home/gitpod/.pyenv/versions/3.12.6/bin/python3: No module named spacy
```

If so, make sure you have ran ```$ pip install -U spacy```. Then try again.

OPTIONAL: The [spaCy VSCode Extension](https://github.com/explosion/spacy-vscode) provides additional tooling and features for working with spaCy’s config files. 

Optional, run below command to comply with SpaCy VS Code extension:

```
$ pip install -U pygls
```