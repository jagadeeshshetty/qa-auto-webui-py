#!/bin/bash
pipenv run pytest
pipenv run allure serve allure-results
