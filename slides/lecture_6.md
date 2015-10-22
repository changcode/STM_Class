# Software Testing Methodology

## Gregory S. DeLozier Ph.D.
## Fall 2015

# Lecture 6

---
# Agenda

- BBST Concepts
- More app progress

---
# BBST

- "Black Box Software Testing"

- Cem Kaner
- Rebecca Fiedler

- Comprehensive discussion of testing

---
# Software Testing

- Is an empirical
- technical
- investigation
- conducted to provide stakeholders
- with information
- about the quality
- of the product or service under test

(Cem Kaner)

---
# Quality

- Value or Usefulness
- To _Someone_

- This is very subjective

---
# Information

- Evidence
- Cause to believe
- Probabilistic

--- 
# Definitions

- Are not absolute
- _Are meaningful_
- You need to know what is meant _here_. 

---
# Black Box

- Can't see the internals
- Tested against external expectations
- Tested by people who know the domain
- Verify that the _system_ is correct
- (aka, "behavioral")

---
# Glass Box

- (Not really "white box"
- Tested against internal expectations
- Does what the programmer expects
- Easier to do
- Less valuable to the consumer
- (aka, "structural)

---
# Testing Levels

- Unit 
- Integration
- System 
- _Orthogonal_ to BB/GB testing
- For instance, we can unit test sorted([])

--- 
# Unit

- Testing of parts
- Can happen at many levels
- Does the part work?

---
# Integration

- Testing of many parts
- Can happen at many levels
- Can happen at levels of complexity
    - 1-1
    - Star
    - All parts

- Do the parts work together? 

---
# System

- Testing of the system
- In its environment
- Does the system meet the needs? 

---
# Functional

- Given input, proper output? 

---
# Non-functional

- Is the system behaving well while producing output?
    - usable
    - stable
    - performant
    - secure
    - etx

---
# Acceptance testing

- Is someone going to pay for it?
- Is there a contract?
- Implied contracts
    - Development vs Marketing
    - R&D vs Product
    - Etc

---
# Why Test?

- To gather evidence
- There are objectives
- Hard to know how well
- Hard to know how much

- Every test is a question

---
# Oracles
- About oracles
    - Accepted definitions of correctness
    - Mathematics
    - Experts
    - Laws

- Oracles are _incomplete_
- Oracles are _hueristic_
- More on this later
  
---
# Evidence?

- Evidence about quality
- Need definition of quality
     - Speed?
     - Correctness?
     - Reliability?
     - Robustness?
     - Completeness?
     - Connectivity?
     - Compliance?

- What is desirable?
- How do we measure that?
 
---
# Contexts?

- Prototyping
- Mass-marked Development
- Critical Environments
- Lawsuits

---
# Testing Mission

- What are we trying to do?
- Success criteria
- Time to complete?
- Resources available?

---
# Testing Strategy

- Given limitations
    - Time
    - Resources

- What will you do?
- How to maximize benefit?

---
# Ex: Scenario Testing

- Complex story
- Make sure the story works

- Viewed as important

--- 
# Ex: Domain Testing

- Consider all possibilities
- Group into partitions
- Select from partitions
- Select from boundaries

- Unusual tests are viewed as unlikely


---
# Techniques

(James Bach's list)

Specify some or all:

- Analyze the situation
- Model the test space
- Select what to cover
- Determine test oracles
- Configure the test system
- Operate the test system
- Observe the test system
- Evaluate the results

---
# TDD as a Technique

- Analyze the situation
    - _Feature is desired_
- Model the test space
    - _Feature gets operated_
- Select what to cover
    - _Feature examples_
- Determine test oracles
    - _Code assertions_

---
# TDD as a Technique

- Configure the test system
    - _Unit tests_
- Operate the test system
    - _Run the tests_
- Observe the test system
    - _Assertion failures_
- Evaluate the results
    - _Code to fix the failures_

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

