# Arclight-1

This is a testbed to show a Twitter friend a sane way to set up unit tests in Python when the code and tests live in different directory trees.

## What are the contents?

In `src` there's a single file that implements a solver for quadratic equations, using the time-honored general quadratic equation we all learned in school.

In `tests` there are a series of `pytest` scripts that each check for a different facet of correctness:

* When given valid parameters, does it reach valid results?
* Does it trap imaginary roots and report them correctly?
* Does it sanity-check its parameters to ensure they're of the correct numeric type?
* Does it make sure that it's being given an actual quadratic equation?

## How do I run these tests?

`test.unix` is a shellscript that should work on most any Unix, including MacOS.

## How is it licensed?

ISC.  Share and enjoy.
