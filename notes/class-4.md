

# Class 4

Lambda Materials:
  + https://learn.lambdaschool.com/ds/module/recq9eVVCzZpgeH58/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module4-software-testing-documentation-and-licensing

Previous Lecture and Materials on Testing (BONUS / FYI) :
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/software/testing.md
  + https://www.youtube.com/watch?v=pS8pzmtqxVA
  + https://github.com/prof-rossetti/lambda-lecture-pytest

See also the [reference test code](/test/).

Testing Philosophies at Google vs. Facebook (BONUS):
  + https://www.youtube.com/watch?v=GjE7clki4a0
 
## Part I

Testing Frameworks (Unittest):
  + https://docs.python.org/3.5/library/unittest.html

Running tests:

```sh
python -m unittest test.team_test
```

> NOTE: may need to add "`__init__.py`" files to both the "app" and "test" directories for this to work from the root directory

## Part II (FYI / BONUS)

> FYI this is related bonus material, not required for your assignment or SC

Testing Frameworks (Pytest):
  + https://docs.pytest.org/en/latest/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pytest.md
  + https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/testing-123

Installing pytest as a development dependency:

```sh
pipenv install pytest --dev
```
Running tests:

```sh
pytest
```

## Part III (BONUS / FYI)

> FYI this is related bonus material, not required for your assignment or SC

Test-Driven Development (TDD):

```py
# from app.game import determine_winner

# FYI normally we'd have this application code (determine_winner()) in another file,
# ... but for this exercise we'll keep it here
def determine_winner(user_choice, computer_choice):
    return "rock" # todo: write logic here to make the tests pass!

def test_determine_winner():
    assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None
```

Continuous Integration (CI):
  + https://travis-ci.com/
  + https://travis-ci.com/s2t2/playlist-service-py/builds/142617662
  + https://github.com/s2t2/playlist-service-py/pull/7
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/devtools/travis-ci.md
  + https://github.com/prof-rossetti/intro-to-python/tree/master/exercises/ci-123
