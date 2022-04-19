# Boxing App Project
> **Created By:** Hasnaath Ali

# Contents
* [ Project Objective ](#obj)
* [ Project Planning ](#plans)
* [ Front End Design ](#FED)
* [ Testing and Automation](#TA)
* [ Future Development](#FD)


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


<a name="FED"></a>
## Front End Design
The front-end of the application was mainly built on very simple HTML code on visual studio. 
The aim is to produce a a simple but working application with a navigation bar for user to navigate 
around the URL. When first loading the boxing application, the user will be met with with imahge below. 
As seen below the users are greeted with a welcome page with a navigation bar at the top. 
Furthermore, looking at the welcome page; the users are also shown a title with 'Boxing Clubs:',
but is seem empty. Therefore the user can navigate (using the navbar) to the add boxing club tab.

![Home page no boxers](https://user-images.githubusercontent.com/101266487/162627545-ba59701a-f158-48e3-8374-6c00479dc215.JPG)

When the user is adding a new club, they are met with the image below where they can add a new club 
with their desired name and location. Furthermore, the user has a drop down menu where they can confirm 
if the boxing club has a licence or not.

![Add club](https://user-images.githubusercontent.com/101266487/162627668-12b03542-8b91-4afc-bf63-8923fe44cc2b.JPG)

After adding the new club, the user will be redirected to the home screen which will now be populated
with the clubs they have created as seen below, for example 'The Money Team' club has been created 
and is viewed first.

![Home page with clubs](https://user-images.githubusercontent.com/101266487/162627747-cb296575-1b5c-49e4-b9f6-ea02406d4dbe.JPG)

After creating a club the user then can create a boxer with again with the desired name and 
weight class ect, as shown in the example below. Also, when defining the what club the boxer is
in, the user has to type in the club id. The club id is set up in a way where the first ever club 
created will be club id and so on.

![Add boxer](https://user-images.githubusercontent.com/101266487/162628130-e453caa5-cfde-42ca-8191-105e04ed50f2.JPG)

When clicking the add boxer button, the user will be redirected to the view boxer page automatically
so you can view the boxer to see their details and to see what club it is assigned to. This is shown 
in the image below. The screenshot shows the first name, last name, the weight class, stance, fighting 
licence and the Club ID. The club ID is given as a number as it is the second club created in this
example. So club ID 2 refers to is Warriors. 

![View Boxer](https://user-images.githubusercontent.com/101266487/163691475-2193245d-637d-4d9d-942a-41a7294491bd.JPG)

Another feature this application has is the edit and delete function. As seen below the user can either 
edit the boxing club or delete the boxing club. However, since there are bxoers assigned to the club, 
you cannot delete the club as the two are linked. Therefore, the boxer must be deleted first before the
club is.

![Edit clubs](https://user-images.githubusercontent.com/101266487/163833735-b0502f14-e04b-460c-8a26-f9a731640509.JPG)


<a name="TA"></a>
## Testing and Automation
To test the python programs, pytest was used. This tests all of the written code to see if there are 
any issues that may need correcting. Using pytest --cov, this allows us to show the coverage which can 
be seen in the image below. These tests are designed to test the apps functionality which are the use 
of the CRUD functionality and the routing of it. The image below shows the test coverage of these 
functions to be 90%.

![pytest](https://user-images.githubusercontent.com/101266487/163870444-8fbac267-c39a-4e22-bfe2-f4fadcb72392.JPG)

If the tests was ever to fail for some reason. The reason for this fault to occur can be indentified 
in the terminal where pytest was entered as seen in the image below.

![failed pytest](https://user-images.githubusercontent.com/101266487/163871277-da98ea86-c7dd-4e84-97b5-da3f4e1a335d.JPG)


### Jenkins ###
In this project, Jenkins would have been used as the CI server which list of commands is excuted in
order to install the various requirements and dependencies of the project. Furthermore, a virtual 
environment would be created and the database URI will be exported before the application is launched.
However, in this project, Jenkins was unable to be downloaded due to the inital admin password never 
loading as seen in the image below. After googling this problem, the problem cannot be solved and 
therefore the continuous use of Jenkins could not be used.

![jenkins failed](https://user-images.githubusercontent.com/101266487/163905601-480eb972-ccaa-43a7-9e92-2177b171a8d1.JPG)


<a name="FD"></a>
## Future Development
As this application was not a fully functioning end product, there was more work that would be needed 
to get it close to the end product. This is:
- Adding an error page when trying to delete a club with a boxer assigned to the club
- Another feature such as adding an addtional page for coaches which is highlighted red in the ERD diagram above
- Better UI design could be used instead of making the page look plain and simple
- A more welcoming home page with details of how the application works
- Adding a view page for the clubs and having edit and delete clubs in the view clubs page instead of the homepage
- Continuous use of Jenkins be deployed if the initial admin password is given


## Acknowledgements
* Earl Gray (QA Tutor)
* Harry Volter (QA Tutor)
* QA Community


## Authors
**Hasnaath Ali**
