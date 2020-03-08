# Lambda DS Unit 3 - Sprint 1

## Intro

Hey everyone, my name is Mike Rossetti and I'll be your instructor for Unit 3. Our primary goals for this unit are to 1) transition from notebooks to local development, as well as to 2) ensure our data science efforts are verifiable and reproducible.

In the first sprint, we'll focus on getting more comfortable with local development. In the second sprint, we'll focus on databases and SQL. And in the third sprint, we'll build upon the first two sprints by creating database-backed web applications which we'll deploy to a remote server so we can share our data science efforts with the world! Excited? Here we go!

### Dev Tools

I know many of you are already familiar with local development to varying degrees, but some of you may be completely unfamiliar. So follow the instructions below as they pertain to your individual situation.

To get started, we'll want to [download and install **Anaconda 3.7**](https://www.anaconda.com/distribution/), which will provide us with the ability to install and manage local installations of Python and third-party Python packages. IMPORTANT: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools.

To run our Python scripts, we'll need a **command-line utility**. Mac users will use the built-in Terminal application (no need to download anything, although you may want to [customize your Terminal appearance](https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/command-line-computing/mac-terminal-config.md)). Windows users who don't already have a preferred command-line utility are encouraged to [download and install Git Bash](https://git-scm.com/downloads), which will integrate well with the other development tools and allow Windows users to write the same commands as Mac users.

To edit our Python scripts, we'll need a **development-class text editor**. Unless you already have a preferred editor or IDE, you're encouraged to [download and install VS Code](https://code.visualstudio.com/). It is important to install the Python language extension and you may want to further [customize your text editor's appearance and functionality](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md#basic-configuration).

Finally, we need a version control utility to manage different versions of our Python scripts, and interface with GitHub, where we can share our code and collaborate with others. Unless you already have one, please take a moment to [create a GitHub account](https://github.com/) and consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources. We'll eventually want to get comfortable with using Git from the command line, so Windows use the aforementioned Git Bash application for this purpose. Mac users can download Git via homebrew (`brew install git`), or in many cases Git may already be installed on your computer. Students on Mac or Windows who are less comfortable with the command-line can use the [GitHub Desktop](https://desktop.github.com/) application as a temporary bridge tool which provides a graphical user interface (GUI) for performing version control operations.

### Optional Preparation Exercise

Finally, after installing and configuring these local development tools, in order to become more comfortable with command-line computing, you're recommended to complete this [Command-line Computing exercise](https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/command-line-computing).

Good luck, drop questions in Slack if you need help, and see you in lecture!









Lambda Materials:
  + https://learn.lambdaschool.com/ds/module/recwEPR24pu5LCnA5
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments

Running Python Applications from the Command-line:
  + https://github.com/prof-rossetti/my-first-python-app

(BONUS) Development Tools / Software:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/git-bash.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/command-line-computing/mac-terminal-config.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/github-desktop.md
  + https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

(BONUS) CLIs:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/conda.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/pip.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pipenv.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/python.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/git.md
  + https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

(BONUS) Imports and Custom Modules:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/README.md

Publishing Packages to the PyPI:
  + https://github.com/s2t2/game-utils-py
  + https://pypi.org/project/s2t2-game-utils/
  + https://test.pypi.org/project/s2t2-game-utils/
  + http://data-creative.info/reference-docs/2019/05/30/how-to-publish-python-package-pypi/

Choosing a License:

  + https://choosealicense.com/


## Class 2

Outline:

  1) Docs and Docstrings
  2) OOP Concepts
  3) Classes and Inheritance in Python


Topics:

  + code formatting / style / documentation (pep8)
  + refactoring / simplification
  + functional vs object-oriented
  + classes, initialization, construction
  + static methods, properties, attributes, class methods
  + inheritance, super

Lambda Materials:

  + https://learn.lambdaschool.com/ds/module/recqeF16aJfb1UTWF/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module2-oop-code-style-and-reviews

Style, Formatting, and PEP8:

  + https://pep8.org/
  + https://pypi.org/project/autopep8/

Docs / Docstrings:

  + https://readthedocs.org/
  + https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html

Doc generation in the wild (Pandas):

  + https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  + https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py#L319

Classes and OOP:

  + https://docs.python.org/3/tutorial/classes.html
  + https://realpython.com/python3-object-oriented-programming/
  + https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
  + https://realpython.com/instance-class-and-static-methods-demystified/#static-methods

Inheritance Example in the wild (SKLearn):

  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L77
  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L589

(BONUS) Refactoring from Functions to Classes:
  + https://github.com/s2t2/playlist-service-py/blob/25cae16201adc935f71e863a79d51690c00e492b/app/spotify_service.py
  + https://github.com/s2t2/playlist-service-py/blob/master/app/spotify_service.py

(BONUS) Importing Classes:
  + https://github.com/s2t2/playlist-service-py/blob/master/app/sync_service.py


## Class 3

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recLjxZbBV3Jmrj2T/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module3-containers-and-reproducible-builds

Using a Docker image:

```sh
docker run hello-world
```

Using a Dockerfile:

```sh
docker build . -t python
# ...
docker run -it python /bin/bash
```

## Class 4

Lambda Materials:
  + https://learn.lambdaschool.com/ds/module/recq9eVVCzZpgeH58/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module4-software-testing-documentation-and-licensing

Testing Frameworks:
  + https://docs.python.org/3.5/library/unittest.html
  + https://docs.pytest.org/en/latest/

(BONUS) Testing Notes:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/software/testing.md

(BONUS) Previous Lecture and Materials on Testing:
  + https://www.youtube.com/watch?v=pS8pzmtqxVA
  + https://github.com/prof-rossetti/lambda-lecture-pytest

(BONUS) Continuous Integration:
  + https://travis-ci.com/
  + https://travis-ci.com/s2t2/playlist-service-py/builds/142617662
  + https://github.com/s2t2/playlist-service-py/pull/7
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/travis-ci.md
  + https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/ci-123 (edited)


setup from scratch:

```sh
pipenv install
pipenv install pytest --dev
```
run tests:

```sh
pytest
```

or add "`__init__.py`" files to the "app" and "test" directories, and run:

```sh
python -m unittest test.team_test
```
