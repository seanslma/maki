# Scheduled Task

## create a shceduled task
- taskschd.msc
- actions panel -> Create Task -> General
- Triggers

When set the scheduled task to run regardless of the user logged in, the optional '**start in**' in action must be set. Otherwise it shows that the task run successfully but nothing happened. The "start in" is mainly to make sure that if you have relative paths in the task to run it understands which directory to run the script in.

Scheduled task cannot access **network drive mapping**, so mapped address must be changed to a network pass, e.g. '%%//server/share/%%' is mapped to 'I:', to access the file in 'I:' we should use '%%//server/share/myfile.csv%%'.

## priority
how to change the priority of scheduled task:
- Create the task, Right click on the task and "export" it
- Edit the task.xml file that you just exported,
- You will find a line similar to <Priority>7</Priority>,
- Change the value to a normal priority (between 4-6)
- A value of 4 will have the same I/O and memory priority as an interactive process.
- 0-real time; 1-high; 2,3-above normal
- Values of 5 and 6 will have lower memory priority
- In the task scheduler, delete the task you initially created
- In the task scheduler, in the actions area, import the task from the XML file
