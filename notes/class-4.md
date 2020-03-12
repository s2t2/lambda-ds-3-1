

# Notes and Reference Materials - Class 4


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


install pytest as a development dependency:

```sh
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
