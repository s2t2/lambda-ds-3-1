

# Notes and Reference Materials - Class 1

Lambda Materials:
  + https://learn.lambdaschool.com/ds/module/recwEPR24pu5LCnA5
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments

## Part I

(FYI) Slides:
  + https://docs.google.com/presentation/d/1Bb8ZVJ0NPJpVrd9PSltdrId9hXVt8Ty7iX5mr9ovIgs/edit?usp=sharing

(FYI) Command-line Utility Reference Docs:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/brew.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/conda.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pipenv.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/pip.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/python.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/git.md

(FYI) Connecting to GitHub via SSH:
  + https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

(FYI) Markdown Cheat-sheet:
  + https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

(FYI) Choosing a License:
  + https://choosealicense.com/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/software/licensing.md

### Git and GitHub

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

### Virtual Environments

> NOTE: we'll use either Anaconda or Pipenv for managing virtual environments.
> The instructions below show you both ways (for instructional purposes), but normally you'd just choose one!

#### Anaconda Environments

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

#### Pipenv Environments

> Make sure you run these commands from the repo's root dir!
> Also make sure to deactivate all anaconda env(s) as necessary (`conda deactivate`) before proceeding

Managing a virtual environment with Pipenv:

```sh
pipenv install --python 3.7 # creates a new virtual env for the first time, also creates Pipfile and Pipfile.lock
pipenv install pandas # installs a given package inside the virtual env, and auto-adds to the Pipfiles
pipenv shell # activates the virtual env
pip list # verifies packages are installed properly
```








## Part II

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

Run the scripts:

```sh
python my_labmdata/my_script.py
python my_labmdata/my_mod.py

python -m my_labmdata/my_script
python -m my_labmdata/my_mod
```






## Part III

Publishing Packages to the PyPI:
  + https://pypi.org/
  + https://test.pypi.org (SIGN UP FOR AN ACCOUNT!)
  + https://pypi.org/help/#publishing
  + https://packaging.python.org/tutorials/packaging-projects/
  + http://data-creative.info/reference-docs/2019/05/30/how-to-publish-python-package-pypi/

(FYI) Example Package Published to PyPI:
  + https://github.com/s2t2/game-utils-py
  + https://pypi.org/project/s2t2-game-utils/
  + https://test.pypi.org/project/s2t2-game-utils/


```sh
pipenv install twine --dev
```

```py
# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="s2t2-lambdata-12",
    version="1.0",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/s2t2/lambdata-12y",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
```

```sh
python setup.py sdist bdist_wheel # saves a compressed version of the code in the "dist" dir
```

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/* # uploads the package to the test PyPI server, where it can be downloaded by others via pip commands
```
