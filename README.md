# stepik-575-u4-po
Stepik course 575, unit 4, PageObject pattern tasks

## Task descriptions
https://stepik.org/lesson/199980/step/6

https://stepik.org/lesson/201964 step 1 to 14

## Preconditions
- Git
- Python 3
- chromedriver installed in PATH
- geckodriver installed in PATH (optional)

## Prepare project on Linux/MacOS

```sh
$ git clone https://github.com/ilyasamorodov/stepik-575-u4-po.git
$ cd stepik-575-u4-po
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install --upgrade pip
$ pip install -r ./requirements.txt
```

## Prepare project on Windows (Powershell)

```sh
PS: git clone https://github.com/ilyasamorodov/stepik-575-u4-po.git
PS: cd stepik-575-u4-po
PS: python -m venv venv
PS: venv/Scripts/activate
PS: pip install --upgrade pip
PS: pip install -r requirements.txt
```

## Run tests examples

```sh
# run only tests with need_review mark
$ pytest -v --tb=line --language=en -m need_review

# run all tests in test_main_page.py
$ pytest -v --tb=line --language=en test_main_page.py

# run all tests in test_product_page.py
$ pytest -v --tb=line --language=en test_product_page.py

# run all tests
$ pytest -v --tb=line --language=en
```

### Test run results example

![run_all_tests_result_screenshot](https://user-images.githubusercontent.com/7586160/73799243-72013580-47c6-11ea-828c-e12911da8f8c.png)
