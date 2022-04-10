# Boxing App Project
> **Created By:** Hasnaath Ali

# Contents
* [ Project Objective ](#obj)
* [ Project Planning ](#plans)
* 


<a name="obj"></a>
## 1. Project Objective
The main objective was to create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules covered during training.
This CRUD application is a Web Application which users can access to create new booxing 
clubs and to create boxers to assign to that particular boxing club. Both the clubs 
and boxers can be edited and deleted as the implicit CRUD funcationality includes:
* Create
  - Create Boxing Club
  - Create Boxer
* View
  - View all Clubs
  - View all Boxers
* Edit
  - Edit Club
  - Edit Boxer
* Delete
  - Delete Club
  - Delete Boxer


<a name="plans"></a>
## 2. Project Planning
Perhaps one of the key aspects of the project as the planning can inform the developer on 
what is there to implement, the user interaction with the application and what risks you may 
be faced with. But mainly a developer must keep track of what they are doing by using a 
project tracker of some sort.

### Project Tracker ###
There are many project management tools which could have been used to track the progress of 
the project; main ones being Jira and the Trello Board. This keeps the developer on track on
what needs to be completed and what is still remaining to complete. In this project the Trello
Board was used as seen in the image below.
At first it is clear to see that the project must have recently started as the only completed
tasks was the User Stories and the ERD Diagram, whilst there was some parts of the project incomplete
and some in development.

![Trello Starting](https://user-images.githubusercontent.com/101266487/162585058-c3a0d40e-779b-4ad8-a1b8-36366821c517.JPG)

As the project came along, most cards would move from the incomplete section to the complete 
section as you can see in the image below. Furthermore, the cards had a little tabs on them to 
see which part was more important and had to be done next as a priority. The priority was always 
changing as when one card became complete, the priority would be removed and added to another
card which needs implementing next. The other tabs include different parts of the project such 
as the Flask implementation and Front End Development.  

![Trello ending](https://user-images.githubusercontent.com/101266487/162585605-2d1d1738-fb4c-4225-ade4-65719638f77a.JPG)


### Risk Assessment ###
When developing an application that requires user interaction, several issues which must be
addressed regarding the user’s privacy. A risk assessment had to be done for this project so 
some action could be taken to counteract any risk that could have cropped at anytime. A risk 
assessment also gives the developer a chance to perhaps implement any measures which could be taken 
before any risks actually happen. 

![Risk assessment](https://user-images.githubusercontent.com/101266487/162586275-08f76a48-6d44-4bb8-be71-ed8d10db2ec0.JPG)


### Functional Requirements & User Stories ###
The functional requirements are how the application will function and highlighting all the 
features that will included in the application. Also, the functional requirements are primarily 
based at the use cases (the user, system functional requirements, goals) for this project and will 
guarantee a fully purposeful application.

![Functional Requirements](https://user-images.githubusercontent.com/101266487/162586823-75b3b98c-d6a1-45f8-8836-11cc63df8fcd.JPG)

A user story is used to see the end goal which is expressed in the uers perspective. Furthermore, a user
story works well with the functional requirments stated above as it would give a developer what
must be required for this project to be a success. A few user stories are lsisted below:
-	As a user I want to view the list of boxers so that I can see which boxers have a license to fight
-	As a user I want to view one boxer so that I edit the boxer’s details
-	As a user I want to edit the boxer so that I can confirm the boxer has a licence
-	As a user I want to view the boxing club details so I can see the location of the boxing club
-	As a user I want to view the list of boxers so that I can see which boxing club the boxer fights for


### ERD Diagram ###
ERD stands for Entity Relationship Diagram, which shows the internal structure of the database which
needs to implemented. This allows the developer to map out the relationship between two tables or more.
In this instance a UML ERD diagram was created which is shown below.

![Boxing app](https://user-images.githubusercontent.com/101266487/162588062-25114e64-a38d-44a4-b3e2-3c833e5368a7.jpg)

As shown in the ERD, the database models a one-to-many relationship between all three tables. The 
tables that have been highlighted in green will be the one that must be implemented and created for 
the applicaiton, whereas the red table might be implemented if the first two are implemented and the 
developer has time to create another table before the deadline is due.


### CI Pipeline ###
CI commonly known as Continuous Integration is the automated integration of code from the contributors 
into a project. The purpose of the CI pipeline is to allow developers to integrate newly-generated 
code easily and frequently. This is achieved through the used of automated testing tools to check 
if the code is correct before fully integrating it. 
So in this instance of the CI pipeline for this project, (in the picture below) code produced on 
the local machine would get pushed to GitHub, which in turn is pushed into Jenkins. Jenkins then
automatically runs test which produces a report.

![CI Pipeline](https://user-images.githubusercontent.com/101266487/162598121-d9b4eeb3-7abf-4b36-8e67-4458ab18e01a.jpg)



