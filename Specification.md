# Git repo: https://github.com/Phuoc-L/Team_2.git
# Team members:
## -Ronnette Herico (@ronnetteherico)
## -Tommy Luu (@TOMMYLULU85)
## -Phuoc Le (@Phuoc-L)
## -Phone Lat Yar (@phonelatyar)

** Product name:** TaskMate
** Product statemement:** This product is a task management software that allows users to keep track of tasks and collaborate with other users on collective tasks.
** Date:** 7/3/2021

# Use cases:
* Add Task
* Delete Task
* Change Task Name
* Change Task Description
* Check Task
* Uncheck Task
* View Task Information
* Assign Team
* Add Completion Date
* Change Task Deadline
* Log In
* Log Out
* Sign Up
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

# Task: Check Task 
## Summary
A user who checks off the number of selected tasks they have completed. 
## Actors
The user
## Preconditions
* precond1: User is already logged in.
* precond 2: User has already distinguished the number of tasks. 
## Triggers
The user selects a checkbox and a black check mark would appear when the task they sought out is completed. 
## Primary Sequence
Hover over the white check box
Click on the box to indicate that the task is completed. 
## Primary Postconditions
* postcondition: The black check mark in the box would be an indicator that the user has completed the desired tasks and has marked it off. 

# Task: Uncheck Tasks 
## Summary
A user who unchecks the number of selected tasks since they haven’t completed them.
## Actors
The user
## Preconditions
User is already logged in.
User has already distinguished the number of tasks. 
User has checked off the tasks they have done. 
## Triggers
The user clicks on the black check mark to uncheck it. 
## Primary Sequence
Hover over the black check mark.
Click on it .
## Primary Postconditions
* postcondition: The number of desired tasks that don’t have a black check mark in the box would be shown as the number of tasks that haven't been completed.

# Task: View Task Information
## Summary
A user who has logged in can view a task's name, description, deadline, completion date, and assigned team.
## Actors
The user
## Preconditions
* The user is logged in
## Triggers
The user has to click the view task information button
## Primary Sequence
The user is rerouted to a page with a list of the selected task's information
## Primary Postconditions
* The system will display the task's information
* The user can select the "back" button to return to the task menu

# Task: Assign Team
## Summary
A user who has logged in can assign a task to an existing team
## Actors
The user
## Preconditions
* The user is logged in
## Triggers
The user has to select the "assign team" button
## Primary Sequence
The user will be rerouted to a separate page where they can assign the task to a team
The system will prompt the user to enter the team name they want the task to be assigned to
The user clicks the confirm button
## Primary Postconditions
* The task will be assigned to a team
## Alternate Postconditions
* If the team does not exist, the system will display the message "The team does not exist"
* The system will prompt the user to re-enter the team name

# Task: Add Completion Date
## Summary
A user who is logged in can add the completion date to their task when they finish the task
## Actors
The user
## Preconditions
User is already logged in.
The task exists.
The user has completed the task.
## Triggers
The user selects the "check task" button
## Primary Sequence
* The user is rerouted to a new page where they can enter their completion date
* The user clicks confirm
## Primary Postconditions
* The task is marked "completed"
* The completion date is added to the task

# Task: Change task deadline
## Summary
A user who is logged in can change the task deadline
## Actors
The user
## Triggers
The user selects the “Change task deadline” option
## Primary Sequence
The user selects the “Change task deadline” option
The system prompts the user to select a deadline
The user selects “Confirm”
The system displays the message “Deadline has been changed”
## Primary postcondition
* The task deadline is changed
## Alternate Sequence
* The user selects the “Cancel” option
	* The deadline of the task remains unchanged

# Task: Log In
## Summary
A user who logs in to their account with a username and password. 
## Actors
The user
## Preconditions
* User knows their account username and password. 
## Triggers
When the user goes to the website then the user can log in. 
## Primary Sequence
The user types in their username in the textbox that says username.
The user types in their password in the textbox that says password.
The user clicks on the Login button once they have filled in the username and password box. 
## Primary Postconditions
* postcondition: The user is in their account where they can view and change the tasks they have done. 
## Alternate Sequences
  * If a user doesn’t remember their password or username, then they click on a phrase that says Forget password/username.
* Another window opens and the user puts in their information to reset their password or username.
### Alternate Trigger
A highlighted text named Forget Password/Username? would be the trigger for resetting the username and password.
### Alternate Postconditions
* Users can change their username or password to their account if they don’t remember them.

# Task: Log Out
## Summary
A user who has logged in can log out of the account they are currently in
## Actors
The user
## Preconditions
* The user is logged in.
## Triggers
The user clicks on the log out button. 
## Primary Sequence
The system will prompt the user with “are you sure you want to log out?”
The user clicks on yes to log out of their account. 
## Primary Postconditions
* The user is logged out of their account.
## Alternate Sequences
* The user clicks “cancel”
	* The user is not logged out of their account

# Task: Sign Up
## Summary
A user can create an account to sign into TaskMate
## Actors
The user
## Preconditions
* The user does not have an account
* The username is available
## Triggers
The user selects the "create account" button
## Primary Sequence
* The user is rerouted to a new page where they can choose their username and password
* The user selects the "create account" button
## Primary Postconditions
* The user's account is created
## Alternate Sequences
* The username not available
* The user is prompted to re-enter a new username

# Task: Create Team
## Summary
A user can create and assign themself or other users to their team.
## Actors
	1.The user
	2.Other users
## Preconditions
	The user is logged into their account.
* The other user has to be part of the same group.
* The name of this team should not match other team names
## Triggers
The user clicks on the create team button.
## Primary Sequence
	1.The system will prompt the user with a “enter the name of this team”.
	2.The user enter a name for this team
	3.The user clicks confirm
	4.The system will prompt the user with a list of group members who are not on a team.
	5.The user will then choose one or more users to be assigned to a team.
	6.The user clicks confirm
## Primary Postconditions
* The team is created and the selected group members are assigned to the team
## Alternate Sequences
* The system will prompt the user with a “enter the name of this team”.
	* The user clicks “cancel”
		* No team is created
* The system will prompt the user with a list of group members who are not on a team.
	* The user clicks “cancel”
		* No team is created

# Task: Assign Tasks
## Summary
One user can assign an already existing task to another user
## Actors
	1.The user
	2.Other user
## Preconditions
* The user is logged into their account.
* The other user has to be a part of the same team.
* The task must already exist in order to assign it to another user.
## Triggers
* The user clicks a task and select “assign task”
## Primary Sequence
	1.The system will prompt the user with a list of their team members.
	2.The user will then choose one of the team members to assign the task to.
	3.The user clicks confirm.
## Primary Postconditions
* The task is assigned to the selected team member.
## Alternate Sequences
* The user clicks cancel
	* The task is not assigned to anyone.


## Non-Functional Requirements
* The system responds to the user within 1 second.
* The menu is clear to see and navigate.
* Users will be able to access the task menu reliably. 

## Glossary
* User: The person navigating the system through their computer. 
* System: The website
* Another user: Any person that is not the current user and is also in the same team

![Diagram](https://drive.google.com/uc?export=view&id=15xf-fMaqV9WZBsCRTYi4JCxqpK6NZpm5)

