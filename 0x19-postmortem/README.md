**Issue summary**

for the project HBNB, after implement the framework flask, it was impossible to execute the program

**Timeline**

 - 16/9 17:30 all is ok
 - 17/9 9:01 impossible to execute the program
 - 17/9 9:02 find a circular import, correction of it
 - 17/9 9:04 impossible to execute the program, the interpretor indicates an assertion error
 - 17/9 10:00 find the solution


**Root cause**

2 methods in 2 different files had the same name. the methods do the same hing but in two different classes.

**Corrective measures**

choose the name of methods with a link with the name of the file and the goal of the method, with a lot of precision even if the name is long. it is permetting to avoid similar name and so problem of execution. It is necessary to execute the program the next day after have finished it because some issues appear later.
