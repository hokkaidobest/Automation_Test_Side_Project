python3 -m pytest -s -v --alluredir=./allure-results --clean-alluredir -n 2
allure serve ./allure-results
rm -r allure-results/