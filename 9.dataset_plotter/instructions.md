## Assignment 9
### Writing scripts in Python
**due at 12 noon on 2015-11-11** via Github

## Instructions

1. To start, [**fork**](https://guides.github.com/activities/forking/) this [repository](https://github.com/PHY3009/assignment_9).

2. [**Clone**](http://gitref.org/creating/#clone) the repository to your computer.

3. Write a Python script which will load a dataset and plot and save a figure. This script
should be:
	* callable from the command line/Shell
	* take 2 arguments, `input_file` and `output_file`, where `input_file` is the dataset
	and `output_file` is the name of the file to write the figure to.

4. Create a README.md which **clearly** and **explicitly** explains what the script does 
and how to use it. The script's functionality very likely depends on the format of the 
input file, make sure this is specified.

5. Create a LICENSE.md file and choose a software license for this script.

*note: [**Add**](http://gitref.org/basic/#add) and [**commit**](http://gitref.org/basic/#commit) 
all changes to Git while you develop the script. Remember, each commit should be for a 
specific feature.*

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
    <td>No comments nor a README.md is used.</td> 
    <td>Comments in script and README.md are used but they do not make clear the purpose of the code.</td> 
    <td>Comments in script and README.md are used to somewhat explain what the code is doing.</td> 
    <td>Comments in script and README.md are used well to clearly explain what the code is doing.</td> 
    <td>Comments in script and README.md are used exceptionally well to clearly explain what code is doing.</td> 
  </tr>
  <tr>
    <th>Accuracy (20%)</td>
    <td>Code exists, but it cannot accomplish the task of loading a dataset and plotting and saving it to a file.</td> 
    <td>Code is written in an iPython notebook to plot and save a figure from a dataset. No script exists that can be called from the command line.</td> 
    <td>Script runs from the command line to plot and save a figure from a dataset. No arguments are given to the script.</td> 
    <td>Script runs from the command line to plot and save a figure from a dataset. Dataset or name of file to save the figure to are given as arguments from the command line.</td> 
    <td>Script runs from the command line to plot and save a figure from a dataset. Dataset and name of file to save the figure to are given as arguments from the command line.</td> 
  </tr>
  <tr>
    <th>Reusability (20%)</td>
    <td>No variables are used.</td> 
    <td>Some variables are used in some questions.</td> 
    <td>Some variables are used in all questions.</td> 
    <td>For all questions, all inputs are assigned to variables and variables are used in solving the problems. </td> 
    <td>Functions are used. All inputs are assigned to variables, variables are used in solving the problems and outputs are saved to variables.</td> 
  </tr>
  <tr>
    <th>Readability (20%)</td>
    <td>No variables are used.</td> 
    <td>Function and variable names are not meaningful.</td> 
    <td>Meaningful function and variable names are used.</td> 
    <td>Meaningful function and variable names are used. Complicated problems are broken down into multiple steps.</td> 
    <td>Whitespace is well used. Meaningful function and variable names are used. Complicated problems are broken down into multiple steps.</td> 
  </tr>
</table>
