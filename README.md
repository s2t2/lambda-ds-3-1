# Lambda DS Unit 3 - Sprint 1

## Class 1

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
