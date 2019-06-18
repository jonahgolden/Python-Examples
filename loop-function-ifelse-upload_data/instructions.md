## Assignment 4
### Solving problems in Python 2
**due at 12 noon on 2015-10-30** via Github

## Instructions

1. To start, [**fork**](https://guides.github.com/activities/forking/) the [repository](https://github.com/PHY3009/assignment_4).

2. [**Clone**](http://gitref.org/creating/#clone) the repository to your computer.

3. Create an iPython notebook called `problems_in_Python_2.ipynb` in which you answer the 
following questions:

a. Write a loop that takes a string, and produces a new string with the characters in 
reverse order, so 'Newton' becomes 'notweN'. Don't forget to comment your code.

b. Write a function that takes in a list or array of numbers and calculates and returns 
the standard error. Don't forget to comment your code & include a docstring.

c. What will happen if someone tries to run your standard error function using a list or 
array of strings? Make a new version of the function which use if/else statements which
will calculate the standard error if the list contains numbers, but will print "Input was
a string, I cannot calculate the standard error of a string" if the input is a string.

d. Use your function to calculate the standard error for each patient in 
[inflammation-01.csv](https://raw.githubusercontent.com/swcarpentry/python-novice-inflammation/gh-pages/data/inflammation-01.csv)

4. [**Add**](http://gitref.org/basic/#add) and [**commit**](http://gitref.org/basic/#commit) 
changes to Git.

6. [**Push**](http://gitref.org/remotes/#push) the changes up to your copy of the 
repository on GitHub.

7. [Create a **pull request**](https://help.github.com/articles/creating-a-pull-request/) 
on the original repository to turn in the assignment.


## Grading rubric

<table>
  <tr>
    <th></td>
    <th>Poor/Unacceptable 0% – 59%</td> 
    <th>Limited 60% – 69%</td> 
    <th>Fair/Adequate 70% – 79%</td> 
    <th>Good 80% – 89%</td> 
    <th>Exceptional 90% – 100%</td> 
  </tr>
  <tr>
    <th>Planning & Documentation (40%)</td>
    <td>No comments or docstrings are used.</td> 
    <td>Comments are used but they do not make clear the purpose of the code.</td> 
    <td>Comments & docstrings are used to somewhat explain what the code is doing.</td> 
    <td>Comments & docstrings are used well to clearly explain what the code is doing.</td> 
    <td>Comments & docstrings are used exceptionally well to clearly explain what code is doing.</td> 
  </tr>
  <tr>
    <th>Accuracy (20%)</td>
    <td>0 answers are correct.</td>
    <td>1/4 answers are correct.</td> 
    <td>2/4 answers are correct.</td> 
    <td>3/4 answers are correct.</td> 
    <td>All 4 answers are correct.</td> 
  </tr>
  <tr>
    <th>Reusability (20%)</td>
    <td>No variables are used.</td> 
    <td>Some variables are used in some questions.</td> 
    <td>Some variables are used in all questions.</td> 
    <td>For all questions, all inputs are assigned to variables and variables are used in solving the problems. </td> 
    <td>For all questions, all inputs are assigned to variables, variables are used in solving the problems and outputs are saved to variables.</td> 
  </tr>
  <tr>
    <th>Readability (20%)</td>
    <td>No variables are used.</td> 
    <td>Variable names are not meaningful.</td> 
    <td>Meaningful variable names are used.</td> 
    <td>Meaningful variable names are used. Complicated problems are broken down into multiple steps.</td> 
    <td>Whitespace is well used. Meaningful variable names are used. Complicated problems are broken down into multiple steps.</td> 
  </tr>
</table>