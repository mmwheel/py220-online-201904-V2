Grading
=======

For assignment 1, you will need to supply your own unit_tests.py 
and integration_test.py files.

The assignment is graded as follows:
1. Run the student unit_tests
2. Run coverage and linting using the regular batch file


Notes on assignment:

I had wanted to do this using pytest but ran into trouble
trying to monkeypatch inputs and found it to be easier
using unittest mock and side effects.  For the sake of
grading, the tests in ./unittests/ are completed and
functional.  The tests in ./pytests/ are a work in
progress.
