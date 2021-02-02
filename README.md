# behave-wikipedia
Uses [Behave](https://behave.readthedocs.io/en/stable/) and [Selenium](https://selenium-python.readthedocs.io/) to run browser tests of Wikipedia implemented following the [Page Object Model](https://www.selenium.dev/documentation/en/guidelines_and_recommendations/page_object_models/) approach

## Installation
Requires [Python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/)
Install dependencies using
```pipenv install```

## Running
```pipenv run behave```

![A test run](https://github.com/memsb/behave-wikipedia/blob/main/docs/test_run.png?raw=true)

For failures screenshots are taken and stored in ```/screenshots```

## Automation

A github action has been set to run the tests on every commit.
Screenshots can be downloaded as artifacts from the job

![A test run](https://github.com/memsb/behave-wikipedia/blob/main/docs/artifacts.png?raw=true)
