# Homework 2 - Basics of Python

This program accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. This project uses single python file which is named hw2.py

### Basic usage

This homework requires Python 3.x to run. You also need to provide integer inputs in order to run program properly.

```sh
$ unzip HW2
$ cd HW2
$ python hw2.py
```

### The expected output

A proper input is provided:
```
Please enter 4 digit binary numbers: 0100,0011,1010,1001
The numbers that are divisible by 5 are: 1010
```

A proper input is provided with no divisible by 5:
```
Please enter 4 digit binary numbers: 0100,0011
None of the numbers are divisible by 5.
```

A non-integer input is entered:
```
Please enter 4 digit binary numbers: asdasd,0101
All of your input is not an integer!
```

A non 4 binary input is entered:
```
Please enter 4 digit binary numbers: 01010,0101,1010
All of your input is not 4 digit!
```