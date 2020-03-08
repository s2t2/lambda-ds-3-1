# Lambda DS Unit 3 - Sprint 1

## Intro

Hey everyone, my name is Mike Rossetti and I'll be your instructor for Unit 3. Our primary goals for this unit are to 1) transition from notebooks to local development, as well as to 2) ensure our data science efforts are verifiable and reproducible.

In the first sprint, we'll focus on getting more comfortable with local development. In the second sprint, we'll focus on databases and SQL. And in the third sprint, we'll build upon the first two sprints by creating database-backed web applications which we'll deploy to a remote server so we can share our data science efforts with the world! Excited? Here we go!

### Dev Tools

I know many of you are already familiar with local development to varying degrees, but some of you may be completely unfamiliar. So follow the instructions below as they pertain to your individual situation.

#### Programming Language

To get started, we'll want to [download and install Anaconda 3.7](https://www.anaconda.com/distribution/), which will provide us with the ability to install and manage local installations of Python and third-party Python packages.

> IMPORTANT NOTE: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools.

#### Command-Line Utility

To run our Python scripts, we'll need a command-line utility.

Mac users who don't already have a preferred command-line utility will use the built-in Terminal application (no need to download anything, although you may want to optionally [customize your Terminal appearance and functionality](https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/command-line-computing/mac-terminal-config.md)).

Windows users who don't already have a preferred command-line utility are encouraged to [download and install Git Bash](https://git-scm.com/downloads), which will integrate well with the other development tools and allow Windows users to write the same commands as Mac users.

#### Text Editor

To edit our Python scripts, we'll need a development-class text editor. Students who don't already have a preferred editor or IDE are encouraged to [download and install VS Code](https://code.visualstudio.com/). After doing so, it is important to install the [Python language extension](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md#python-syntax-auto-completion) which provides code auto-completion capabilities, and you may want to optionally further [customize your text editor's appearance and functionality](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md#basic-configuration).

#### Virtual Environment Utility

For reasons we'll discuss, it is a best practice to work on project-specific environments which have project-specific versions of the Python programming language and third-party Python packages.

There are two main tools to help us do this. The first is the aforementioned Anaconda, which provides the `conda` utility. NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Git Bash users on Windows may need to run `conda init bash` and Zsh users on Mac may need to run `conda init zsh`. NOTE: if experiencing issues recognizing `conda` commands on Mac OS Catalina, reference these [Catalina setup steps](https://github.com/prof-rossetti/intro-to-python/issues/13).

The second, which we'll be using more often in this unit, is [Pipenv](https://pipenv.readthedocs.io/en/latest/). Mac users can download Pipenv via homebrew (`brew install pipenv`). Windows users can consult [this link](https://pipenv.readthedocs.io/en/latest/install/#pragmatic-installation-of-pipenv) for download instructions via pip.

#### Version Control Utility

Finally, we need a version control utility to manage different versions of our Python scripts, and interface with GitHub, where we can share our code and collaborate with others.

Unless you already have one, please take a moment to [create a GitHub account](https://github.com/) and consider signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources.

We'll eventually want to get comfortable with using Git from the command line, so Windows use the aforementioned Git Bash application for this purpose. Mac users can download Git via homebrew (`brew install git`), or in many cases Git may already be installed on your computer.

Students on Mac or Windows who are less comfortable with the command-line can use the [GitHub Desktop](https://desktop.github.com/) application as a temporary bridge tool which provides a graphical user interface (GUI) for performing Git version control operations. If doing so, students should [customize GitHub Desktop](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/github-desktop.md#configuration) to recognize their preferred dev tools (e.g. VS Code as the preferred text editor, and Terminal or Git Bash as the preferred command-line utility.)

## Additional Reference

For more information about any of the aforementioned command-line utilities, students may optionally reference the following notes:

  + [Homebrew (Mac)](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/brew.md)
  + [The `conda` Utility](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/conda.md)
  + [The `pipenv` Package](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pipenv.md)
  + [The `pip` Utility](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/pip.md)
  + [The `python` Utility](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/python.md)
  + [The `git` Utility](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/git.md)

## Preparation Exercise

Finally, after installing and configuring these local development tools, in order to become more comfortable with command-line computing, you're recommended to complete this optional [Command-line Computing exercise](https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/command-line-computing).

Good luck, drop questions in Slack if you need help, and see you in lecture!
