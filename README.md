# stepik-575-u4-po
Stepik course 575, unit 4, PageObject pattern tasks

## Task description
https://stepik.org/lesson/199980/step/6


## Preconditions
- Git
- Python 3
- chromedriver installed in PATH

## Prepare project on Linux/MacOS

```sh
$ git clone https://github.com/ilyasamorodov/stepik-575-u4-po.git
$ cd stepik-575-u4-po
$ python -m venv venv
$ pip install --upgrade pip
$ source ./venv/bin/activate
$ pip install -r ./requirements.txt
```

## Prepare project on Windows (Powershell)

```sh
PS: git clone https://github.com/ilyasamorodov/stepik-575-u4-po.git
PS: cd stepik-575-u4-po
PS: python -m venv venv
PS: pip install --upgrade pip
PS: venv/Scripts/activate
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