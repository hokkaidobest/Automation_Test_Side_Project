python3 -m pytest -s -v --alluredir=./allure-results --clean-alluredir
allure serve ./allure-results
rm -r allure-results/