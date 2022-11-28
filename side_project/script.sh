python3 -m pytest -s -v tests_web/test_web_product_page.py --alluredir=./allure-results --clean-alluredir
allure serve ./allure-results
rm -r allure-results/