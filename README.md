## SDSS Computing Studies Python Assignment
### Basic Code in Python with Turtle Graphics

Objectives:
* To observe syntax and formatting of code in a python file
* To make use of the VSC Debugger to find errors and execute python programs

### Introduction
Last day, we were making drawings using turtle graphics in the python interpreter.  However, each command was executed one at a time as we typed them in.  Furthermore, once the interpreter closes all commands are lost.

To save the commands, we copied and pasted them from the terminal into a file.  Today we will see what parts we need to keep to make an executable python program.

1. *Filename* All python files must have a .py file extensions.  This helps the operating system determine how to deal with the program.  Note that filenames, in fact everything, in python is case sensitive.  Note that there are certain names we can't use.  We can't name the file "turtle.py" because we use the "import turtle" command.  Avoid using key words as file names

    TAKE THIS OPPORTUNITY TO RENAME THE FILE "sample" to "sample.py"


2.  *Program Structure* In Python, indenting is very important.  All commands should be left justified.  There are some exceptions, which we will see in later units and have to do with organizing programs into blocks of code that go together.

3. *Program Syntax* Create a file called "assignment.py" in this project.  Copy and paste your instructions that you saved from last day into this file.  You will notice that there is little symbol that looks like a "play" button (triangle pointed to the right) in the top right corner of your screen. This will only show up when you have an exectutable program.  If you press it, you will get a lot of errors.  When you try to run a program with errors, the debugger will find them and try to describe the errors as they pop up.

4.  Remove all the text in your file that is NOT the specific commands that you typed in.  This also means removing the >>> prompts as these are not actual parts of the commands.  If you have removed all of the errors, you will have successfully debugged your program and can execute the commands repeatedly!



### Assignment
An alternate way of moving your turtle around the screen is to use absolute coordinates.  The turtle screen uses a standard cartesian coordinate system with (0,0) in the middle of your screen.
Open up sample.py to see how we can move the turtle to different sections of the screen.  Don't worry about the extra code, but focus instead on the **goto** statements.

Create a turtle drawing.  
You need to include the following:
* goto statements to place objects at different parts of your screen
* fill to create backgrounds and colored foreground objects
* multiple objects (example: trees on ground with blue sky and sun and clouds!)
B class:
create functions to generate your objects


### Assignment part B
Open up the maze.py file. 
Have your turtle navigate the maze.