

# Class 1

Announcement:

```
Hey @channel, my name is Mike Rossetti and I'll be your instructor for Unit 3. :wave: To prepare for the first class, please review the official Lambda material and register for a test PyPI account:

  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering
  + https://learn.lambdaschool.com/ds/sprint/recA7O3QeO8AQxsxE
  + https://test.pypi.org/account/register/

Also ensure you are able to run each of the following commands without error:

  + conda --version
  + pipenv --version
  + git --version
  + code ~/Desktop (Mac / Windows Git Bash) or code C:\Users\USERNAME\Desktop (Windows other)

If you need help setting up your local development environment, I encourage you to consult this detailed "Onboarding Guide", which will walk you through the process and address common questions raised by students in previous cohorts:

  + https://github.com/s2t2/lambda-ds-3-1/blob/master/ONBOARDING.md

If you have any questions or run into any issues, post a message here and we can work through them together. Looking forward to working with you, and see you on Monday morning!
```

Lambda Materials:
  + https://learn.lambdaschool.com/ds/module/recwEPR24pu5LCnA5
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments

Topics:
  1. Git Repositories
  2. Pipenv Virtual Environments
  3. Python Imports, Modules, and Packages
  4. Releasing a Python Package to PyPI


## Part I - Git Repositories

README files (BONUS):
  + https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

Choosing a License (BONUS):
  + https://choosealicense.com/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/software/licensing.md

Managing Repositories:

```sh
cd ~/Desktop # navigates to the place where you'd like to download the repo
git clone REMOTE_ADDRESS # downloads repo from GitHub (where REMOTE_ADDRESS comes from GitHub - prefer SSH address if possible)
cd REPO_NAME # navigates into the repo's root directory (where REPO_NAME is the name of the folder / repo that got downloaded - same as on GitHub)
code . # use VS Code to open all files and folders in this directory
```

The Git commit process (will run any time we are ready to commit new changes):

```sh
git status # what files have changed?
git diff # how have the files changed?
git add . # prepare to commit all the files and folders in this directory
git status # (optional)
git commit -m "Setup repo and virtual env" # creates a new version / commit with the specified message
git log # (optional) shows the version history. press "q" to quit
git remote -v # shows the remote addresses associated with this local repo, for example the "origin" address
git push origin master # uploads the code to GitHub
```

## Part II - Virtual Environments

A virtual environment is a place where we install specific version of the python programming language and third-party Python packages. Different projects often require different dependencies, and project-specific virtual environments help us prevent conflicts between different versions.

> NOTE: we'll use either Anaconda or Pipenv for managing virtual environments. The instructions below show you both ways (for instructional purposes), but normally you'd just choose one!

### Anaconda Environments

Advantages:
  + Can be created, modified, activated from anywhere on the filesystem
  + Integrates with pip for python package management

Disadvantages:
  + Requires specification of development and production dependencies in different files ("requirements.txt" vs. "dev-requirements.txt", for example)
  + Requires specification of python version using a separate file called the "runtime.txt"

Managing a virtual environment with Anaconda:

```sh
# requirements.txt file
pandas
```

```sh
conda create -n my-lambdata-env python=3.7 # creates a new virtual env
conda activate my-lambdata-env # activates the virtual env
pip install -r requirements.txt # installs inside the virtual env all packages listed in the requirements.txt file
pip list # verifies packages are installed properly
```

### Pipenv Environments

Advantages:
  + Handles python package management
  + Can specify development and production dependencies, as well as the python version, in same file ("Pipfile")
  + Performs a "locking" process to provide more details about the package versions and ensure dependencies are not in conflict

Disadvantages:
  + Must be created, modified, activated from the given project directory !!!!!
  + Replaces pip for python package management
  + Locking process takes a while

> IMPORTANT: Make sure you run the following commands from the repo's root dir!
>
> IMPORTANT: Also make sure to deactivate all anaconda env(s) as necessary (`conda deactivate`) before proceeding...

Managing a virtual environment with Pipenv:

```sh
pipenv --python 3.7 # creates a new virtual env for the first time, also creates Pipfile
pipenv install pandas # installs a given package inside the virtual env, creates a Pipfile.lock if installing something for the first time, and auto-adds pandas to the Pipfile and Pipfile.lock
pipenv shell # activates the virtual env

python --version # verifies the right version of Python has been installed
pip list # verifies packages have been installed properly
```






## Part III - Python Imports, Modules, and Packages

Python Modules:
  + https://docs.python.org/3.7/tutorial/modules.html


```py
# my_lambdata/__init__.py

# nothing to see here!
```

```py
# my_lambdata/my_mod.py

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# this code breaks our ability to import enlarge from other files, if left in the global scope:
#
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))
```

```py
# my_lambdata/my_script.py

import pandas

from my_lambdata.my_mod import enlarge

print("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

print("-----------------")
x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x)) # invoking our function!!
```

Running the scripts:

```sh
python my_lambdata/my_script.py
python my_lambdata/my_mod.py

# note, the alternative "module" invocation syntax
# ... required if our script imports from another local file:
python -m my_lambdata.my_script
python -m my_lambdata.my_mod
```






## Part IV - Releasing a Package to PyPI

Publishing Packages to the PyPI:
  + https://pypi.org/
  + https://test.pypi.org (SIGN UP FOR AN ACCOUNT!)
  + https://pypi.org/help/#publishing
  + https://packaging.python.org/tutorials/packaging-projects/
  + http://data-creative.info/reference-docs/2019/05/30/how-to-publish-python-package-pypi/

Example Package Published to PyPI (BONUS):
  + https://github.com/s2t2/game-utils-py
  + https://pypi.org/project/s2t2-game-utils/
  + https://test.pypi.org/project/s2t2-game-utils/

Installing the "twine" package as a development dependency:

```sh
pipenv install twine --dev
```

> FYI: passing --dev specifies the package should be installed as a development dependency. We do this with packages that our source code doesn't require to perform its desired functionality (e.g. packages for testing and distributing the code)

Specifying metadata about our package in a new file called "setup.py":

```py
# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-package-name", # the name that you will install via pip
    version="1.0",
    author="Your Full Name",
    author_email="your@email.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
```

After configuring the "setup.py" file, invoking it will save a compressed version of the code in the "dist" directory.

```sh
python setup.py sdist bdist_wheel
```

After the package source code has been "built" locally, use twine to upload the distribution files to PyPI (or in this case the test PyPI server), where it can be downloaded by others via Pip commands:

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# OR, if you see 403 "file already exists" errors:
twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
```

> NOTE: the process whenever you want to release a new version of your package to PyPI is something like:
>  1. make change and save file
>  2. revise version value in the setup.py file (for example from 1.0 to 1.1, or from 1.1 to 1.2) and save the file
>  3. make a commit
>  4. run the bdist_wheel command to package your code
>  5. run the twine command to upload the packaged code

