# Software Testing Methodology

## Gregory S. DeLozier Ph.D.
## Fall 2015

# Lecture 5
---
# Agenda

- Show some virtual machine stuff
- Continue with Chapter 5
 
    - User interface
    - Forms submission

---
# Review
 
To start:

   ```
   $ python3 manage.py runserver
   ```

To run functional tests:

   ```
   $ python3 functional_tests.py
   ```

To run unit tests:

   ```
   $ python3 manage.py test
   ```

---
# Failing?

The book says:
- Add print statements, to show, eg, what the current page text is.
- Improve the error message to show more info about the current state.
- Manually visit the site yourself.
- Use time.sleep to pause the test during execution.

---
# Structure of Tests

- Setup
- Exercise
- Assert

---
#Code Cycle

- Red - write a test that fails
- Green - make it work even if cheating
- Refactor
    - Eliminate duplication
    - Third duplicate rule

- Triangulation
    - Write a better test
    - Why does the problem bother you?


