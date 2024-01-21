# EnglishClassesMapper
This project is a personal automation to map all my tasks for the week that i have to come up with. This automation will use TopWay website (TopWay Edu and TopWay Cloud) to map classes, contacts, compositions and checkpoints.

### Step By Step:
## 1 - Map scheduled classes
- Open browser in a new tab to https://cloud.topwayschool.com/login;
- Login to Topway Cloud platform (using enviroment variables);
- Navigate to agenda page https://cloud.topwayschool.com/home/agenda;
- In agenda, click to see the scheduled classes to the next week;
- Extract the scheduled classes.

## 2 - Map the next contacts
- Open browser in a new tab to https://edu.topwayschool.com/app;
- Login to Topway Edu platform (using enviroment variables);
- Navigate to the last available book (the current book that the student is using);
- Click the correct unit according to the name of the scheduled classes (got in step 1);
- Extract the contacts remaining.

## 3 - Create tasks in Asana
# To the next instructions the automation may use the Asana API.
- Create the tasks with the correct date and hour to the scheduled classes. Link the task with English project tag;
- Create the tasks of the contacts remaining to do on the Monday of next week. Link the task with English project tag.