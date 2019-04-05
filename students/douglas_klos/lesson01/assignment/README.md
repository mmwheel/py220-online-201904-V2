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
using unittest mock and side effects.  Both test suites
are running the same tests, however unittest also tests 
main.py, where as pytest does not. 
