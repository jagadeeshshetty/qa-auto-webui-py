#!/bin/bash
pipenv run pytest -v -m allure_options --clean-alluredir --disable-warnings
pipenv run allure serve allure-results
