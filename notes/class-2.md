
# Notes and Reference Materials - Unit 3 - Sprint 1 - Class 2

Outline:

  1) Docs, Style, PEP8 and Docstrings
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

## Part I

Style, Formatting, PEP8, and Docstrings:

  + https://pep8.org/
  + https://www.python.org/dev/peps/pep-0008/
  + https://www.python.org/dev/peps/pep-0257/
  + https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
  + https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Style-checking:

  + https://pypi.org/project/autopep8/
  + http://pep8online.com/checkresult
  + https://codeclimate.com/

```sh
# use pip or pipenv to install. if pipenv save as dev dependency:
pipenv install autopep8 --dev

# make a commit before running the following command, as the in-place flag will modify your files:
autopep8 --in-place --aggressive --recursive .
```

(FYI) Doc generation, Read The Docs, Sphinx:

  + https://readthedocs.org/
  + https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html
  + https://www.youtube.com/watch?v=b4iFyrLQQh4

(FYI) Doc generation example (Pandas):

  + https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
  + https://github.com/pandas-dev/pandas/blob/master/pandas/core/frame.py#L319

## Part II

Classes and OOP:

  + https://docs.python.org/3/tutorial/classes.html
  + https://realpython.com/python3-object-oriented-programming/
  + https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
  + https://realpython.com/instance-class-and-static-methods-demystified/#static-methods

(FYI) Example of Refactoring from Functions to Classes:
  + https://github.com/s2t2/playlist-service-py/blob/25cae16201adc935f71e863a79d51690c00e492b/app/spotify_service.py
  + https://github.com/s2t2/playlist-service-py/blob/master/app/spotify_service.py
  + https://github.com/s2t2/playlist-service-py/blob/master/app/sync_service.py


## Part III

Class Inheritance in Python:

  + https://www.w3schools.com/python/python_inheritance.asp

Inheritance Example (SKLearn):

  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L77
  + https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py#L589
