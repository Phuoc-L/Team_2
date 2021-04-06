# Git repo: https://github.com/Phuoc-L/Team_2.git
# Team members:
## -Ronnette Herico (@ronnetteherico)
## -Tommy Luu (@TOMMYLULU85)
## -Phuoc Le (@Phuoc-L)

** Product name: TaskMate **
** Product statemement: This product is a task management software that allows users to keep track of tasks and collaborate with other users on collective tasks. **
** Date: 7/3/2021 **


# Use cases:
* Add Task
* Delete Task
* Change Task Name
* Change Task Description
* Check Task
* Uncheck Task
* View Completed Tasks
* View Uncompleted Tasks
* View Task Description
* Change Task Deadline
* Log In
* Log Out
* Create group
* Create Team
* Assign Task


# Task: Add task
## Summary
A user who has logged in can add a task to the task manager
## Actors
The user
## Preconditions
* The user has logged in
## Triggers
The user selects the “Add task” option
## Primary Sequence
* The system prompts the user to enter the task name, deadline, and task description
* The user selects the option "Add task”
* The system displays the message “Task added”
## Primary Postconditions
* The task is added to the task menu

# Task: Delete task
## Summary
A user who has logged in can delete a task that is currently on the task manager
## Actors
The user
## Preconditions
* The user is logged in
## Triggers
* The user selects the "Delete Task" option
## Primary Sequence
* The system displays the message "Are you sure you want to delete this task?"
* The user selects the "Yes" option
* The system displays the message "Task deleted"
## Primary Postconditions
* The selected task is deleted
### Alternate Sequences
* The user selects the “no” option
    * No task is deleted

# Task: Change Task Name 
## Summary
A user who has logged in can change the task name of an existing task
## Actors
The user
## Preconditions 
* The user is logged in
* The task to be deleted exists
## Triggers
The user selects the “Change task name” option
## Primary Sequence
* The system displays the message “Would you like to change this task’s name?”
* The user selects the “Yes” option
* The user is prompted to enter a new task name
* The system displays the message “Task name has been changed”
## Primary postconditions
* The task name is changed
## Primary postconditions
* The user selects the "Cancel" option
    * No change is made to the selected task's name

# Task: Change Task Description 
## Summary
A user who has logged in can change the description of an existing task
## Actors
The user
## Preconditions
* The user is logged in
* The task whose description is to be changed exists
## Triggers
* The user selects the "Change task description" opetion
## Primary Sequence
* The system displays the message “Would you like to change this task’s description?”
* The user selects the “Yes” option
* The user is prompted to enter a new task description
* The system displays the message “Task description has been changed"
## Primary Postconditions
* The selected task description is then changed to the new task description
## Alternate Sequences
* The user clicks “cancel”
    * No change is made to the selected task's description

