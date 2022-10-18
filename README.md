The tests are written with the unittest module and can be run as follows: `python -m unittest tests/file_to_test.py`

To run all unit tests: `python -m unittest discover -s 'tests/' -p '*_tests.py'`

Test coverage is done using the coverage library. To use it simply replace the `python` part of the test command with `coverage run`. For example: `coverage run --source=app/src -m unittest discover -s 'tests/' -p '*_tests.py'`. You can then use the `coverage report` command to view a coverage report or `coverage html` to generate a more detailed report that can be viewed in a browser. 