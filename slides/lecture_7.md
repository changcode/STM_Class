# Software Testing Methodology

## Gregory S. DeLozier Ph.D.
## Fall 2015

# Lecture 7

---
# Agenda

- More app progress
- Reviewing a white paper on tools
- An oracle-based project
- A testing challenge - tiny_db

---
# App Progress

- It is worthwhile to keep working through that app? 
- Should we jump ahead to 
    - UI
    - Deployment
    - Regression

---
# Tools Paper

- This is a common format
- This is expensive research
- "Magic Quadrant" research
- Keep in mind the scale of these ideas

---
# Testing Challenges

- Web Sites
    - Exposed applications
    - Accessible to technology
    - Requirements are known
    - Oracles are available
    - BBST methods

---
# Testing Challenges

- FOSS Packages
    - Easy to get
    - Well understood
    - Testable by usual methods
    - Glass Box testing, perhaps
    - Useful to community

---
# Oracle Project

- NY Public Library
- Online Card Catalog
- There are two versions
    - http://catalog.nypl.org
    - http://browse.nypl.org

---
# Acceptance Problem

- They search the same catalog
- You can search without an account
- Assuming the old one works
    - Does the new one work?
    - Did they get what they paid for?

---
# The Mission

- Define criteria for 'value'
- Define types of failures
- Devise a test plan
- Carry out the test plan
- Don't irritate the NYPL
- Constrain to non-member activities

---
# Getting Started

- How to start?
- What to test?
- How to test? 

---
# Homework A

- Assess the NYPL new catalog

- Initial Report
    - A test plan
    - A test methodology
    - A prototype of a test

- Conclusion Report
    - A test report
    - At least 10 specific requirements tested
    - Automated tests

---
# Homework B

- Assess a potential software choice
    - Python Package - tinydb
    - For use as a small store customer database
    - Potentially 1000 customers, 500 items/customer
    - TinyDB is easy to use, they say
    - vs SQLite

- Tinydb 
    - Small database package
    - ( small demo forthcoming ) 
    - https://github.com/msiemens/tinydb
    - https://tinydb.readthedocs.org
    -(Faster with 'ujson' -- see https://pypi.python.org/pypi/ujson) 
    -(Also: https://github.com/msiemens/tinydb/blob/master/docs/usage.rst)

- Same approach and mission as "A"




