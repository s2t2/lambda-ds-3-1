
# Unit 3 Onboarding

This document contains an introduction to the local development environment and provides instructions for how to install and configure all the necessary local development tools.

## Notebooks vs Local Development

Co-lab Notebook Advantages:
  + Minimal learning curve
  + High degree of visibility and shareability
  + Effective presentation when code mixed with markdown and data visualizations
  + GPU / TPU processing power

Co-lab Notebook Disadvantages:
  + Can only write and execute Python code, not other languages
  + Minimal processing power and parallel processing capabilities (excluding GPU / TPU)
  + Relatively low ability to manage files and credentials
  + Relatively low degree of customization
  + Unable to run certain kinds of apps, like web apps written in the Flask framework

Local Development Advantages:
  + Can write and execute code written in many different languages and frameworks
  + Greater ability to manage files and credentials
  + Greater degree of customization / control
  + Greater privacy (not managed by Google)
  + More processing power and parallel processing capabilities (excluding GPU / TPU)

Local Development Disadvantages:
  + Steeper learning curve, likely many tools to learn
  + Not as immediately shareable, unless pushing code to GitHub or a remote server

## Local Development Tools

Category | Recommended Tool(s) | Purpose
--- | --- | ---
Text Editor or IDE | VS Code | For creating, reading, editing, and deleting files of text and code.
Command-line Application | Mac Terminal, Windows Git Bash, the built-in terminal in VS Code, or whatever you can get to work! | For interfacing with the computer in programmatic ways (i.e. installing and running software).
Programming Language | Python (`python`) | For executing software written in a given programming language.
Programming Language Virtual Environment Manager | Anaconda (`conda`) or Pipenv (`pipenv`) | For installing different versions of a programming language, to suit project-specific purposes, because sometimes you might need to use a different version.
Programming Language Package Manager | Pip (`pip`) in general and in Anaconda environments, but replaced by `pipenv` for Pipenv environments. | For installing third-party packages written in a given programming language.
Version Control Utility | Git (`git`) | For incrementally saving different versions of software files, and interfacing with GitHub, which is an online place to share code repositories.
Server Management Utility | Heroku (`heroku`) | For provisioning and managing remote servers on which to run software.

### Text Editor

To edit Python files locally, we'll need a development-class text editor. Students who don't already have a preferred editor or IDE are encouraged to [download and install VS Code](https://code.visualstudio.com/). After doing so, it is important to install the [Python language extension](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md#python-syntax-auto-completion) which provides code syntax-highlighting and auto-completion capabilities.

> OPTIONAL: you may also want to further [customize your text editor's appearance and functionality](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/vs-code.md#basic-configuration), as desired.

### Command-Line Application

To run Python files locally, we'll need a command-line application.

Mac users who don't already have a preferred command-line application are encouraged to use the built-in Terminal application (no need to download anything).

> OPTIONAL (for Mac users): you may want to [customize your Terminal appearance and functionality](https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/command-line-computing/mac-terminal-config.md), as desired.
> NOTE: newer Macs may use the "zsh" shell instead of the "bash" shell, in which case you can do the "\~/.bash_profile" customizations using a file like "\~/.zshrc" instead.

Windows users who don't already have a preferred command-line application are encouraged to [download and install Git Bash](https://git-scm.com/downloads), which will integrate well with the other development tools and allow Windows users to write the same commands as Mac users. Ultimately, Windows users may opt to use an alternative tool such as the Command Prompt or Anaconda Prompt, but if you do you are responsible for translating unix-style commands you'll see everywhere to windows-style commands. The command-line computing exercise referenced at the bottom of this document can help!

Mac or Windows students who'd rather configure and use the built-in terminal inside the VS Code text editor may do so, just make sure it works for you!

### Programming Language

To get started with Python locally, if you haven't already done so as instructed during Unit 2, you'll want to [download and install Anaconda 3.7](https://www.anaconda.com/distribution/), which will provide the ability to install and manage local installations of Python and third-party Python packages.

> IMPORTANT NOTE: remember to check the "add to PATH" option during installation, especially on Windows, so Anaconda will integrate with the other local development tools, such as Git Bash on Windows.

> FYI: this installation process can take a half-hour or more, so prefer to do it over a strong Internet connection.

After installing Anaconda, you'll have access to the Python language and its side-kick, the Pip package manager. For more information on Python, see this bonus [`python` reference document](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/python.md). For more information on Pip, see this bonus [`pip` reference document](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/pip.md).

### Virtual Environment Manager

For reasons we'll discuss, it is a best practice to work on project-specific environments which have project-specific versions of the Python programming language and third-party Python packages. There are two main tools to help us do this.

The first alternative, which you may be using almost exclusively in other units, is the aforementioned Anaconda, which provides the `conda` utility. It is good to be familiar with using `conda` virtual environments. For more information on Anaconda, see this bonus [`conda` reference document](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/conda.md).

> NOTE: when using `conda` to activate a virtual environment for the first time, when prompted to do so, Git Bash users on Windows may need to run `conda init bash` and Zsh users on Mac may need to run `conda init zsh`.
> NOTE: if experiencing issues recognizing `conda` commands on Mac OS Catalina, reference these [Catalina setup steps](https://github.com/prof-rossetti/intro-to-python/issues/13).

The second alternative, which we'll be using almost exclusively in this unit, is [Pipenv](https://pipenv.readthedocs.io/en/latest/). For more information on Pipenv, see this bonus [`pipenv` reference document](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pipenv.md). Installation guidance:

  + Mac users are encouraged to download Pipenv via [homebrew](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/brew.md) (`brew install pipenv`). NOTE: Homebrew is a popular and amazing programmatic installation tool that no Mac developer should go without!
  + Windows users can consult [this link](https://pipenv.readthedocs.io/en/latest/install/#pragmatic-installation-of-pipenv) for download instructions via Pip.


### Version Control Utility

Finally, we need a version control utility to manage different versions of our software files, and interface with GitHub, where we can share our code and collaborate with others.

Unless you already have one, please take a moment to [create a GitHub account](https://github.com/) and consider optionally signing up for the [GitHub Student Developer Pack](https://education.github.com/pack), which provides some free resources. You are encouraged to also optionally [generate SSH keys and associate them with your GitHub account](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh), which will allow you to connect to GitHub over the SSH protocol so you don't have to repeatedly type your username and/or password like you would with the HTTPS protocol.

We'll ideally want to get comfortable using Git from the command line. For more information on Git, see this bonus [`git` reference document](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/clis/git.md). Installation guidance:

  + Windows users can leverage the aforementioned Git Bash application for this purpose (nothing else to install).
  + Mac users can download Git via homebrew (`brew install git`), or in many cases Git may already be installed on your computer.

Although you should really invest the time to become a Git command-line pro, students on either Mac or Windows who are less comfortable with the command-line may optionally start by using the [GitHub Desktop](https://desktop.github.com/) application as a temporary bridge solution which provides a graphical user interface (GUI) for performing Git version control operations. If doing so, students should [customize GitHub Desktop](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/github-desktop.md#configuration) to recognize their preferred dev tools (e.g. VS Code as the preferred text editor, and Terminal or Git Bash as the preferred command-line utility.)

## Success Criteria

After installing and configuring these local development tools, you should be able run each of the following commands without error:

  + `conda --version`
  + `pipenv --version`
  + `git --version`
  + `code ~/Desktop` (Mac Terminal, Windows Git Bash) OR `code C:\Users\USERNAME\Desktop` (Windows other)

## Preparation Exercise

Finally, in order to become more comfortable with these tools and command-line computing in general, consider completing this optional [Command-line Computing Exercise](https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/command-line-computing).

Good luck, drop questions in Slack if you need help, and see you in class!
